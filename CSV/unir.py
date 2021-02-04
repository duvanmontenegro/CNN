import pandas as pd
import csv
# df=csv.reader("exportdf.csv")
# df = pd.read_csv("exportdf.txt",header=0,delim_whitespace=True)
# df['group_num'] = df.groupby('user')['id'].transform(lambda x: range(1, len(x)+1))
# df.pivot(index='group', columns='group_num')
# print(df)

print(' *** Using pandas.read_csv() with multiple char delimiters ***')

# Read a csv file to a dataframe with multiple delimiters in regular expression
df =  pd.read_csv('exportdfv1-2.csv',  sep='[:,|_]', engine='python')
# df =  pd.read_csv('all\export_dataframeInsatisfecho-u2-1.csv',  sep='[:,|_]', engine='python')
# df['group_num'] = df.groupby('user')['EEG 1'].transform(lambda x: range(1, len(x)+1))
# df['id'] = df.groupby('user')['time'].transform(lambda x: range(1, len(x)+1))#FuncionaMedio
# df['group_num'] = df.groupby('user')['id'].transform(lambda x: range(1, len(x)+1))
print(df)
# df.columns = [''.join([lvl1, str(lvl2)]) for lvl1, lvl2 in df.columns]
# df.pivot(index='user', columns='group_num')user,1,time,EEG 1,EEG 2,EEG 3,EEG 4,EEG 5,EEG 6,EEG 7,EEG 8,EEG 9
df.pivot(index='user', columns='id', values=['time','EEG 1','EEG 2','EEG 3','EEG 4','EEG 5','EEG 6','EEG 7','EEG 8','EEG 9'])
# df.columns = [''.join([lvl1, str(lvl2)]) for lvl1, lvl2 in df.columns]
# df = df[['user','id','time','EEG 1','EEG 2','EEG 3','EEG 4','EEG 5','EEG 6','EEG 7','EEG 8','EEG 9']]

print(df)
# df.to_csv(r'C:\Users\Dsmith\Documents\Tesis\CNN\project\CSV\export_dataframe.csv', index = False, header=True)
# df.to_csv(r'C:\Users\Dsmith\Documents\Tesis\CNN\project\CSV\exportdfv3.csv', index = False, header=True)
# df.to_csv(r'C:\Users\Dsmith\Documents\Tesis\CNN\project\CSV\exportdfv1-2.csv', index = False, header=True)

# def main():

# 	print(' *** Using pandas.read_csv() with Custom delimiter ***')

# 	# Read a csv file to a dataframe with custom delimiter
# 	# usersDf =  pd.read_csv('users_3.csv', sep='__'  , engine='python')
# 	# usersDf =  pd.read_csv('exportdf.csv', sep='__'  , engine='python')

# 	# print('Contents of Dataframe : ')
# 	# print(usersDf)
# 	# print(usersDf.shape)
# 	# bdf = usersDf.to_numpy()
# 	# print("Data:",bdf)

# 	# print('********')

# 	# print(' *** Using pandas.read_csv() with space or tab as delimiters ***')
# 	# # Read a csv file to a dataframe with delimiter as space or tab
# 	# usersDf =  pd.read_csv('exportdf.csv',  sep='\s+', engine='python')

# 	# print('Contents of Dataframe : ')
# 	# print(usersDf)


# 	print(' *** Using pandas.read_csv() with multiple char delimiters ***')

# 	# Read a csv file to a dataframe with multiple delimiters in regular expression
# 	usersDf =  pd.read_csv('exportdf.csv',  sep='[:,|_]', engine='python')

# 	print('Contents of Dataframe : ')
# 	print(usersDf)
# 	print(usersDf.shape)
# 	bdf = usersDf.to_numpy()
# 	print("Data:",bdf)

# if __name__ == '__main__':
# 	main()