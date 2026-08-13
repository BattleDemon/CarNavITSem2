import pynmea2

t_data = "$GNRMC,045255.000,V,,,,,,,,,,N*50"
t_data = "$GNRMC,045343.000,V,,,,,,,120826,,,N*59"

t_data = "$GNRMC,224706.000,A,3519.60234,S,14903.48138,E,0.00,0.00,130826,,,A*62"

data = pynmea2.parse(t_data)

print(data)
print(data.latitude)
print(data.longitude)
