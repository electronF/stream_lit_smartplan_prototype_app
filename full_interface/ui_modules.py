import streamlit as st

def static_form():
    with  st.form("my_form"):
        strengths_str  = st.text_area("Entrer les forces de l'etudiant ")
        challenges_str  = st.text_area("Entrer les defis de l'etudiant ")
        needs_str  = st.text_area("Entrer les besoin de l'etudiant ")
        submitted = st.form_submit_button("Recommander")
        return strengths_str, challenges_str, needs_str, submitted
    return None, None, None, None