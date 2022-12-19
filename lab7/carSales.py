import pandas as pd

df = pd.read_csv("carSale.csv").set_index('Month').T
car_dict = df.to_dict()
print(df)

# 1
ford_dict = car_dict.get("Ford Motor Company")
sale_values = list(dict.values(ford_dict))
sale_values[:] = [int(value.replace(',', '')) for value in sale_values]
total_ford_sales = sum(sale_values)
print(total_ford_sales)

# 2
may_sales = list(df.loc['May'])
may_sales[:] = [int(sales.replace(',', '')) for sales in may_sales]
print(sum(may_sales))

# 3
august_sales = list(df.loc['Aug'])
august_sales[:] = [int(sales.replace(',', '')) for sales in august_sales]
print(sum(august_sales) / len(august_sales))

# 4

