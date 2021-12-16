**LostPoets** 

I used an API Key I got from OpenSea to acquire 10K sales data points and 10K item(asset) data points and stored them in MongoDB. 
(the total for each is about 25K, but the API cuts off at 10K datapoints). 

1. Both datasets were cleaned and EDA/Visualization was done on the sales dataset for the following (plots below): 
- top 10 tokens by highest price paid  
- volume trade (all tokens that were traded at least 10 times) 
- highest average prices for tokens 
- top sellers by amount received 
- top buyers by total amount spent 
- the buyers + sellers that had the most interaction between them
- total amount exchanged between buyers and sellers 
- total amount of sales by week 
- total amount of sales by day 

2. I also tried a linear regression trying to determine the price of an asset given the sales data. I got an R2 of 0.10 so I'm not planning on using this in my web application. 
3. I also tried a timeseries model which is not a good predictor neither although it does give me trends for weekly and daily so this might be something I pursue. 

4. Lastly, I also scraped the images for the items. I am going to put them together in the web application such that someone could ask to see which ones are the 'origin' poets and those would be displayed. Or at least if someone is looking at a specific item, they could see the image.  



![Engineering Workflow MVP](https://user-images.githubusercontent.com/81533137/145894991-c603f3b1-f071-44c6-9407-9a3830b71a55.png)
![Sellers By Total Amount Received](https://user-images.githubusercontent.com/81533137/145896218-e6e7f8b0-14fb-43c0-a760-9f609ba9dd21.png)
![Token by Highest Price Paid](https://user-images.githubusercontent.com/81533137/145896221-1a60c726-0743-40e5-8c23-73b619feb596.png)
![Total Amount of Sales by Week](https://user-images.githubusercontent.com/81533137/145896223-a6a212a9-d725-46ec-b6ac-5fa6d153daf8.png)
![Total Number of Interactions between Specific Buyers and Sellers](https://user-images.githubusercontent.com/81533137/145896227-52394fa6-5c81-47b8-a02b-0f609f5a7d98.png)
![Volume Trade](https://user-images.githubusercontent.com/81533137/145896405-2b864d7e-724d-440b-b303-f9afad15fe6f.png)
![Buyers By Total Amount Received](https://user-images.githubusercontent.com/81533137/145896273-0e8408b9-5f7f-4af3-bae0-e5c1235d2b23.png)
![Daily Total Amount of Sales](https://user-images.githubusercontent.com/81533137/145896274-e47cc5f2-e588-4654-82f3-9c22bfa582eb.png)
![Highest Average Prices](https://user-images.githubusercontent.com/81533137/145896383-1f10fcf2-e566-4c37-8cf9-8a8cc6c9456a.png)
