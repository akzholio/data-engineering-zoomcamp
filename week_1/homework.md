## Week 1 Homework

In this homework we'll prepare the environment 
and practice with Docker and SQL


## Question 1. Knowing docker tags

Run the command to get information on Docker 

```docker --help```

Now run the command to get help on the "docker build" command

Which tag has the following text? - *Write the image ID to the file* 

- `--imageid string`
- `--iidfile string`
- `--idimage string`
- `--idfile string`

## Answer 1.
`✅ --iidfile string`

## Question 2. Understanding docker first run 

Run docker with the python:3.9 image in an interactive mode and the entrypoint of bash.
Now check the python modules that are installed ( use pip list). 
How many python packages/modules are installed?

- 1
- 6
- 3
- 7

## Answer 2.
`✅ 3`

# Prepare Postgres

Run Postgres and load data as shown in the videos
We'll use the green taxi trips from January 2019:

```wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-01.csv.gz```

You will also need the dataset with zones:

```wget https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv```

Download this data and put it into Postgres (with jupyter notebooks or with a pipeline)


## Question 3. Count records 

How many taxi trips were totally made on January 15?

Tip: started and finished on 2019-01-15. 

Remember that `lpep_pickup_datetime` and `lpep_dropoff_datetime` columns are in the format timestamp (date and hour+min+sec) and not in date.

- 20689
- 20530
- 17630
- 21090

## Answer 3.
```
select 
    count(1) 
from green_taxi_data 
where date(lpep_pickup_datetime) = '2019-01-15' 
    and date(lpep_dropoff_datetime) = '2019-01-15';

✅ 20530
```

## Question 4. Largest trip for each day

Which was the day with the largest trip distance
Use the pick up time for your calculations.

- 2019-01-18
- 2019-01-28
- 2019-01-15
- 2019-01-10

## Answer 4.

```
✅
+------------+-------------------+
| date       | max_trip_distance |
|------------+-------------------|
| 2019-01-15 | 117.99            |

select 
    date(lpep_pickup_datetime), 
    max(trip_distance) as max_trip_distance 
from green_taxi_data 
group by 1 
order by 2 desc;
```

## Question 5. The number of passengers

In 2019-01-01 how many trips had 2 and 3 passengers?
 
- 2: 1282 ; 3: 266
- 2: 1532 ; 3: 126
- 2: 1282 ; 3: 254
- 2: 1282 ; 3: 274

## Answer 5.
```
✅ 2: 1282 ; 3: 254
select 
    count(1) 
from green_taxi_data 
where date(lpep_pickup_datetime) = '2019-01-01' 
    and passenger_count = [2/3];
```
## Question 6. Largest tip

For the passengers picked up in the Astoria Zone which was the drop off zone that had the largest tip?
We want the name of the zone, not the id.

Note: it's not a typo, it's `tip` , not `trip`

- Central Park
- Jamaica
- South Ozone Park
- Long Island City/Queens Plaza

## Answer 6.

```
✅ Long Island City/Queens Plaza

WITH BASE AS
	(SELECT "DOLocationID" AS LOCATION_ID,
			MAX(TIP_AMOUNT) AS MAX_TIP_AMOUNT
		FROM PUBLIC.GREEN_TAXI_DATA
		WHERE "PULocationID" IN
				(SELECT LOCATION_ID
					FROM PUBLIC.TAXI_ZONE_LOOKUP_DATA
					WHERE ZONE_NAME = 'Astoria')
		GROUP BY 1
		ORDER BY 2 DESC)
SELECT *
FROM BASE
LEFT JOIN PUBLIC.TAXI_ZONE_LOOKUP_DATA USING (LOCATION_ID)
ORDER BY 2 DESC
LIMIT 1;
```

## Submitting the solutions

* Form for submitting: [form](https://forms.gle/EjphSkR1b3nsdojv7)
* You can submit your homework multiple times. In this case, only the last submission will be used. 

Deadline: 26 January (Thursday), 22:00 CET


## Solution

We will publish the solution here