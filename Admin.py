from Doctor import Doctor
from Patient import Patient
from Database import Database

class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address = ''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """

        self.__username = username
        self.__password = password
        self.__address =  address

    def get_admin_data(self):
        return {
            "username": self.__username,
            "password": self.__password,
            "address": self.__address
        }
    def updateAdminFromGui(self, username, address, password):
        self.__username = username
        self.__address = address
        self.__password = password


    def view(self,a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')

    def login(self) :
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """
    
        print("-----Login-----")
        #Get the details of the admin

        username = input('Enter the username: ')
        password = input('Enter the password: ')

        # check if the username and password match the registered ones
        #ToDo1

        if self.__password == password and self.__username == username:
            return True
        pass

    def find_index(self,index,doctors):
        
            # check that the doctor id exists          
        if index in range(0,len(doctors)):
            
            return True

        # if the id is not in the list of doctors
        else:
            return False
            
    def get_doctor_details(self, doctors) :
        doc = int(input('Select Doctor ID: '))-1

        print(f'Name: {doctors[doc].full_name()}')
        print(f'Speciality: {doctors[doc].get_speciality()}')

        print("\n === Patients === ")
        for patient in doctors[doc].get_patients():
            print(f'{patient}')

        print('\n=== Appointments ===')
        for app in doctors[doc].get_appointments():
            print(f'{app}')

    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """

        print("-----Doctor Management-----")

        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')
        print(' 5 - Add Appointment Date')

        #ToDo3
        pass

        op = input('Option: ')


        # register
        if op == '1':
            print("-----Register-----")

            # get the doctor details
            print('Enter the doctor\'s details:')
            #ToDo4
            pass

            # check if the name is already registered

            first_name = input('Enter firstname: ')
            surname = input('Enter surname: ')
            speciality = input('Enter specialty: ')
            name_exists = False
            for doctor in doctors:
                if first_name == doctor.get_first_name() and surname == doctor.get_surname():
                    name_exists = True
                    print('Name already exists. \n')
                    #ToDo5
                    break
                    pass # save time and end the loop

            #ToDo6
            pass# add the doctor ...
            if name_exists == False:
                doctors.append(Doctor(first_name, surname, speciality))
                Database().createDoctor(first_name, surname, speciality)
                                                         # ... to the list of doctors
                print('Doctor registered.')

        # View
        elif op == '2':
            print("-----List of Doctors-----")
            #ToDo7
            pass
            sn = 1
            for doctor in doctors:
                print("{0})".format(sn), doctor.get_first_name(), doctor.get_surname())
                sn += 1

            doc = int(input('Select Doctor ID: '))-1

            print(f'Name: {doctors[doc].full_name()}')
            print(f'Speciality: {doctors[doc].get_speciality()}')

            print("\n === Patients === ")
            for patient in doctors[doc].get_patients():
                print(f'{patient}')

            print('\n=== Appointments ===')
            for app in doctors[doc].get_appointments():
                print(f'{app}')



        # Update
        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(self,doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    doctor_index=self.find_index(self,index,doctors)

                    if doctor_index!=False:

                        print('Choose the field to be updated:')
                        print(' 1 First name')
                        print(' 2 Surname')
                        print(' 3 Speciality')
                        op = int(input('Input: ')) # make the user input lowercase
                        newInput = input('Enter update: ').lower()
                        doc = doctors[index]
                        if op == 1:
                            doc.set_first_name(newInput)
                            field = 'first_name'
                        elif op == 2: 
                            doc.set_surname(newInput)
                            field = 'surname'
                        elif op == 3:
                            doc.set_speciality(newInput)
                            field = 'speciality'

                        Database().updateDoctor(index, field, newInput)
                        print('Doctor Updated Successfylly \n',doctors[index])
                        break
                        
                    else:
                        print("Doctor not found")

                except ValueError:
                    print('The ID entered is incorrect')

        # Delete
        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(self, doctors)

            index = int(input('Enter the ID of the doctor to be deleted: ')) -1
            doctor_index=self.find_index(self,index, doctors)
            if doctor_index:
                doctors.pop(index)
                Database().deleteDoctor(index)
                self.view(self, doctors)
            else:
                print('The id entered is incorrect')

        elif op == '5':

            try:
                sn = 1
                for doctor in doctors:
                    print("{0})".format(sn), doctor.get_first_name(), doctor.get_surname())
                    sn += 1
                index = int(input('Enter the ID of the doctor: ')) -1
                doctor_index=self.find_index(self,index,doctors)
                doctor = doctors[doctor_index]
                print('----- Appointment Date Selection -----')
                day = int(input('Enter Day'))

                month = int(input('Enter Month'))

                year = int(input('Enter Year'))

                date = f'{day}/{month}/{year}'
                doctor.add_appointment(date)
                Database().updateDoctor(index, 'appointments', date)
            except ValueError:
                print('Invalid Value')

        else:
            print('Invalid operation choosen. Check your spelling!')


    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        #ToDo10
        number = 1
        for patient in patients:
            print(f'{number}) {patient.__str__()}')
            number += 1

    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return # stop the procedures

        except ValueError: # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return # stop the procedures

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        patients[patient_index].print_symptoms() # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) -1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors)!=False:
                    
                doctor = doctors[doctor_index]
                if patients[patient_index].get_doctor() != "None":
                    searchIndex = 0
                    for doc in doctors:
                        if doc.full_name() == patients[patient_index].get_doctor():
                            doc.del_patient(patients[patient_index].full_name())
                            Database().updateDoctor(searchIndex, 'patients-rm', patients[patient_index].full_name())
                        searchIndex += 1
                patients[patient_index].link(doctor.full_name())
                doctor.add_patient(patients[patient_index].full_name())
                Database().updateDoctor(doctor_index, 'patients', patients[patient_index].full_name())
                Database().updatePatient(patient_index, 'doctor', doctor.full_name())
                self.view(patients)
                
                print('The patient is now assign to the doctor.')

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect')

    def scheduleDoctorAppointment(self, doctors):
        try:
            sn = 1
            for doctor in doctors:
                print("{0})".format(sn), doctor.get_first_name(), doctor.get_surname())
                sn += 1
            index = int(input('Enter the ID of the doctor: ')) -1
            doctor_index=self.find_index(index,doctors)
            doctor = doctors[doctor_index]
            print('----- Appointment Date Selection -----')
            day = int(input('Enter Day: '))

            month = int(input('Enter Month: '))

            year = int(input('Enter Year: '))


            date = f'{day}/{month}/{year}'
            doctor.add_appointment(date)
            Database().updateDoctor(index, 'appointments', date)
        except ValueError:
            print('Invalid value')


    def discharge(self, patients, discharge_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        print("-----Discharge Patient-----")
        try:
            self.view(self, patients)
            patient_index = int(input('Please enter the patient ID: ')) - 1
            patient = patients[patient_index]
            discharge_patients.append(patient)
            p_data = patient.get_data()
            Database().addPatient('discharged', p_data[0], p_data[1], p_data[2], p_data[3], p_data[4])
            patients.pop(patient_index)
            Database().removePatient('active', patient_index)
        except IndexError:
            print('Invalid selection')

        print('Patient Discharged Successfuly')

    def view_discharge(self, discharged_patients):
        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(self, discharged_patients)

    def update_details(self):
        """
        Allows the user to update and change username, password and address
        """

        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        op = int(input('Input: '))

        if op == 1:
            newUsername = input('Enter new username: ').lower()
            self.__username = newUsername
        elif op == 2:
            password = input('Enter the new password: ')
            # validate the password
            if password == input('Enter the new password again: '):
                self.__password = password

        elif op == 3:
            newAddress = input('Enter new Address: ')
            self.__address = newAddress

        else:
            print('Invalid option selected')
        Database().updateAdmin(self.__username, self.__password, self.__address)

        print(f'{self.__username} {self.__address}')

    def fetch_patient_symptoms(self, patients):
        patient_index = int(input('Please enter the patient ID: ')) - 1
        patient = patients[patient_index]
        patient.print_symptoms()


    def fetchReport(self, patients, doctors):
        doctors_count = len(doctors)
        patients_count = len(patients)

        unFilteredList = []
        for patient in patients:
            for symptom in patient.get_symptoms():
                unFilteredList.append(symptom.lower())
            
        filteredList = list(dict.fromkeys(unFilteredList))

        symptomsObj = {}

        for item in filteredList:
            symptomsObj[item] = unFilteredList.count(item)

        patientsPerDoc = {}
        appointmentStats = []
        for doctor in doctors:
            #get no of pat per doc
            patientsPerDoc[doctor.full_name()] = len(doctor.get_patients())
            #get no of app per doc per month
            doc = []
            doc.append(doctor.full_name())
            month = 1
            count = 0
            while month < 13:
                for app in doctor.get_appointments():
                    if app.split('/')[1] == str(month):
                        count +=1
                doc.append(count)
                month += 1
                count = 0
            appointmentStats.append(doc)


        report = {}

        report['doctors_count'] = doctors_count
        report['patients_count'] = patients_count
        report['patient_symptoms_data'] = symptomsObj
        report['patients_per_doc'] = patientsPerDoc
        report['appointments_per_month'] = appointmentStats

        return report
    
    def printReport(self, report):
        print("\n=========== HOSPITAL MANAGEMENT SYSTEM REPORT ===========\n")

        print("===== PERSONEL METRICS ====")
        print(f"Total Number Of Doctors: {report['doctors_count']}")
        print(f"Total Number Of Patients: {report['patients_count']}")

        print("\n\n===== ILLNESS METRICS =====")
        for attr, value in report['patient_symptoms_data'].items():
            print(f'{attr}: {value} patient(s)')
        
        print("\n\n===== NUMBER OF PATIENTS PER DOCTOR =====")
        for attr, value in report['patients_per_doc'].items():
            print(f'{attr}: {value} patient(s)')

        print("\n\n========== NUMBER OF PATIENT APPOINTMENT PER MONTH PER DOCTOR ==========\n")
        tableHead = '{:^12}'.format('Doctor') + '{:^12}'.format('Jan') + '{:^12}'.format('Feb') + '{:^12}'.format('Mar') + '{:^12}'.format('Apr') + '{:^12}'.format('May') + '{:^12}'.format('Jun') + '{:^12}'.format('Jul') + '{:^12}'.format('Aug') + '{:^12}'.format('Sep') + '{:^12}'.format('Oct') + '{:^12}'.format('Nov') + '{:^12}'.format('Dec')

        print(tableHead)
        for docStat in report['appointments_per_month']:
            docStatString = '' 
            for item in docStat:
                docStatString = docStatString + '{:^12}'.format(item)
            
            print(docStatString)
        print("\n\n")
    
    def patient_management(self, patients):
        print("-----Patient Management-----")

        # menu
        print('Choose the operation:')
        print(' 1 - Register Patient')
        print(' 2 - View All Patients')
        print(' 3 - View Symptoms')
        print(' 4 - Add Symptoms')
        # print(' 5 - Delete')


        op = input('Option: ')

        if op == '1':
            try:
                print('-----Register Patient-----\n')
                fname = input('Enter First Name: ')
                lname = input('Enter Surname: ')
                age = int(input('Enter Age: '))
                mobile = int(input('Enter Mobile: '))
                postcode = input('Enter Postcode: ')

                new_patient = Patient(fname, lname, age, mobile, postcode)
                patients.append(new_patient)
                Database().addPatient('active', fname, lname, age, mobile, postcode)

                print('Patient Registered Successfully')    
            except ValueError:
                print('Bad input')        
        elif op == '2':
            self.view_patient(patients)
        elif op == '3':
            self.view_patient(patients)
            self.fetch_patient_symptoms(patients)
        elif op == '4':
            self.view_patient(patients)
            patient_index = int(input('Please enter the patient ID: ')) - 1
            patient = patients[patient_index]
            symptom = input('Enter the patients symptoms: ')
            patient.add_symptoms(symptom)
        else:
            print('Invalid operation choosen. Check your spelling!')