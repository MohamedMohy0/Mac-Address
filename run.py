import streamlit as st
from getmac import get_mac_address

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
st.title("Get Mac Address")

but=st.button("Get The Mac")
if but:
    mac=get_mac_address()
    st.info(f"Your Mac Address is : {mac}")
