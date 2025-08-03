import streamlit as st
from constants import navigation, info, linkedin_link, skill_col_size

st.set_page_config(page_title="Main Page", page_icon="🏠", layout="wide",initial_sidebar_state="collapsed") 

margin_r,body,margin_l = st.columns([0.4, 3, 0.4])

with body:
    navigation()
        
    #main page --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    st.header("About Me",divider='rainbow')

    col1, col2, col3 = st.columns([1.3, 0.2, 0.7])

    with col1:
        st.write(info['brief'])
        st.markdown(f"###### 👩‍💻 Name: {info['name']}")
        st.markdown(f"###### 🎓 MSc: {info['study_msc']}")
        st.markdown(f"###### 🎓 BSc: {info['study_bsc']}")
        st.markdown(f"###### 📍 Location: {info['location']}")
        st.markdown(f"###### 📚 Interest: {info['interest']}")
        st.markdown(f"###### 👀 Linkedin: {linkedin_link}")
        
        with open("src/ekaterina-ustuikhina-resume.pdf", "rb") as file:
            pdf_file = file.read()

        st.download_button(
            label="Download my resume",
            data=pdf_file,
            file_name="ekaterina-ustuikhina-resume.pdf",
            mime="application/pdf")

    with col3:
        st.image("src/images/ekaterina_photo.jpeg", width=350)

    # skills --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    st.subheader("My skills ⚒️",divider='rainbow')

    for skill_group in info['skills']:
        st.write(f"##### {skill_group}")