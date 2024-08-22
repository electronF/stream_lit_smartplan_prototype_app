import time

import streamlit as st

import ui_components 
import ui_modules


def main():
    st.set_page_config(
        page_title="Recommandations Utilisateur-Utilisateur",
    )

    css_style = open('./style.css', 'r').read()
    
    st.markdown(f'<style>{css_style}</style>', unsafe_allow_html=True)
    st.sidebar.header("Recommandations d'items basees sur le profil des utilisateurs")
    
    
    with st.sidebar:
        ui_components.simple_title("Entree les information sur le profil de l'etudiant")
        strengths_str, challenges_str, needs_str, submitted = ui_modules.static_form()

    ui_components.title("Processus de recommandation")
    etape = st.empty()
    sub_cols = st.columns(1, gap="medium")
    
    ui_components.progress_tools(etape, 0, 10, time.time())

if __name__ == "__main__":
    main()