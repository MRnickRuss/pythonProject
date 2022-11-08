from math import pi


def deg_to_gms(deg):
    degrees = int(deg)
    minutes = int((deg - degrees) * 60)
    seconds = round(((deg - degrees) * 60 - minutes) * 60)
    return f"{degrees}° {minutes}' {seconds}''"

def gms_to_deg(degrees, minutes, seconds):
    deg = degrees + minutes / 60 + seconds / 3600
    return deg


def deg_to_rad(deg):
    rad = deg * pi / 180
    return rad


def rad_to_deg(rad):
    deg = rad * 180 / pi
    return deg


    print(deg_to_gms(36.97))
    print(gms_to_deg(36, 58, 12))
    print(deg_to_rad(36.97))
    print(rad_to_deg(deg_to_rad(36.97)))
