#arithmetic calculatar
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

        userOperation = input("Please select operation:\n 1 Add \n 2 Subtract \n 3 Multiply \n 4 Divide \n 5 Exit \n : ")
        option =int(userOperation)
        if option in [1,2,3,4]:
           numbers = [float(num) for num in input("enter space separated numbers ").split()]

           if option == 1:
              print("sum the number is:", add(numbers))

           elif option == 2:
              print("the difference of the number is:", subtract(numbers))
           elif option == 3:
             print("the product of the numbers is :", multiply(numbers))
           elif option == 4:
             print("the division of the number is :", division(numbers)) 
        elif option == 5:
             print("exit successfuly")
             break          
        else:
             print("invalid input")
             break
calculator()    
