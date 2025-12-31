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
                data.append([item[0], item[1], item[2], item[3], item[4]])
            elif tablename == self.__admin_table:
                # return [item[0], item[1], item[2]]
                return {"username": item[0], "password": item[1], "postcode": item[2]}
        return data
    
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
            patients.append(value)
        elif field == 'appointments':
            appointments.append(value)

        with open('database/doctors.txt', 'r') as file:
            f_data = file.readlines()
        f_data[id+1] = '{}|{}|{}|{}|{}|'.format(first_name, surname, speciality, patients, appointments)
        with open('database/doctors.txt', 'w') as file:
            file.writelines(f_data)

    def deleteDoctor(self, id):
        with open('database/doctors.txt', 'r') as file:
            f_data = file.readlines()
        # with open('database/doctors.txt', 'w') as file:
        for number, line in enumerate(f_data):
            if number != id:
                print(line)