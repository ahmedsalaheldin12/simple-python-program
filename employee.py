def calcAllSalaries(data):
    total_salary =0
    for key in data:
        total_salary += data[key]['salary']
    print(total_salary)


def getAge(email,data):
    for key in data:
        if data[key]['email'] == email:
            print(data[key]['age'])
        else:
            print('Email Not Found')

