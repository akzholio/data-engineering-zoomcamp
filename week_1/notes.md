# Postgres
Install pgcli: `pip install pgcli`

Connect to running DB: `pgcli -h localhost -p 5432 -u prefect -d ny_taxi_data`

Order is important:
```
      POSTGRES_DB: ny_taxi_data
      POSTGRES_USER: prefect
      POSTGRES_PASSWORD: prefect
```
