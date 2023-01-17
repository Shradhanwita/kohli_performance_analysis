import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read the csv file

df = pd.read_csv("dataset.csv")
print(df.head(10))

# # Find the total number of runs Kohli has scored

# total_runs = df["Runs"].sum()
# no_of_matches = len(df["Runs"])
# print(f"\nTotal number of runs Kohli has scored in {no_of_matches} matches: ",total_runs)

# # Find the avg number of runs Kohli has scored

# avg_runs = df["Runs"].mean()
# print(f"\nAverage score of Kohli in {no_of_matches} matches: ",int(avg_runs))

# # Number of matches he has played at different positions

# # positions = df["Pos"]
# # print(positions)
# # print(positions.unique())

# positions = df["Pos"].unique()
# print(positions)

# df["Pos"] = df["Pos"].map({
#     3.0: "Batting at 3",
#     4.0: "Batting at 4",
#     2.0: "Batting at 2",
#     1.0: "Batting at 1",
#     7.0: "Batting at 7",
#     5.0: "Batting at 5",
#     6.0: "Batting at 6",
# })

# print(df["Pos"].head())
# pos_counts = df["Pos"].value_counts()# value_counts - returns frequency of occurence
# print(pos_counts) 
# print(type(pos_counts)) # series obj - particular column

# pos_values = pos_counts.values
# pos_lables = pos_counts.index
# print(pos_values)

# fig = plt.figure(figsize=(10,7))
# plt.pie(pos_values,labels=pos_lables)

# plt.show()


# op_counts = df["Opposition"].value_counts()
# print(op_counts)
# op_values = op_counts.values
# op_lables = op_counts.index
# print(op_values)
# plt.pie(op_values,labels=op_lables)

# plt.show()

# gr_counts = df["Ground"].value_counts()
# print(gr_counts)
# gr_values = gr_counts.values
# gr_lables = gr_counts.index
# print(gr_values)
# plt.pie(gr_values,labels=gr_lables)

# plt.show()

# diss_counts = df["Dismissal"].value_counts()
# print(diss_counts)
# diss_values = diss_counts.values
# diss_lables = diss_counts.index
# print(diss_values)
# plt.pie(diss_values,labels=diss_lables)

# plt.show()

def show_pie_plot(df,key):
    counts = df[key].value_counts()
    count_values = counts.values
    count_labels = counts.index

    fig = plt.figure(figsize=(10,7))
    plt.pie(count_values,labels=count_labels)
    plt.show()


# show_pie_plot(df,"Pos")
# show_pie_plot(df,"Opposition")
# show_pie_plot(df,"Ground")
# show_pie_plot(df,"Dismissal")





# # Total run scored in different positions

# total_runs_at_pos = df.groupby("Pos")["Runs"].sum()
# total_runs_at_pos_values = total_runs_at_pos.values
# total_runs_at_pos_labels = total_runs_at_pos.index
# print(total_runs_at_pos)

# fig = plt.figure(figsize=(10,7))
# plt.pie(total_runs_at_pos_values,labels=total_runs_at_pos_labels)
# plt.show()

# # Total sixes scored with different oppositions

# total_6s = df.groupby("Opposition")["6s"].sum()
# total_6s_values = total_6s.values
# total_6s_labels = total_6s.index 
# print(total_6s)
# fig = plt.figure(figsize=(10,7))
# plt.pie(total_6s_values,labels=total_6s_labels)
# plt.show()






# Number of centuries scored by Kohli in first and second innings


centuries = df.query("Runs>=100")
print(centuries)


innings = centuries["Inns"]
tons = centuries["Runs"]

fig = plt.figure(figsize=(10,7))
plt.bar(
    innings,tons,color="blue",width=0.2
)
plt.show()



# Calculate the dismissals of Kohli



dismissals = df["Dismissal"].value_counts()
print(dismissals)


dismissals_counts = dismissals.values
dismissals_labels = dismissals.index

show_pie_plot(df,"Dismissal")



# Against which teams he has scored the most runs

fig = plt.figure(figsize=(10,7))
plt.bar(
    df["Opposition"],df["Runs"],color="red",width=0.2
)
plt.show()


# Against which teams he has scored the most centuries

fig = plt.figure(figsize=(10,7))
plt.bar(
    centuries["Opposition"],centuries["Runs"],color="green",width=0.2
)
plt.show()


# Analyse the strike rate
# Kohli's strike rate in first innings vs second innings
# Runs scored by him vs 4s played
# Runs scored by him vs 6s played







