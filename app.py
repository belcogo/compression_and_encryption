import streamlit as st
from src.hamming import Hamming
from src.repeticao_ri import RRepetition

st.title("Detecção e Correção de Erros")

hamming = Hamming()

col2, col3 = st.columns(2)

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

if selected_algorithm == 'Código de repetição Ri':
  text_input_r = st.text_input(
    label="Digite o valor de R (repetições) desejado",
    value=0,
  )
  rRepetition = RRepetition(int(text_input_r))

text_input = st.text_area(
  label="Digite seu codeword ou símbolos",
)

submit = st.button("Submeter")


if submit:
  st.header(f"Resultado:")
  if selected_algorithm == "Hamming (7,4)" and selected_method == "Codificar":
    encoded_result = hamming.encode(text_input)
    st.subheader(encoded_result)
  elif selected_algorithm == "Hamming (7,4)" and selected_method == "Decodificar":
    decoded_result = hamming.decode(text_input)
    st.subheader(decoded_result)
  elif selected_algorithm == 'Código de repetição Ri':
    if selected_method == "Codificar":
      repetition = text_input_r
      encoded_result = rRepetition.transmit(text_input)
      st.subheader(encoded_result)
    elif selected_algorithm == 'Código de repetição Ri' and selected_method == "Decodificar":
      repetition = text_input_r
      dencoded_result = rRepetition.decode(text_input)
      st.subheader(dencoded_result)
  