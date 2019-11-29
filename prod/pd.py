import glob
import os
import pandas as pd

list_of_files = glob.iglob('/home/mi/cmc/*') # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)

df=pd.read_csv(latest_file)

coin_head = df.head(100) #Первые 5 монет
coin_tail = df.tail(10) #Последние 10 монет
shape_table = df.shape #Размер таблицы
#df.info() #Информация о таблице
obs_table = shape_table[0] #Количество наблюдений

mineable = df.loc[df['Tags'] == '[\'mineable\']']
count_mineable = mineable.count() # Количество mineable монет

market_cap = df.loc[df['Market_cap'] != 0]
sum_market_cap = market_cap.loc[:,'Market_cap']
summmc = sum_market_cap.loc[sum_market_cap != 'NaN'].sum() # Total market cap

#print(df.columns) # Название столбцов
na_number = df.isna().sum() # Количество пропусков в столбцах
df['Year_added'] = df['Added'].str[:4] #Создание столбца год добавления
df['Month_added'] = df['Added'].str[5:7]

year_counting = df.groupby('Year_added')['Year_added'].count() #Количество монет по году добавления
month_counting = df.groupby('Month_added')['Month_added'].count() #Количество монет по месяцу добавления

i = 1
k = 1
m = k + 100
while i < 2400:
	k1 = df.loc[df.loc[:,'Rank'] >= k ]
	m1 = k1.loc[k1.loc[:,'Rank'] <= m ]
	print('{:.2f}% Максимальное изменение за неделю в минус по ранку от {} до {}'.format(m1['Week_change'].min(), k, m),)
	i += 100
	k += 100
	m = k + 100

#df.info()

'''
#% Максимальное изменение за неделю в минус при объеме
i = 1
k = 100
m = k * 10
while i < 10:
	k1 = df.loc[df.loc[:,'Volume'] > k ]
	m1 = k1.loc[k1.loc[:,'Volume'] < m ]
	print('{:.2f}% Максимальное изменение за неделю в минус при объеме от {}$ до {}$'.format(m1['Week_change'].max(), k, m),)
	i += 1
	k *= 10
	m = k * 10
'''
#print(m10.loc[:,['Name','Symbol','Week_change', 'Volume']].sort_values('Week_change', ascending = False)) #Сортировка по изменению за неделю
 