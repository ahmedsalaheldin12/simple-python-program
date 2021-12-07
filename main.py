import csv

import admin
import employee
from admin import *
from employee import *
def main():
    data = {}
    emails = []
    with open('data.csv', 'r') as file:
        reader = csv.DictReader(file)
        counter = 1
        for row in reader:
            data[counter] = row
            counter +=1
    while True:
        print('Welcome, Press 1 to Login or anything else to exit')
        x = (input())
        if x == '1':
            username = input('Enter Your Email: ')
            passwd = input('Enter Your Password: ')
            # validate username and password
            for key in data:
                if data[key]['email'] == username and data[key]['password'] == passwd:
                    print(f"Hello {data[key]['name']} {data[key]['management_type']}")
                    while True:
                        if data[key]['management_type'] == 'admin':
                            print("1-Add Employee or Admin\n2-Remove Employee\n3-Modify data\n4-Exit")
                            choice = int(input('Enter your choice: '))
                            if choice == 1:
                                admin.addEmployee('data.csv',data)
                            if choice == 2:
                                emailll = input('Enter Email: ')
                                admin.removeEmployee(emailll, data, 'data.csv')
                            if choice == 3:
                                emaillll = input('ENter email: ')
                                admin.modifyEmployee(emaillll,data,'data.csv')
                            if choice == 4:
                                break
                        elif data[key]['management_type'] == 'employee':
                            print("1-Calculate Salary \n2-Calculate all salaries\n3-Get age\n4-Exit")
                            e_choice = int(input('Enter your choice: '))
                            if e_choice == 1:
                                print(data[key]['salary'])
                            if e_choice == 2:
                                employee.calcAllSalaries(data)
                            if e_choice == 3:
                                emaill = input('Please Enter EMail: ')
                                employee.getAge(emaill,data)
                            if e_choice == 4:
                                break

        else:
            print('Goodbye sir')
            break


main()