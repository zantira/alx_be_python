current_weather = input("What's the weather like today? (sunny/cold/rainy): ").lower()

if current_weather == "sunny":
    print("Wear a t-shirt and sunglass.")

elif current_weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")

elif current_weather == "cold":
    print("Make sure to wear to wear a warm coat and a scarf.")

else:
    print("Sorry, I don't have recommendations for this weather.")
