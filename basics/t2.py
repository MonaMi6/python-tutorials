#!/usr/bin/env python3

from lib import km_to_miles, miles_to_km

def main():
    print('введите значение в милях (10miles) или километрах (10km)')
    value = input()
    if value.find("km") != -1:
        pos = value.find("km")
        km = value[:pos] 
        km = int(km)
        miles = km_to_miles(km)
        print("значение в километрах",km,"равно", miles,"миль")

    if value.find("miles") != -1:
        pos = value.find("miles")
        miles = value[:pos]
        miles = int(miles)
        km = miles_to_km(miles)
        print("значение в милях", miles,"равно",km,"километров")
    

main()

