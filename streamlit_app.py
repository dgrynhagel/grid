import streamlit as st
import pandas as pd
import pymongo
import duckdb
import modules.gargamel as dg

st.set_page_config(
    page_title="SamFan CRM",
    page_icon=":bar_chart:",
    layout = "wide"
)

tab1,tab2,tab3 = st.tabs(['Osoby','Imprezy','Osoby Imprezy'])
osoby = pd.DataFrame(dg.get_osoby())
imprezy = pd.DataFrame(dg.get_imprezy())
#sidebar filters
st.sidebar.write("Filtruj osoby")
Nazwisko = st.sidebar.multiselect(
    " Wybierz nazwisko:",
      options = pd.Series(osoby["NAZWISKO"].unique()).sort_values(),
      key = 'osoby'
)
osoby_selection = osoby.query (
      "NAZWISKO == @Nazwisko" 
)

st.sidebar.write("This is sidebar for something")
with tab1:   
    st.data_editor(osoby_selection)
with tab2:
    st.dataframe(imprezy)
with tab3:
    with st.form("osobyImprezy"):
        st.multiselect(
            " Wybierz nazwisko:",
            options = pd.Series(osoby["NAZWISKO"].unique()).sort_values(),
            key = 'osobyimprezy'
        )
        Nazwa = st.multiselect(
            " Wybierz impreze:",
            options = pd.Series(imprezy["NAZWA"].unique()).sort_values()
        )
        # imprezy_selection = imprezy.query (
        #     "NAZWA == @Nazwa" 
        # )

        st.form_submit_button('Dodaj osobę do imprezy')