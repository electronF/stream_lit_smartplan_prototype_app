import json
import time

import pandas as pd
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
    with sub_cols[0]:
        if (
                submitted
                and (
                    (strengths_str != None and strengths_str.strip() != "") 
                    or (challenges_str != None and challenges_str.strip() != "") 
                    or needs_str != None and needs_str.strip() != ""
                )
            ): 
            s_time = time.time()
            ui_components.sub_title('----- Prompt Forces -----')
            ui_components.sub_title('----- Prompt Defis -----')

            ui_components.sub_title('----- Prompt Besoins -----')
            ui_components.progress_tools(etape, 1, 10, s_time)

            ui_components.sub_title('>> Obtenir une liste des forces, des défis et des besoins <<')
            ui_components.progress_tools(etape, 2, 10, s_time)
            
            success = True
            if success == True:
                # components.success_message('Lists obtenu avec success')
                ui_components.sub_title('-------- Liste des forces --------')
                # components.ouptut_message("\n".join(map(lambda value: '-> '+value, strengths)))
                ui_components.sub_title('-------- Liste des defis --------')
                # components.ouptut_message("\n".join(map(lambda value: '-> '+value, challenges)))
                ui_components.sub_title('-------- List des besoins --------')
                # components.ouptut_message("\n".join(map(lambda value: '-> '+value, needs)))
                
                ui_components.sub_title('>> Obtention du profil structure <<')
                ui_components.success_message('Success')
                
                ui_components.progress_tools(etape, 2, 10, s_time)
                ui_components.sub_title('-------- Profil --------')
               
                ui_components.sub_title('>> Obtention des embeddings du profil <<')
                ui_components.progress_tools(etape, 3, 10, s_time)

                ui_components.sub_title('>> Obtention des IDs des profils similaraires')
                ui_components.success_message('Succes')
                ui_components.progress_tools(etape, 4, 10, s_time)

                ui_components.sub_title("---- IDs des profils similaires ------")
                ui_components.ouptut_message(";  ")

                ui_components.sub_title('>> Obtention des objectifs candidats <<')

                ui_components.success_message('Obtenus')
                ui_components.progress_tools(etape, 5, 10, s_time)

                ui_components.sub_title("---- Objectifs candidats ------")
                
                # Utilise ceci pour creer un dataframe
                # st.dataframe()


                ## Here add categories and sub categories

                ui_components.sub_title('>> Creation du prompts avec les objectifs candidats <<')
                ui_components.success_message('Prompt cree')
                ui_components.sub_title('---------- Prompt ------------')

                ui_components.progress_tools(etape, 6, 10, s_time)


                # components.sub_title('>> Obtention des objectifs avec claude <<')
                ui_components.progress_tools(etape, 7, 10, s_time)

                ui_components.sub_title('>> Obtention des objectifs avec gemini <<')
                ui_components.progress_tools(etape, 8, 10, s_time)

                ui_components.sub_title('>> Obtention des objectifs avec gpt <<')
                ui_components.progress_tools(etape, 9, 10, s_time)

                ui_components.sub_title('>> Fusion des reponses <<')
                ui_components.progress_tools(etape, 10, 10, s_time)
                ui_components.success_message('Fusion reussie')
                ui_components.ouptut_message('La liste des recommandation sont disponibles ci-dessous')
                
                ui_components.sub_title('>> Objectifs + Toutes les categories ou ils se trouvent <<')
                
                ui_components.sub_title('>> Objectifs + Objectifs similaires <<')

            else:
                error = False
                if  error == False:
                    ui_components.sub_title_error('Erreur 1')
                else:
                    ui_components.sub_title_error('Erreur 2')
        else:
            pass
if __name__ == "__main__":
    main()