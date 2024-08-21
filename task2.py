import  pandas as pd
import os
# import sys

def filter_files(directory: str):
    # read in all csv files from a given directory
    # directory = sys.argv # check if exists
    array = []
    for filename in os.listdir(directory):
        if (filename.endswith(".csv")):
            array.append(pd.read_csv(os.path.join(directory, filename)))
    # combine all dataframes
    df = pd.concat(array)

    # using only 'Pink Morsels' in the 'product' field
    df = (df[df['product'] == 'pink morsel'])
    # combining 'quantity' & 'price' into 'sales'
    df['sales'] = df.apply(lambda x: float(x['price'][1:]) * x['quantity'], axis=1)

    # include sales, region, & date as only fields
    df.drop(columns=["product","quantity", "price"]).to_csv("../filtered_daily_sales_data.csv", index=False)

# use path from venv
filter_files("../data")