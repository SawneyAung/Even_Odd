class NumberChecker:
    
    def checkOddEven(self, input):
        # Write function description
        # The purpose of this function is to check whether the number give by the user is either even or odd

        # Write code below this line
        try:
            # Check if the input is a single integer
            if isinstance(input, int):
                if input % 2 == 0:
                    return ('Even')
                else:
                    return ('Odd')
            
            # Check if the input is a list of integers
            elif isinstance(input, list):
                output = []
                for num in input:
                    if not isinstance(num, int):
                        raise ValueError("List conatins non-integers values")
                    if num % 2 == 0:
                        output.append('Even')
                    else:
                        output.append('Odd')
                return (output)

            else:
                raise ValueError('Invalid input')
            
        except ValueError:
            print('Invalid input')
        # Write code above this line 

# Instructor's test cases
# ===== ===== ===== ===== ===== 

numberChecker = NumberChecker()

print(numberChecker.checkOddEven(5))
# Expected Output: Odd
print(numberChecker.checkOddEven(10))
# Expected Output: Even
print(numberChecker.checkOddEven([3, 5, 7, 10]))
# Expected Output: ['Odd', 'Odd', 'Odd', 'Even']
print(numberChecker.checkOddEven('Hello'))
# Expected Output: Invalid input