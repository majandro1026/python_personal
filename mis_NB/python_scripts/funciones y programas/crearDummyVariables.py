def crearDummies(data, columnas):
    '''
    Esta función facilita la creación de variables dummy en un dataset, especificando el dataset y las columnas a convertir

    data: type(DataFrame)
    columnas: type(list), lista de columnas a transformar

    Autor:Manuel Alejandro Pacheco Murcia
    
    '''

    import pandas as pd
    dummy = pd.get_dummies(data[columnas], prefix=columnas)
    data = data.drop(columnas, axis=1)
    data = pd.concat([data, dummy], axis=1)
    return data
