
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("dark")

st.write(
'''
## LOSTPOETS in (the) OpenSea(s)

### The Sales 🔥🔥🔥
'''
)

poets = pd.read_csv('poets_clean.csv')
# st.dataframe(poets)

sales_df = pd.read_csv('sales.csv')
# st.dataframe(sales_df)


## cleaning 
sales_df.total_price = sales_df.total_price.astype(float) 
sales_df.total_price = sales_df.total_price/10.**18
sales_df.total_price = sales_df.total_price * sales_df.payment_token_usd_price
sales_df.asset_token_id = sales_df.asset_token_id.astype(int) 
sales_df['created_date'] = pd.to_datetime(sales_df['created_date'])

# st.write(
# '''
# **Highest Prices**
# '''
# )

highest_paid = 'Highest price paid for a poet 😱'.upper()
most_traded = 'Most frequently traded poets (maestros 🎓)'.upper()
highest_average = 'Poets with highest average trading price ☄️'.upper()
prompt = 'Do you want to know them better?'
option_swim = st.selectbox(
     'Poets swimming amongst us ☁️☁️ ',
     (prompt, highest_paid, most_traded, highest_average))
##☁️☁️

## HIGHEST PRICES PAID
if option_swim == highest_paid: 
	fig, ax = plt.subplots()
	fig.patch.set_alpha(0)
	ax.scatter([1, 2, 3], [1, 2, 3])
	# DF to use 
	token_prices = (sales_df.groupby(['asset_token_id']).mean()["total_price"]
	                                                    .to_frame().reset_index())
	token_prices_top_10 = token_prices.sort_values(by=['total_price'],ascending=False)[:10]
	sns.barplot(x = 'asset_token_id', y = 'total_price', data = token_prices_top_10, order = token_prices_top_10['asset_token_id'])
	plt.xlabel("token ID", size=12)
	plt.ylabel("\$$", size=15)
	plt.title("Highest Price Paid for a Poet", size=15)
	st.pyplot(fig)

## VOLUME OF TRADE
if option_swim == most_traded: 
	fig, ax = plt.subplots()
	fig.patch.set_alpha(0)
	ax.scatter([1, 2, 3], [1, 2, 3])
	# DF to use 	
	highest_volume = (sales_df.groupby(['asset_token_id']).sum()
	                                     .sort_values(by=['asset_num_sales'],ascending=False)
	                                     .reset_index())
	# drop the first row as this is the 1st token 
	highest_volume = highest_volume.iloc[1:]
	highest_top = highest_volume[highest_volume.asset_num_sales > 9]
	(sns.barplot(x = 'asset_token_id', y = 'asset_num_sales', 
	             data = highest_top, order = highest_top['asset_token_id']))
	plt.xlabel("token ID", size=12)
	plt.ylabel("price paid", size=12)
	plt.title("Volume Trade", size=15)
	st.pyplot(fig)

## HIGHEST AVE. TRADING PRICE 
if option_swim == highest_average: 
	fig, ax = plt.subplots()
	fig.patch.set_alpha(0)
	ax.scatter([1, 2, 3], [1, 2, 3])
	# DF to use 	
	highest_volume = (sales_df.groupby(['asset_token_id']).sum()
                                     .sort_values(by=['asset_num_sales'],ascending=False)
                                     .reset_index())
	highest_volume = highest_volume.iloc[1:]
	price_per_trade = highest_volume.copy()
	# add column representing average price per trade 
	price_per_trade['average_price_per_trade'] = (price_per_trade.total_price / 
	                                             price_per_trade.asset_num_sales)
	# sort by descending average price per trade 
	price_per_trade = price_per_trade.sort_values(by=['average_price_per_trade'],ascending=False)

	#drop the first row as this is the '0' token which doesn't exist
	price_per_trade = price_per_trade.iloc[1:]
	top_price_per_trade = price_per_trade[price_per_trade.average_price_per_trade >50000]
	(sns.barplot(x = 'asset_token_id', y = 'average_price_per_trade', 
             data = top_price_per_trade, order = top_price_per_trade['asset_token_id']))
	plt.xlabel("token ID", size=12)
	# plt.xticks(rotation=60)
	plt.ylabel("average price during trades", size=12)
	plt.title("Highest Average Prices", size=15)
	st.pyplot(fig)



sellers_ = 'Who is selling the most?'.upper()
buyers_ = 'Who is buying the most?'.upper()
interactions_freq = 'Interactions interactions! Who is brushing shoulders the most?'.upper()
interactions_amount = 'And the highest amount of shoulder brushing/amount exchanged?'.upper()
prompt = 'Who is exchanging the poets?'
option_people = st.selectbox(
     'Fish in the sea 🐬',
     (prompt, sellers_, buyers_, interactions_freq, interactions_amount))

if option_people == sellers_: 
	fig, ax = plt.subplots()
	fig.patch.set_alpha(0)
	ax.scatter([1, 2, 3], [1, 2, 3])
	# DF to use 	
	sellers = (sales_df.groupby(['seller_username']).sum()
	                                     .sort_values(by=['payment_token_usd_price'],ascending=False)
	                                     .reset_index())
	# drop the first row as this is the 'unknown' seller
	sellers = sellers.iloc[1:]
	top_sellers = sellers.iloc[:15]
	(sns.barplot(x = 'seller_username', y = 'payment_token_usd_price', 
	             data = top_sellers, order = top_sellers['seller_username']))
	plt.xlabel("seller username", size=12)
	plt.xticks(rotation=70)
	plt.ylabel("total money received", size=12)
	plt.title("Sellers By Total Amount Received", size=15)
	plt.savefig("Sellers By Total Amount Received.png", bbox_inches='tight', dpi=260)
	st.pyplot(fig)

