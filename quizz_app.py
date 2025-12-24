#quizz application
def calculate_score(answers,correct_answers):
    score=0
    for i in range(len(answers)):
     if answers[i].lower()==correct_answers[i].lower():
         score +=1
    return score
    
questions=['1:what is the national bird of india',
               '2:who is most followed indian cricketer of india',
               '3:what is the full form of opt']
correct_answers=['peacock','virat kohli','one time password']
users_answer=[]
    
for question in questions:
    answer=input(question)
    users_answer.append(answer)
score=calculate_score(users_answer,correct_answers)
print(f'your score is {score} out of{len(questions)}')