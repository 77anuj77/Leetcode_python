import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    df = animals

    df = df[df["weight"] > 100]
    df = df.sort_values("weight", ascending=False)

    return df[["name"]]