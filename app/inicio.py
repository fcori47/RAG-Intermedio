import chromadb, os
import streamlit as st
from chromadb.config import Settings

CHROMA_SETTINGS = chromadb.HttpClient(host=os.getenv('HOST'), port=os.getenv('PORT'), settings=Settings(allow_reset=True, anonymized_telemetry=False))

st.title('RAG Intermedio')

if st.button('Test VectorDB'):
    st.write(CHROMA_SETTINGS.heartbeat() )