#
import streamlit as st
import polars as pl 
import pandas as pd 
import pytimetk as tk
from itables import show 


st.title("Análise de dados de exportação de vinhos do Brasil - 3DTAT - FIAP")


data_export = (pl.read_csv("./data/EXP_VINHO_2000_2022_20231118_mensal.csv", 
                           separator=";")
            .select(pl.all()
            .exclude(['Código CUCI Item','Descrição CUCI Item'])))

data_export.with_columns(pl.col(['Ano','Mês']).str.concat("Ano"-"))

st.dataframe(data_export)

show(data_export)

cpi_us = pd.read_csv("./data/cpi_brazil_us/cpi_series.csv", sep=";")

cpi_us['year'] = pd.to_datetime(cpi_us['year'], format='%Y')



st.plotly_chart(cpi_us.plot_timeseries(
    date_column="year", 
    value_column="cpi",
    smooth_frac = 0.8,
    title="CPI US - Índice de jan/2000 a dez/2022"
))
#st.table(cpi_us)



