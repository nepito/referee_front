import pandas as pd
import streamlit as st

PAGE_TITLE = "Fut Sala | NIES"
PAGE_ICON = "🛂"
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

event, fix_data = st.tabs(["Eventos", "Curación de datos"])

team_list: list = ["Equipo A", "Equipo B"]
players = {
    "Equipo A": ["Hector", "Puma", "Nepo"],
    "Equipo B": ["Peso Pluma", "Mirra", "Naim"]
}

with event:
    if 'events' not in st.session_state:
        st.session_state.events = []
    team = st.selectbox("Selecciona al equipo:", team_list)
    player_list = players[team]
    player = st.selectbox("Selecciona al anotador:", player_list)
    assister = st.selectbox("Selecciona al asistidor:", ["No hubo", *player_list])
    if st.button("Registrar evento"):
        st.session_state.events.append({"team": team, "player": player, "assister": assister})
        #b = [{"team": team, "player": player, "assister": assister}, *events]
        st.write(st.session_state.events)
        #st.write(b)

with fix_data:
    st.markdown("Aquí deberemos corregir")
    st.title('Counter Example')
    if 'count' not in st.session_state:
        st.session_state.count = 0

    increment = st.button('Increment')
    if increment:
        st.session_state.count += 1

    st.write('Count = ', st.session_state.count)
    


st.markdown("Made with 💖 by [nies.futbol](https://nies.futbol)")
