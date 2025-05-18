import json

def reading_questions():
    with open('objective_questions.json', 'r') as file:
        data = json.load(file)
        return data

def start_examination():
    print("Starting the examination process...")

    data = reading_questions()
    print("Examination process started.")
 
    marks = 0
    total_marks = len(data['questions'])
    questions = data['questions']
    for qi, question in  enumerate(questions):

        # printing the question
        print('({}/{}) {}'.format(qi + 1, total_marks, question['question']))

        # printing the options
        for oi, option in enumerate(question['options']):
            print('\t ({}) {}'.format(oi + 1, option))
        
        # taking input from the user
        answer = int(input("Enter your answer: ")) - 1

        # checking if the answer is correct
        if answer == question['correct']:
            marks += 1
            print("Correct!")
        else:
            print("Incorrect. The correct answer is:", question['options'][question['correct']])

    print("Examination completed!!!!.")
    
    # evaluating the marks
    print("Your marks: ", marks, "/", total_marks)
    percentage = (marks / total_marks) * 100
    if percentage >= 40:
        print('passed with :', percentage)
    else:
        print('failed with :', percentage)
    

start_examination()