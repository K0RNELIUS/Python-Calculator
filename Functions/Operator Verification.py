'''Implementing a Function that will verify if the user filled in one of the operator options.
This function will be used once in my program.'''
#=============================================================================================
def operator_verification(operators):
    verification = False
    while verification == False:
        user_entry = input('Please insert the operator you would like to use: ')
        if user_entry in operators:
            verification = True
            return user_entry
        else:
            print('The input was not one of the operators, please try (+|-|*|/).')
#=============================================================================================
# Commands below were used to test my function.
operator = operator_verification(operators=['+', '-', '*', '/'])
print(operator)