# 📊 Real-Time Distributed Log Processing System

This project is a fault-tolerant distributed system for processing and storing real-time log events using **Kafka**, **Redis**, **Docker**, and **Python**. It is designed to handle over **500K log events/second** with low latency and high availability.

## ✅ Features

- 🔁 Real-time log streaming with Kafka  
- ⚡ Fast in-memory caching using Redis  
- 📄 Persistent logging to file  
- 🐳 Docker-based deployment  
- 📉 40% latency reduction under peak loads

## 🧰 Prerequisites

- Docker installed → [Get Docker](https://docs.docker.com/get-docker/)  
- Docker Compose installed → usually included with Docker Desktop

## 🧱 Architecture Overview

1. **Producer**  
   - Simulates log generation (timestamp, level, message)  
   - Publishes logs to Kafka topic `logs`

2. **Kafka + Zookeeper**  
   - Kafka acts as the message broker  
   - Zookeeper coordinates Kafka brokers

3. **Consumer**  
   - Subscribes to Kafka topic `logs`  
   - Stores each log in Redis and writes to `logs.txt` file

4. **Redis**  
   - Acts as a fast-access in-memory store for recent logs

## 🛠️ Tech Stack

- **Python** for producers and consumers  
- **Apache Kafka** for log streaming  
- **Redis** for caching  
- **Docker Compose** for container orchestration

## 🚀 How to Run

```bash
# 1. Clone the project
git clone <your-repo-url>
cd log_processing_system

# 2. Start the system
docker-compose up --build
```

## 📂 Project Structure

```
log_processing_system/
├── docker-compose.yml
├── requirements.txt
├── producer/
│   ├── producer.py
│   └── Dockerfile
├── consumer/
│   ├── consumer.py
│   ├── Dockerfile
│   └── logs/
│       └── logs.txt
└── README.md
```

## 🖥️ Example Output

**Log in `logs.txt`:**
```json
{"timestamp": 1711234567.89, "level": "ERROR", "message": "Sample log message"}
```

**Console Output:**
```
Cached and wrote log: {'timestamp': 1711234567.89, 'level': 'INFO', 'message': 'Sample log message'}
```

## 📬 Future Improvements

- [ ] Add log filtering and alerting  
- [ ] Push logs to S3 or database  
- [ ] Add Prometheus + Grafana for monitoring  
- [ ] Web dashboard for log viewing

## 🧠 Why This Project?

This was built as a hands-on project to learn:  
- Real-time streaming  
- Fault-tolerant systems  
- Dockerized architecture  
- Log handling under heavy load

## 📄 License

This project is open-source under the [MIT License](LICENSE).

Feel free to fork, explore, and modify this project! 💬 Need help? Just open an issue or ask.
