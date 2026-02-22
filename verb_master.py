import streamlit as st
import spacy

# Load grammar model
@st.cache_resource
def load_nlp():
    # link ကနေ ဒေါင်းထားတဲ့ model ကို နာမည်အတိုင်း ခေါ်သုံးမယ်
    return spacy.load("en_core_web_sm")

nlp = load_nlp()

st.title("📖 Thuta's Oxford 3000 Master")

v1 = st.text_input("V1 (Base Form) ကို ရိုက်ထည့်ပါ:").strip().lower()

if v1:
    doc = nlp(v1)
    token = doc[0]
    
    # Generate inflections
    v2 = token._.inflect("VBD")
    v3 = token._.inflect("VBN")
    ving = token._.inflect("VBG")

    st.success(f"'{v1}' Forms Found!")
    col1, col2, col3 = st.columns(3)
    col1.metric("V2 (Past)", v2)
    col3.metric("V-ing", ving)
    col2.metric("V3 (Participle)", v3)
