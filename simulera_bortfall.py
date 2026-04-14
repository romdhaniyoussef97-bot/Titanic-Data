""" Vi simulerar bortfall i variabeln kön """

import pandas as pd
import numpy as np

def simulera_bortfall(df, kolumn='Sex', andel=0.5, random_state=42):
    df_copy = df.copy()

    if kolumn not in df_copy.columns:
        raise ValueError(f"Kolumnen {kolumn} finns inte i datasetet")

    np.random.seed(random_state)

    n_bortfall = int(len(df_copy) * andel)
    index = np.random.choice(df_copy.index, size=n_bortfall, replace=False)

    df_copy.loc[index, kolumn] = np.nan

    return df_copy


# Ladda dataset
filvag = "/Users/victoria/Documents/aikurs/02_datareningEDA/train.csv"
df = pd.read_csv(filvag)

# Skapa bortfall
df_bortfall = simulera_bortfall(df, kolumn='Sex', andel=0.5)

# Spara ny fil
df_bortfall.to_csv("/Users/victoria/Documents/aikurs/02_datareningEDA/train_bortfall.csv", index=False)

print("Dataset med bortfall sparad!")
print("Antal NaN i Sex:", df_bortfall['Sex'].isna().sum())