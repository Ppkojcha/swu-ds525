# Capstone Project Kojcharat Narupatpajong 64199130032

## Data model 
![image](https://user-images.githubusercontent.com/111840507/208472009-2328bcae-0a24-4740-82dc-4ccac958f187.png)
<br>

## Data model (Datawarehouse)
![image](https://user-images.githubusercontent.com/111840507/208472125-464ef7e9-ca55-43f3-bcbd-39576ffb3547.png)
<br>

## Project instruction

[Project instruction 64199130032.pdf](https://github.com/Ppkojcha/swu-ds525/files/10270046/Project.instruction.64199130032.pdf)
<br>

## Project presentation
[store sales.pdf](https://github.com/Ppkojcha/swu-ds525/files/10270023/store.sales.pdf)
<br>
### 1. Change directory to project **"08-capstone-project"**:
```sh
$ cd 08-capstone-project
```
<br>

### 2. Prepare access (AWS):
- credential AWS terminal
```sh
$ cat ~/.aws/credentials
```
![image](https://user-images.githubusercontent.com/111840507/208474090-342073eb-acc9-4bd9-857f-fc29ebe2205f.png)

- Copy 3 key ดังนี้ <br>

> - aws_access_key_id
> - aws_secret_access_key
> - aws_session_token

<br>

### 3. เตรียม Datalake storage (AWS S3):
- สร้าง S3 bucket ด้วย *"All public access"*
> - **preawcapstone**

![image](https://user-images.githubusercontent.com/111840507/208476326-dc5bb3ae-ef89-430c-adff-b03e2c417aa8.png)

<br>

### 4. เตรียม Datawarehouse storage (AWS RedShift):
- สร้าง Redshift cluster 

- ![image](https://user-images.githubusercontent.com/111840507/208477331-5aefa8a4-65f2-455d-8e81-bc7ebe733c3e.png)

- Copy "**Endpoint**" and ข้อมูล Cluster  เพื่อที่จะอัพเดตใน Redshift credential



<br>

### 5. สร้าง virtual environment ชื่อ **"ENV"** (ในครั้งแรก):
```sh
$ python -m venv ENV
```
<br>

### 6. Activate เข้าสู่ environment:
```sh
$ source ENV/bin/activate
```
<br>

### 7. ติดตั้ง libraries ที่จำเป็น (ในครั้งแรก):
```sh
$ pip install -r prerequisite/requirements.txt
```
<br>

### 8. เตรียม environment Docker:
- ถ้าเป็นระบบ Linux  ให้รันคำสั่งด้านล่างก่อน 

```sh
mkdir -p ./dags ./logs ./plugins
```
```sh
echo -e "AIRFLOW_UID=$(id -u)" > .env
```

- หลังจากนั้นใช้คำสั่งด้านล่าง เพื่อเริ่ม  Docker

```sh
docker-compose up
```
<br>

### 9. **"Datawarehouse"** ผ่าน Airflow:
- เข้าสู่ Airflow ผ่าน port 8080 (localhost:8080) 
> - Username: "airflow"<br>
> - Password: "airflow"<br>

- ข้อมูลบน Datawarehouse จะถูกโหลด เข้าสู่  Redshift 
```sh
select * from customer;
```
![image](https://user-images.githubusercontent.com/111840507/208483226-fb4dbcd0-e6de-4f5d-a10c-00e3376fb7e3.png)
<br>

### 10. สร้าง Dashboard ด้วย Tableau:

![image](https://user-images.githubusercontent.com/111840507/208483805-2bf94c71-d30b-4197-8387-5989a5ffe041.png)

<br>

<br>

## Shutdown 
##### 1. shutdown Docker:
```sh
$ docker-compose down
```

##### 2. Deactivate the virtual environment:
```sh
$ deactivate
```
