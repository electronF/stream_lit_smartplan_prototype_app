import time

import streamlit as st


def title(text:str):
    obj =  st.write(
        f"""
        <div style="width:100%; color: blue; padding:10px; align-text:center; font-size:32px; font-weight:bold;">
            {text}  
        </div>
        """, 
        unsafe_allow_html=True
    )
    return obj

def sub_title(text:str):
    obj =  st.write(
        f"""
        <div style="width:100%; color: blue; padding:10px; align-text:center; font-size:16px; font-weight:bold;">
            {text}  
        </div>
        """, 
        unsafe_allow_html=True
    )
    return obj

def sub_title_success(text:str):
    obj =  st.write(
        f"""
        <div style="width:100%; color: green; padding:10px; align-text:center; font-size:16px; font-weight:bold;">
            {text}  
        </div>
        """, 
        unsafe_allow_html=True
    )
    return obj

def sub_title_error(text:str):
    obj =  st.write(
        f"""
        <div style="width:100%; color: red; padding:10px; align-text:center; font-size:16px; font-weight:bold;">
            {text}  
        </div>
        """, 
        unsafe_allow_html=True
    )
    return obj


def simple_title(text:str):
    obj =  st.write(
        f"""
        <div style="width:100%; padding:10px; align-text:center; font-size:16px;">
            {text}  
        </div>
        """, 
        unsafe_allow_html=True
    )
    return obj


def step_message(text:str):
    obj =  st.write(
        f"""
        <div style="width:100%; color:rgb(240, 240, 240); padding:10px; border-radius:0.2rem; background-color:rgb(28, 127, 208); align-text:center; font-size:16px;">
            {text}  
        </div>
        """, 
        unsafe_allow_html=True
    )
    st.write("\n")
    return obj

def success_message(text:str):
    obj = st.write(
        f"""
        <div style="width:100%; color:rgb(240, 240, 240); padding:10px; border-radius:0.2rem; background-color:rgb(0, 171, 105); align-text:center; font-size:16px;">
            {text}  
        </div>
        """, 
        unsafe_allow_html=True
    )
    st.write("\n")
    return obj

def ouptut_message(text:str):
    tab = "&nbsp;&nbsp;&nbsp;&nbsp;" 
    new_text = text.replace("\n", "<br \>").replace("\t", tab)
    obj = st.write(
        f"""
        <div style="width:100%; color:rgb(40, 40, 40); padding:10px; border-radius:0.5rem; border:2px soild gray; background-color:rgb(200, 200, 200); align-text:center; font-size:16px;">
            {new_text}  
        </div>
        """, 
        unsafe_allow_html=True
    )
    st.write("\n")
    return obj

def error_message(text:str):
    new_text = text.replace("\n", "<br \>")
    st.write(
        f"""
        <div style="width:100%; color:rgb(250, 250, 250); padding:10px; border-radius:0.5rem; border:2px soild gray; background-color:rgb(246, 56, 56); align-text:center; font-size:16px;">
            {new_text}  
        </div>
        """, 
        unsafe_allow_html=True
    )
    st.write("\n")


def progress_tools(updater:st, current_step:int, max_step:int, start_time:float):
    code = """
    <div style="display:flex; padding:10px;">
        <span style="margin-left:auto; margin-right:2rem;">
            <span style="font-weight:bold;">Progression:</span> 
            <span style="color:blue"> {}/{} </span>
        </span>
        <span>
            <span style="font-weight:bold;">temps:</span>
            <span style="color:blue"> {:.0f}s </span>
        </span>
    </div>
    """.format(current_step, max_step, time.time()-start_time)
    updater.write(code, unsafe_allow_html=True)