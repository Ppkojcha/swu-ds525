# Creating and Scheduling Data Pipelines

![ERdiagram](https://user-images.githubusercontent.com/111840507/190895168-3456cd37-5502-4541-ac8b-d41cc50bedcd.jpg)

## Getting Started
Change Directory
```sh
cd 05-creating-and-scheduling-data-pipelines
```sh

ถ้าใช้งานระบบที่เป็น Linux ให้เรารันคำสั่งด้านล่างนี้ก่อน
```sh
mkdir -p ./dags ./logs ./plugins
echo -e "AIRFLOW_UID=$(id -u)" > .env
```

หลังจากนั้นให้รัน
```sh
docker-compose up
```

เสร็จแล้วให้คัดลอกโฟลเดอร์ `data` ที่เตรียมไว้ข้างนอกสุด เข้ามาใส่ในโฟลเดอร์ `dags` เพื่อที่ Airflow จะได้เห็นไฟล์ข้อมูลเหล่านี้ แล้วจึงค่อยทำโปรเจคต่อ

**หมายเหตุ:** จริง ๆ แล้วเราสามารถเอาโฟลเดอร์ `data` ไว้ที่ไหนก็ได้ที่ Airflow ที่เรารันเข้าถึงได้ แต่เพื่อความง่ายสำหรับโปรเจคนี้ เราจะนำเอาโฟลเดอร์ `data` ไว้ในโฟลเดอร์ `dags` เลย

 
เราจะสามารถเข้าไปที่หน้า Airflow UI ได้ที่ port 8080
Login 
```sh
Username: airflow
Password: airflow
```
สร้าง Connection เชื่อมต่อ Postgres กับ Airflow จากเมนู Admin>Connections 
![connection](https://user-images.githubusercontent.com/111840507/203013979-a1bd528a-f258-4734-88d9-44029ec37380.jpg)


ทำการตั้งค่าการเชื่อมต่อใน Postgres Port 8088 
![adminer](https://user-images.githubusercontent.com/111840507/203014904-e5012703-307d-40f3-be93-c74877486c01.jpg)

Login 
```sh
System : PostgreSQL
Server : warehouse
Username: postgres
Password: postgres
Database : postgres

```

สร้างไฟล์ .py 

![airflow](https://user-images.githubusercontent.com/111840507/203016733-1bdff1c9-20d4-4769-a24a-78a0b910b252.jpg)
![table](https://user-images.githubusercontent.com/111840507/203016835-a6453f21-5ea1-4d6d-b910-2694204c404b.jpg)


For Clear Terminal
```sh
clear
```

To shutdown, press Ctrl+C and run:

```sh
docker-compose down
```
