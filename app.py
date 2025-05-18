import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Student Habits vs Performance", layout="wide")
st.title("📊 Student Habits and Academic Performance")

st.markdown("""
This interactive dashboard analyzes how student habits — such as studying hours, sleep, and screen time —
relate to academic performance using a dataset of students. Use the controls below to explore the data.
""")

# File upload
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv", "zip"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("Preview of the Dataset")
    st.dataframe(df.head())

    st.subheader("Distribution of Final Scores")
    if 'Final Score' in df.columns:
        fig, ax = plt.subplots()
        sns.histplot(df['Final Score'], bins=20, kde=True, ax=ax)
        ax.set_xlabel("Final Score")
        ax.set_ylabel("Frequency")
        st.pyplot(fig)
    else:
        st.warning("'Final Score' column not found in dataset.")

    st.subheader("Compare Two Variables")
    col1, col2 = st.columns(2)
    with col1:
        x_var = st.selectbox("Select X-axis variable", df.columns)
    with col2:
        y_var = st.selectbox("Select Y-axis variable", df.columns)

    fig2, ax2 = plt.subplots()
    sns.scatterplot(data=df, x=x_var, y=y_var, ax=ax2)
    ax2.set_title(f"{y_var} vs {x_var}")
    st.pyplot(fig2)
else:
    st.info("Please upload a dataset to start the analysis.")
