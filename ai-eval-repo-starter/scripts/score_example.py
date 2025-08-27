"""
score_example.py — example script to compute average scores per model.
Usage:
    python scripts/score_example.py
"""
import pandas as pd

df = pd.read_csv("evaluations/scored_results.csv")
print("Average score per model:")
print(df.groupby("model")["score"].mean())
