# deploy - github e streamlit cloud
# https://appstudents-dsngvbagpz8frmzxoryhapp.streamlit.app/
# https://chat.whatsapp.com/ILL00cZZykV4w4n8DqkYI9
import warnings

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

warnings.filterwarnings("ignore")


st.markdown("# Live 03")

st.markdown("## Visualização de performance dos alunos")
df = pd.read_csv("data/StudentsPerformance.csv", sep=";")
st.dataframe(df)


st.markdown("## Informações sobre o dataset")
st.table(df["parental level of education"].value_counts())

df["total score"] = df["math score"] + df["reading score"] + df["writing score"]
df["avg score"] = df["total score"] / 3


st.dataframe(df[["total score", "avg score"]].describe())

math_gabaritou = df[df["math score"] == 100]["avg score"].count()
reading_gabaritou = df[df["reading score"] == 100]["avg score"].count()
writing_gabaritou = df[df["writing score"] == 100]["avg score"].count()

st.markdown(f"### Gabaritou matemática: {math_gabaritou}")
st.markdown(f"### Gabaritou leitura: {reading_gabaritou}")
st.markdown(f"### Gabaritou escrita: {writing_gabaritou}")

total = len(df)
p_math = (math_gabaritou / total) * 100
p_writing = (writing_gabaritou / total) * 100
p_reading = (reading_gabaritou / total) * 100


st.markdown(f"### Porcentagem de alunos que gabaritaram matemática: {p_math:.2f}%")
st.markdown(f"### Porcentagem de alunos que gabaritaram escrita: {p_writing:.2f}%")
st.markdown(f"### Porcentagem de alunos que gabaritaram leitura: {p_reading:.2f}%")

df_agrupado = df.groupby(by=["gender", "race/ethnicity"])["gender"].count()

df_agrupado = pd.DataFrame(df_agrupado)

st.dataframe(df_agrupado)


st.dataframe(
    df.groupby(by=["gender", "race/ethnicity"])[
        ["math score", "writing score", "reading score"]
    ].agg(["mean", "count"])
)

st.dataframe(df["race/ethnicity"].value_counts())

fig, ax = plt.subplots(1, 2, figsize=(15, 7))
plt.subplot(121)
sns.histplot(data=df, x="avg score", bins=30, kde=True, color="g")
plt.subplot(122)
sns.histplot(data=df, x="avg score", kde=True, hue="gender")

st.pyplot(fig)


plot = sns.pairplot(df, hue="gender")
st.pyplot(plot.fig)

fig1, ax = plt.subplots(figsize=(15, 7))
sns.heatmap(
    df[
        ["math score", "writing score", "reading score", "avg score", "total score"]
    ].corr(),
    annot=True,
    fmt=".2f",
)
st.pyplot(fig1)

# name = st.text_input("Digite seu nome:")
# surname = st.text_input("Digite seu sobrenome:")
# password = st.text_input("Digite sua senha:", type="password")
#
# user = {"name": name, "surname": surname, "password": password}
#
#
# input_button = st.button("Clique aqui")
#
# if input_button:
#     st.write(
#         "Olá",
#         user.get("name"),
#         user.get("surname"),
#     )
#     if user.get("name") == "Carlos" and user.get("password") == "123":
#         st.success("Você está autorizado")
#     else:
#         st.error("Desculpe, você não está autorizado")
