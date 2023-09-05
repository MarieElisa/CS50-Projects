list_month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def main():
    while True:
        date = input("Date: ").strip() #Input date
        if get_ISO(date): #Go to get_ISO() v
            print(get_ISO(date))
            break
        else: #If no value is returned from get_ISO(), reprompt
            pass


def get_ISO(x):
    try:
        mm, dd, yyyy = x.split("/") #Try to split with slash

        if int(mm) <= 12 and int(dd) <= 31:
            return f"{yyyy}-{int(mm):02d}-{int(dd):02d}" #Calling int() will find any other ValueError
        else:
            pass #Month and Day are invalid

    except ValueError:
        try:
            mm, dd, yyyy = x.split() #Try to split with space

            if mm in list_month: #Check if the month is in the list
                mm = list_month.index(mm) + 1

            dd = int(dd) #Check for a comma after the day's number
            pass

        except ValueError: #If comma exists or can't split with space, ValueError will be raised
            try:
                dd = dd.strip(",") #If comma exists, it will be smoothly removed
                if int(mm) <= 12 and int(dd) <= 31:
                    return f"{yyyy}-{int(mm):02d}-{int(dd):02d}" #Calling int() will find any other ValueError
            except ValueError:
                pass #Input invalid, reprompt


main()
