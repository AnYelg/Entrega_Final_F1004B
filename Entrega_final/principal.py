import streamlit as st
import entrega as simulador
import resumen_cod as res
import var_est as prime

PAGES = {
    "Resumen del codigo hecho" : res,
    "Resultados del primer código" : prime,
    "Simulador del Volcán" : simulador,
    
}

st.sidebar.title('Índice:')

opcion = st.sidebar.radio("", list(PAGES.keys()))

st.title("Entregable Final")

st.markdown("Andrea Yela González A01025250")

page = PAGES[opcion]
page.prin()