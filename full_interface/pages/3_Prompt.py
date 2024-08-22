import json

import pandas as pd

import streamlit as st

import ui_components 


def main():
    st.set_page_config(
        page_title="Recommandations Utilisateur-Utilisateur",
    )

    css_style = open('./style.css', 'r').read()
    st.markdown(f'<style>{css_style}</style>', unsafe_allow_html=True)
    st.sidebar.header("Exemples de prompts")

    ui_components.title("Quelque exemples de prompts")
    prompts_str = open("./src/prompt.json", "r").read()
    prompts = pd.DataFrame(json.loads(prompts_str))
    st.dataframe(prompts)
    


if __name__ == "__main__":
    main()