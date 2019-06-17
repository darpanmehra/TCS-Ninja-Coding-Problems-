
n=input("Enter Date (dd-mm-yyyy):")
x=n.split("-")
date=int(x[0])
month=int(x[1])
year=int(x[2])

if (month<1 or month>12):
  print("invalid month")

if (month==1):
  if(date<32):
      print("January has 31 days")
  else:
      print("Invalid Date for January")
elif (month==3):
    if(date<32):
        print("March has 31 days")
    else:
        print("Invalid Date for March")
elif (month==4):
    if(date<31):
        print("April has 30 days")
    else:
        print("Invalid Date for April")
elif (month==5):
    if(date<32):
        print("May has 31 days")
    else:
        print("Invalid Date for May")
elif (month==6):
    if(date<31):
        print("June has 30 days")
    else:
        print("Invalid Date for June")
elif (month==7):
    if(date<32):
        print("July has 31 days")
    else:
        print("Invalid Date for July")
elif (month==8):
    if(date<32):
        print("August has 31 days")
    else:
        print("Invalid Date for August")
elif (month==9):
    if(date<31):
        print("September has 30 days")
    else:
        print("Invalid Date for September")
elif (month==10):
    if(date<32):
        print("October has 31 days")
    else:
        print("Invalid Date for October")
elif (month==11):
    if(date<31):
        print("November has 30 days")
    else:
        print("Invalid Date for November")
elif (month==12):
    if(date<32):
        print("December has 31 days")
    else:
        print("Invalid Date for December")
elif (month==2):
    if(year%4==0 and year%100!=0 or year%400==0):
        if(date<30):
            print("February has 29 days")
        else: print("Invalid date for February")
    else:
        if(date<29):
            print("February has 28 days")
        else:print("Invalid date for February")
