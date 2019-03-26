import json

#Class Constructor

class Monitoring:
    def __init__(self, temperature, humidity):
        self.temperature = temperature
        self.humidity = humidity
r1 = Monitoring(20, 30)

print(r1.temperature)        
print(r1.humidity)
