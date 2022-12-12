import streamlit as st

from twitch import GetClip

option = st.sidebar.selectbox(
    'Selectionner le filtre souhaité',
    ('None','Streameur', 'Catégorie du jeu'))

if not option: st.stop()

getclip=GetClip()
if option=="Streameur":
    streamer_name = st.sidebar.text_input("Entrer le nom du streamer :")
    if streamer_name == "": st.stop()

    top = st.sidebar.number_input(
        "Le top combien du clip le plus vu ?", step=1, value=1
        )
    params = {}

    datestart = st.sidebar.text_input("Date du début (AAAA-MM-JJTHH:MM:SSZ)")
    if datestart != "": params["started_at"] = datestart
    dateend = st.sidebar.text_input("Date de fin (AAAA-MM-JJTHH:MM:SSZ)")
    if dateend != "": params["ended_at"] = dateend

    st.title("Clip le plus vu pour le streamer :")
    st.write(getclip.url_best_clip_streamer(
        streamer_name, top=top, params=params
        ))

elif option=="Catégorie du jeu":
    game_name = st.sidebar.text_input("Entrer la catégorie du jeu :")
    if game_name == "": st.stop()

    top = st.sidebar.number_input(
        "Le top combien du clip le plus vu ?", step=1, value=1
        )

    st.title("Clip le plus vu pour le streamer :")
    st.write(getclip.url_best_clip_game(game_name, top=top))

    # st.video(
    #     getclip.url_best_clip_game(game_name)
    #     )

st.write("Affichage de la vidéo")
st.video(
    "https://www.twitch.tv/videos/1674565174?t=4h5m19s",
    #format="video/mp"
    )

#https://clips.twitch.tv/ThoughtfulPhilanthropicYakinikuDBstyle-l0vdnziKRWGRQcoF
