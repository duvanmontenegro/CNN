import pandas as pd
import csv

# Lee y oraganiza los datos

df =  pd.read_csv('exportdfv1-2.csv',  sep='[:,|_]', engine='python')
# Utilizamos groupby para dar un 1 por el numero de personas
# en el caso de exportdfv1-1.csv y exportdfv1-2.csv, no lo usamos ya que el id esta como un campo
# df['id'] = df.groupby('user')['time'].transform(lambda x: range(1, len(x)+1))#FuncionaMedio
# df['group_num'] = df.groupby('user')['id'].transform(lambda x: range(1, len(x)+1))
print(df)
# Aplana
# df.columns = [''.join([lvl1, str(lvl2)]) for lvl1, lvl2 in df.columns]
# Organiza las columnas
# df.pivot(index='user', columns='group_num')user,1,time,EEG 1,EEG 2,EEG 3,EEG 4,EEG 5,EEG 6,EEG 7,EEG 8,EEG 9
# invierte las columnas a nuestra conveniencia 
df.pivot(index='user', columns='id', values=['time','EEG 1','EEG 2','EEG 3','EEG 4','EEG 5','EEG 6','EEG 7','EEG 8','EEG 9'])
# df = df[['user','id','time','EEG 1','EEG 2','EEG 3','EEG 4','EEG 5','EEG 6','EEG 7','EEG 8','EEG 9']]

print(df)
# df.to_csv(r'C:\Users\Dsmith\Documents\Tesis\CNN\project\CSV\export_dataframe.csv', index = False, header=True)
# df.to_csv(r'C:\Users\Dsmith\Documents\Tesis\CNN\project\CSV\exportdfv3.csv', index = False, header=True)
# df.to_csv(r'C:\Users\Dsmith\Documents\Tesis\CNN\project\CSV\exportdfv1-2.csv', index = False, header=True)
