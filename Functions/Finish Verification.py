'''Implementing a Function that will verify if the user filled the continue question with our options.
This function will be used once in my program.'''
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
# Commands below were used to test my function.
answer = finish_verification(options=['Yes', 'yes', 'No', 'no'])
print(answer)