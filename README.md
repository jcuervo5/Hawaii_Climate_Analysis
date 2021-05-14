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

* Start by finding the most recent date in the data set.

* Using the most recent date from the data set, the previous 12 months of precipitation data was retrieved by querying the 12 preceding months of data. 

* The query results were loaded into a Pandas DataFrame with the date column set as the index.

* The results were plotted and Pandas was used to print the summary statistics for the precipitation data.

### Station Analysis

* Queries were designed to: 

    1. Calculate the total number of stations in the dataset.

    2. Find the most active stations (i.e. which stations have the most rows?).

    3. List the stations and observation counts in descending order.

    4. Find which station id had the highest number of observations?

    5. Using the most active station id, calculate the lowest, highest, and average temperature.

    6. Design a query to retrieve the last 12 months of temperature observation data (TOBS).

    7. Filter by the station with the highest number of observations.

    8. Find the last 12 months of temperature observation data for this station.

## Create Climate App

After completing the initial analysis, a Flask API was designed based on the queries that were developed.

* Flask was used to create the following routes.

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


