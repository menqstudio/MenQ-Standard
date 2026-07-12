export declare const FOUNDATION_CLASS_NAMES: Readonly<{
  stack: "menq-stack";
  cluster: "menq-cluster";
  surface: "menq-surface";
  content: "menq-content";
}>;

export declare function foundationClass(
  name: keyof typeof FOUNDATION_CLASS_NAMES,
): (typeof FOUNDATION_CLASS_NAMES)[keyof typeof FOUNDATION_CLASS_NAMES];
