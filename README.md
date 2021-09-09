# SQLAlchemy Challenge

For this challenge I will be planning a trip to Honolulu, Hawaii and in order to better understand the climate SQLAlchemy will be used in order to complete my analysis.

Before beginning any analysis, I make sure that I am connecting to my database correctly and my existing database is being reflected onto the new model. After the setting up the connection I review how many tables I have, their names, and the type of rows that it contains. I also use DB Browser for SQLite to view more details on my database. 

--- 

### Analyzing The Precipitation 

To analyze the precipitation, I begin by retrieving the most recent date being August 23, 2017. Because I want to retrieve a year worth of data from the most recent date, I perform a mathematical equation to retrieve the date one year from the last date in the data set.  After storing the desired date, I can now move on to creating a query to retrieve the precipitation data for that year.  For the query I use my stored date to then use it as a filter for the date and precipitation to pull a year of the most recent data. This data is then converted into a data frame to be used on a Pandas plot.

Below you can see the Precipitation Analysis plot. Based on the plot there were a couple of instances where the inches of precipitation were very high, it would be best to avoid the months of August, September, February, April and May. Based on the data, the best months to avoid large amounts of precipitation would be October, November, and June.

---

### Analyzing The Most Active Station

After retrieving information for the precipitation an analysis also needed to be made on the stations. I wanted to know how many stations there were in total and which station was the most active based on how much data it contained. After filtering through the data, station USC00519281 appeared to be the most active. I then used the station name to use as a filter for my query to retrieve statistical information such as the min, max, and average. Using a similar mathematical calculation from my previous query along with the station name, I was able to pull the temperatures for the latest year for the most active station. The data is then made into a data frame to then plot on a histogram.

Below you can see the Station Analysis plot. It can be observed on the histogram that the temperature of about 76/77 was the most frequent for station USC00519281. 

  

