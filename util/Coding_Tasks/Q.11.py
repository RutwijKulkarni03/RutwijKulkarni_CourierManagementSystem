'''11. Address Formatting: Develop a function that takes an address as input (street, city, state, zip code)
and formats it correctly, including capitalizing the first letter of each word and properly formatting the
zip code.'''

# Function to format an address
def format_address(street, city, state, zip_code):
    formatted_address = f"{street.title()}, {city.title()}, {state.upper()} {zip_code}"
    return formatted_address

# Example usage:
def main():
    street = input("Enter street address: ")
    city = input("Enter city: ")
    state = input("Enter state: ")
    zip_code = input("Enter zip code: ")

    formatted_address = format_address(street, city, state, zip_code)
    print("Formatted address:", formatted_address)

if __name__ == "__main__":
    main()
