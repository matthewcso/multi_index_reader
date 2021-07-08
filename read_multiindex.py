import pandas as pd
from os.path import splitext

def column_selector(x):
    list_x = list(x)
    list_x = [str(element) for element in list_x]
    list_x = list(filter(lambda element: element.find('Unnamed') == -1, list_x))

    return str(list_x)

def convert_multi_index(filename, sheet_name, skiprows=0, skipfooter=0, header=[1, 2], remove_unnamed = True, strip = True):
    df = pd.read_excel(filename, sheet_name, skiprows=int(skiprows), skipfooter=int(skipfooter), header=[int(x-1) for x in header])
    df.columns = df.columns.to_flat_index()
    if remove_unnamed:
        df.columns = [column_selector(x) for x in df.columns]
        if strip:
            df.columns = [x.replace('\n', ' ').replace('\\n', ' ').strip("[]") for x in df.columns]
    else:
        df.columns = [str(x) for x in df.columns]
    df.to_csv(splitext(filename)[0]+sheet_name+'_deindexed'+'.csv', index=False)
    return df

def get_sheet_names(filename):
    return(list(pd.read_excel(filename, sheet_name=None).keys()))