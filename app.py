import streamlit as st
from src.hamming import Hamming

st.title("Detecção e Correção de Erros")

hamming = Hamming()

col2, col3 = st.columns(2)

text_input = st.text_area(
  label="Digite seu codeword ou símbolos",
)

with col2:
  selected_method = st.radio(
    label = "Selecione a ação:",
    options=["Codificar", "Decodificar"],
  )

with col3:
  selected_algorithm = st.radio(
    label = "Qual método de codificação você deseja?",
    options=["Código de repetição Ri", "Hamming (7,4)"],
  )

submit = st.button("Submeter")

if submit:
  st.header(f"Resultado:")
  if selected_algorithm == "Hamming (7,4)" and selected_method == "Codificar":
    encoded_result = hamming.encode(text_input)
    st.subheader(encoded_result)