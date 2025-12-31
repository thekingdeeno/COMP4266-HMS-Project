# Imports
import json
from Admin import Admin
from Doctor import Doctor
from Patient import Patient
from Database import Database

def main():
    """
    the main function to be ran when the program runs
    """
    database = Database()

    # Initialising the actors
    admin_data = database.initialiseData('admin')
    admin = Admin(admin_data['username'], admin_data['password'], admin_data['postcode']) # username is 'admin', password is '123'
    doctors = []
    patients = []
    discharged_patients = []

    for doc in database.initialiseData('doctors'):
        doctors.append(Doctor(doc[0], doc[1], doc[2]))

    for p in database.initialiseData('patients'):
        patients.append(Patient(p[0], p[1], p[2], p[3], p[4]))
    
    for dis in database.initialiseData('discharged'):
        discharged_patients.append(Patient(dis[0], dis[1], dis[2], dis[3], dis[4]))

    # keep trying to login tell the login details are correct
    while True:
        if admin.login():
            running = True # allow the program to run
            break
        else:
            print('Incorrect username or password.')

    while running:
        # print the menu
        print('Choose the operation:')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- Discharge patients')
        print(' 3- View discharged patient')
        print(' 4- Assign doctor to a patient')
        print(' 5- Update admin detais')
        print(' 6- Quit')

        # get the option
        op = input('Option: ')

        if op == '1':
            # 1- Register/view/update/delete doctor
         #ToDo1
          pass
          Admin.doctor_management(Admin, doctors)

        elif op == '2':
            while True:
                op = input('Do you want to discharge a patient(Y/N):').lower()

                if op == 'yes' or op == 'y':
                    Admin.discharge(Admin, patients, discharged_patients)

                elif op == 'no' or op == 'n':
                    break

                # unexpected entry
                else:
                    print('Please answer by yes or no.')
        
        elif op == '3':
            Admin.view_discharge(Admin, discharged_patients)

        elif op == '4':
            # 4- Assign doctor to a patient
            admin.assign_doctor_to_patient(patients, doctors)

        elif op == '5':
            # 5- Update admin detais
            admin.update_details()

        elif op == '6':
            running = False

        else:
            # the user did not enter an option that exists in the menu
            print('Invalid option. Try again')

if __name__ == '__main__':
    main()
