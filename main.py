#arithmetic calculatar
import math
def calculator():
    while True:
        
        def add(numbers):           
           return sum(numbers)
        
        def subtract(numbers):
           diff = numbers[0]
           for num in numbers[1:]:
               diff -= num
           return diff
        
        def multiply(numbers):
            product =1
            for num in numbers:
                product *= num
            return product
        
        def division(numbers):
            div = numbers[0]
            for num in numbers[1:]:
                if num == 0:
                    print("Error: Division by zero!")
                div /= num
            return div
        def power(numbers):
            base = numbers[0]
            for exponent in numbers[1:]:
                result = base ** exponent
            return result 
            
        userOperation = input("Please select operation:\n 1 Add \n 2 Subtract \n 3 Multiply \n 4 Divide \n 5 Power \n 6 Factorial \n 7 Exit \n : ")
        option =int(userOperation)
        if option in [1,2,3,4,5,6,7]:
            if option == 7:
                print("exit successfuly")
                break
            elif option == 6:
               while True: 
                def factorial(n):
                    if n == 0:
                        return 1
                    else:
                        return n * factorial(n-1)
               
    # Example usage:
                number = int(input("Enter a non-negative integer: "))
                if number < 0:
                    print("Factorial is not defined for negative numbers.")
                else:
                    print("Factorial of", number, "is", factorial(number))
                return


            def is_number(input_list):
                for item in input_list:
                    if not (isinstance(item, int) or isinstance(item, float)):
                        return False
                return True

            numbers = input("Enter numbers separated by spaces: ").split()
            try:
                numbers = [int(x) if '.' not in x else float(x) for x in numbers]
                if is_number(numbers):
                    if option == 1:
                        print("the sum of the numbers is:", add(numbers))

                    elif option == 2:
                        print("the difference of the numbers is:", subtract(numbers))
                    elif option == 3:
                        print("the product of the numbers is :", multiply(numbers))
                    elif option == 4:
                        print("the division of the numbers is :", division(numbers))
                    elif option ==5:
                        print(f"raising {numbers[0]} to the power of {numbers[1]} is :",power(numbers))              
                else:
                    print("At least one item is not a number.")
            except ValueError:
                 print("Invalid input. Please enter only numeric values.")
        else:
            print("invalid input please input 1 - 5")
calculator()    
