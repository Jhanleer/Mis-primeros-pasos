"""
Unit Converter using a functional approach with menu system
"""

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5.0/9.0

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def km_to_miles(km):
    """Convert Kilometers to Miles."""
    return km * 0.621371

def miles_to_km(miles):
    """Convert Miles to Kilometers."""
    return miles / 0.621371

def kg_to_pounds(kg):
    """Convert Kilograms to Pounds."""
    return kg * 2.20462

def pounds_to_kg(pounds):
    """Convert Pounds to Kilograms."""
    return pounds / 2.20462

def meter_to_feet(meter):
    """Convert Meters to Feet."""
    return meter * 3.28084

def feet_to_meter(feet):
    """Convert Feet to Meters."""
    return feet / 3.28084

def main():
    menu_options = {
        1: ("Fahrenheit to Celsius", fahrenheit_to_celsius, "Fahrenheit"),
        2: ("Celsius to Fahrenheit", celsius_to_fahrenheit, "Celsius"),
        3: ("Kilometers to Miles", km_to_miles, "Kilometers"),
        4: ("Miles to Kilometers", miles_to_km, "Miles"),
        5: ("Kilograms to Pounds", kg_to_pounds, "Kilograms"),
        6: ("Pounds to Kilograms", pounds_to_kg, "Pounds"),
        7: ("Meters to Feet", meter_to_feet, "Meters"),
        8: ("Feet to Meters", feet_to_meter, "Feet"),
    }
    
    while True:
        print("\nUnit Converter")
        for key, (description, _, unit) in menu_options.items():
            print(f"{key}. {description}")
        print("9. Exit")

        try:
            choice = int(input("Select an option: "))
            if choice == 9:
                print("Exiting...")
                break
            elif choice in menu_options:
                description, conversion_function, input_unit = menu_options[choice]
                value = float(input(f"Enter value in {input_unit}: "))
                converted_value = conversion_function(value)
                output_unit = description.split("to")[1].strip()
                print(f"{value} {input_unit} = {converted_value:.2f} {output_unit}")
            else:
                print("Invalid option. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()