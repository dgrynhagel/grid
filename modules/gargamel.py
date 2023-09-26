# import oracledb
import pandas as pd
import pymongo
import streamlit as st


# def connect_oracle():
#     connection = oracledb.connect(
#     user="wlodek",
#     password ='wlodek',
#     dsn="192.168.50.63/xe")

#     print("Successfully connected to Oracle Database")

#     return connection.cursor()


def connect_mongo(conn_id,db_name):
    client = pymongo.MongoClient(**st.secrets[conn_id])
    db = client[db_name]
    return db

def get_osoby():
    db = connect_mongo("mongo_cloud",'CRM')
    filters = db.Osoby.find({}, {"_id":0})
    filters = list(filters)  # make hashable for st.cache_data
    return filters

def get_imprezy():
    db = connect_mongo("mongo_cloud",'CRM')
    filters = db.Imprezy.find({})
    filters = list(filters)  # make hashable for st.cache_data
    return filters