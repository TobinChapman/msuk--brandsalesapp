import streamlit as st

# Add a selectbox to the sidebar
option = st.sidebar.selectbox(
    'Which number do you like best?',
     ['1', '2', '3', '4'])

'You selected:', option

# Use a button to confirm the selection
if st.sidebar.button('Confirm'):
    st.sidebar.write('You confirmed the selection')