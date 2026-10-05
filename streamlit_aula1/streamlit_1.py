import streamlit as st
import pandas as pd


nome = "Pedro"
idade = "17"

df = pd.DataFrame({
   'first column': ['Português','Matemática','Python','Frame'],
   'second column': [5, 9, 7, 10]})

supe = pd.DataFrame({
    'compra': ['','Arroz', 'Feijão', 'Leite', 'Óleo', 'Açúcar', 'Café'],
    'preço': ['',5.50, 16.64, 3.29, 6.99, 3.60, 18.50]})





st.title("Meu primeiro dash")

st.subheader(nome)

st.write("Ola", nome, "idade",idade)

st.write(df)
st.write(supe)

item = st.selectbox("Selecione um item do supermercado:", supe['compra'] )

if item != '':
    
    preco_item = supe[supe["compra"] == item]["preço"].values[0]

    
    st.success(f"O preço do {item} é R$ {preco_item}")  
    qtd = st.number_input("Quantidade:", min_value=1, value=1)
    total = preco_item * qtd
    st.write(f"Preço Total: R$ {total}")
    
    
