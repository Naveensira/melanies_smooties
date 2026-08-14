import streamlit as st
import requests
smoothiefroot_response = requests.get("https://my.smoothiefroot.com/api/fruit/watermelon](https://my.smoothiefroot.com/api/fruit/watermelon)")  
#st =(smoothiefroot_response.json())
sf_df = st.dataframe(data=smoothiefroot_response.json(),use_container_width=True)




