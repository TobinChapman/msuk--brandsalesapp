import streamlit as st

# Create an empty space
result_area = st.empty()

# Calculate the result
input_value = st.slider("Select a value", 0, 100, 50)
result = input_value * 2

# Display the result in the empty space
result_area.write("The result is {}".format(result))