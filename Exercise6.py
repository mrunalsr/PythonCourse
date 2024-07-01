#find no of days in month if we enter Jan =31 FEb = 28 etc and if it is a leap year then Feb return 29 days
def Year_month(year,month):
    if year%4 == 0:
        print("It is a leap year")
        if month == 'Jan' or month == 'March' or month == 'May' or month == 'July' or month == 'August' or month == 'Oct' or month == 'Dec':
            return "31 Days"
        if month == 'Feb':
            return "29 Days"
        if month == 'April' or month == 'June' or month == 'September' or month == 'November':
            return "30 Days"

    else:
        print("It is not a leap year")
        if month == 'Jan' or month == 'March' or month == 'May' or month == 'July' or month == 'August' or month == 'Oct' or month == 'Dec':
            return "31 Days"
        if month == 'Feb':
            return "28 Days"
        if month == 'April' or month == 'June' or month == 'September' or month == 'November':
            return "30 Days"

Yr = int(input("Enter the year  here : "))
mth = str(input("Enter the name of month here : "))
result = Year_month(Yr,mth)
print(f"The year entered by you is {Yr} and it contain {result}")