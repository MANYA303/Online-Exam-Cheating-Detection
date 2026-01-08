import streamlit as st
import pandas as pd
from cheating_model import detect_cheating
import plotly.express as px

st.set_page_config(page_title="Exam Cheating Detection", layout="wide")

st.title("🛡️ Online Exam Cheating Detection")
st.caption("Behavioral Analytics using Anomaly Detection")

st.sidebar.header("Settings")
threshold = st.sidebar.slider("Detection Sensitivity", 0.01, 0.2, 0.05)

uploaded_file = st.file_uploader("Upload Exam Logs CSV", type=["csv"])

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    result = detect_cheating(data, threshold)

    suspicious = result[result["suspicious"]=="Yes"]

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Students", len(result))
    col2.metric("Suspicious Students", len(suspicious))
    col3.metric("Suspicion %", round(len(suspicious)/len(result)*100,2))

    fig = px.pie(result, names="suspicious", title="Detection Result")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("All Students")
    st.dataframe(result)

    st.subheader("Suspicious Students")
    st.dataframe(suspicious)

    st.download_button(
        "Download Report",
        suspicious.to_csv(index=False),
        "suspicious_students.csv"
    )
else:
    st.info("Upload exam_logs.csv to start")
