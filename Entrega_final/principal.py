import streamlit as st
import entrega as simulador
import resumen_cod as res
import var_est as prime
import primer as vdj

PAGES = {
    "¿Qué es un videojuego serio?" : vdj,
    "Resumen del codigo hecho" : res,
    "Resultados del código" : prime,
    "Simulador del Volcán" : simulador,
    
    
}

st.sidebar.title('Índice:')

opcion = st.sidebar.radio("", list(PAGES.keys()))

st.title("Entregable Final: ¿Dónde está mi proyectil?")

st.image("logo1.jpg")

st.markdown("Andrea Yela González A01025250")

page = PAGES[opcion]
page.prin()