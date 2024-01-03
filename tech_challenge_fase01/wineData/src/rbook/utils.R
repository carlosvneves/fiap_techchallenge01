library(timetk)
library(tidyverse)
library(readr)
library(lubridate)
library(knitr)
library(kableExtra)


# helper functions
tbl_render <- function(tbl){
    
    
    tbl_col_names <- c()


    for (name in colnames(tbl)) {
        if (name == 'date') {
            name = "Dia/Mês/Ano"
        } else if (name == 'country') {
            name = "País"
        } else if (name == 'value') {
            name = "Valor FOB (US$)"
        } else if (name == 'volume'){
            name = "Quilograma Líquido (1L=1Kg)"
        } else {
            name = NULL
        }

        if(!is.null(name)) {
            tbl_col_names <-c(tbl_col_names, name)
        }
    }
    
    DT::datatable(tbl, filter = "bottom", colnames = tbl_col_names) |>
        DT::formatCurrency(columns = c('value'), "$") |>
        DT::formatDate(columns = c('date'),
                       'toLocaleDateString') |>
        DT::formatRound(columns = c('volume'),
                        mark = ".",
                        dec.mark = ",")
    
}