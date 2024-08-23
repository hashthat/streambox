import streamlit as st


def main():
    st.set_page_config(page_title="Chatting is fun when you get to chat with your favorite books!", page_icon=":books:")

    st.header("chat with multiple PDFs! :books:")
    st.text_input("Ask about the current document:")

    with st.sidebar:
        st.subheader("Your Docs")
        st.file_uploader("Upload your PDFS here and click on 'Process'")
        st.button("Process")


    if __name__ == '__main__':
        main()