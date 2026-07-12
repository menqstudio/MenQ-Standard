export const FOUNDATION_CLASS_NAMES = Object.freeze({
  stack: "menq-stack",
  cluster: "menq-cluster",
  surface: "menq-surface",
  content: "menq-content",
});

export function foundationClass(name) {
  const value = FOUNDATION_CLASS_NAMES[name];
  if (!value) {
    throw new TypeError(`Unknown foundation class: ${String(name)}`);
  }
  return value;
}
