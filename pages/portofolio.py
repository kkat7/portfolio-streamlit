import streamlit as st
import streamlit.components.v1 as components
from constants import navigation, portfolio
from streamlit_pdf_viewer import pdf_viewer

# page config ----------------------------------------------------------------
st.set_page_config(page_title="Portfolio", page_icon="🎨", layout="wide",initial_sidebar_state="collapsed")
margin_r,body,margin_l = st.columns([0.4, 3, 0.4])

with body:
   navigation()
   st.header("🎨 Portfolio",divider='rainbow')

   def portfolio_component(project):
      st.subheader(project['name'], divider='grey')
      st.write(project['description'])

      if 'links' in project:
         for link in project['links']:
            st.link_button(f"{link['action']} {link['name']}", link['link'])
      
      if 'files' in project:
         for file in project['files']:
            if file['type'] == 'pdf':
               with st.expander(file['name']):
                  pdf_viewer(
                     input=f"{file['path']}",
                     key=f"{project['name']}-{file['name']}",
                     width=700,
                     height=1000,
                     zoom_level=file['zoom_level'],
                     viewer_align="center",
                     show_page_separator=True,
                  )

      # Sections divider
      st.text("")
      st.text("")
      
   for project in portfolio:
      portfolio_component(project)