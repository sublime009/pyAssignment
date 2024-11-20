greet = 'Welcome to Learnfactory!'
student_name = input('Enter your name:')
print(f'{student_name}! {greet}')
exam_score = float(input('Enter your exam score: '))

if exam_score < 0 or exam_score > 100:
    print(f'{student_name} {exam_score} is an invalid score')
else:
    if exam_score  >= 90 or exam_score == 100:
        print(f'{student_name} your score is {exam_score} \nYou got an A!')

    elif exam_score >= 80 or exam_score == 89:
        print(f'{student_name} your score is {exam_score} . \nYou got an B!')

    elif exam_score >= 70 or exam_score == 79:
        print(f'{student_name} your score is {exam_score}. \nYou got an C!')

    elif exam_score >= 60 or exam_score == 69:
        print(f'{student_name} your score is {exam_score}. \nYou got a D!')

    else:
        print(f'{student_name} your score is{exam_score}.\nYou got an F!')
