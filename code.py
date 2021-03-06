# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path 
data = pd.read_csv(path)

data.rename(columns = {'Total':'Total_Medals'} , inplace = True)

print(data.head(10))

#Code starts here



# --------------
#Code starts here

data['Better_Event'] = np.where(data['Total_Summer']>data['Total_Winter'] ,'Summer','Winter')

data['Better_Event'] =np.where(data['Total_Summer'] ==data['Total_Winter'],'Both',data['Better_Event'])

print(data['Better_Event'])

better_event = data['Better_Event'].value_counts().idxmax()

print(better_event)


# --------------
#Code starts here
#print(data)
top_countries  = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]

#print(top_countries)

top_countries.drop(top_countries.index[146], inplace = True)
print(top_countries)

def top_ten(top_countries, column_name):
 country_list = []
 top_countries =  top_countries.nlargest(10,column_name)
 country_list = list(top_countries['Country_Name'])
 return country_list

top_10_summer = top_ten(top_countries,'Total_Summer')
top_10_winter = top_ten(top_countries,'Total_Winter')
top_10 = top_ten(top_countries,'Total_Medals')

common = list(set(top_10_summer) & set(top_10_winter) & set(top_10))
print(common)



print(top_10_summer,top_10_winter,top_10)


# --------------
#Code starts here

summer_df = data[data['Country_Name'].isin(top_10_summer)]

#print(summer_df)

winter_df  = data[data['Country_Name'].isin(top_10_winter)]

#print(winter_df)

top_df = data[data['Country_Name'].isin(top_10)]
print(top_df)

plt.plot(data['Country_Name'] , data['Total_Summer'] , label = 'line 1')
plt.plot(data['Country_Name'] , data['Total_Winter'],label = 'line 2')
plt.plot(data['Country_Name'] , data['Total_Medals'],label = 'line 3')


# --------------
#Code starts here

#summer_df['Golden_Ratio'] = round(summer_df['Gold_Summer']/summer_df['Total_Summer'], 2)

#print(summer_df['Golden_Ratio'], summer_df)

#summer_max_ratio = summer_df['Golden_Ratio'].idxmax()
#summer_country_gold = summer_df.loc[23,'Country_Name']

#print(summer_max_ratio, summer_country_gold)

summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer'] 

summer_max_ratio=max(summer_df['Golden_Ratio']) 
summer_country_gold=summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']

print(summer_max_ratio, summer_country_gold)


winter_df['Golden_Ratio']=winter_df['Gold_Winter']/winter_df['Total_Winter'] 

winter_max_ratio=max(winter_df['Golden_Ratio']) 
winter_country_gold=winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']

print(winter_max_ratio, winter_country_gold)



top_df['Golden_Ratio']=top_df['Gold_Total']/top_df['Total_Medals'] 

top_max_ratio=max(top_df['Golden_Ratio']) 
top_country_gold=top_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']

print(top_max_ratio, top_country_gold)





# --------------
#Code starts here
data_1  = data.drop(data.index[len(data)-1])

data_1['Total_Points'] = 3*data_1['Gold_Total'] + 2*data_1['Silver_Total']+ 1*data_1['Bronze_Total']


most_points=max(data_1['Total_Points']) 
best_country=data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']

print(most_points,best_country)


# --------------
#Code starts here

best = data[data['Country_Name'] == best_country]


best =best[['Gold_Total','Silver_Total', 'Bronze_Total']]
print(type(best))

best.plot(kind = 'bar')

plt.xlabel("United States")
plt.ylabel("Medals Tally")
plt.xticks(rotation = 45)


