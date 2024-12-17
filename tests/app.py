import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("pizzas.csv")

modelo = LinearRegression()
x = df[["diametro"]]
y = df[["preco"]]

modelo.fit(x, y)

st.title("Prevendo o valor de uma pizza com base no seu diâmetro")
st.divider()

diametro = st.number_input("Digite o tamanho do diâmetro da pizza: ")

if diametro:
    col1, col2 = st.columns(2)
    preco_previsto = modelo.predict([[diametro]])[0][0]

    with col1:
        st.metric(label="Diametro (cm)", value=diametro)
    with col2:
        st.metric(label="Valor (R$)", value=preco_previsto)