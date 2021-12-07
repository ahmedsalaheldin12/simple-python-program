import csv


def addEmployee(file,data):
    emp_id = input('Enter your Id: ')
    name = input('Enter your Name: ')
    salary = input('Enter your Salary: ')
    age = input('Enter your Age: ')
    position = input('Enter your Position: ')
    technology = input('Enter your Technology: ')
    email = input('Enter your EMail: ')
    for key in data:
        if data[key]['email'] == email:
            print('This email is exist, enter a unique email')
            email = input('Enter your EMail: ')
    passwdd = input('Enter your Password: ')
    if len(passwdd) < 6:
        passwdd = input('Your password must be more than 6 digits: ')
    mang_type = input('Enter your Management type: ')
    data[str(len(data.keys()) + 1)] = {'id':emp_id,'name':name,
                                'salary':salary,
                                'age':age,
                                'position':position,
                                'technology':technology
                                ,'email':email,
                                'password':passwdd,
                                'management_type':mang_type}
    with open(file, 'a') as f:
        csv_app = csv.writer(f)
        csv_app.writerow([emp_id,name,salary,age,position,technology,email,passwdd,mang_type])


def removeEmployee(email,data,file):
    x = 0
    for key in data:
        if data[key]['email'] == email:
            x = key
            break

    print('not found')

    del data[x]
    headers = ['id','name','salary','age','position','technology','email','password','management_type']
    with open(file, 'w', newline="") as f:
         csv_app = csv.DictWriter(f,fieldnames=headers)
         csv_app.writeheader()
         for l in data:
             csv_app.writerow(data[l])

def modifyEmployee(email,data,file):
    removeEmployee(email,data,file)
    addEmployee(file,data)
