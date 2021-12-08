question_list = open("QuestionMap.txt", "r")
lst = []
for question in question_list:
    question = question[0:question.find(":")]
    lst.append(question)

print(lst)