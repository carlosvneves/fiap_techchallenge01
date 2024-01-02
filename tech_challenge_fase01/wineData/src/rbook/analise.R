setwd("C:/projects/alura_postech/tech_challenge_fase01/wineData/src")


library(timetk)
library(tidyverse)
library(readr)
library(lubridate)

## Time Series Data Input

ts_tbl <- readr::read_delim("../data/EXP_VINHO_2000_2022_20231118_mensal.csv", 
                                                  delim = ";", 
                            escape_double = FALSE, trim_ws = TRUE)

ts_tbl <- ts_tbl |> mutate(Date = lubridate::make_date(Ano, Mês, 1)) |> 
    rename( Valor = `Valor FOB (US$)`) |> 
    rename( Volume = `Quilograma Líquido`) |> 
    rename( Paises = `Países`) |> 
    select(c(Date, `Paises`, Valor, Volume ))  

## Time Series 

    
### Time Series Visualization (Valor)
ts_tbl |> select(Date, Paises, Valor) |> filter(Paises == "Paraguai") |> plot_time_series(Date, log(Valor), .smooth = F, .interactive = F)

ts_tbl |> select(Date, Paises, Valor) |> filter(Paises == "Paraguai") |>  plot_time_series(Date, Valor, .smooth = T, 
                                                  .smooth_span = .5,
                                                  .interactive = T,
                                                  .title = 'Valor Exportado em US$',
                                                  .plotly_slider = T)

## Time Series Visualization (Volume)
ts_tbl |> select(Date, Volume) |> plot_time_series(Date, log(Volume), .smooth = F, .interactive = F)

ts_tbl |> select(Date, Volume) |> plot_time_series(Date, Volume, 
                                                   .smooth = T, 
                                                   .smooth_span = 0.5, 
                                                   .interactive = F, 
                                                   .title = 'Volume Exportado em L',
                                                   .plotly_slider = T)
