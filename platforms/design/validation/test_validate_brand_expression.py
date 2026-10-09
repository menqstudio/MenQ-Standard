#!/usr/bin/env python3
"""Tests for the contrast checks of validate_brand_expression.py (CR-0013).

The validator was GREEN while the primary Button painted white text over a gradient whose cyan end
is 2.43:1.  These tests hold the check that now reads the stylesheets to both answers: every rule
that must be RED is broken here and asserted RED with the selector, the theme, the stop and the
ratio in the message, next to controls that are GREEN.

Two kinds of fixture, both written as bytes so a CRLF checkout changes nothing:

* a copy of the real brand-expression tree and the real validator, run as a program, for "the
  fixed tree is GREEN" and "the old rule is RED";
* small stylesheets and a small token source in a temporary directory, for each rule of the check.

Run:

    python platforms/design/validation/test_validate_brand_expression.py
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
sys.path.insert(0, str(HERE))
import validate_brand_expression as brand  # noqa: E402

VALIDATOR = "platforms/design/validation/validate_brand_expression.py"
BUNDLE = "platforms/design/brand-expression/components/bundle.css"
BRO = "platforms/design/product-extensions/bro/components/bro.css"
TREE = (
    "platforms/design/brand-expression",
    "platforms/design/product-extensions",
    "platforms/design/specifications/design-platform-registry.json",
    "platforms/design/decisions/D-027-MENQ-BRAND-EXPRESSION-LAYER-V1.md",
    "DECISION_INDEX.md",
    VALIDATOR,
)

# The rules as they stood at 391ff55, before CR-0013.
OLD_BUTTON = b".btn--primary { background: var(--gradient-brand); color: var(--color-content-inverse); border-color: transparent; box-shadow: none; }"
OLD_AVATAR = b".mq-avatar--bro { background: var(--gradient-brand); color: var(--color-content-inverse); box-shadow: var(--shadow-glow); }"
BUTTON_RULE = re.compile(rb"^\.btn--primary \{[^\n]*\}$", re.M)
AVATAR_RULE = re.compile(rb"^\.mq-avatar--bro \{[^\n]*\}$", re.M)

# A token source with only what the stylesheet fixtures name.  White on #0369a1 is 5.93:1 and on
# #06b6d4 is 2.43:1; #020617 on #0ea5e9 is 7.28:1 and on #22d3ee is 11.16:1.
TOKENS = {
    "tokens": [
        {"id": "t.inverse", "cssName": "color-content-inverse", "modes": {"light": {"value": "#ffffff"}, "dark": {"value": "#020617"}}},
        {"id": "t.primary", "cssName": "color-action-primary", "modes": {"light": {"value": "#0369a1"}, "dark": {"reference": "t.blue"}}},
        {"id": "t.hover", "cssName": "color-action-primary-hover", "modes": {"light": {"value": "#075985"}, "dark": {"value": "#22d3ee"}}},
        {"id": "t.accent", "cssName": "color-accent", "modes": {"light": {"value": "#06b6d4"}, "dark": {"value": "#22d3ee"}}},
        {"id": "t.blue", "cssName": "blue-500", "value": "#0ea5e9"},
        {"id": "t.wash", "cssName": "color-selected", "modes": {"light": {"value": "rgba(2, 132, 199, 0.12)"}, "dark": {"value": "rgba(14, 165, 233, 0.18)"}}},
    ]
}
DERIVED = b""":root, [data-theme], .section-contrast {
  --gradient-brand: linear-gradient(135deg, var(--color-action-primary), var(--color-accent));
  --fill: var(--color-action-primary);
}
[data-theme="dark"], .section-contrast { --fill: var(--gradient-brand); }
"""


class StylesheetCase(unittest.TestCase):
    """check_surface_contrast over a stylesheet and a token source written into a temporary directory."""

    def setUp(self) -> None:
        self.dir = Path(tempfile.mkdtemp(prefix="menq-brand-css-"))
        self.addCleanup(shutil.rmtree, self.dir, True)
        self.source = self.dir / "tokens.source.json"
        self.source.write_bytes(json.dumps(TOKENS).encode("utf-8"))

    def run_css(self, css: bytes, derived: bytes = DERIVED) -> tuple[list[str], dict[str, int]]:
        path = self.dir / "sheet.css"
        path.write_bytes(derived + css)
        errors: list[str] = []
        counts = brand.check_surface_contrast(errors, css_paths=(path,), source_path=self.source)
        return errors, counts

    def assert_one(self, errors: list[str], *fragments: str) -> None:
        self.assertEqual(len(errors), 1, errors)
        for fragment in fragments:
            self.assertIn(fragment, errors[0])

    # -- the defect ---------------------------------------------------------------------------

    def test_inverse_text_over_the_brand_gradient_is_red_in_light_at_the_cyan_stop(self) -> None:
        errors, _ = self.run_css(OLD_BUTTON + b"\n")
        self.assert_one(
            errors, "surface contrast light:", ".btn--primary", "color var(--color-content-inverse)",
            "gradient stop 2 var(--color-accent) = #06b6d4", "at 2.43:1", "< 4.5:1",
        )

    def test_the_same_gradient_is_measured_and_passes_in_the_dark_scopes(self) -> None:
        # Remove Light and the old rule has nothing left to fail: the dark scopes are 7.28 and 11.16.
        css = b'[data-theme="dark"] .x { background: var(--gradient-brand); color: var(--color-content-inverse); }\n'
        dark_only = b"""[data-theme="dark"], .section-contrast {
  --gradient-brand: linear-gradient(135deg, var(--color-action-primary), var(--color-accent));
}
"""
        errors, counts = self.run_css(css, derived=dark_only)
        # Light has no --gradient-brand in this sheet: an unresolved background is RED, not skipped.
        self.assert_one(errors, "surface contrast light:", "var(--gradient-brand) is not a token")
        self.assertEqual(counts["gradient_stops"], 4)

    def test_a_gradient_that_passes_at_every_stop_in_every_scope_is_green(self) -> None:
        css = b".ok { color: #ffffff; background: linear-gradient(90deg, #0369a1, #075985 60%, #020617); }\n"
        errors, counts = self.run_css(css)
        self.assertEqual(errors, [])
        self.assertEqual(counts["gradient_stops"], 3 * len(brand.THEME_SCOPES))

    def test_the_fixed_shape_solid_in_light_and_gradient_in_dark_is_green(self) -> None:
        css = b".btn--primary { background: var(--fill); color: var(--color-content-inverse); }\n"
        errors, counts = self.run_css(css)
        self.assertEqual(errors, [])
        self.assertEqual((counts["solid"], counts["gradient_stops"]), (1, 4))  # light; dark and section-contrast

    # -- every stop, not the ends ---------------------------------------------------------------

    def test_a_failing_middle_stop_is_red_and_named(self) -> None:
        css = b".mid { color: #ffffff; background: linear-gradient(to right, #0369a1 0%, #06b6d4 50%, #075985 100%); }\n"
        errors, _ = self.run_css(css)
        self.assertEqual(len(errors), len(brand.THEME_SCOPES), errors)
        self.assertTrue(all("gradient stop 2 #06b6d4 50% = #06b6d4 at 2.43:1" in error for error in errors), errors)

    def test_a_failing_first_stop_is_red_and_named(self) -> None:
        css = b".first { color: #ffffff; background-image: radial-gradient(circle at 10% 20%, #06b6d4, #0369a1); }\n"
        errors, _ = self.run_css(css)
        self.assertEqual(len(errors), len(brand.THEME_SCOPES), errors)
        self.assertIn("gradient stop 1 #06b6d4 = #06b6d4 at 2.43:1", errors[0])

    # -- a stop that cannot be resolved is RED, never skipped -------------------------------------

    def unresolved(self, stop: bytes) -> list[str]:
        css = b".u { color: var(--color-content-inverse); background: linear-gradient(135deg, var(--color-action-primary), " + stop + b"); }\n"
        errors, counts = self.run_css(css)
        self.assertEqual(len(errors), len(brand.THEME_SCOPES), errors)
        self.assertEqual(counts["gradient_stops"], len(brand.THEME_SCOPES))  # stop 1 was still measured
        for error in errors:
            self.assertIn(".u ", error)
            self.assertIn("gradient stop 2", error)
            self.assertIn("cannot be resolved to one opaque colour", error)
        return errors

    def test_a_stop_naming_an_undefined_custom_property_is_red(self) -> None:
        errors = self.unresolved(b"var(--color-not-a-token)")
        self.assertIn("var(--color-not-a-token) is not a token and no stylesheet defines it", errors[0])

    def test_a_color_mix_stop_is_red(self) -> None:
        self.unresolved(b"color-mix(in srgb, var(--color-accent) 50%, transparent)")

    def test_a_transparent_stop_is_red(self) -> None:
        self.unresolved(b"transparent")

    def test_a_translucent_stop_is_red(self) -> None:
        errors = self.unresolved(b"var(--color-selected)")
        self.assertIn("is translucent", errors[0])

    def test_a_stop_with_words_that_are_not_a_position_is_red(self) -> None:
        self.unresolved(b"#0369a1 url(x.png)")

    def test_a_malformed_rgb_stop_is_red(self) -> None:
        for stop in (b"rgba(3, 105, 161, 1, 0)", b"rgb(3, 105)", b"rgb(10%, 20%, 30%)", b"#0369a1ff"):
            with self.subTest(stop=stop):
                errors = self.unresolved(stop)
                self.assertIn("unsupported color", errors[0])

    def test_a_fallback_is_used_for_an_undefined_custom_property(self) -> None:
        css = b".f { color: #ffffff; background: linear-gradient(#0369a1, var(--color-not-a-token, #06b6d4)); }\n"
        errors, _ = self.run_css(css)
        self.assertEqual(len(errors), len(brand.THEME_SCOPES), errors)
        self.assertIn("gradient stop 2 var(--color-not-a-token, #06b6d4) = #06b6d4 at 2.43:1", errors[0])

    def test_a_gradient_without_a_colour_stop_is_red(self) -> None:
        errors, _ = self.run_css(b".g { color: #ffffff; background: linear-gradient(90deg, 50%); }\n")
        self.assertEqual(len(errors), len(brand.THEME_SCOPES), errors)
        self.assertIn("cannot be resolved: no colour stop found", errors[0])

    def test_a_custom_property_loop_is_red(self) -> None:
        loop = b":root, [data-theme], .section-contrast { --a: linear-gradient(var(--b), #000000); --b: var(--a); }\n"
        errors, _ = self.run_css(b".l { color: #ffffff; background: var(--a); }\n", derived=loop)
        self.assertEqual(len(errors), len(brand.THEME_SCOPES), errors)
        self.assertIn("cannot be resolved: custom-property loop", errors[0])

    def test_a_fill_that_is_a_gradient_in_one_scope_must_resolve_in_every_scope(self) -> None:
        derived = b""":root, [data-theme], .section-contrast { --fill: color-mix(in srgb, var(--color-action-primary) 50%, transparent); }
