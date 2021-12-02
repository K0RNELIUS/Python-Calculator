'''Small calculator with the purpose of reviewing some of the concepts taugh in my algotithms class.'''
#=============================================================================================
# Functions:
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
def finish_verification(options):
    verification = False
    while verification == False:
        user_entry = input('Would you like to continue using the calculator? ')
        if user_entry in options:
            verification = True
            return user_entry
        else:
            print('Please answer the question with yes or no.')
#=============================================================================================
# Local where the funcitions will be called and the rest of the program:
prompt = '{0} {1} {2} = {3}' # Model in which the result will be displayed.
keep_using_the_calculator = True
while keep_using_the_calculator:
    # Verifications:
    operator = operator_verification(operators=['+', '-', '*', '/'])
    first_number = number_verification('first')
    second_number = number_verification('second')
    # Calculation of the results:
    if operator == '+':
        result = first_number + second_number
    elif operator == '-':
        result = first_number - second_number
    elif operator == '*':
        result = first_number * second_number
    elif operator == '/':
        result = first_number / second_number
    # Display of the result:
    print(prompt.format(first_number, operator, second_number, result))
    # Checking if the use would like to continue:
    answer = finish_verification(options=['Yes', 'yes', 'No', 'no'])
    if answer == 'No' or answer == 'no':
        keep_using_the_calculator = False