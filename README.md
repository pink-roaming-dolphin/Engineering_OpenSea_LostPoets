Blog post about project here: [Medium - OpenSea Project](https://medium.com/@zey-o/lost-poets-on-the-loose-sleeping-interlocutors-1d7696d25a3b)

Streamlit apps for the 2 parts of the project can be found here: 
- [5 pm Tea: Generating more Poets with GAN](https://share.streamlit.io/zey-o/engineering_opensea_lostpoets/main/gan_poets.py)
- [LostPoets financial analysis](https://share.streamlit.io/zey-o/engineering_opensea_lostpoets/main/financial_sales_streamlit.py)

Project presentation can be found here: [presentation](https://github.com/zey-o/Engineering_OpenSea_LostPoets/blob/main/Presentation_OpenSea_LostPoets.pdf)


## Analyze & Play: LostPoets on OpenSea

**Abstract**

This project uses engineering and data tools to analyze an NFT collectible called LostPoets as it is listed on the marketplace OpenSea and deploys it on a Streamlit app. It also creates a GAN model to derive generated images from the scraped images of the NFT collectible. Using the Opensea Assets & Events API to get data, the first part does a financial analysis of the sales transactions in order to deduce which users have been exchanging the most with each other, the volume of trades, the highest prices achieved whereas the second part of the project downloads the collection images and uses them to create poet look alikes. 

**Design**

The NFT collectible called LostPoets had +25K items and +25K token trades to analyze and visualize the exchange data. I used the OpenSea API to access the data which has a limit of 10K data points per execution: the Events API to get data on 10K transactions & the Assets API to get data on 10K LostPoet items include image URLs. Consequently I scraped the image URL’s to download those 10K images. 

The data from the API was stored in a MongoDB and was later pulled in to work with pandas + python to do data cleaning and EDA. An initial linear regression model was fit on the financial data but we got an R2 value of 1.1 so instead we went ahead with EDA and found statistics on who the most frequent buyer/sellers are, what the volume of trades is, the daily and weekly trends. 

The data from the Assets API was used with a DL algorithm to generate more poets to add to the gamification aspect of the LostPoets. 

**Data**

Dataset was obtained by using the OpenSea Assets & Events API’s. 
10K transaction data & 10K assets data were obtained with 26 and 28 features consecutively. 
This data was stored on a MongoDB. 
One of the columns in the assets data was image URL’s so 10K images were scraped and stored locally. 

**Algorithms**
- Keras, PIL, CV2 for Deep Learning 
- scikit-learn and Prophet for Linear Regression (with no promising results) 

**Tools**
- OpenSea API for data acquisition
- MongoDB for data storage
- pandas, python for data cleaning 
- Matplotlib, Seabrn for visualization & EDA 
- GoogleColab for modelling 
- Streamlit for web application  
