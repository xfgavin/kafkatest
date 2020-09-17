#!/usr/bin/env python3
from kafka import KafkaConsumer
consumer = KafkaConsumer('kafkatest')
for message in consumer:
    print (message)
