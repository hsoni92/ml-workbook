# train_math_xgboost.py
import re
import pickle
from pathlib import Path
import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import fitz  # PyMuPDF

# Reuse all the sets/regexes from the heuristic part
MATH_CHARS = set("∫∑∏√∛∜∞∆∇∂αβγδεζηθικλμνξοπρςστ υφχψωΓΔΘΛΞΠΣΥΦΨΩ∀∃¬∧∨∩∪⊂⊃⊆⊇⊕⊗≤≥≠≡≈⋅×÷∗∝±−²³¹ⁿ⁰⁴⁵⁶⁷⁸⁹ⁱ₊₋₌₍₎ₐₑₒₓₔ←→↑↓⇐⇒⇔↔∈∉∋∝∼≅≪≫⊥∥∧∨".split())
SUPER_SUB = set("⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ⁿᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖʳˢᵗᵘᵛʷˣʸᶻᵅᵝᵞᵟᵋᵌᵊᵎᵏᵐᵑᵒᵓᵔᵕᵖᵗᵘᵙᵚ₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎ₐₑₒₓₔₚₛₜᵤᵥᵥᵦᵧᵨᵩᵪ")
GREEK = set("αβγδεζηθικλμνξοπρςστ υφχψωΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤ ΥΦΧΨΩ")

MATH_PATTERNS = [
    r'\b\d+\s*[+\-×÷=]\s*\d+',  # Simple arithmetic
    r'[∫∑∏√∞∆∇∂]',  # Math symbols
    r'[αβγδεζηθικλμνξοπρςστυφχψω]',  # Greek letters
    r'[²³¹⁰⁴⁵⁶⁷⁸⁹ⁱⁿ₊₋]',  # Superscript/subscript
    r'[≤≥≠≡≈]',  # Comparison operators
    r'[∈∉∋∝∼≅]',  # Set theory
    r'[∀∃¬∧∨]',  # Logic symbols
    r'[∩∪⊂⊃⊆⊇]',  # Set operations
    r'[←→↑↓⇐⇒⇔↔]',  # Arrows
]
math_regex = re.compile("|".join(f"({p})" for p in MATH_PATTERNS))

def extract_features(text: str, block_lines=None, page_width=612.0):
    if not text:
        text = ""
    n = len(text)
    if n == 0:
        return {f"feat_{i}": 0 for i in range(150)}

    feats = {}

    # 1–50: individual symbol counts (very powerful)
    # Clean feature names: replace invalid XGBoost characters [, ], < with safe alternatives
    symbol_map = {
        '[': 'LBRACKET', ']': 'RBRACKET', '{': 'LBRACE', '}': 'RBRACE',
        '<': 'LT', '>': 'GT'
    }
    for i, c in enumerate("∫∑∏√∞∆∇∂=±−×÷^()[]{}²³¹⁰⁴⁵⁶⁷⁸⁹ⁱⁿ₊₋"):
        # Use mapped name if character is problematic, otherwise use the character
        safe_char = symbol_map.get(c, c)
        feats[f"sym_{safe_char}"] = text.count(c)

    # 51–70: grouped counts
    feats["math_chars"]      = sum(c in MATH_CHARS for c in text) / n
    feats["super_sub"]       = int(any(c in SUPER_SUB for c in text))  # Convert bool to int
    feats["greek"]           = sum(c in GREEK for c in text) / n
    feats["digits"]          = sum(c.isdigit() for c in text) / n
    feats["equals"]          = text.count("=") / max(1, text.count(" "))
    feats["regex_hits"]      = len(math_regex.findall(text))

    # layout features (if available)
    if block_lines and len(block_lines) <= 4:
        spans = block_lines[0]["spans"]
        if spans:
            x0 = min(s["bbox"][0] for s in spans)
            x1 = max(s["bbox"][2] for s in spans)
            w = x1 - x0
            feats["centered"] = int(abs((x0 + x1)/2 - page_width/2) < 50)  # Convert bool to int
            feats["short_line"] = int(w < page_width * 0.65)  # Convert bool to int
            feats["n_lines"] = len(block_lines)
        else:
            feats["centered"] = feats["short_line"] = 0
            feats["n_lines"] = 1
    else:
        feats["centered"] = feats["short_line"] = 0
        feats["n_lines"] = 5

    # heuristic score itself (very strong meta-feature)
    feats["heuristic_score"] = contains_math_score(text, block_lines, page_width)

    return feats

