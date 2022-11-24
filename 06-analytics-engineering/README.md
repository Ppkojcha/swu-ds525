# Analytics Engineering

## Getting Started เริ่มต้น


## Change Directory เข้า Folder 06-analythics-engineering

```sh
cd 06-analytics-engineering
```

## For Create Virtual Environment: สร้าง Environment 

```sh
python -m venv ENV
```

## For Activate Virtual Environment: เข้าสู่ ENV Environment

```sh
source ENV/bin/activate
```

## For Install Package ติดตั้ง Package ที่จำเป็นในไฟล์ Requirements.txt

```sh
pip install -r requirements.txt
```



## Create a dbt project 

```sh
dbt init
```
![image](https://user-images.githubusercontent.com/111840507/203825997-5565d756-395e-46d1-804a-0466b4692103.png)

## ระบบจะให้ใส่ชื่อของ Project ในที่นี้ ใส่เป็น Jaffle  และถามถึง Database ที่จะใช้ 


## Edit the dbt profiles

```sh
code ~/.dbt/profiles.yml
```

![image](https://user-images.githubusercontent.com/111840507/203826330-a8fe506a-1d0d-4d99-aeda-8da422f22a8e.png)
## เมื่อ RUN CODE ด้านบน จะPOP UP File Profiles.yml ขึ้นมา ให้แก้ไขดังนี้

# FOR dbt Profiles

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
![image](https://user-images.githubusercontent.com/111840507/203826356-2be05863-4183-4465-9fc0-905631b989db.png)


## Test dbt connection ตรวจสอบ Connection

## โดย เข้า Change Directory เข้า Folder Jaffle แล้ว ตามด้วย CODE 
```sh
cd jaffle
dbt debug
```


## You should see "All checks passed!".
## หาก Connection เรียบร้อยจะขึ้น "All checks passed!"
![image](https://user-images.githubusercontent.com/111840507/203826777-ac9bd40d-2698-4c2e-bdb1-64ce7f781e51.png)


## To create models
## สร้าง MODEL เมื่อ

```sh
dbt run
```
![image](https://user-images.githubusercontent.com/111840507/203827132-ed6356c9-ec0c-4715-b3c5-140880ead22b.png)


## To test models

```sh
dbt test
```
![image](https://user-images.githubusercontent.com/111840507/203827319-c9e95d6c-956f-47cd-8dbe-775ccbdc866d.png)
![image](https://user-images.githubusercontent.com/111840507/203827341-171967cb-fd67-4baa-87dc-79e479eb1304.png)

## Open SQL  URL (port 3000)
![image](https://user-images.githubusercontent.com/111840507/203827797-12eb562e-3350-4c99-8111-240d76bb21c8.png)

## Example Select SQL
![image](https://user-images.githubusercontent.com/111840507/203828527-477c71a0-1264-4a29-94f6-86a7f8d478b9.png)

1. ![image](https://user-images.githubusercontent.com/111840507/203828602-d816110f-4a8b-4436-82df-738184a423ad.png)

2. ![image](https://user-images.githubusercontent.com/111840507/203828684-69d41562-c6c3-419f-8064-778d6968e933.png)

## To view docs (on Gitpod)

```sh
dbt docs generate
dbt docs serve
```
