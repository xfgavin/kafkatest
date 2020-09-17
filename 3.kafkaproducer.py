#!/usr/bin/env python3
from kafka import KafkaProducer
import numpy as np
producer = KafkaProducer(bootstrap_servers='localhost:9092')

mu, sigma = 10, 1 # mean and standard deviation
s = np.mean(np.random.normal(mu, sigma, 1000))
x = np.array([s])
producer.send('kafkatest', x.tobytes())
#producer.send('kafkatest', key=b'message-two', value=b'This is Kafka-Python')
producer.close()
