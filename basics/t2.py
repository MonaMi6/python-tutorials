#!/usr/bin/env python3

from lib import miles_to_km

def main():
    print ('введите значение в милях')
    miles = input()
    miles = int(miles)
    km = miles_to_km(miles)

    message = str(miles) + " миль равно " + str(km) + " километров "
    print(message) 

    print (f"{miles} миль равно {km} километров")

main()

