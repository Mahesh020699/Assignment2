import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def import_dataset(dataset):
    
    df_1 = pd.read_excel(dataset,skiprows=3)
    data_1 = df_1.copy()
    df_2 = data_1.drop(columns =["Country Code","Indicator Name","Indicator Code"],axis =1)
    df_2 = df_2.set_index("Country Name")
    df_2 = df_2.transpose()
    return df_1, df_2
    

df1, df2 = import_dataset("data.xls")
print(df2.describe())
df2.fillna(0)

grouped = df1.groupby("Country Name")

# Filter rows related to India
bd_group = grouped.get_group("India")
grp_1=bd_group.set_index("Indicator Name")

grp_1 = grp_1.loc[:, '2000':'2021']
grp_1=grp_1.transpose()

# Select a subset of indicators
indicators = ["School enrollment, primary and secondary (gross), gender parity index (GPI)",
              "Poverty headcount ratio at $2.15 a day (2017 PPP) (% of population)",
              "Urban population",
              "Agricultural land (% of land area)",
              "Electric power consumption (kWh per capita)",
              "Total greenhouse gas emissions (kt of CO2 equivalent)"]

bd_indicators = grp_1[indicators]

# Compute the correlation matrix
corr_matrix = bd_indicators.corr()

# Set the labels for the heatmap
labels = ["Primary and secondary school enrollment",
          "Poverty headcount",
          "Urban population growth",
          "Agricultural land",
          "Electric power consumption",
          "Total greenhouse gas emissions"]

# Visualize the correlation matrix as a heatmap
sns.heatmap(corr_matrix, cmap="RdBu", annot=True, xticklabels=labels, yticklabels=labels)
plt.title("India Indicators correlation")
plt.show()



def Bar_corelation(data, ind, plot):
    
    
    data= data.drop(["Country Code","Indicator Code"],axis =1) #drop the unused column from the dataset
    data.set_index("Indicator Name",inplace = True) # setting up the index for the "Indicator Name"
    data = data.loc[ind]
    data = data.reset_index(level = "Indicator Name")
    data.groupby(["Country Name"])
    data = data.loc[data["Country Name"].isin(["India", "Afghanistan", "Bangladesh", "Canada", "United Kingdom", "Brazil", "Germany", "Australia", "Croatia","China"]), :]
    if plot == "bar" :    
        data[['1990', '2000', '2010', '2019']] = data[['1990', '2000', '2010', '2019']].abs()
        data.plot(x= "Country Name",y = ['1990', '2000', '2010', "2019"], figsize = (15,5), kind = plot)
    elif plot == "line":
        data.plot(x= "Country Name",y = ['1990', '2000', '2010', "2019"], figsize = (15,5), kind = plot)
    elif plot == "area":
        data.plot(x= "Country Name",y = ['1990',"2016"], figsize = (15,5), kind = plot)
    plt.title(ind)
    plt.ylabel("Frequency")
    plt.show()
    
    
Bar_corelation(df1, "Population growth (annual %)", "bar")
Bar_corelation(df1, "Renewable energy consumption (% of total final energy consumption)", "bar")
Bar_corelation(df1, "Electric power consumption (kWh per capita)", "line")
Bar_corelation(df1, "Forest area (sq. km)", "area")
Bar_corelation(df1, "Total greenhouse gas emissions (kt of CO2 equivalent)", "line")



'''
def line_corelation(data, ind, plt):
    data2= data
    data2 = data.drop(["Country Code","Indicator Code"],axis =1)
    data2.set_index("Indicator Name",inplace = True)
    data2 = data2.loc[ind]
    data2 = data2.reset_index(level = "Indicator Name")
    data2 = data2.drop(["Indicator Name"], axis = 1)
    data2 = data2.T
    header = data2.iloc[0].values.tolist()
    data2.columns = header
    data2=data2[1:]
    data2.index.name = 'Year'
    data2.plot(x="Afghanistan", y=data2.index, label="Afghanistan", kind="line", stacked=False)
    
    #plt.plot(data2["Year"], [data2[c] for c in ["India", "Afghanistan", "Bangladesh", "Canada", "United Kingdom", "Brazil", "Germany", "Australia", "Croatia","China"]], label=["India", "Afghanistan", "Bangladesh", "Canada", "United Kingdom", "Brazil", "Germany", "Australia", "Croatia","China"])
    #data2 = data2.loc[data["Country Name"].isin(["India", "Afghanistan", "Bangladesh", "Canada", "United Kingdom", "Brazil", "Germany", "Australia", "Croatia","China"]), :]
    #data2.to_csv("testtt.csv")


line_corelation(df1, "Agricultural irrigated land (% of total agricultural land)", "line")
'''




'''
data2 = data2.reset_index(level = "Indicator Name")
data2.groupby(["Country Name"]).sum()
data2 = data2.head(15)
data2.plot(x = "Country Name", y = ['1965', '1970', '1975', '1980', '1985', '1990','1995','2000','2005'], figsize = (15,5), kind = plot)
plt.title("Agricultural land (% of land area)")
plt.show()'''


'''
df1= df1.drop(["Country Code","Indicator Code"],axis =1) #drop the unused column from the dataset
df1.set_index("Indicator Name",inplace = True) # setting up the index for the "Indicator Name"
#df2 = df1.copy()
df1 = df1.loc["Population growth (annual %)"]
df1 = df1.reset_index(level = "Indicator Name")
df1.groupby(["Country Name"]).sum() #group the data on the base of country Name
# taking the head 15 simple data of country
#print(df1)

df1 = df1.loc[df1["Country Name"].isin(["India", "Afghanistan", "United States", "Andorra", "United Arab Emirates", "Syrian Arab Republic", "Germany", "South Sudan", "Croatia","China"]), :]
#df1 = df1.loc[10:14, ["Country Name", "1961", "1981", "2001", "2021"]]    

#df1 = df1.head(15)
#df1 = df1.groupby("Country Name")
#df1 = df1[["India", "United Kingdom", "Aruba"]]
# ploting the data in bar plot
df1.plot(x= "Country Name",y = ['1961', '1981', '2001', "2021"],figsize = (15,5), kind="bar")
plt.title("Population growth (annual %)")
plt.ylabel("Frequency")
plt.show()'''
    