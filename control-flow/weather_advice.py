weather = input("What's the weather like today? (sunny/cold/rainy): ").lower()

if weather == "sunny":
    print("Wear a t-shirt and sunglass.")

elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")

elif weather == "cold":
    print("Make sure to wear to wear a warm coat and a scarf.")

else:
    print("Sorry, I don't have recommendations for this weather.")
