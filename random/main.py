def main():
    birthdate = input("Enter your birthdate in ddmmyyyy format: ")
    
    if len(birthdate) != 8 or not birthdate.isdigit():
        print("Invalid format. Please enter the date in ddmmyyyy format.")
        return
    
    day = birthdate[:2]
    month = birthdate[2:4]
    year = birthdate[4:]
    
    print("Day:", day)
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    
    month_index = int(month) - 1
    if 0 <= month_index < 12:
        month_name = months[month_index]
        print("Month:", month_name)
    else:
        print("Invalid month.")
    
    print("Year:", year)

if __name__ == "__main__":
    main()
    main()
