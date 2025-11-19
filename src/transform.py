#FICHERO CON LAS FUNCIONES DE TRANSFORMACIONES

def transf_ladder_score(df):
    try:
        # Unificar en la columna 'Happiness score'
        df['Happiness score'] = df['Happiness score'].combine_first(df['Ladder score'])
        # Opcional: eliminar la columna 'Ladder score' ya que ahora está todo en 'Happiness score'
        df.drop(columns=['Ladder score'], inplace=True)
    except Exception as e:
        print(f"ERROR: NO SE HA PODIDO TRANSFORMAR LA COLUMNA LADDER SCORE")

    return df