'''Implementing a Function that will verify if the user made a number input.
This function will be used twice in my program.'''
#=============================================================================================
def number_verification(number):
    verification = False
    while verification == False:
        try:
            user_entry = float(input(f'Please fill in the {number} number of the operation: '))
            verification = True
            return float(user_entry)
        except ValueError:
            print('The input was not a number. Please try again below.')
#=============================================================================================
# Commands below were used to test my function.
number = number_verification()
print(number)