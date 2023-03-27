def asker(questions):
    answers = []
    for question in questions:
        answers.append(input(question))
    return answers


def asker_dict(task_count, questions):
    dictionary = dict()
    for i in range(task_count):
        answers = asker(questions)
        dictionary[answers[0]] = answers[1]
    return  dictionary


#Задание 1
def task_1():
    answers = asker(["Введите дату: ", "Введите задачу: "])
    print("".join(map(str, answers)))


#Задание 2 & 3
def task_2_3():
    dictionary = asker_dict(3, ["Введите дату: ", "Введите задачу: "])
    for key in dictionary.keys():
        print(key + ' ' + dictionary[key])


if __name__ == '__main__':
    #task_1()
    task_2_3()
