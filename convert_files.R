library(reticulate)
library(dplyr)

source_python('read_multiindex.py')

filename <- 'cdi_ca_on__1903-38_mn.xlsx'
sheet_names <- get_sheet_names(filename)

skiprows <- c(1, 2, 2, 2, 2, 2, 2, 2, 2)
skipfooters <- c(0, 4, 4, 4, 4, 4, 4, 4, 4)
params <- data.frame(sheet_names = sheet_names, skiprows=skiprows, skipfooters = skipfooters)

for (i in 1:nrow(params)){
    sheet_name <- params$sheet_names[i]
    print(sheet_name)
    skiprow <- params$skiprows[i]
    skipfooter <- params$skipfooters[i]

    convert_multi_index(filename, sheet_name, skiprows=skiprow, skipfooter=skipfooter, header=c(1, 2)) 
}





df <- readr::read_csv('cdi_ca_on__1903-38_mnAllDat_deindexed.csv')
print(df)