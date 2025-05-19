#!/bin/sh

python producer/app_producer.py &
python consumer/app_consumer.py
