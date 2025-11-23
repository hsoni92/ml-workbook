import pickle
import pandas as pd
import xgboost as xgb
from train import extract_features

# load once at startup
model = xgb.Booster()
model.load_model("math_detector_xgb.model")
with open("math_detector_features.pkl", "rb") as f:
    FEATURES = pickle.load(f)

def is_math_xgboost(text: str, block_lines=None, page_width=612.0) -> str:
    feats = extract_features(text, block_lines, page_width)
    # Create a DataFrame with feature names to match training format
    row_dict = {f: feats.get(f, 0) for f in FEATURES}
    df_row = pd.DataFrame([row_dict])
    dmatrix = xgb.DMatrix(df_row)
    prob = model.predict(dmatrix)[0]
    if prob > 0.70:   return "displayed"
    if prob > 0.40:   return "inline_or_mixed"
    return "prose"