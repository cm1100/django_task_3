import pandas as pd
import numpy as np


def get_interests():
    df = pd.read_csv("data.csv")



    X = np.array(df["Profession"])


    return X

get_interests()



