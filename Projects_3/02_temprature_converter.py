print("-" * 30)
print("1- Celsius to Fahrenheit")
print("2- Fahrenheit to Celsius")
print("-" * 30)

choice = input("Your choice (1/2):")

if choice == "1":
    celsius = float(input("Type your Celsius value:"))
    fahrenheit = (celsius *1.8) +32
    print(f'{celsius} C equals to {fahrenheit} F')
elif choice == "2":
    fahrenheit = float(input("Type your Fahrenheit value:"))
    celsius = (fahrenheit - 32) / 1.8
    print(f'{fahrenheit}F equals to {celsius}C')
else:
    print("Wrong answer")