import pandas as pd
csv_path = '../Cooursera---IBM---Data-science-Methodology/recipes.csv'

df = pd.read_csv(csv_path)
df.head()
df.shape


q= {'town':['kerman','tehran','hamedan','shiraz'],'active_case':[40,50,30,58],'death':[3,5,6,4]}
q['town']
q['active_case']
q['death']

q_frame = pd.DataFrame (q)
q_frame

countries = df[['country','almond','apple']]
countries

qq= countries.loc[0:1000,['country','almond']]
qq
pp=countries.iloc[:,0:3]
pp

pp1 = df[['country']]
pp2=df.loc[:,['country']]
pp1
pp2

type (pp1)
type (pp2)

pp3=df[['country']]
pp3.unique()
pp3

yy =df[df['almond']=='Yes']
yy
yy.loc[0:100,:]
yy.to_csv('pandas-almond-yes.csv')
# =========================================================== #
csv_path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Datasets/TopSellingAlbums.csv'
df = pd.read_csv(csv_path)
df.head()

xlsx_path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Datasets/TopSellingAlbums.xlsx'

df = pd.read_excel(xlsx_path)
df.head()
x = df[['Length']]
x
df.loc[4,'Artist']
