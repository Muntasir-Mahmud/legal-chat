import streamlit as st
from dotenv import load_dotenv

from utils import get_pdf_text, get_text_chunks


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
            with st.spinner("Processing"):
                # Get pdf text
                raw_text = get_pdf_text(pdf_docs)

                # Get the text chunks
                text_chunks = get_text_chunks(raw_text)

                # Create vector store
                vectorstore = get_vectorstore(text_chunks)

                # create conversation chain
                st.session_state.conversation = get_conversation_chain(vectorstore)

if __name__ == "__main__":
    main()
