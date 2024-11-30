# Function:     This program determines if a date entered by the user is valid.  
# Input:        Interactive
# Output:       Valid date is printed or user is alerted that an invalid date was entered.

validDate = True
MIN_YEAR = 0
MIN_MONTH = 1
MAX_MONTH = 12
MIN_DAY = 1

def is_leap_year(year):
    """Checks if a year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_max_days(month, year):
    """Returns the maximum number of days in a month for a given year."""
    if month == 2: 
        if is_leap_year(year):
            return 29
        else:
            return 28
    elif month in [1, 3, 5, 7, 8, 10, 12]: 
        return 31
    else:
        return 30

# Get User Input
month = int(input("Enter a month: "))
day = int(input("Enter a day: "))
year = int(input("Enter a year: "))

# Check to be sure date is valid

if year <= MIN_YEAR:  # Invalid year
    validDate = False
elif month < MIN_MONTH or month > MAX_MONTH:  # Invalid month
    validDate = False
else:
    max_days = get_max_days(month, year)
    if day < MIN_DAY or day > max_days:  # Invalid day
        validDate = False
    else:
        validDate = True

        
# Test to see if date is valid and output date and whether it is valid or not

# endOfJob()
if validDate == True:
    # Output statement
    print(f"{month}/{day}/{year} is a valid date.")
else:
    # Output statement
    print(f"{month}/{day}/{year} is an invalid date.")
