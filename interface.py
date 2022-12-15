import streamlit as st

from twitch import GetClip
from utils import markdown

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

    markdown("Date du début :", center=True, sidebar=True, size="20px")
    cols = st.sidebar.columns([1,2])
    with cols[0]:
        datestart = st.date_input("Date :", key="Dstart")
    with cols[1]:
        hourstart = st.time_input("Heure :", key="Hstart")
        
    markdown("Date de fin :", center=True, sidebar=True, size="20px")
    cols = st.sidebar.columns([1,2])
    with cols[0]:
        dateend = st.date_input("Date :", key="Dend")
    with cols[1]:
        hourend = st.time_input("Heure :", key="Hend")

    params = {}
    if (datestart != "")&(hourstart != ""): params["started_at"] = str(datestart) + "T" + str(hourstart) + "Z"
    if (dateend != "")&(hourend != ""): params["ended_at"] = str(dateend) + "T" + str(hourend) + "Z"

    for i in range(top):
        markdown(text=f"Top {i+1}", center=True, size="30px")
        markdown(
            f"Title : {getclip.url_best_clip_streamer(streamer_name, top=top, params=params)[i].get('title')}", 
            size="15px"
            )
        markdown(getclip.url_best_clip_streamer(streamer_name, top=top, params=params)[i].get("url"))

elif option=="Catégorie du jeu":
    game_name = st.sidebar.text_input("Entrer la catégorie du jeu :")
    if game_name == "": st.stop()

    top = st.sidebar.number_input(
        "Le top combien du clip le plus vu ?", step=1, value=1
        )

    markdown("Date du début :", center=True, sidebar=True, size="20px")
    cols = st.sidebar.columns([1,2]) #(AAAA-MM-JJTHH:MM:SSZ)
    with cols[0]:
        datestart = st.date_input("Date :", key="Dstart", value=None)
    with cols[1]:
        hourstart = st.time_input("Heure :", key="Hstart", value=None)
        
    markdown("Date de fin :", center=True, sidebar=True, size="20px")
    cols = st.sidebar.columns([1,2])
    with cols[0]:
        dateend = st.date_input("Date :", key="Dend", value=None)
    with cols[1]:
        hourend = st.time_input("Heure :", key="Hend", value=None)

    params = {}
    if (datestart != "")&(hourstart != ""): params["started_at"] = str(datestart) + "T" + str(hourstart) + "Z"
    if (dateend != "")&(hourend != ""): params["ended_at"] = str(dateend) + "T" + str(hourend) + "Z"

    for i in range(top):
        markdown(text=f"Top {i+1}", center=True, size="30px")
        markdown(
            f"Title : {getclip.url_best_clip_game(game_name, top=top, params=params)[i].get('title')}", 
            size="15px"
            )
        markdown(getclip.url_best_clip_game(game_name, top=top, params=params)[i].get("url"), size="15px")

    # st.video(
    #     getclip.url_best_clip_game(game_name)
    #     )

# st.write("Affichage de la vidéo")
# st.video(
#     "https://www.youtube.com/watch?v=woRskojCCRU",
#     format="video/3gpp2"
#     )

#https://clips.twitch.tv/ThoughtfulPhilanthropicYakinikuDBstyle-l0vdnziKRWGRQcoF
