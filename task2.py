import  pandas as pd

def filter_files():
    # reading original dataframe
    array = []
    for i in range(3):
        array.append(pd.read_csv(f"../data/daily_sales_data_{i}.csv")) # use path from venv

    df = pd.concat(array)
    # using only 'Pink Morsels' in the 'product' field
    df = (df[df['product'] == 'pink morsel'])

    # combining 'quantity' & 'price' into 'sales'
    df['sales'] = df.apply(lambda x: float(x['price'][1:]) * x['quantity'], axis=1)

    # include sales, region, & date as only fields
    df.drop(["quantity", "price"], axis=1).to_csv("../filtered_daily_sales_data.csv")

filter_files()