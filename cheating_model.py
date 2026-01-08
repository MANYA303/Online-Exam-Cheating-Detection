import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_cheating(data, contamination=0.05):
    features = data.drop(columns=["student_id"])
    model = IsolationForest(contamination=contamination, random_state=42)
    data["anomaly"] = model.fit_predict(features)
    data["suspicious"] = data["anomaly"].map({1:"No", -1:"Yes"})
    return data
