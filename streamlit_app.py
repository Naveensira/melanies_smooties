# Import python packages
import streamlit as st
#from snowflake.snowpark.context import get_active_session
cnx=st.connection("snowflake")
session=cnx.session()

# Write directly to the app
st.title(f":cup_with_straw: Customize your smoothie! :cup_with_straw: {st.__version__}")
st.write ("""Choose your fruits you want to custom Smoothie!""")
#st.write(
#  """Replace this example with your own code!
#  **And if you're new to Streamlit,** check
#  out our easy-to-follow guides at
#  [docs.streamlit.io](https://docs.streamlit.io).
#  """
#)

#import streamlit as st
#option = st.selectbox(
#    " What is your favorite fruits?",
#    ("Banana", "Strawberries", "Peaches"),
#)

#st.write("Your favorite fruit is:", option)


name_on_order = st.text_input("Name on Smoothie")
st.write("The name on your smoothy will be", name_on_order)

from snowflake.snowpark.functions import col

session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
st.dataframe(data=my_dataframe, use_container_width=True)

Ingredients_list = st.multiselect(
    "choose upto 5 ingredients :"
    , my_dataframe
    ,max_selections=5
)

time_to_insert =st.button ('submit Order')

if Ingredients_list:
    st.write(Ingredients_list)
    st.text(Ingredients_list)

    Ingredients_string = ''

    for fruit_chosen in Ingredients_list:
        Ingredients_string += fruit_chosen + ' '


    #st.write(Ingredients_string)
    
    my_insert_stmt = """ insert into smoothies.public.orders(name_on_order,ingredients)
                    values ('""" + name_on_order + """','""" +Ingredients_string  + """')"""

    #st.write(my_insert_stmt)
    #time_to_insert =st.button ('submit Order')

    if time_to_insert:
       session.sql(my_insert_stmt).collect()
        
       st.success('Your Smoothie is ordered!', icon="✅")
