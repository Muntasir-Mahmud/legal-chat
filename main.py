import streamlit as st
from dotenv import load_dotenv


def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with legal ai guru",
                       page_icon=":books:")
    st.header("Chat with legal ai guru")
    st.text_input("Ask your questions.")

    with st.sidebar:
        st.subheader("legal documnets")
        pdf_docs = st.file_uploader("Upload your PDFs", accept_multiple_files=True)
        if st.button("Process"):
            pass

if __name__ == "__main__":
    main()
