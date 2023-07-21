def getEmployeeName():
    employeeName = input("Enter Employee Name: ")
    return employeeName

def getHoursWorked():
    hours = float(input("Enter Hours: "))
    return hours

def getHourlyRate():
    hourlyRate = float(input("Enter Hourly Rate: "))
    return hourlyRate

def getTaxRate():
    taxRate = float(input("Enter Tax Rate: "))
    taxRate = taxRate / 100
    return taxRate

def calcTaxAndNetPay(hours, hourlyRate, taxRate):
    grossPay = hours * hourlyRate
    incomeTax = grossPay * taxRate
    netPay = grossPay - incomeTax
    return grossPay, incomeTax, netPay

def printInfo(employeeName, hours, hourlyRate, grossPay, taxRate, incomeTax, netPay):
    print(employeeName, f"{hours:,.2f}", f"{hourlyRate:,.2f}", f"{grossPay:,.2f}", f"{taxRate:,.1%}", f"{incomeTax:,.2f}", f"{netPay:,.2f}")

def printTotals(totalEmployees, totalHours, totalGrossPay, totalTax, totalNetPay):
    print(f"\nTotal Number of Employees: {totalEmployees}")
    print(f"Total Hours: {totalHours:,.2f}")
    print(f"Total Gross Pay: {totalGrossPay:,.2f}")
    print(f"Total Tax: {totalTax:,.2f}")
    print(f"Total Net Pay: {totalNetPay:,.2f}")

if __name__ == "__main__":
    totalEmployees = 0
    totalHours = 0.00
    totalGrossPay = 0.00
    totalTax = 0.00
    totalNetPay = 0.00

    while True:
        employeeName = getEmployeeName()
        if (employeeName.upper() == "END"):
            break
        hours = getHoursWorked()
        hourlyRate = getHourlyRate()
        taxRate = getTaxRate()
        grossPay, incomeTax, netPay = calcTaxAndNetPay(hours, hourlyRate, taxRate)

        printInfo(employeeName, hours, hourlyRate, grossPay, taxRate, incomeTax, netPay)

        totalEmployees += 1
        totalHours += hours
        totalGrossPay += grossPay
        totalTax += incomeTax
        totalNetPay += netPay

print("\n--------------------------------------------------")
printTotals(totalEmployees, totalHours, totalGrossPay, totalTax, totalNetPay)
print("\n--------------------------------------------------")











