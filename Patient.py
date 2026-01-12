class Patient:
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode, doctor='None', symptoms=[]):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            address (string): address
        """
        self.__doctor = doctor
        self.__first_name = first_name
        self.__surname = surname
        self.__age = age
        self.__mobile = mobile
        self.__postcode = postcode
        self.__symptoms = symptoms

    
    def full_name(self) :
        return f'{self.__first_name} {self.__surname}'

    def get_doctor(self) :
        return self.__doctor

    def link(self, doctor):
        """Args: doctor(string): the doctor full name"""
        self.__doctor = doctor

    def print_symptoms(self):
        print('-----Patient Symptoms-----')
        number = 1
        for symptom in self.__symptoms:
            print(f'{number}) {symptom}\n')
            number += 1

    def get_symptoms(self):
        return self.__symptoms

    def add_symptoms(self, symptom):
        self.__symptoms.append(symptom)

    def __str__(self):
        return f'{self.full_name():^30}|{self.__doctor:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}'
    
    def get_data(self):
        return [self.__first_name, self.__surname, self.__age, self.__mobile, self.__postcode, self.__symptoms]