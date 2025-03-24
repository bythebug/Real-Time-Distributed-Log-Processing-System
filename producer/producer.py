from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    log = {
        "timestamp": time.time(),
        "level": random.choice(["INFO", "WARN", "ERROR"]),
        "message": "Sample log message"
    }
    producer.send('logs', value=log)
    time.sleep(0.001)