def contains_math_score(text: str, block_lines=None, page_width=612.0) -> float:
    """Heuristic function to score how likely text contains math."""
    if not text:
        return 0.0

    score = 0.0
    n = len(text)

    # Symbol-based features
    math_char_ratio = sum(c in MATH_CHARS for c in text) / n
    score += math_char_ratio * 0.3

    # Greek letters
    greek_ratio = sum(c in GREEK for c in text) / n
    score += greek_ratio * 0.25

    # Superscript/subscript
    if any(c in SUPER_SUB for c in text):
        score += 0.2

    # Regex matches
    regex_matches = len(math_regex.findall(text))
    score += min(regex_matches / max(1, n / 50), 0.3)

    # Equals sign ratio
    equals_ratio = text.count("=") / max(1, text.count(" "))
    score += min(equals_ratio * 0.1, 0.15)

    # Layout features
    if block_lines and len(block_lines) <= 4:
        spans = block_lines[0]["spans"]
        if spans:
            x0 = min(s["bbox"][0] for s in spans)
            x1 = max(s["bbox"][2] for s in spans)
            centered = abs((x0 + x1)/2 - page_width/2) < 50
            if centered:
                score += 0.1

    return min(score, 1.0)

# ————————————————————————
# 1. Generate training data using the heuristic as silver labels
# ————————————————————————
data = []
for pdf_path in Path("pdf_dataset").rglob("*.pdf"):
    doc = fitz.open(pdf_path)
    for page in doc:
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if block["type"] != 0:  # skip images
                continue
            text = ""
            lines = []
            for line in block["lines"]:
                ltext = "".join(span["text"] for span in line["spans"])
                text += ltext + "\n"
                lines.append(line)
            if text.strip():
                feats = extract_features(text, lines, page.rect.width)
                score = feats["heuristic_score"]
                label = 1 if score >= 0.45 else 0          # silver label
                feats["label"] = label
                data.append(feats)

df = pd.DataFrame(data)

# Check if we have any data
if len(df) == 0:
    raise ValueError("No training data found! Please check that PDF files exist in 'pdf_dataset' directory.")

# Check if label column exists
if "label" not in df.columns:
    raise ValueError("Label column not found in DataFrame. Check that data collection loop is working correctly.")

# Clean feature names: remove or replace invalid characters for XGBoost
def clean_feature_name(name):
    """Replace invalid XGBoost feature name characters."""
    # XGBoost doesn't allow [, ], < in feature names
    name = name.replace('[', 'LBRACKET').replace(']', 'RBRACKET')
    name = name.replace('<', 'LT').replace('>', 'GT')
    return name

# Rename columns to clean feature names
rename_dict = {col: clean_feature_name(col) for col in df.columns if col != "label"}
df = df.rename(columns=rename_dict)

# Ensure all numeric columns are properly typed (convert object to numeric)
for col in df.columns:
    if col != "label" and df[col].dtype == 'object':
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(float)

df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# ————————————————————————
# 2. Train XGBoost
# ————————————————————————
feature_cols = [c for c in df.columns if c != "label"]
X = df[feature_cols]
y = df["label"]

# Final check: ensure all features are numeric (should already be done, but double-check)
for col in X.columns:
    if X[col].dtype == 'object':
        X[col] = pd.to_numeric(X[col], errors='coerce').fillna(0).astype(float)
    elif X[col].dtype == 'bool':
        X[col] = X[col].astype(int)

# Check class distribution
print(f"Class distribution:\n{y.value_counts()}")
print(f"Total samples: {len(y)}")

# Only use stratify if both classes have at least 2 samples
min_class_count = y.value_counts().min()
if min_class_count >= 2:
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
    print("Using stratified split")
else:
    print(f"Warning: One class has only {min_class_count} sample(s). Using non-stratified split.")
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

dtrain = xgb.DMatrix(X_train, label=y_train)
dval   = xgb.DMatrix(X_val,   label=y_val)

params = {
    "objective": "binary:logistic",
    "eval_metric": "logloss",
    "max_depth": 6,
    "eta": 0.3,
    "subsample": 0.8,
    "colsample_bytree": 0.8,
    "seed": 42
}

bst = xgb.train(
    params,
    dtrain,
    num_boost_round=500,
    evals=[(dval, "val")],
    early_stopping_rounds=30,
    verbose_eval=50
)

# ————————————————————————
# 3. Save model + feature list
# ————————————————————————
bst.save_model("math_detector_xgb.model")
with open("math_detector_features.pkl", "wb") as f:
    pickle.dump(feature_cols, f)

print("Training done. Final validation accuracy:",
      accuracy_score(y_val, (bst.predict(dval) > 0.5).astype(int)))