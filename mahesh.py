#necesarry modules were imported
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#defining the function
def import_dataset(dataset):
    """
    This function reads an Excel file and returns two dataframes, one with years as columns and another with countries as columns.
    
    Parameters
    ----------
    dataset : str
        The filename of the Excel file to read.
    
    Returns
    -------
    df1 : pandas.DataFrame
        The original dataframe read from the Excel file.
    df2 : pandas.DataFrame
        A transposed dataframe with years as columns and countries as rows.
    """
    
    
    df_1 = pd.read_excel(dataset,skiprows=3)
    data_1 = df_1.copy()
    df_2 = data_1.drop(columns =["Country Code","Indicator Name","Indicator Code"],axis =1)
    df_2 = df_2.set_index("Country Name")
    df_2 = df_2.transpose()
    return df_1, df_2
    

def plot_heatmap():
    """
    Plot a heatmap of the correlations between a subset of indicators for a specific country.

    Returns
    -------
    None.

    """
    
    
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
    plt.title("India Indicators correlation", fontsize=20)
    plt.show()

#defining the corelation function
def Bar_corelation(data, ind, plot):
    """
    This function plots a bar, line or area chart for a specific indicator across multiple countries.
    
    Parameters
    ----------
    data : pandas.DataFrame
        The original dataframe read from the Excel file.
    indicator : str
        The name of the indicator to plot.
    plot : str
        The type of plot to create. Must be one of "bar", "line", or "area".
    """
    
    
    data= data.drop(["Country Code","Indicator Code"],axis =1)
    data.set_index("Indicator Name",inplace = True) 
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
    
    # calculate skewness and kurtosis values
    skewness = data.loc[:, '1990':'2019'].skew()
    kurtosis = data.loc[:, '1990':'2019'].kurtosis()
    print(f"Skewness values: {skewness}")
    print(f"Kurtosis values: {kurtosis}")
    
    plt.title(ind, fontsize=20)
    plt.ylabel("Frequency")
    plt.show()
    
    
# Main Program
if __name__ == "__main__":
    
    
    # Loading and preprocessing the data
    df1, df2 = import_dataset("data.xls")
    # use of describe function
    print(df2.describe())
    df2.fillna(0)
    plot_heatmap()
    #Plotting the bar, line, and area plots according to the indicators
    Bar_corelation(df1, "Population growth (annual %)", "bar")
    Bar_corelation(df1, "Renewable energy consumption (% of total final energy consumption)", "bar")
    Bar_corelation(df1, "Electric power consumption (kWh per capita)", "line")
    Bar_corelation(df1, "Forest area (sq. km)", "area")
    Bar_corelation(df1, "Total greenhouse gas emissions (kt of CO2 equivalent)", "line")

