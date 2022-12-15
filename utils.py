def get_token(params_for_token = {
    "response_type": "token",
    "client_id": "fmxbop0687cv14jk7j1egwrb9p7rml",
    "redirect_uri": "https://localhost/Twitch/OAuthTwitch/Token",
    "scope": "user:read:broadcast",
    "client_secret": "y3g8wy62hvdmw8b6zes5w1psa9fna8"
    }):
    import requests
    return "4f3xlvg8nbyxbpzgo8b2dbfick1rvn"
    return requests.post(
    f"https://id.twitch.tv/oauth2/authorize?response_type={params_for_token.get('response_type')}&client_id={params_for_token.get('client_id')}&redirect_uri={params_for_token.get('redirect_uri')}&scope={params_for_token.get('scope')}",
    data={"grant_type": "client_credentials"},
    auth=(params_for_token.get("client_id"),params_for_token.get("client_secret"))
    ).json()

def markdown(text, center=False, size="30px", color=None, sidebar=False):
    import streamlit as st
    text_to_center = ("<div style='text-align:center';>", "</div>") if center else ("", "")
    if sidebar:
        st.sidebar.markdown(
            f"{text_to_center[0]}<span style='font-size:{size};color:{color};'>{text}</span>{text_to_center[1]}",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"{text_to_center[0]}<span style='font-size:{size};color:{color};'>{text}</span>{text_to_center[1]}",
            unsafe_allow_html=True
        )