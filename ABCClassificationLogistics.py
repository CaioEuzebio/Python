#geral = open('mes1.csv')
df1 = pd.read_csv("junho.csv", encoding='latin-1', low_memory=False)
df2 = pd.read_csv("julho.csv", encoding='latin-1', low_memory=False)
df3 = pd.read_csv("agosto.csv", encoding='latin-1', low_memory=False)
dfprod = pd.read_csv("products.csv", encoding='latin-1', low_memory=False)

dfgeral = pd.concat([df1,df2,df3])
dfgeral

dfgeral2 = dfgeral.drop(dfgeral.columns[[0,1,2,3,4,5,7,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,51,52,53]], axis=1)
dfgeral2
dfpivot = dfgeral2.pivot_table(index='PartNo', aggfunc='sum')
dfpivot

dftotal = dfpivot.sort_values(['Qty'], ascending=[0])
dftotal

dfprod.rename(columns={'Material Part No':'PartNo'}, inplace=True)

dftotal2 = pd.merge(dftotal, dfprod[['PartNo','Description']], on='PartNo', how='left')
dftotal2

totalout = dftotal2['Qty'].sum()
totalout

dftotal2['Percentual'] = np.true_divide(dftotal2['Qty'], totalout).round(2).astype(str) + '%'
dftotal2['Percentual']*100



dftotal2
