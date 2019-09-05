# Define the dataframe

df = pd.read_csv("output.csv", low_memory=False)

#Creating a new dataframe as pivot table in this case with aggfunc as (sum)

pivotpar = df.pivot_table(index='Row Labels Column Name', aggfunc='sum')

