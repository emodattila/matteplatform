# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 09:12:01 2025

@author: emokov
"""

import streamlit as st

st.set_page_config(page_title="Matteplattform", layout="wide")

# Sidopanel - Navigation
st.sidebar.title("Navigering")
sida = st.sidebar.radio("Gå till", ["🏠 Startsida", "📚 Lektioner", "💡 Projektidéer", "🌟 Elevgalleri"])

# Startsida
if sida == "🏠 Startsida":
    st.title("Välkommen till Matteplattformen")
    st.write("Det här är en digital verkstad för matematik, programmering och projekt!")
    st.write("Här kan du utforska lektioner, hitta projektidéer och se exempel på vad andra elever har byggt.")

# Lektioner
elif sida == "📚 Lektioner":
    st.title("📚 Lektioner")
    st.header("Exempel: Ränta på ränta")
    kapital = st.number_input("Startkapital (kr)", 1000)
    ränta = st.slider("Ränta (%)", 0.0, 15.0, 5.0)
    år = st.slider("Antal år", 1, 30, 10)
    slutvärde = kapital * (1 + ränta/100) ** år
    st.write(f"Efter {år} år har du {slutvärde:,.0f} kr.")

# Projektidéer
elif sida == "💡 Projektidéer":
    st.title("💡 Projektidéer")
    st.markdown("""
    - **Simulera smittspridning med SIR-modellen**
    - **Bygg en valutakonverterare** (procent, växelkurs)
    - **Visualisera funktioner och derivator** med `matplotlib`
    - **Bygg en AI som gissar handskrivna siffror** (MNIST)
    - **Analys av klimatdata**: importera csv och analysera med Python
    """)

# Elevgalleri
elif sida == "🌟 Elevgalleri":
    st.title("🌟 Elevgalleri")
    st.info("Här kan du i framtiden visa upp elevprojekt – med bild, kod och beskrivning!")
    st.image("https://images.unsplash.com/photo-1581090700227-1e8e601f10ed", caption="Exempelprojekt", use_column_width=True)
    st.write("**Projekt:** Räntesnurra i Python")
    st.write("**Elev:** Alice, Teknikprogrammet")
