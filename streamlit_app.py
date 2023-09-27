import streamlit as st
import pandas as pd
import pymongo
import duckdb
import modules.gargamel as dg
from bson import ObjectId

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

        imprezy_selectbox = pd.DataFrame(imprezy,columns = ["_id","NAZWA"])
        dictionary_imprezy = {}
        dictionary_imprezy2 = {}
        options_imprezy = []
        for row in imprezy_selectbox.itertuples():
           if isinstance(row[1], ObjectId):
               key = str(row[1])
           else:
               key = row[1]
           dictionary_imprezy[key] = row[2]
           dictionary_imprezy2[row[2]] = key 
           options_imprezy.append(row[2])
          # print( str(row[2]))
        #print(dictionary_imprezy)
        st.write(dictionary_imprezy['64eae6052126e93e4bc97c6d'])
        imprezy_testdict = dict(imprezy_selectbox.values)
        imprezy_values = imprezy_selectbox['NAZWA'].tolist()
        imprezy_options = imprezy_selectbox['_id'].tolist()
        imprezy_dict = dict(zip(str(imprezy_options),imprezy_values))
        
        Nazwa = st.selectbox(
            " Wybierz impreze:",
            options = options_imprezy,
           format_func=lambda x: dictionary_imprezy[x]
        )
        # imprezy_selection = imprezy.query (
        #     "NAZWA == @Nazwa" 
        # )

        st.form_submit_button('Dodaj osobę do imprezy')
    
    st.write(Nazwa)    