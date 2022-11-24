# Analytics Engineering

## Getting Started


## Change Directory
```sh
cd 06-analytics-engineering
```

## For Create Virtual Environment:
```sh
python -m venv ENV
```

## For Activate Virtual Environment:
```sh
source ENV/bin/activate
```

## For Install Package 
```sh
pip install -r requirements.txt
```



## Create a dbt project

![image](https://user-images.githubusercontent.com/111840507/203825997-5565d756-395e-46d1-804a-0466b4692103.png)
```sh
dbt init
```

## Edit the dbt profiles
![image](https://user-images.githubusercontent.com/111840507/203826330-a8fe506a-1d0d-4d99-aeda-8da422f22a8e.png)

```sh
code ~/.dbt/profiles.yml
```

## DBT Profiles

![image](https://user-images.githubusercontent.com/111840507/203826356-2be05863-4183-4465-9fc0-905631b989db.png)

```yml
jaffle:
  outputs:

    dev:
      type: postgres
      threads: 1
      host: localhost
      port: 5432
      user: postgres
      pass: postgres
      dbname: postgres
      schema: public

    prod:
      type: postgres
      threads: 1
      host: localhost
      port: 5432
      user: postgres
      pass: postgres
      dbname: postgres
      schema: prod

  target: dev
```

## Test dbt connection

```sh
cd jaffle
dbt debug
```

## You should see "All checks passed!".
![image](https://user-images.githubusercontent.com/111840507/203826777-ac9bd40d-2698-4c2e-bdb1-64ce7f781e51.png)

## To create models

```sh
dbt run
```

To test models

```sh
dbt test
```

To view docs (on Gitpod)

```sh
dbt docs generate
dbt docs serve
```
