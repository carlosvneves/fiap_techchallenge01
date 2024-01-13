#
import streamlit as st
import polars as pl 
import pandas as pd 
import pytimetk as tk
from itables import show 

st.set_page_config(page_title='Carlos Neves-Vinhos do Brasil-3DTAT-FIAP',

                   layout="wide",
                   page_icon=':wine_glass:')




# data_export = (pl.read_csv("./data/EXP_VINHO_2000_2022_20231118_mensal.csv", 
#                            separator=";")
#             .select(pl.all()
#             .exclude(['Código CUCI Item','Descrição CUCI Item'])))

# data_export.with_columns(pl.col(['Ano','Mês']).str.concat("Ano"-"))

# st.dataframe(data_export)

# show(data_export)

# cpi_us = pd.read_csv("./data/cpi_brazil_us/cpi_series.csv", sep=";")

# cpi_us['year'] = pd.to_datetime(cpi_us['year'], format='%Y')



# st.plotly_chart(cpi_us.plot_timeseries(
#     date_column="year", 
#     value_column="cpi",
#     smooth_frac = 0.8,
#     title="CPI US - Índice de jan/2000 a dez/2022"
# ))
#st.table(cpi_us)

def main():
    st.title("Análise de dados de exportação de vinhos do Brasil")
    st.subheader('Tech Challenge 01: Pós-Tech Data Analytics (3DTAT-FIAP)')

    
    
    st.markdown("""    

    ***
                
    # Bem-vindo(a)

    ***

    ## Apresentação
    
    **Esta aplicação tem por objetivo apresentar um análise sobre a exportação de vinhos do Brasil.**
    
    A aplicação deverá fornecer informações que permitam ao interessado ter uma compreensão sobre o processo de exportação 
    de vinhos do Brasil, por meio de gráficos e tabelas interativas. A análise parte dos seguintes dados:
    -   Países de destinatários dos vinhos produzidos no Brasil :earth_americas:
    -   Quantidade em litros de vinho exportado (1KG =1L) :wine_glass:
    -   Valor exportado em US$ :money_with_wings:

    Aleḿ dos dados acima, também fornecemos _insights_ sobre a relação entre a exportação de vinhos e os dados abaixo:
    -   Dados climáticos :mostly_sunny: 
    -   Dados demográficos :people_holding_hands:
    -   Dados econômicos :chart_with_upwards_trend:
    -   Dados de avaliações de vinhos :sports_medal:

    ***

    ## Fontes de dados: 

    ### Exportação de vinhos

    Os dados inicialmente fornecidos são de uma vinícola parceira, e podem ser encontrados [aqui](http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_01). Tomando como referência os relatórios produzidos pela Emprapa em [2020](https://ainfo.cnptia.embrapa.br/digital/bitstream/item/215377/1/COMUNICADO-TECNICO-214-Publica-602-versao-2020-08-14.pdf) e [2021](https://ainfo.cnptia.embrapa.br/digital/bitstream/item/227610/1/ComTec-223-21.pdf, sabemos que a origem dos dados incialmente fornecidos é a Secretaria de Comércio Exterior do do Ministério da Indústria, Comércio Exterior e Serviços (MDIC).

    Com o intuito de confirmar tal informação, ainda extraímos os dados diretamente da plataforma [Comexstat](http://comexstat.mdic.gov.br/pt/geral/97910) de responsabilidade do MDIC. Neste caso, os vinhos de mesa correspondem ao produto de Código CUCI 11217 - "Vinhos de uvas frescas (exceto vinho espumante); mostos de uvas cuja fermentação tenha sido impedida ou interrompida por adição de álcool". Ao compararmos os dados da Comexstat com os dados da Vitibrasil, vemos que o valor exportado está expresso em US$ 1.000,00 (FOB) a preços correntes, ou seja, ao se comparar os dados ao longo do tempo, é necessário considerar o efeito da inflação na moeda norte-americana.

    De acordo com o [Manual de utilização dos dados estatísticos do comércio exterior brasileiro] (https://balanca.economia.gov.br/balanca/manual/Manual.pdf), a classificação Uniforme para o Comércio Internacional - CUCI, também conhecida como Standard International Trade Classification - SITC é uma classificação de produto da ONU usada para estatísticas de comércio exterior (valores de exportação e importação e volumes de mercadorias), permitindo comparações internacionais de mercadorias e produtos manufaturados.

    O valor FOB indica o preço da mercadoria em dólares americanos sob o Incoterm FOB (Free on Board), modalidade na qual o vendedor é responsável por embarcar a mercadoria enquanto o comprador assume o pagamento do frete, seguros e demais custos pós embarque. Nesse caso, o valor informado da mercadoria expressa o valor exclusivamente da mercadoria.

    Já o peso líquido da mercadoria permite que mesmo produtos com quqantidades estatísticas diferentes do quilograma também possuam disponível a medida em quilograma, referindo-se ao peso líquido da mercadoria, ou seja, mercadoria desconsiderando embalagens, caixas ou quaisquer outros adicionais de transporte.

    ### Dados socieconômicos, climáticos e de avaliações de vinhos 
        
    - [Our World in Data](https://ourworldindata.org)
    - [Banco Mundial](https://data.worldbank.org)
    - [Instituto Nacional de Meteorologia (INMET)](https://www.inmet.gov.br/)
    - [X-Wines: A Wine Dataset for Recommender Systems and Machine Learning](https://github.com/rogerioxavier/X-Wines/)
   
    ## Metodologia:


    ***

                        
    """)

    

if __name__ == '__main__':
    main()
