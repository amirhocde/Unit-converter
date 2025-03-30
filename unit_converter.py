def display_menu():
    print("Unit Converter")
    print("1. Convert length")
    print("2. Convert weight")
    print("3. Convert temperature")
    print("4. Exit")

def convert_length():
    print("Length Conversion")
    print("1. Meters to Kilometers")
    print("2. Kilometers to Meters")
    print("3. Meters to Miles")
    print("4. Miles to Meters")
    choice = input("Enter your choice: ")
    value = float(input("Enter the value to convert: "))
    if choice == '1':
        result = value / 1000
        print(f"{value} meters is {result} kilometers.")
    elif choice == '2':
        result = value * 1000
        print(f"{value} kilometers is {result} meters.")
    elif choice == '3':
        result = value * 0.000621371
        print(f"{value} meters is {result} miles.")
    elif choice == '4':
        result = value / 0.000621371
        print(f"{value} miles is {result} meters.")
    else:
        print("Invalid choice.")

def convert_weight():
    print("Weight Conversion")
    print("1. Grams to Kilograms")
    print("2. Kilograms to Grams")
    print("3. Pounds to Kilograms")
    print("4. Kilograms to Pounds")
    choice = input("Enter your choice: ")
    value = float(input("Enter the value to convert: "))
    if choice == '1':
        result = value / 1000
        print(f"{value} grams is {result} kilograms.")
    elif choice == '2':
        result = value * 1000
        print(f"{value} kilograms is {result} grams.")
    elif choice == '3':
        result = value * 0.453592
        print(f"{value} pounds is {result} kilograms.")
    elif choice == '4':
        result = value / 0.453592
        print(f"{value} kilograms is {result} pounds.")
    else:
        print("Invalid choice.")

def convert_temperature():
    print("Temperature Conversion")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Enter your choice: ")
    value = float(input("Enter the value to convert: "))
    if choice == '1':
        result = (value * 9/5) + 32
        print(f"{value} degrees Celsius is {result} degrees Fahrenheit.")
    elif choice == '2':
        result = (value - 32) * 5/9
        print(f"{value} degrees Fahrenheit is {result} degrees Celsius.")
    else:
        print("Invalid choice.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            convert_length()
        elif choice == '2':
            convert_weight()
        elif choice == '3':
            convert_temperature()
        elif choice == '4':
            print("Exiting the Unit Converter.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()