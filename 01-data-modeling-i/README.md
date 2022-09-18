# Data Modeling I

##Command Line for Data Modeling I
## Getting Started


Change Directory
```sh
cd 01-data-modeling-i/
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

### Prerequisite when install psycopg2 package

For Debian/Ubuntu users:

```sh
sudo apt install -y libpq-dev
```

For Mac users:

```sh
brew install postgresql
```

## Postgres

For Running Postgres
```sh
docker-compose up
```
Login 
```sh
system: PostgreSQL
Server: postgres
Username: postgres
Password: postgres
Database: postgres
ports: 5432  8080
```

For Create Table
```sh
python create_tables.py
```

For Load JSON File To Postgres
```sh
python etl.py
```

For Clear Terminal
```sh
clear
```

To shutdown, press Ctrl+C and run:

```sh
docker-compose down
```

To shutdown, Dectivate Virtual Environment:
```sh
deactivate
```
