# task 1
"""name="Jawad Zaheer"
number=3
number1=3.5
number2=True
_name2="Farhad"
numb=12
print(name)
print(number)
print(number1)
print(number2)
print(_name2)
print(numb)
while="qwerty"
print(while)"""

#task 2
"""import keyword as abc
print(abc.kwlist)"""

#task 4
"""temp1=220
temp2=20
temp3=22
temp4=22.02
temp5=11
print("The Temperature in Islamabad today is {} degrees outside!".format(temp4))"""

#task 5

# it is a single line comment
"""" It is a multi line comment """

#task 6
"""a=b=c="apple"
print(id(a))
print(id(b))
print(id(c))"""


#task 7

"""a=12
b=11.8
c="jawad"
d=False
e=3j
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))"""

#task 8
"""num = 344

# perform multiplication if the number is an integer
if isinstance(num, int):
	print(num*2)
	print("The number is an integer")

# perform division if the number is a float
else:
	print(num/2)
	print("The number is a float")"""

#task 9
# Declare the string
"""my_string = "Python lab conduction"

# Iterate over each character in the string and print its memory address
for char in my_string:
    print(f"Character: {char}, Address: {id(char)}")"""

#task 10
# Given list
"""L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

# Applying the slicing operations
full_slice = L[:]
slice_from_5 = L[5:]
slice_up_to_5 = L[:5]
slice_up_to_last_2 = L[:-2]
slice_from_neg_7_to_neg_2 = L[-7:-2]

# Printing the results
print("Full Slice [:]               :", full_slice)
print("Slice from index 5 [5:]      :", slice_from_5)
print("Slice up to index 5 [:5]     :", slice_up_to_5)
print("Slice up to last 2 [:-2]     :", slice_up_to_last_2)
print("Slice from -7 to -2 [-7:-2]  :", slice_from_neg_7_to_neg_2)"""

# task question
# Function to perform arithmetic operations
"""def perform_arithmetic_operations(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2 if num2 != 0 else "undefined (division by zero)"

    print(f"Addition: {num1} + {num2} = {addition}")
    print(f"Subtraction: {num1} - {num2} = {subtraction}")
    print(f"Multiplication: {num1} * {num2} = {multiplication}")
    print(f"Division: {num1} / {num2} = {division}")
# Main function
def main():
    try:
        # Taking input from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Performing arithmetic operations
        perform_arithmetic_operations(num1, num2)
    except ValueError:
        print("Invalid input! Please enter numerical values.")

# Entry point of the program
if __name__ == "__main__":
    main()"""

#task question 2
"""import statistics
def interchange_first_last(lst):
    if len(lst) > 1:
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst

def sum_of_elements(lst):
    return sum(lst)

def calculate_mean(lst):
    return statistics.mean(lst)

def calculate_median(lst):
    return statistics.median(lst)

def main():
    # Sample list for demonstration
    sample_list = [10, 20, 30, 40, 50]

    # a. Interchange first and last elements in the list
    interchanged_list = interchange_first_last(sample_list.copy())
    print(f"List after interchanging first and last elements: {interchanged_list}")

    # b. Sum all elements in the list
    total_sum = sum_of_elements(sample_list)
    print(f"Sum of all elements in the list: {total_sum}")

    # c. Calculate mean and median of the list
    mean_value = calculate_mean(sample_list)
    median_value = calculate_median(sample_list)
    print(f"Mean of the list: {mean_value}")
    print(f"Median of the list: {median_value}")

if __name__ == "__main__":
    main()"""














