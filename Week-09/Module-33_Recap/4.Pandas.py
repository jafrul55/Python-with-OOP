import pandas as pd
# df = pd.read_csv("diabetes.csv")
df = pd.read_csv("diabetes.csv",index_col="Outcome")
#for decrease value:
df_head = df.head()

# print(df.head())
# print(df.describe())

# print(df_head)
# print(df_head.groupby('Pregnancies').sum())
# print(df_head.groupby('Pregnancies').mean())
# print(df_head['Pregnancies'].value_counts())
# print(df_head["Outcome"])
# print(df_head["Age"])
# for getting row: you have to insert index_col = "Outcome"

# print(df_head.loc[0])
# print(df_head.loc[1])

#we use it to print ascending order:
# df_head.sort_values("Age",ascending=True,inplace=True)

#we use it to print decending order:
# df_head.sort_values("Age",ascending=False,inplace=True)

#But if we use here "inplace = False" then output will be unascending 
# df_head.sort_values("Age",ascending=True,inplace=False)

#we can also use ascending and descending order for multiple value:
# df_head.sort_values(["Age","BMI"],ascending=[False,True],inplace=True)
# print(df_head)

#data cleaning:
# dropna(),fillna()
# 1.dropna(): if raw wise get none that he will delete
# 2.fillna(): None value will  be replace
# print(df_head)
# print(df_head.isnull()) #none raw will delete
# print(df_head.dropna())

# print(df_head.fillna(1000)) #None value will replace with given value

# we can convert dictionary to Data structure:
dct = {"Name":"Rahim","age":23}
df = pd.DataFrame(dct,index=["first"])
print(df)





