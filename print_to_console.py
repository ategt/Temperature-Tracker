from random import randint
from time import sleep
import serial
import time
import re

try:
  _serial = serial.Serial("COM4", 9600)
  comma = ",".encode()

  result = _serial.read_all()

  for _ in range(90000):
    result = _serial.readline()

    readings = result.split(comma)
    first_reading = readings[0]
    avg_reading = readings[-1]
            
    print("\r",mv_to_f(int(first_reading.decode("utf-8"))), ",", first_reading.decode("utf-8"), ",", avg_reading.decode("utf-8").strip(), " - ", randint(0, 250), " " * 25, end='')
    sleep(0.5)

finally:            
  _serial.close()  