from model import HistoryModel
from base_template import init_base_template
import streamlit as st


if __name__ == "__main__":
    init_base_template()
    prompt = st.text_input("What if?",
                           help="Give an alternate historical fact and see how the world would have changed.")
    model = HistoryModel()
    with st.spinner("Writing history..."):
        response = model.get_response(prompt, [])
        st.markdown(response.content)

