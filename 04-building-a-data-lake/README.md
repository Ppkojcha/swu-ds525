# Building a Data Lake

![datalake](https://user-images.githubusercontent.com/111840507/201708646-3f597e21-568d-4636-8809-b7efe48d1a21.jpg)


เพื่อให้เราสามารถสร้างไฟล์ได้จาก Jupyter Lab ให้รันคำสั่งด้านล่างนี้

```sh
sudo chmod 777 .
```

แล้วค่อยรัน

```sh
docker-compose up
```
# Command Line for Building a Data Lake

## Getting Started


Change Directory
```sh
cd 04-building-a-data-lake/workshop
```


For Running docker
```sh
docker-compose up
```


For Clear Terminal
```sh
clear
```

To shutdown, press Ctrl+C and run:

```sh
docker-compose down
```



Open URL and Token 

![token](https://user-images.githubusercontent.com/111840507/201709805-63c79099-b9c7-47df-989d-0e34d48a00f1.jpg)
![token1](https://user-images.githubusercontent.com/111840507/201709986-4c18ad03-76e6-45a7-ae34-69e0608e186a.jpg)


#  Partition
![partition](https://user-images.githubusercontent.com/111840507/201712376-0f9bc957-e15f-4d04-be15-4beb2b7e9f62.jpg)


# Create table actors PartitionBy ("year")
![actor](https://user-images.githubusercontent.com/111840507/201712504-033dade7-06c9-4d1a-b254-fb151625dd91.jpg)
![actor1](https://user-images.githubusercontent.com/111840507/201712536-6cd85ef7-1764-4fee-980b-8f978bdef8e0.jpg)



# Create table events PartitionBy ("month")
![event](https://user-images.githubusercontent.com/111840507/201712888-0789db8b-3caa-4565-9e4f-a2a01b33f6d9.jpg)
![event1](https://user-images.githubusercontent.com/111840507/201712882-4eee5274-f9cc-4ac4-ab7b-4f4e892465f5.jpg)

# Create table repos PartitionBy ("month")
![repo](https://user-images.githubusercontent.com/111840507/201712873-874d66fa-bdca-4cd1-9e92-4fdec9f75ada.jpg)
![repo1](https://user-images.githubusercontent.com/111840507/201712890-5df513df-cb72-447a-959c-6d6397f62424.jpg)

