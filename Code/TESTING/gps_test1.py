import pynmea2

t_data = "$GNRMC,045255.000,V,,,,,,,,,,N*50"
t_data = "$GNRMC,045343.000,V,,,,,,,120826,,,N*59"

data = pynmea2.parse(t_data)

print(data)
print(data.latitude)
print(data.longitude)
