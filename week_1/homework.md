# Week 1 Homework + Solutions

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
```
✅ --iidfile string

docker build --help | grep "Write the image ID to the file"
```

## Question 2. Understanding docker first run 

Run docker with the python:3.9 image in an interactive mode and the entrypoint of bash.
Now check the python modules that are installed ( use pip list). 
How many python packages/modules are installed?

- 1
- 6
- 3
- 7

## Answer 2.
```
✅ 3

docker run -it python:3.9 bas
pip list

Package    Version
---------- -------
pip        22.0.4
setuptools 58.1.0
wheel      0.38.4
```

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
✅ 20530

SELECT COUNT(1)
FROM GREEN_TAXI_DATA
WHERE DATE(LPEP_PICKUP_DATETIME) = '2019-01-15'
	AND DATE(LPEP_DROPOFF_DATETIME) = '2019-01-15';
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
✅ 2019-01-15

SELECT DATE(LPEP_PICKUP_DATETIME),
	MAX(TRIP_DISTANCE) AS MAX_TRIP_DISTANCE
FROM GREEN_TAXI_DATA
GROUP BY 1
ORDER BY 2 DESC
LIMIT 1;
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

SELECT
	(SELECT COUNT(1)
		FROM GREEN_TAXI_DATA
		WHERE DATE(LPEP_PICKUP_DATETIME) = '2019-01-01'
			AND PASSENGER_COUNT = 2) AS TRIP_WITH_2_PASSENGERS_ON_2019_01_01,

	(SELECT COUNT(1)
		FROM GREEN_TAXI_DATA
		WHERE DATE(LPEP_PICKUP_DATETIME) = '2019-01-01'
			AND PASSENGER_COUNT = 3) AS TRIP_WITH_3_PASSENGERS_ON_2019_01_01;
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

WITH MAX_TIP_AMOUNT_AT_DROPOFF_LOCATION AS
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
FROM MAX_TIP_AMOUNT_AT_DROPOFF_LOCATION
LEFT JOIN PUBLIC.TAXI_ZONE_LOOKUP_DATA USING (LOCATION_ID)
ORDER BY 2 DESC
LIMIT 1;
```
