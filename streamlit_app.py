import pandas as pd
import streamlit as st

PAGE_TITLE = "Fut Sala | NIES"
PAGE_ICON = "🛂"
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

event, fix_data = st.tabs(["Eventos", "Curación de datos"])

team_list: list = ["Equipo A", "Equipo B"]
players = {
    "Equipo A": ["Hector", "Puma", "Hector"],
    "Equipo B": ["Peso Pluma", "Mirra", "Naim"]
}

with event:
    team = st.selectbox("Selecciona al equipo:", player_list)
    player_list = players[team]
    player = st.selectbox("Selecciona al anotador:", player_list)
    assister = st.selectbox("Selecciona al asistidor:", player_list)

with fix_data:
    


st.markdown("Made with 💖 by [nies.futbol](https://nies.futbol)")
