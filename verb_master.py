import streamlit as st
import os

# --- Model Download Section ---
# ဤအပိုင်းသည် Cloud ပေါ်တွင် Error မတက်အောင် အတင်းဆွဲချခိုင်းခြင်းဖြစ်သည်
try:
    import en_core_web_sm
except ImportError:
    os.system("python -m spacy download en_core_web_sm")
    import en_core_web_sm

import spacy
import pyinflect

# Load Model
nlp = en_core_web_sm.load()

st.title("📖 Thuta's Oxford 3000 Master")

v1 = st.text_input("V1 (Base Form) ကို ရိုက်ထည့်ပါ:").strip().lower()

if v1:
    doc = nlp(v1)
    if len(doc) > 0:
        token = doc[0]
        v2 = token._.inflect("VBD")
        v3 = token._.inflect("VBN")
        ving = token._.inflect("VBG")

        st.success(f"'{v1}' Forms Found!")
        col1, col2, col3 = st.columns(3)
        col1.metric("V2 (Past)", v2)
        col2.metric("V3 (Participle)", v3)
        col3.metric("V-ing", ving)
    else:
        st.error("စကားလုံး မှန်အောင်ရိုက်ပါ")
