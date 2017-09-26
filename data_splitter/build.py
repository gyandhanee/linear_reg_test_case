from import_data.build import load_data

def data_splitter(df):
    X = df.iloc[:,:-1]
    y = df.iloc[:,-1]
    return X, y