import streamlit as st
from constants import navigation, hackathons

st.set_page_config(page_title="Hackathons", page_icon="💻",initial_sidebar_state="collapsed",layout="wide") #
margin_r,body,margin_l = st.columns([0.4, 3, 0.4])

with body:
    navigation()

    st.header("💻 Hackathons",divider='rainbow')
    st.write("")

    def hackathon_unit(hackathon):
        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            st.subheader(hackathon["name"])
        with col3:
            st.write("")
            st.markdown("######   " + hackathon["date"])
        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            st.markdown("##### " + hackathon["challenge"])
        with col3:
            st.markdown("######   " + hackathon["location"])
        st.write(hackathon["content"])
        st.link_button("Visit Hackathon Website", hackathon["link"])
        if "images" in hackathon:
            columns = st.columns([image["width"] for image in hackathon["images"]])
            for i in range(len(hackathon["images"])):
                image = hackathon["images"][i]
                with columns[i]:
                    st.image(image["path"], width=500 * image["width"])
                    
        st.divider()

    for hackathon in hackathons:
        hackathon_unit(hackathon)







