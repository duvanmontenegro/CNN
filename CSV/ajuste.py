import pandas as pd

df = pd.read_csv (r'ds1.csv')
df2=df.pivot(index="user", columns="time", values=["EEG 1","EEG 2","EEG 3","EEG 4","EEG 5","EEG 6","EEG 7","EEG 8","EEG 9"])
#df2.to_csv(r'ds2.csv')
#print(df2.index)
#df2["Class"] = df2.apply(lambda x: "1" if x.index.str.contains('Insatisfecho') else "0", axis=1)
#df2.index.str.replace(r'(^.*Insatisfecho.*$)', '1')
#df2.loc[df2.index.str.contains('Insatisfecho'),'index'] = '1'
#df2.loc[df2.index.str.contains('Satisfecho'),'index'] = '0'
df2.index=df2.index.str.replace(r'(^.*Insatisfecho.*$)', '1')
df2.index=df2.index.str.replace(r'(^.*Satisfecho.*$)', '0')
# df2.to_csv(r'ds2.csv')
print(df2)

