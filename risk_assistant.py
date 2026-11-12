from pathlib import Path  # Python 自带的路径工具，用来读取示例文件


def analyze_risk(text):
    """分析传入的文字，返回风险信号、数量和演示等级。"""
    text = text.lower()  # 统一转小写，便于匹配英文关键词

    risk_explanations = {
        "debt": "Debt growth may increase repayment pressure.",
        "cash flow": "Declining cash flow may weaken liquidity.",
        "repayment pressure": "High repayment pressure may increase default risk."
    }

    found_signals = []  # 存放找到的“关键词、解释”

    for keyword, explanation in risk_explanations.items():
        if keyword in text:
            found_signals.append((keyword, explanation))

    signal_count = len(found_signals)  # 统计找到了几种信号

    if signal_count >= 3:
        risk_level = "High"
    elif signal_count >= 1:
        risk_level = "Medium"
    else:
        risk_level = "Low"

    return found_signals, signal_count, risk_level


# 直接运行这个文件时，使用示例文本；被网页导入时，不执行下面的代码
if __name__ == "__main__":
    file_path = Path("data/sample_risk_case.txt")
    risk_text = file_path.read_text(encoding="utf-8")
    found_signals, signal_count, risk_level = analyze_risk(risk_text)

    print("Risk signals found:")
    for keyword, explanation in found_signals:
        print(f"- {keyword}: {explanation}")

    print(f"Total risk signals: {signal_count}")
    print(f"Prototype risk level: {risk_level}")