# Get user input for salary and number of dependents
salary = float(input("Enter the employee's salary: 1250 "))
numDependents = int(input("Enter the number of dependents: 2 "))

# Calculate state tax (6.5%)
stateTax = 0.065 * salary

# Calculate federal tax (28.0%)
federalTax = 0.28 * salary

# Calculate dependent deduction (2.5% per dependent)
dependentDeduction = 0.025 * salary * numDependents

# Calculate total withholding
totalWithholding = stateTax + federalTax + dependentDeduction

# Calculate take-home pay
takeHomePay = salary - totalWithholding

# Print the results
print(f"The listed items include state tax (${stateTax}), federal tax (${federalTax}), dependents (${dependentDeduction}), salary (${salary}), and take-home pay (${takeHomePay}).")
