# input statements (hardcoded values)
salary = 60000.0
numDependents = 3

# calculate taxes here
stateTax = 0.065 * salary
federalTax = 0.28 * salary
dependentDeduction = 0.025 * salary * numDependents
totalWithholding = stateTax + federalTax + dependentDeduction
takeHomePay = salary - totalWithholding

# output statements
print(f"Salary: ${salary:.2f}")
print(f"State Tax (6.5%): ${stateTax:.2f}")
print(f"Federal Tax (28%): ${federalTax:.2f}")
print(f"Dependent Deduction (2.5% x {int(numDependents)}): ${dependentDeduction:.2f}")
print(f"Total Withholding: ${totalWithholding:.2f}")
print(f"Take Home Pay: ${takeHomePay:.2f}")

