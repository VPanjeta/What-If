import streamlit as st

def init_base_template():
    st.set_page_config(page_title='What If?', page_icon=':thinking_face:', layout='wide', initial_sidebar_state='auto')
    st.sidebar.header('What If? 🤔')
    st.sidebar.markdown('---')
    st.sidebar.markdown('## About')
    st.sidebar.markdown("""Welcome to What If?: Rewriting History with Alternate Facts! Our app takes you on a wild ride
     through time and space, exploring alternate histories that challenge your understanding of the past, present, 
     and future.

We're here to entertain and educate, with engaging content that transports you to new worlds, 
introduces fascinating characters, and challenges you to think differently. Alternate facts are those little nuggets of 
information that, if they had been different, could have changed the course of history. We explore everything from 
dinosaurs to aliens, ancient myths to modern-day conspiracy theories.
""")

    st.header('What If? 🤔')
    st.subheader('Rewriting History with Alternate Facts')
    st.markdown('---')


