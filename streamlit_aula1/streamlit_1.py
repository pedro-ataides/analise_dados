import streamlit as st
import pandas as pd

st.set_page_config(page_title= "Pibble mart", page_icon='https://i.scdn.co/image/ab67616d0000b27332fdd9cfd9c3b89028ff58e6', layout="centered")

nome = "Pedro"
idade = "17"

df = pd.DataFrame({
   'first column': ['Português','Matemática','Python','Frame'],
   'second column': [5, 9, 7, 10]})

supe = pd.DataFrame({
    'compra': ['','Arroz', 'Feijão', 'Leite', 'Óleo', 'Açúcar', 'Café'],
    'preço': ['',5.50, 16.64, 3.29, 6.99, 3.60, 18.50]})

if "sacola_compras" not in st.session_state:
    st.session_state.sacola_compras = []

def sacola(item, qtd, total):
    nova_compra = {"Item": item, "Quantidade": qtd, "Total (R$)": total}
    # Adiciona o item à lista na memória da sessão
    st.session_state.sacola_compras.append(nova_compra)
    st.toast(f"{item} adicionado à sacola!")  # Alerta visual rápido


st.title("Meu primeiro dash")

st.subheader(nome)

st.write("Ola", nome, "idade",idade)

st.write(df)
st.write(supe)

item = st.selectbox("Selecione um item do supermercado:", supe['compra'] )

if item != '':
    
    preco_item = supe[supe["compra"] == item]["preço"].values[0]

    
    st.success(f"O preço do {item} é R$ {preco_item}")  
    qtd = st.number_input("Quantidade:", min_value=1, value=1,)
    total = preco_item * qtd
    st.write(f"Preço Total: R$ {total}")
    if st.button("Confirmar Adição"):
      sacola(item, qtd, total) 
      
    if st.session_state.sacola_compras:
     st.write("---")
    st.subheader("Sua Sacola Atual:")
    df_sacola = pd.DataFrame(st.session_state.sacola_compras)
    st.dataframe(df_sacola)

    total_geral = df_sacola["Total (R$)"].sum()
    st.info(f"**Valor total da sacola:** R$ {total_geral:.2f}")
        






    st.write("---")
    st.subheader("Calculadora de Troco (Pagamento em Dinheiro)")

    col1, col2 = st.columns(2)
    
    with col1:

        st.metric(label="Valor total a pagar", value=f"R$ {total_geral:.2f}")
        
    with col2:

        valor_pago = st.number_input("Valor pago em dinheiro (R$)", value=0.0, step=1.0)
        

    if st.button("Calcular Troco", type="primary"):
        troco = None

        if valor_pago < total_geral:
            st.error("Erro: O valor pago em dinheiro é menor do que o valor total da sacola!")
        else:

            troco = valor_pago - total_geral
            

        if troco is not None:
            st.success(f"**Resultado:** O troco do cliente é de R$ {troco:.2f}")