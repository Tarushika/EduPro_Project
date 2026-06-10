import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="EduPro Dashboard", layout="wide")

st.title("📊 EduPro Online Learning Analytics Dashboard")

# Load Data
df = pd.read_csv("EduPro_Final.csv")

# KPIs
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Learners", df["UserID"].nunique())

with col2:
    st.metric("Total Courses", df["CourseID"].nunique())

with col3:
    st.metric("Total Enrollments", len(df))

# Sidebar Filters
st.sidebar.header("Filters")

age_group = st.sidebar.multiselect(
    "Age Group",
    options=df["AgeGroup"].unique(),
    default=df["AgeGroup"].unique()
)

gender = st.sidebar.multiselect(
    "Gender",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

filtered_df = df[
    (df["AgeGroup"].isin(age_group)) &
    (df["Gender"].isin(gender))
]

# Age Distribution
st.subheader("Age Distribution")

age_count = filtered_df["AgeGroup"].value_counts()

fig, ax = plt.subplots()
age_count.plot(kind="bar", ax=ax)
st.pyplot(fig)

# Gender Distribution
st.subheader("Gender Distribution")

gender_count = filtered_df["Gender"].value_counts()

fig, ax = plt.subplots()
gender_count.plot(kind="pie", autopct="%1.1f%%", ax=ax)
st.pyplot(fig)

# Course Level Analysis
st.subheader("Course Level Analysis")

level_count = filtered_df["CourseLevel"].value_counts()

fig, ax = plt.subplots()
level_count.plot(kind="bar", ax=ax)
st.pyplot(fig)

st.subheader("Dataset Preview")
st.dataframe(filtered_df.head())