import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Заголовок приложения
st.title("Анализ данных об успеваемости студентов")

# Загрузка датасета
df = pd.read_csv("student-mat.csv")

# Краткий обзор
st.subheader("Обзор данных")
st.write(df.head())

# Выбор визуализации
option = st.selectbox(
    "Выберите тип визуализации:",
    [
        "Распределение итоговых оценок (G3)",
        "Boxplot: итоговые оценки по полу",
        "Алкоголь и успеваемость",
        "Корреляционная матрица",
        "Scatter: время на учебу и оценки"
    ]
)

# Визуализации
st.subheader("График")

if option == "Распределение итоговых оценок (G3)":
    fig, ax = plt.subplots()
    sns.histplot(df["G3"], bins=20, kde=True, ax=ax)
    st.pyplot(fig)

elif option == "Boxplot: итоговые оценки по полу":
    fig, ax = plt.subplots()
    sns.boxplot(x="sex", y="G3", data=df, ax=ax)
    st.pyplot(fig)

elif option == "Алкоголь и успеваемость":
    fig, ax = plt.subplots()
    sns.boxplot(x="Walc", y="G3", data=df, ax=ax)
    st.pyplot(fig)

elif option == "Корреляционная матрица":
    numeric_cols = df.select_dtypes(include=['int64', 'float64'])
    corr = numeric_cols.corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".1f", ax=ax)
    st.pyplot(fig)

elif option == "Scatter: время на учебу и оценки":
    fig, ax = plt.subplots()
    sns.scatterplot(x="studytime", y="G3", data=df, ax=ax)
    st.pyplot(fig)
