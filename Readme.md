
# Kafka Cluster on AWS EC2

## 구성
    kafka broker 서버는 3대로 클러스터를 구성

## 인스턴스 스펙

## 구축 방법
### 1. SSH 접속
### 2. hostname 변경
1. 1번 서버 
    ```sudo hostnamectl set-hostname kafka-1```
2. 2번 서버 : 
    ```sudo hostnamectl set-hostname kafka-2```
3. 3번 서버 : 
    ```sudo hostnamectl set-hostname kafka-3```
### 3. hosts 파일 추가  - 프라이빗 IP를 입력(listener로 사용)
    x.x.x.x kafka-1
    x.x.x.x kafka-2
    x.x.x.x kafka-3

### 타임존 변경

### 4. Java 설치 
   sudo yum install -y java-11-amazon-corretto.x86_64
   java -version

### 5. kafka 다운로드 
    wget https://downloads.apache.org/kafka/3.6.0/kafka_2.12-3.6.0.tgz
    tar -xvf kafka_2.12-3.6.0.tgz
    sudo ln -s /home/ec2-user/kafka_2.12-3.6.0 /opt/kafka

### 6. properties 변경
   1. zookeeper 설정파일 변경 \
   ```/opt/kafka/config/zookeeper.properties```
   2. kafka server.properties 변경 - kafka-1, 2, 3는 설정값이 다름 \
   ```/opt/kafka/config/server.properties```
   3. kafka distributed connector 설정 파일 생성 \
   ```/opt/kafka/s3-sink-connect-distributed.properties```

### 7. s3 sink connector plugin 다운로드
    wget https://api.hub.confluent.io/api/plugins/confluentinc/kafka-connect-s3/versions/4.1.1/archive
    unzip archive
    mkdir -p /opt/kafka/plugins/kafka-connect-s3
    sudo cp confluentinc-kafka-connect-s3-4.1.1/lib/* /opt/kafka/plugins/kafka-connect-s3/

### Zookeeper dataDir 생성, myid에는 zookeeper 서버 번호(각 1,2,3)이 입력된 파일을 생성
    mkdir -p /data/zookeeper
    echo 1 > /data/zookeeper/myid

### Zookeeper & Kafka 실행
    /opt/kafka/bin/zookeeper-server-start.sh -daemon /opt/kafka/config/zookeeper.properties
    /opt/kafka/bin/kafka-server-start.sh -daemon  /opt/kafka/config/server.properties

### 토픽 생성
    /opt/kafka/bin/kafka-topic.sh --bootstrap-server localhost:9092 --create --topic subway-arrival-topic --replication-factor 3 --partitions 3

### aws 접속 정보 등록
    aws configure

### kafka s3 sink connector 실행
    ./bin/connect-distributed.sh -daemon ./config/connect.properties

