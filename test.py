import pandas as pd

df = pd.DataFrame({"a":[1,2,3,5], "b": [2,4,5,5], "c":[1,2,3,4]})

a = ["b", "a"]

df = df.loc[:, df.columns.isin(a)]
df = df[a]

print(df)
