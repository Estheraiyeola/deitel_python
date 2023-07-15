
def questions():
    question_one = input('What is your problem? ')
    if question_one != '':
        question_two = input('Have you had this problem before? (yes or no): ')
        if question_two == "yes" or question_two == "Yes":
            print('Well you have it again')
        elif question_two == "no" or question_two == "No":
            print('Well, you have it now')
        else:
            print('Invalid input.')
    else:
        print('You have not entered anything!')
        questions()

questions()
