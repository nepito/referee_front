import time
import pandas as pd
import streamlit as st

PAGE_TITLE = "Fut Sala | NIES"
PAGE_ICON = "🛂"
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

event, fix_data = st.tabs(["Eventos", "Curación de datos"])

matches = {
    "Eco Pasto vs Vaqueros": ["Eco Pasto", "Vaqueros FC"],
    "Backpack Boyz vs Kingstone": ["Backpack Boyz", "Kingstone"],
    "Troncos vs Mesebrios": ["Troncos FC", "Mesebrios"]
}
jugadores = pd.read_csv("./tests/data/jugadores.csv")
team_list: list = ["Equipo A", "Equipo B"]
def get_players_from_match(fixture):
    teams = matches[fixture]
    return {
        teams[0]: list(jugadores[jugadores.equipo == teams[0]].jugador),
        teams[1]: list(jugadores[jugadores.equipo == teams[1]].jugador)
        }

players = {
    "Equipo A": ["Hector", "Puma", "Nepo"],
    "Equipo B": ["Peso Pluma", "Mirra", "Naim"]
}

ph = st.empty()
with event:
    #N = 20*60
    #for secs in range(0,N):
    #    mm, ss = secs//60, secs%60
    #    ph.metric("Countdown", f"{mm:02d}:{ss:02d}")
    #    time.sleep(1)
    secs = 27
    fixture = st.selectbox("Selecciona el partido:", list(matches.keys()))
    players = get_players_from_match(fixture)
    if 'events' not in st.session_state:
        st.session_state.events = []
    team_list = list(players.keys())
    team = st.selectbox("Selecciona al equipo:", team_list)
    player_list = players[team]
    player = st.selectbox("Selecciona al anotador:", player_list)
    assister = st.selectbox("Selecciona al asistidor:", ["No hubo", *player_list])
    if st.button("Registrar evento"):
        st.session_state.events.append(
            {"team": team, "player": player, "assister": assister, "match": fixture, "time": secs}
            )
        st.write(st.session_state.events)


with fix_data:
    st.markdown("Aquí deberemos corregir")
    events = pd.DataFrame.from_dict(st.session_state.events)
    edited_df = st.data_editor(events, num_rows="dynamic")


st.markdown("Made with 💖 by [nies.futbol](https://nies.futbol)")
