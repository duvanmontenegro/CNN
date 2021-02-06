import pandas as pd

df = pd.read_csv (r'exportdfv1-1.csv')

print(df)
rta=df.user.str.find("Insatisfecho")
print(rta)
print(type(df.user))
print(df.user[0])

print("inicia")
cont=0
for us in df.user:
	if us.find("Insatisfecho")==0:
		df.user.iloc[cont]=1
		print(cont)

	else:
		df.user.iloc[cont]=0
	cont=cont+1
print("termina")
print(df.user)
print(df)

df['id'] = df.groupby('user')['time'].transform(lambda x: range(1, len(x)+1))
print(df)
Falta especificar para que ponga los egg como datos
# df2=df.pivot(index="user", columns="time", values=["EEG 1","EEG 2","EEG 3","EEG 4","EEG 5","EEG 6","EEG 7","EEG 8","EEG 9"])
df2=df.pivot(index="user", columns="id", values=["time","EEG 1","EEG 2","EEG 3","EEG 4","EEG 5","EEG 6","EEG 7","EEG 8","EEG 9"])
df2.to_csv(r'C:\Users\Dsmith\Documents\Tesis\CNN\project\CSV\resultv1-1.csv', index = False, header=True)
#df2.to_csv(r'ds2.csv')
#print(df2.index)
#df2["Class"] = df2.apply(lambda x: "1" if x.index.str.contains('Insatisfecho') else "0", axis=1)
#df2.index.str.replace(r'(^.Insatisfecho.$)', '1')
#df2.loc[df2.index.str.contains('Insatisfecho'),'index'] = '1'
#df2.loc[df2.index.str.contains('Satisfecho'),'index'] = '0'

print(df2)
# df2.index=df2.index.str.replace(r'(^.Insatisfecho.$)', '1')
# df2.index=df2.index.str.replace(r'(^.Satisfecho.$)', '0')

# df2.to_csv(r'ds2.csv')
print(df2)