if option_people == buyers_: 
	fig, ax = plt.subplots()
	fig.patch.set_alpha(0)
	ax.scatter([1, 2, 3], [1, 2, 3])
	# DF to use 	
	buyers = (sales_df.groupby(['winner_account_username']).sum()
                                     .sort_values(by=['payment_token_usd_price'],ascending=False)
                                     .reset_index())
	# drop the first row as this is the 'unknown' seller
	buyers = buyers.iloc[1:]
	top_buyers = buyers.iloc[:15]
	(sns.barplot(x = 'winner_account_username', y = 'payment_token_usd_price', 
	             data = top_buyers, order = top_buyers['winner_account_username']))
	plt.xlabel("buyers username", size=12)
	plt.xticks(rotation=70)
	plt.ylabel("total money spent", size=12)
	plt.title("Buyers By Total Amount Spent", size=15)
	st.pyplot(fig)

if option_people == interactions_freq: 
	fig, ax = plt.subplots()
	fig.patch.set_alpha(0)
	ax.scatter([1, 2, 3], [1, 2, 3])
	# DF to use 	

	buyer_seller = sales_df.copy()

	# remove rows where either seller or buyer is unknown 
	buyer_seller = buyer_seller[buyer_seller['seller_username'] != 'unknown']
	buyer_seller = buyer_seller[buyer_seller['winner_account_username']!= 'unknown']

	buyer_seller['seller_buyer_combo'] = (sales_df.seller_username + " --> " +
	                                      sales_df.winner_account_username)
	interactions_num_sales = (buyer_seller.groupby(["seller_buyer_combo"])
                         .sum()
                         .sort_values(by=['asset_num_sales'],ascending=False) 
                         .reset_index())
	top_num_interactions = interactions_num_sales[interactions_num_sales.asset_num_sales >75000]
	(sns.barplot(x = 'seller_buyer_combo', y = 'asset_num_sales', 
             data = top_num_interactions, 
             order = top_num_interactions['seller_buyer_combo']))
	plt.xlabel("From Seller to Buyer", size=12)
	plt.xticks(rotation=70)
	plt.ylabel("Number of sales", size=12)
	plt.title("Total Number of Interactions between Specific Buyers and Sellers", size=15)
	st.pyplot(fig)

if option_people == interactions_amount: 
	fig, ax = plt.subplots()
	fig.patch.set_alpha(0)
	ax.scatter([1, 2, 3], [1, 2, 3])
	# DF to use 	
	buyer_seller = sales_df.copy()

	# remove rows where either seller or buyer is unknown 
	buyer_seller = buyer_seller[buyer_seller['seller_username'] != 'unknown']
	buyer_seller = buyer_seller[buyer_seller['winner_account_username']!= 'unknown']

	buyer_seller['seller_buyer_combo'] = (sales_df.seller_username + " --> " +
	                                      sales_df.winner_account_username)
	interactions_total_price = (buyer_seller.groupby(["seller_buyer_combo"])
                            .sum()
                            .sort_values(by=['total_price'],ascending=False)
                            .reset_index())
	top_usd_interactions = interactions_total_price[interactions_total_price.total_price >75000]
	(sns.barplot(x = 'seller_buyer_combo', y = 'total_price', 
             data = top_usd_interactions, 
             order = top_usd_interactions['seller_buyer_combo']))
	plt.xlabel("From Seller to Buyer", size=12)
	plt.xticks(rotation=70)
	plt.ylabel("Amount of sales", size=12)
	plt.title("Total Amount Exchanged between Specific Buyers and Sellers", size=15)
	st.pyplot(fig)

daily_ = 'Day to day'.upper()
monthly_ = 'Month to month'.upper()
prompt = 'When is the question'
option_trends = st.selectbox(
     'And daily and montly trends for the poets amongst us 🥦🍓☔️🌞',
     (prompt, daily_, monthly_))

if option_trends == daily_: 
	fig, ax = plt.subplots()
	fig.patch.set_alpha(0)
	ax.scatter([1, 2, 3], [1, 2, 3])
	# DF to use 	
	monthly_sales = (sales_df.groupby(sales_df.created_date.dt.strftime('%W'))
                 .total_price.sum()
                 .to_frame().reset_index())
	(sns.lineplot(x = 'created_date', y = 'total_price', 
             data = monthly_sales))
	plt.xlabel("week of the year", size=12)
	plt.xticks(rotation=70)
	plt.ylabel("total amount of sales", size=12)
	plt.title("Total Amount of Sales by Week", size=15)
	st.pyplot(fig)


if option_trends == monthly_: 
	fig, ax = plt.subplots()
	fig.patch.set_alpha(0)
	ax.scatter([1, 2, 3], [1, 2, 3])
	# DF to use
	daily_sales = (sales_df.groupby(sales_df.created_date.dt.strftime('%D'))
                 .total_price.sum()
                 .to_frame().reset_index())
	ax = sns.lineplot(x = 'created_date', y = 'total_price', 
             data = daily_sales)
	plt.xlabel("day of the year", size=12)
	all_xticks = ax.get_xticks()
	plt.xticks([all_xticks[0], all_xticks[-1]], visible=True, rotation="horizontal")
	plt.ylabel("daily total sales", size=12)
	plt.title("Daily Total Amount of Sales", size=15)
	st.pyplot(fig)



st.write(
'''
### The Collection 🎨🖼️
[[LOSTPOETS]](https://lostpoets.xyz/) is an NFT collectible and a strategy game by pak. 
The NFT collection includes 65536 obtainable NFTs and 1024 Origin NFTs. 
The project's release is broken down into several stages. 

As of December 10, 2021, [OpenSea](https://opensea.io/collection/lostpoets) has over 27K poets listed on the marketplace 
and there have been over 26K trades in this collection. 
'''
)

