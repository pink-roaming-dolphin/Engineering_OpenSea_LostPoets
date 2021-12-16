### Analysis/ Engineering Project on Lost Poets NFT Collection on OpenSea ###

**Workflow**
*Project*
There is an NFT art project that as minted beginning of September and has been trading since then. The trading volume is 26.5K as of today and there are 27.5 K items in this collection (so distinct NFTs under the same collection). 

The NFT collection can be found here: : 
[LostPoets by pak](https://opensea.io/collection/lostpoets)

*Data collection/storage*
I want to get the data related to this collection and analyze the transactions made on this collection. 
For the data collection, I will use 2 OpenSea APIs (well 3, if you count the Collections API which gives you the simple information on the collection such as editors, contract address etc). The other 2 APIs will enable me to collect the data on each of the items and the data on the transactions. 

I will store this information in a MongoDB Database (not sure if this should be a SQL database instead). 

*Data processing*
I will do EDA on the data collected looking at the owners of the data, the price changes in the last 3.5 months and see which poets got more attention. 
Depending on time/ how the time goes, I will try and see if I can model a linear regression model looking at price as effected by owner, trade volume etc. 

*Deployment*
I will do a web application in which either I do visualization on the EDA results or a Flask app using the linear model. 

**Tools** 
- OpenSea API (Assets API & Events API) for data acquisition in real time 
- MongoDB or SQLite for database managemet (not sure which one is more appropriate) 
- Numpy & Pandas for EDA (and possibly SKLearn for modeling) 
- Tools for visualization (Bokeh?) (and possibly Flask/Streamlit for building an app) 

**MVP Goal**
Have data collection/storage and EDA and/or modelling done

![lost_poets_workflow_2](https://user-images.githubusercontent.com/81533137/145303850-eb400fd7-3d14-4596-8849-5db01b04b505.jpg)
