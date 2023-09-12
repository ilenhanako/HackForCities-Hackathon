# FEATURE ENGINEERING
'''
Creating a few new features out of DateTime. Namely:

Year
Month
Date in the given month
Days of week
Hour
'''

df["Year"]= df['DateTime'].dt.year
df["Month"]= df['DateTime'].dt.month
df["Date_no"]= df['DateTime'].dt.day
df["Hour"]= df['DateTime'].dt.hour
df["Day"]= df.DateTime.dt.strftime("%A")
df.head()

# EXPLORATORY DATA ANALYSIS: needed to draw conclusions, see trends etc

#plot newly created features, namely Timeseries
new_features = [ "Year","Month", "Date_no", "Hour", "Day"]

for i in new_features:
    plt.figure(figsize=(10, 2),facecolor="#99ccff")
    ax=sns.lineplot(x=df[i],y="Vehicles",data=df, hue="Junction", palette=colors )
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# Count plot to show the number of vehicles at each junction over the years
plt.figure(figsize=(12,5),facecolor="#99ccff")
count = sns.countplot(data=df, x =df["Year"], hue="Junction", palette=colors)
count.set_title("Count Of Traffic On Junctions Over Years")
count.set_ylabel("Number of Vehicles")
count.set_xlabel("Date")

# Select only numeric dtypes
numeric_df = df.select_dtypes(include=[np.number])
# Compute correlation matrix
corrmat = numeric_df.corr()
# Plot heatmap
plt.subplots(figsize=(10,10),facecolor="#99ccff")
sns.heatmap(corrmat,cmap= "Pastel2",annot=True,square=True)

# Overall representation of any data: Pair Plot
sns.pairplot(data=df, hue= "Junction",palette=colors)
