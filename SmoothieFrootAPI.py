import streamlit as st
import requests
smoothiefroot_response = requests.get(https://my.smoothiefroot.com/api/fruit/watermelon")  
#st =(smoothiefroot_response.json())
sf_df = st.dataframe(data=smoothiefroot_response.json(),use_container_width=True)

# import streamlit as st
# import requests
# import pandas as pd  # Added to help format the data correctly

# # 1. Fetch the data from the API
# smoothiefroot_response = requests.get("https://my.smoothiefroot.com/api/fruit/watermelon")  

# # 2. Convert the response to JSON
# fruit_json = smoothiefroot_response.json()

# # 3. Convert JSON into a Pandas DataFrame so Streamlit can display it as a table
# # (Using [fruit_json] wraps the single fruit dictionary into a list format)
# df = pd.DataFrame([fruit_json])

# # 4. Display the clean data frame
# sf_df = st.dataframe(data=df, use_container_width=True)





