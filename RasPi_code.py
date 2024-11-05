from bluepy import btle 
import time 
import RPi.GPIO as GPIO 
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)  
 
l1=23 
l2=24 
l3=25 
l4=8 
 
 
GPIO.setup(l1, GPIO.OUT) 
GPIO.setup(l2, GPIO.OUT) 
GPIO.setup(l3, GPIO.OUT) 
GPIO.setup(l4, GPIO.OUT) 
 
GPIO.output(l1, False) 
GPIO.output(l2, False) 
GPIO.output(l3, False) 
GPIO.output(l4, False) 
 
MAC = "8C:AA:B5:8B:50:92" 
SERVICE_UUID = "4fafc201-1fb5-459e-8fcc-c5c9c331914b" 
CHARACTERISTIC_UUID = "beb5483e-36e1-4688-b7f5-ea07361b26a8" 
time.sleep(1) 
print("Connect to:" + MAC) 
dev = btle.Peripheral(MAC) 
print("\n--- dev ----------------------------") 
print(type(dev)) 
print(dev) 
 
11 
 
print("\n--- dev.services -------------------") 
for svc in dev.services: 
    print(str(svc)) 
         
print("\n------------------------------------") 
print("Get Serice By UUID: " + SERVICE_UUID) 
service_uuid = btle.UUID(SERVICE_UUID) 
service = dev.getServiceByUUID(service_uuid) 
 
while True: 
     
  
    characteristics = dev.getCharacteristics() 
 
 
    for char in characteristics: 
 
        if(char.uuid == CHARACTERISTIC_UUID ): 
 
            print(char.read()) 
            if char.read()==b'aaaa': 
                GPIO.output(l1, True) 
                GPIO.output(l2, False) 
                GPIO.output(l3, False) 
                GPIO.output(l4, True) 
                print("Forward") 
            if char.read()==b'bbbb': 
                GPIO.output(l1, False) 
                GPIO.output(l2, True) 
                GPIO.output(l3, True) 
                GPIO.output(l4, False) 
                print("Reverse") 
            if char.read()==b'cccc': 
                GPIO.output(l1, True) 
                GPIO.output(l2, False) 
                GPIO.output(l3, False) 
                GPIO.output(l4, False) 
                print("Left") 
            if char.read()==b'dddd': 
                GPIO.output(l1, False) 
                GPIO.output(l2, False) 
                GPIO.output(l3, False) 
                GPIO.output(l4, True) 
                print("Right")