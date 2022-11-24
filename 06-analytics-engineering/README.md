# Analytics Engineering

## Getting Started


Change Directory
```sh
cd 06-analytics-engineering
```

For Create Virtual Environment:
```sh
python -m venv ENV
```

For Activate Virtual Environment:
```sh
source ENV/bin/activate
```

For Install Package 
```sh
pip install -r requirements.txt
```



Create a dbt project
![image](https://user-images.githubusercontent.com/111840507/203825997-5565d756-395e-46d1-804a-0466b4692103.png)
```sh
dbt init
```

Edit the dbt profiles

```sh
code ~/.dbt/profiles.yml
```

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

Test dbt connection

```sh
cd jaffle
dbt debug
```

You should see "All checks passed!".

To create models

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
