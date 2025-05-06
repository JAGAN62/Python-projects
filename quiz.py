import random





questions={'what is the extension to save python file ?':'.py',
           'what data type is true and false ?':'boolean',
           'what data type uses this "()" to store data ?':'tuple',
           'what keyword is used to create a class ?':'class',
           'what is the value of this expression "10 //3" ?':'3',
           'which year python got invented ?':'1991',
           'how to read input from the user ?':'input',
           'list data type in python is mutable or immutable ?':'mutable',
           'is python case sensitive or not "yes or no" ?':'yes',
           'what is the solution for this expression "4+3%5" ?':'7',
           'which character is used to single line comment ?':'#',
           }


def quiz_game():
    questions_list=list(questions.keys())
    no_of_question=5
    score=0
    selected_questions=random.sample(questions_list,no_of_question)
    

    for index,ques in enumerate(selected_questions):
        print(f'{index + 1}.{ques}')
        user_answer=input('Your Answer:').lower().strip()
        if (questions[ques] == user_answer.lower()):
            print(f'correct!')
            score+=1
        else:
            print(f'your answer is incorrect! correct Answer is:{questions[ques]}')
        print()
    print(f'your final score is {score}/{no_of_question}')


    
    

quiz_game()