[data-theme="dark"], .section-contrast { --fill: linear-gradient(#0ea5e9, #22d3ee); }
"""
        errors, _ = self.run_css(b".s { color: var(--color-content-inverse); background: var(--fill); }\n", derived=derived)
        self.assert_one(errors, "surface contrast light:", ".s ", "cannot be resolved to one opaque colour")

    def test_an_unresolvable_foreground_over_a_gradient_is_red(self) -> None:
        errors, _ = self.run_css(b".i { color: currentColor; background: var(--gradient-brand); }\n")
        self.assertEqual(len(errors), len(brand.THEME_SCOPES), errors)
        self.assertIn("the foreground currentColor cannot be resolved", errors[0])

    # -- which rules and which scopes are read ------------------------------------------------------

    def test_a_foreground_set_by_another_rule_with_the_same_selector_is_found(self) -> None:
        css = b".b { color: var(--color-content-inverse); }\n.b { background: var(--gradient-brand); }\n"
        errors, _ = self.run_css(css)
        self.assert_one(errors, "surface contrast light:", ".b ", "at 2.43:1")

    def test_the_last_colour_declared_for_a_selector_is_the_one_judged(self) -> None:
        css = b".c { color: #020617; background: linear-gradient(#06b6d4, #06b6d4); }\n.c { color: #ffffff; }\n"
        errors, _ = self.run_css(css)
        self.assertEqual(len(errors), 2 * len(brand.THEME_SCOPES), errors)
        self.assertTrue(all("paints color #ffffff over" in error for error in errors), errors)

    def test_a_state_rule_takes_the_foreground_of_its_base_rule(self) -> None:
        css = b".b { color: var(--color-content-inverse); background: var(--color-action-primary); }\n.b:hover { background: var(--gradient-brand); }\n"
        errors, _ = self.run_css(css)
        self.assert_one(errors, "surface contrast light:", ".b:hover", "at 2.43:1")

    def test_a_state_rule_that_sets_its_own_colour_is_judged_by_it(self) -> None:
        css = b".b { color: #020617; }\n.b:hover { color: #ffffff; background: linear-gradient(#06b6d4, #06b6d4); }\n"
        errors, _ = self.run_css(css)
        self.assertEqual(len(errors), 2 * len(brand.THEME_SCOPES), errors)
        self.assertTrue(all(".b:hover" in error and "at 2.43:1" in error for error in errors), errors)

    def test_a_foreground_named_through_a_stylesheet_custom_property_is_resolved(self) -> None:
        derived = DERIVED + b":root, [data-theme], .section-contrast { --ink: #ffffff; }\n"
        errors, _ = self.run_css(b".k { color: var(--ink); background: linear-gradient(#0369a1, #06b6d4); }\n", derived=derived)
        self.assertEqual(len(errors), len(brand.THEME_SCOPES), errors)
        self.assertIn("paints color var(--ink) over gradient stop 2 #06b6d4 = #06b6d4 at 2.43:1", errors[0])

    def test_a_translucent_foreground_is_composited_over_the_fill(self) -> None:
        # White at half strength over #0369a1 is 2.36:1; taken as solid white it would be 5.93:1.
        errors, _ = self.run_css(b".a { color: rgba(255, 255, 255, 0.5); background: #0369a1; }\n")
        self.assertEqual(len(errors), len(brand.THEME_SCOPES), errors)
        self.assertRegex(errors[0], r"\.a .* = #0369a1 at 2\.\d\d:1")

    def test_short_hex_and_named_colours_are_resolved(self) -> None:
        css = b".h { color: #fff; background: linear-gradient(#000, #123); }\n.n { color: white; background: linear-gradient(black, #111111); }\n"
        errors, counts = self.run_css(css)
        self.assertEqual(errors, [])
        self.assertEqual(counts["gradient_stops"], 4 * len(brand.THEME_SCOPES))

    def test_background_image_is_read_as_well_as_background(self) -> None:
        errors, _ = self.run_css(b".p { color: var(--color-content-inverse); background-image: var(--gradient-brand); }\n")
        self.assert_one(errors, "surface contrast light:", ".p ", "at 2.43:1")

    def test_a_rule_inside_a_media_block_is_read(self) -> None:
        css = b"@media (max-width: 720px) { .m { color: var(--color-content-inverse); background: var(--gradient-brand); } }\n"
        errors, _ = self.run_css(css)
        self.assert_one(errors, "surface contrast light:", ".m ", "at 2.43:1")

    def test_each_selector_of_a_list_is_read(self) -> None:
        css = b".one, .two { color: var(--color-content-inverse); background: var(--gradient-brand); }\n"
        errors, _ = self.run_css(css)
        self.assertEqual(sorted(e.split(": ")[1].split(" (")[0] for e in errors), [".one", ".two"], errors)

    def test_a_gradient_in_a_rule_with_no_text_colour_is_counted_not_judged(self) -> None:
        errors, counts = self.run_css(b".fill { height: 100%; background-image: var(--gradient-brand); }\n")
        self.assertEqual(errors, [])
        self.assertEqual((counts["decorative"], counts["gradient_stops"]), (1, 0))

    def test_a_light_scope_that_takes_the_gradient_is_red(self) -> None:
        css = b'[data-theme="light"] { --fill: var(--gradient-brand); }\n.t { color: var(--color-content-inverse); background: var(--fill); }\n'
        errors, _ = self.run_css(css)
        self.assertEqual(len(errors), 1, errors)
        self.assertIn("surface contrast light: .t ", errors[0])

    def test_a_declaration_made_only_inside_section_contrast_is_read(self) -> None:
        css = b".section-contrast { --fill: linear-gradient(#020617, #0f172a); }\n.c { color: var(--color-content-inverse); background: var(--fill); }\n"
        errors, _ = self.run_css(css)
        self.assertEqual(len(errors), 2, errors)  # both stops, in that scope only
        self.assertTrue(all(error.startswith("surface contrast section-contrast: .c ") for error in errors), errors)

    def test_a_stylesheet_scope_may_redefine_a_token(self) -> None:
        css = b".section-contrast { --color-accent: #020617; }\n.r { color: var(--color-content-inverse); background: var(--gradient-brand); }\n"
        errors, _ = self.run_css(css)
        scopes = sorted(error.split(":")[0] for error in errors)
        self.assertEqual(scopes, ["surface contrast light", "surface contrast section-contrast"], errors)

    # -- text on a solid fill -------------------------------------------------------------------

    def test_text_on_a_solid_fill_below_the_threshold_is_red(self) -> None:
        errors, _ = self.run_css(b".solid { color: var(--color-content-inverse); background: var(--color-accent); }\n")
        self.assert_one(errors, "surface contrast light:", ".solid", "background var(--color-accent) = #06b6d4 at 2.43:1")

    def test_text_on_a_solid_fill_above_the_threshold_is_green(self) -> None:
        errors, counts = self.run_css(b".solid { color: var(--color-content-inverse); background-color: var(--color-action-primary); }\n")
        self.assertEqual(errors, [])
        self.assertEqual(counts["solid"], len(brand.THEME_SCOPES))

    def test_a_translucent_solid_fill_is_counted_as_not_measured(self) -> None:
        errors, counts = self.run_css(b".wash { color: var(--color-content-inverse); background: var(--color-selected); }\n")
        self.assertEqual(errors, [])
        self.assertEqual((counts["translucent"], counts["solid"]), (len(brand.THEME_SCOPES), 0))

    # -- the parser fails closed ------------------------------------------------------------------

    def test_a_stylesheet_that_cannot_be_parsed_is_red(self) -> None:
        for css in (b".x { color: #fff; background: #000; \n", b".x { color: #fff; } }\n", b'.x::before { content: "}"; }\n', b".x { color #fff }\n",
                    b'.x::before { content: "a; color: #fff"; }\n'):
            with self.subTest(css=css):
                errors, _ = self.run_css(css)
                self.assertEqual(len(errors), 1, errors)
                self.assertIn("surface contrast: cannot parse", errors[0])

    def test_a_missing_stylesheet_is_red(self) -> None:
        errors: list[str] = []
        brand.check_surface_contrast(errors, css_paths=(self.dir / "absent.css",), source_path=self.source)
        self.assertEqual(len(errors), 1, errors)
        self.assertIn("surface contrast: cannot parse", errors[0])


class TokenPairCase(unittest.TestCase):
    """The 17 token pairs that were already checked are still checked."""

    def test_the_real_token_source_passes_its_pairs(self) -> None:
        errors: list[str] = []
        brand.check_contrast(errors)
        self.assertEqual(errors, [])
        self.assertEqual(len(brand.CONTRAST_PAIRS), 17)

    def test_a_token_value_that_breaks_a_pair_is_red(self) -> None:
        source = json.loads(brand.SOURCE.read_bytes().decode("utf-8"))
        token = next(t for t in source["tokens"] if t["cssName"] == "color-action-primary")
        token["modes"]["light"] = {"value": "#06b6d4"}
        with tempfile.TemporaryDirectory(prefix="menq-brand-tokens-") as folder:
            path = Path(folder) / "brand-tokens.source.json"
            path.write_bytes(json.dumps(source).encode("utf-8"))
            errors: list[str] = []
            brand.check_contrast(errors, source_path=path)
        self.assertEqual(len(errors), 1, errors)
        self.assertRegex(errors[0], r"^contrast light: color-content-inverse on color-action-primary is \d\.\d\d:1 \(< 4\.5:1, WCAG AA\)$")


class RealTreeCase(unittest.TestCase):
    """The real validator, run as a program on a copy of the real brand-expression tree."""

    def setUp(self) -> None:
        self.root = Path(tempfile.mkdtemp(prefix="menq-brand-tree-"))
        self.addCleanup(shutil.rmtree, self.root, True)
        for rel in TREE:
            source, target = REPO / rel, self.root / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            if source.is_dir():
                shutil.copytree(source, target, ignore=shutil.ignore_patterns("__pycache__"))
            else:
                target.write_bytes(source.read_bytes())

    def validate(self) -> tuple[int, str]:
        result = subprocess.run([sys.executable, str(self.root / VALIDATOR)], capture_output=True, text=True, encoding="utf-8")
        return result.returncode, result.stdout + result.stderr

    def replace_rule(self, rel: str, rule: re.Pattern[bytes], old: bytes) -> None:
        path = self.root / rel
        data = path.read_bytes()
        self.assertEqual(len(rule.findall(data)), 1, f"{rel}: expected exactly one rule to replace")
        self.assertNotIn(old, data, f"{rel} still holds the pre-CR-0013 rule")
        path.write_bytes(rule.sub(lambda _: old, data))

    def test_the_fixed_tree_is_green_and_measures_gradient_stops(self) -> None:
        code, output = self.validate()
        self.assertEqual(code, 0, output)
        self.assertTrue(output.startswith("BRAND EXPRESSION VALIDATION: GREEN\n"), output)
        measured = re.search(r"(\d+) gradient colour stops and (\d+) solid fills", output)
        self.assertIsNotNone(measured, output)
        self.assertGreater(int(measured.group(1)), 0, "GREEN while measuring no gradient stop")
        self.assertGreater(int(measured.group(2)), 0, "GREEN while measuring no solid fill")
        self.assertIn("34 WCAG AA contrast pairs", output)

    def test_a_token_value_that_breaks_a_pair_is_red_in_the_program_too(self) -> None:
        path = self.root / "platforms/design/brand-expression/source/brand-tokens.source.json"
        source = json.loads(path.read_bytes().decode("utf-8"))
        token = next(t for t in source["tokens"] if t["cssName"] == "color-action-primary")
        token["modes"]["light"] = {"value": "#06b6d4"}
        path.write_bytes(json.dumps(source, ensure_ascii=False, indent=2).encode("utf-8"))
        code, output = self.validate()
        self.assertEqual(code, 1, output)
        self.assertRegex(output, r"(?m)^- contrast light: color-content-inverse on color-action-primary is \d\.\d\d:1 \(< 4\.5:1, WCAG AA\)$")

    def test_the_old_primary_button_rule_is_red(self) -> None:
        self.replace_rule(BUNDLE, BUTTON_RULE, OLD_BUTTON)
        code, output = self.validate()
        self.assertEqual(code, 1, output)
        self.assertTrue(output.startswith("BRAND EXPRESSION VALIDATION: RED\n"), output)
        self.assertIn(
            f"- surface contrast light: .btn--primary ({BUNDLE}) paints color var(--color-content-inverse) over "
            "gradient stop 2 var(--color-accent) = #06b6d4 at 2.43:1 (< 4.5:1, WCAG AA)\n",
            output,
        )
        self.assertEqual(output.count("\n- "), 1, output)  # the azure stop and both dark scopes pass

    def test_the_old_bro_avatar_rule_is_red(self) -> None:
        self.replace_rule(BRO, AVATAR_RULE, OLD_AVATAR)
        code, output = self.validate()
        self.assertEqual(code, 1, output)
        self.assertIn(
            f"- surface contrast light: .mq-avatar--bro ({BRO}) paints color var(--color-content-inverse) over "
            "gradient stop 2 var(--color-accent) = #06b6d4 at 2.43:1 (< 4.5:1, WCAG AA)\n",
            output,
        )
        self.assertEqual(output.count("\n- "), 1, output)

    def test_a_light_fill_put_back_on_the_gradient_is_red_for_every_rule_that_uses_it(self) -> None:
        path = self.root / BUNDLE
        data = path.read_bytes()
        solid = b"--fill-action-primary: var(--color-action-primary);"
        self.assertEqual(data.count(solid), 1)
        path.write_bytes(data.replace(solid, b"--fill-action-primary: var(--gradient-brand);"))
        code, output = self.validate()
        self.assertEqual(code, 1, output)
        for selector, sheet in ((".btn--primary", BUNDLE), (".mq-avatar--bro", BRO)):
            self.assertIn(f"- surface contrast light: {selector} ({sheet}) paints", output)

    def test_the_real_stylesheets_keep_inverse_text_off_the_brand_gradient_in_light(self) -> None:
        errors: list[str] = []
        counts = brand.check_surface_contrast(errors)
        self.assertEqual(errors, [])
        self.assertGreater(counts["gradient_stops"], 0)


if __name__ == "__main__":
    unittest.main()
