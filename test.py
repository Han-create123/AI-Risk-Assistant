from pathlib import Path

file_path = Path("data/sample_risk_case.txt")
risk_text = file_path.read_text(encoding="utf-8").lower()

risk_explanations = {
    "debt": "Debt growth may increase repayment pressure.",
    "cash flow": "Declining cash flow may weaken liquidity.",
    "repayment pressure": "High repayment pressure may increase default risk."
}

found_signals = []

print("Risk signals found:")
for keyword, explanation in risk_explanations.items():
    if keyword in risk_text:
        found_signals.append(keyword)
        print(f"- {keyword}: {explanation}")

signal_count = len(found_signals)

if signal_count >= 3:
    risk_level = "High"
elif signal_count >= 1:
    risk_level = "Medium"
else:
    risk_level = "Low"

print(f"Total risk signals: {signal_count}")
print(f"Prototype risk level: {risk_level}")
