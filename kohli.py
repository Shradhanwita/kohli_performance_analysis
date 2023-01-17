import pandas as pd

df = pd.read_csv("dataset.csv")
#print(df)

# print(df.head(10)) #gives first 10 rows
# print(df.tail(10)) #gives last 10 rows

# df.info()

# print(df.shape)

# print(df.describe())

print(df["Opposition"].describe())

print(df)
print(df["Runs"].value_counts())

new_df = df[["Runs","4s","6s","Opposition"]]
print(new_df)
#print(new_df.describe())

# print(new_df.iloc[2:5])
# print(new_df.iloc[2:13]["Runs"])

# vs_aussies = df[df["Opposition"] == "v Australia"]
# print(vs_aussies.head(10))
# print(vs_aussies["Runs"].sum())
# print(vs_aussies["6s"].sum())

vs_aussies = df[df["Opposition"] == "v Australia"]
vs_a_c = vs_aussies[vs_aussies["Runs"]>=100]
print(vs_a_c.head(10))


def find_centuries(x):
    if x>=100:
        return "OG"
    else:
        return "NOOB"

df["Centuries"] = df["Runs"].apply(find_centuries)
print(df)

