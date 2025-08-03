import streamlit as st
from constants import navigation, experience


st.set_page_config(page_title="Experience", page_icon="📚", layout="wide",initial_sidebar_state="collapsed")
margin_r,body,margin_l = st.columns([0.4, 3, 0.4])

with body:
    navigation()

    st.header("📚 Experience",divider='rainbow')
    st.write("")

    def experience_unit(title, position, date, location, content, link):
        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            st.subheader(title)
        with col3:
            st.write("")
            st.markdown("######   " + date)
        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            st.markdown("##### " + position)
        with col3:
            st.markdown("######   " + location)
        st.write(content)
        st.link_button(f"Visit {link['name']}", link["url"])
        st.divider()

    for exp in experience:
        experience_unit(exp["company"], exp["role"], exp["date"],exp["location"],exp["content"],exp["link"])



