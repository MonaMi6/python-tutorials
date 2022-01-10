#!/usr/bin/env python3

from lib import km_to_miles

def main():
    print ('введите значение в километрах')
    km = input()
    km = int(km)
    miles = km_to_miles(km)

    message = str(km) + " километров равно " + str(miles) + " миль"
    print(message) 

    print (f"{km} километров равно {miles} миль")

main()

