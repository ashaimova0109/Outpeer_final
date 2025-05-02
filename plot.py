import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Успеваемости студентов")

data_mat = pd.read_csv("student-mat.csv")

st.subheader("Обзор данных")
st.write(data_mat.head())

option = st.selectbox(
    "Выберите тип визуализации:",
    [
        "Распределение итоговых оценок (G3)",
        "Итоговые оценки по полу",
        "Алкоголь и успеваемость",
        "Корреляционная матрица"
    ]
)

st.subheader("График")

if option == "Распределение итоговых оценок (G3)":
    fig, ax = plt.subplots()
    sns.histplot(data_mat["G3"], bins=20, kde=True, ax=ax)
    st.pyplot(fig)

elif option == "Итоговые оценки по полу":
    fig, ax = plt.subplots()
    sns.boxplot(x="sex", y="G3", data=data_mat, ax=ax)
    st.pyplot(fig)

elif option == "Алкоголь и успеваемость":
    fig, ax = plt.subplots()
    sns.boxplot(x="Walc", y="G3", data=data_mat, ax=ax)
    st.pyplot(fig)

elif option == "Корреляционная матрица":
    numeric_cols = data_mat.select_dtypes(include=['int64', 'float64'])
    corr = numeric_cols.corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".1f", ax=ax)
    st.pyplot(fig)
