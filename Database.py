import json


class Database:

    def __init__(self):

        self.__doctors_table = 'doctors'
        self.__acive_patients_table = 'patients'
        self.__discharged_patients_table = 'discharged'
        self.__admin_table = 'admin'

    def formatFile(self, filename):
        try:
            file = open(f'database/{filename}.txt')
            line = 1
            tableData = []

            for ln in file:
                tabelRow = ln.split("|")
                if tabelRow[-1] == '\n':
                    tabelRow[-1] = tabelRow[-1][:-1]
                tableData.append(tabelRow)
                line +=1
            file.close()
            return tableData
        except FileNotFoundError:
            print('That data file doesnt exist')

    def initialiseData(self, tablename):
        table = self.formatFile(tablename)
        data = []
        for item in table[1:]:
            if tablename == self.__doctors_table:
                data.append([item[0], item[1], item[2], item[3], item[4]])
            elif tablename == self.__acive_patients_table or tablename == self.__discharged_patients_table:
                data.append([item[0], item[1], item[2], item[3], item[4], item[5], item[6]])
            elif tablename == self.__admin_table:
                # return [item[0], item[1], item[2]]
                return {"username": item[0], "password": item[1], "postcode": item[2]}
        return data
    
    def updateAdmin(self, username, password, postcode):
        adminPath = f'database/{self.__admin_table}.txt'
        with open(adminPath,'r') as file:
            data = file.readlines()
        data[1] = f'{username}|{password}|{postcode}'
        with open(adminPath, 'w') as file:
            file.writelines(data)
    
    def createDoctor(self, first_name, surname, speciality):
        with open('database/doctors.txt', 'a') as file:
            file.write(f'\n{first_name}|{surname}|{speciality}|[]|[]|')

    
    def updateDoctor(self, id, field, value):
        doctor = self.initialiseData('doctors')[id]
        first_name = doctor[0]
        surname = doctor[1]
        speciality = doctor[2]
        
        patients = doctor[3]
        appointments = doctor[4]

        if field == 'first_name':
            first_name = value
        elif field == 'surname':
            surname = value
        elif field == 'speciality':
            speciality = value
        elif field == 'patients':
            comma = ","
            if len(patients[:-1][1:]) == 0:
                comma = ""
            value = patients[:-1] + comma + value + ']'
            patients = value
        elif field == 'patients-rm':
            patients = patients.replace(f'{value},', '')
            patients = patients.replace(value, '')
            if patients[-2] == ',':
                patients = patients[:-2] + ']'
        elif field == 'appointments':
            comma = ","
            if len(appointments[:-1][1:]) == 0:
                comma = ""
            value = appointments[:-1] + comma + value + ']'
            appointments = value

        with open('database/doctors.txt', 'r') as file:
            f_data = file.readlines()
            newline='\n'
            if id+2 == len(f_data):
                newline = ''
        f_data[id+1] = '{}|{}|{}|{}|{}|{}'.format(first_name, surname, speciality, patients, appointments, newline)
        with open('database/doctors.txt', 'w') as file:
            file.writelines(f_data)

    def deleteDoctor(self, id):
        with open('database/doctors.txt', 'r') as file:
            f_data = file.readlines()
        with open('database/doctors.txt', 'w') as file:
            for number, line in enumerate(f_data):
                if number == id :
                    l = line
                    if len(f_data) == number + 2:
                        l = l.strip('\n')
                    file.write(l)
                if number != id+1 and number != id:
                    file.write(line)
    
    def addPatient(self, section, first_name, surname, age, mobile, postcode):
        tablename = ''
        if section == 'active':
            tablename = self.__acive_patients_table
        elif section == 'discharged':
            tablename = self.__discharged_patients_table
        else:
            print('Invalid patient category')

        with open(f'database/{tablename}.txt', 'a') as file:
            file.write(f'\n{first_name}|{surname}|{age}|{mobile}|{postcode}|None|[]|')

    def removePatient(self, section, id):
        tablename = ''
        if section == 'active':
            tablename = self.__acive_patients_table
        elif section == 'discharged':
            tablename = self.__discharged_patients_table
        else:
            print('Invalid patient category')

        with open(f'database/{tablename}.txt', 'r') as file:
            f_data = file.readlines()
        with open(f'database/{tablename}.txt', 'w') as file:
            for number, line in enumerate(f_data):
                if number == id:
                    l = line
                    if len(f_data) == number + 2:
                        l = l.strip('\n')
                    file.write(l)
                if number != id+1 and number != id:
                    file.write(line)


    def updatePatient(self, id, field, value):
        patient = self.initialiseData('patients')[id]
        
        first_name = patient[0]
        surname = patient[1]
        age = patient[2]
        mobile = patient[3]
        postcode = patient[4]
        doctor = patient[5]
        symptoms = patient[6]

        if field == 'doctor':
            doctor = value
        
        elif field == 'symptoms':
            comma = ","
            if len(symptoms[:-1][1:]) == 0:
                comma = ""
            value = symptoms[:-1] + comma + value + ']'
            symptoms = value
        
        with open('database/patients.txt', 'r') as file:
            f_data = file.readlines()
            newline='\n'
            if id+2 == len(f_data):
                newline = ''
        f_data[id+1] = '{}|{}|{}|{}|{}|{}|{}|{}'.format(first_name, surname, age, mobile, postcode, doctor, symptoms, newline)
        with open('database/patients.txt', 'w') as file:
            file.writelines(f_data)