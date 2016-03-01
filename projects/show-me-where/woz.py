from utils import geocoding

user_input = input("What do you want to do? ")
user_input = user_input.lower()

if user_input == "hello":
	user_name = input("What is your name? ")
	print("Hello", user_name)

elif user_input == "geocode":
	user_location = input("What is your location? ")
	print("Ok...geocoding:", user_location)
	result = geocoding.geocode(user_location)
	print(result)

elif user_input == "help":
	print(geocode.__name__)
	print(geocode.__doc__)

else:
	print("Sorry, I don't know how to respond to", user_input)