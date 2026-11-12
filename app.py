import streamlit as st  # 导入网页工具
from risk_assistant import analyze_risk  # 从 risk_assistant.py 借用我们写的分析函数

st.title("AI Risk Assistant")
risk_text = st.text_area("Paste financial text here")

if st.button("Analyze Risk"):
    found_signals, signal_count, risk_level = analyze_risk(risk_text)
    st.write(f"Total risk signals: {signal_count}")
    st.write(f"Prototype risk level: {risk_level}")
    for keyword, explanation in found_signals:  # 逐条取出找到的关键词和解释
        st.write(f"- {keyword}: {explanation}")  # 在网页上显示这一条