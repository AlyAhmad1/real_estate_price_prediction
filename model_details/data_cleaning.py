import pandas as pd
from common import is_float, convert_sqft_num, remove_pps_outliers, plot_scatter_chart, remove_bhk_outliers

def data_cleaning():
    df = pd.read_csv("Bengaluru_House_Data.csv")

    # drop unnecessary columns.
    df2 = df.drop(['area_type', 'availability', 'society', 'balcony'], axis=1)

    # calculate N/A values
    # print(df2.isnull().sum())

    # drop N/A values ( we are dropping Null values because it is in small number ) if it is in large number then,
    # we can input some values in it like median/mean or some forward or reverse input value.
    df3 = df2.dropna()

    # create separate column for BHK values. ( example values are [2 BHK, 4 BHK, 4 bedrooms, 10 bedrooms])
    df3['bhk'] = df3['size'].apply(lambda x: int(x.split(" ")[0]))
    # print(df3.head())

    # check values are float in total_sqft
    # print(df3[~df3['total_sqft'].apply(is_float)])

    # there are multiple errors there in the above data in total_sqft columns. error in a sense like some values are in range
    # some values are in meters etc. so we need all in the float.
    # print(df3[~df3['total_sqft'].apply(is_float)]['total_sqft']) # this will show none float values in dataset.
    df4 = df3.copy()
    df4['total_sqft'] = df4['total_sqft'].apply(convert_sqft_num)

    # price_per_square_feet.
    df5 = df4.copy()
    df5['price_per_sqft'] = df5['price']*100000/df5['total_sqft']  # multiplied price with 100000 because its in lakh.
    # print(df5.head())

    # now we will mark location as other if it's count in the column is < 10.
    df5['location'] = df5['location'].apply(lambda x: x.strip(" "))

    location_stats = df5['location'].value_counts()
    location_stats_less_then_10 = location_stats[location_stats <= 10]

    df5['location'] = df5['location'].apply(lambda x: 'other' if x in location_stats_less_then_10 else x)
    # print(len(df5.location.unique()))
    # print(df5.shape)


    # ----------------------------------------------- outlier removal ----------------------------------------------------
    # let's remove outliers. ( as a dom ain requirements ) one bhk room is equal to 300 sqft. so will remove data which is less.
    df6 = df5[~(df5.total_sqft / df5.bhk<300)]
    # print(df6.shape)

    # remove outliers which are not in 1-std range.
    df7 = remove_pps_outliers(df6)
    # print(df7.shape)
    # print(df7.head())

    # plot prices vs sqft for a single location ( for 2 & 3 bhk )
    # plot_scatter_chart(df7, "Hebbal")


    df8 = remove_bhk_outliers(df7)
    # print(df8.shape)

    # remove the rows ( which have bathrooms more than bedrooms.)
    df9 = df8[df8.bath<df8.bhk+2]
    # print(df9.shape)

    # drop columns size & price_per_sqft ( bcz we were using these for outlier detection )
    df10 = df9.drop(['size','price_per_sqft'],axis='columns')


    # ----------------------------------------------- one hot encoding  ----------------------------------------------------
    # here we have location column which is in string so we will convert it to numbers by one-hot-encoding technique.
    dummies = pd.get_dummies(df10.location)

    # cancat dummies with original data-frame.
    df11 = pd.concat([df10.drop('location', axis='columns'), dummies.drop('other', axis='columns')], axis='columns')
    # print(df11.shape)
    return df11

