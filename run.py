import streamlit as st
from getmac import get_mac_address


st.title("Get Mac Address")

but=st.button("Get The Mac")
if but:
    mac=get_mac_address()
    st.info(f"Your Mac Address is : {mac}")