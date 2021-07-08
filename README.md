# multi_index_reader

Convert multi-indexed Excel files into "normally" indexed csv files for R projects.
Requirements:
- Python 3 with pandas, openpyxl (pip install -r requirements.txt)
- R with reticulate, tidyverse 

How to use:
- Install all the requirements.
- If R, source_python('read_multiindex.py') somewhere.
- Use convert_multi_index to convert multi-indexed files. Arguments:
  - filename (str): Excel file to convert.
  - sheet_name (str): name of Excel sheet.
  - skiprows (int): number of rows to skip at top before reading file text
  - skipfooter (int): number of rows to skip at bottom 
  - header (R vector, Python list of int): header rows after skipping skiprows, for example, if there is a 2-level index, we use c(1, 2). Respects R indexing rules.
  - remove_unnamed (bool): Whether or not to remove levels tagged as 'Unnamed:(number)\_level\_(number)
  - strip (bool): whether or not to remove beginning/trailing `[]`
 
