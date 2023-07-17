import pandas as pd

one_df = pd.read_csv("one.csv", sep="|")
two_df = pd.read_csv("two.csv", sep="|")

total = pd.merge(one_df, two_df, how="outer", on="Email")
added_df = total[~total["Email"].isin(one_df["Email"])]
removed_df = total[~total["Email"].isin(two_df["Email"])]
print(added_df)
print(removed_df)

# monkey paching
# WAP to find out the percent matching between 2 strings and determine the percentage