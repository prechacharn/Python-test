import pandas as pd
df = pd.read_csv('test_candidate_03.csv')
grouped_df = df.groupby("shop_id")["gmv_usd"].sum()
sorted_df = grouped_df.sort_values(ascending=False)
top_10_shops = sorted_df.head(10)
print(top_10_shops)
