tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей', 
    'Дмитрий', 'Борис', 'Елена', 'Александр', 'Мария'
]

klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

def gen_tuple(list_1, list_2):
    if len(list_1) > len(list_2):
        dif = len(list_1) - len(list_2)
        for i in range(dif):
            list_2.append(None)
            
    for i in range(len(list_1)):

        ready = (list_1[i], list_2[i])
        yield ready

print(*gen_tuple(tutors, klasses))