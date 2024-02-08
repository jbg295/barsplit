def BarSplit():
    closerHours = float(input("Enter closer's hours: "))
    otherHours = float(input("Enter other's hours: "))
    money = float(input("Enter tips in dollars: "))
    totalHours = closerHours + otherHours
    dollarsPerHour = money / totalHours
    closerMoney = dollarsPerHour * closerHours
    otherMoney = dollarsPerHour * otherHours
    print("Total Hours: $", totalHours)
    print("Dollars Per Hour: $", dollarsPerHour)
    print("Closer: $", closerMoney)
    print("Other: $", otherMoney)




BarSplit()
    
