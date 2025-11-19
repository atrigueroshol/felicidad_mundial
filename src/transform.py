#FICHERO CON LAS FUNCIONES DE TRANSFORMACIONES

"""
Funcion pasar los datos de la columna Ladder score a Hapiness score y se elimina la columna Ladder score
"""
def transf_ladder_score(df):
    try:
        # Unificar en la columna 'Happiness score'
        df['Happiness score'] = df['Happiness score'].combine_first(df['Ladder score'])
        # Opcional: eliminar la columna 'Ladder score' ya que ahora está todo en 'Happiness score'
        df.drop(columns=['Ladder score'], inplace=True)
    except Exception as e:
        print(f"ERROR: NO SE HA PODIDO TRANSFORMAR LA COLUMNA LADDER SCORE: {e}")

    return df

"""
Funcion para insertar la moda de ese país en el campo regional indicator cuando su valor es nulo
"""
def transf_regional_indicator(df, country):
    for countries in country["Country"]:
        moda = df[df["Country"] == countries]["Regional indicator"].mode()[0]
        df.loc[(df["Country"] == countries) & (df["Regional indicator"].isnull()), "Regional indicator"] = moda
        
    return df