# Hawaii Climate Analysis

## Introduction

The purpose of this project was to build an App using Flask that could query a database containing several months of climate data retrieved from weather stations in Hawaii. 
All of the analysis uses SQLAlchemy ORM queries, Pandas, and Matplotlib. 

## Technologies

* Python
* SQLAlchemy
* Pandas
* Matplotlib
* Flask

### Precipitation Analysis

* Using the most recent date from the data set, the previous 12 months of precipitation data was retrieved by querying the data. 

* The query results were loaded into a Pandas DataFrame with the date column set as the index.

* The results were then plotted and Pandas was used to print the summary statistics for the precipitation data.

### Station Analysis

* Queries were designed to: 

    * Calculate the total number of stations in the dataset.

    * Find the most active stations (i.e. which stations have the most rows?).

    * List the stations and observation counts in descending order.

    * Find which station id had the highest number of observations?

    * Using the most active station id, calculate the lowest, highest, and average temperature.

    * Design a query to retrieve the last 12 months of temperature observation data (TOBS).

    * Filter by the station with the highest number of observations.

    * Find the last 12 months of temperature observation data for this station.

### Climate App

After completing the initial analysis, a Flask API was designed based on the queries that were developed.

* Flask was used to create the following routes when ran locally.

#### Routes

* `/`

  * Home page.

  * Lists all routes that are available.

* `/api/v1.0/precipitation`

  * Converts the query results to a dictionary using `date` as the key and `prcp` as the value.

  * Returns the JSON representation of the dictionary.

* `/api/v1.0/stations`

  * Returns a JSON list of stations from the dataset.

* `/api/v1.0/tobs`
  * Queries the dates and temperature observations of the most active station for the last year of data.

  * Returns a JSON list of temperature observations (TOBS) for the previous year.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * Returns a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

  * When given the start only, calculates `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

  * When given the start and the end date, calculates the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.

![Precipitation](https://user-images.githubusercontent.com/75442215/125850180-83afd3ec-3a58-4605-8295-df9588887b08.png)
![tobs](https://user-images.githubusercontent.com/75442215/125850183-f7794056-74a2-4aca-93f2-aaa7dae8d2f1.png)


