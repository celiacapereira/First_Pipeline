def is_null(df_insert): 
    if df_insert.isnull().values.any() == True:
            return "Fail"
    else:
        return "Pass"