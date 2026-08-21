import pynmea2

t_data = ["$GNRMC,045255.000,V,,,,,,,,,,N*50","$GNRMC,045343.000,V,,,,,,,120826,,,N*59","$GNRMC,224706.000,A,3519.60234,S,14903.48138,E,0.00,0.00,130826,,,A*62"]

for i in t_data:
    raw_data = i
    data = pynmea2.parse(raw_data)

    print(i)
    print(data.latitude)
    print(data.longitude)
    print(data.spd_over_grnd)
