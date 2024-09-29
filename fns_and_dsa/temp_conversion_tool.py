#This script will define functions to convert temperatures between Celsius and Fahrenheit
#The script will ask the user to input the temperature in Celsius or Fahrenheit

CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELCIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR 
    return celsius

temperature = int(input("Enter the temperature to convert: "))
celcius_or_fahrenheit = input("Is the temperature in Celsius or Fahrenheit? C/F: ")

if celcius_or_fahrenheit == "C":
    result =(celsius_to_fahrenheit(temperature))  
    print(f"{temperature}°C is {result}°F")

    
elif celcius_or_fahrenheit == "F":
    result =(fahrenheit_to_celsius(temperature))
    print(f"{temperature}°F is {result}°C")

else:
    print("Invalid input")
