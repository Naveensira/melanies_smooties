# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col, when_matched
from snowflake.snowpark.context import get_active_session

# Get the current credentials session
session = get_active_session()

# Write directly to the app header
st.title(":cup_with_straw: Pending Smoothie Orders :cup_with_straw:")
st.write("Orders that need to be filled:")

# 1. Fetch the data as a pandas DataFrame
my_dataframe = session.table("smoothies.public.orders") \
    .filter(col("ORDER_FILLED") == False) \
    .to_pandas()

# 2. Display and process the data in your Streamlit UI
if not my_dataframe.empty:
    # Use data_editor to allow inline editing of columns
    editable_df = st.data_editor(my_dataframe, use_container_width=True)

    submitted = st.button("Submit Changes")
    
    if submitted:
        og_dataset = session.table("smoothies.public.orders")
        edited_dataset = session.create_dataframe(editable_df)
        
        try:
            # Merge the edited rows back into the main table
            og_dataset.merge(
                edited_dataset,
                (og_dataset['ORDER_UID'] == edited_dataset['ORDER_UID']),
                [when_matched().update({'ORDER_FILLED': edited_dataset['ORDER_FILLED']})]
            )
            
            st.success("Orders successfully updated!", icon="👍")
            # Force the app to rerun so filled orders vanish immediately
            st.rerun()
            
        except Exception as e: 
            st.error(f"Something went wrong while updating: {e}")

else:
    st.success("There are no pending orders right now.", icon="👍")
