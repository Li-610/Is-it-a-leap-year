def is_leap_year(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

def main():
    # Prompt the user to input a year
    year_input = input("Enter a year: ")

    try:
        year = int(year_input)
        if is_leap_year(year):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    except ValueError:
        print("Invalid input. Please enter a valid numeric year.")

if __name__ == "__main__":
    main()
