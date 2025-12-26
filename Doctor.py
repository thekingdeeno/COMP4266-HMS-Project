class Doctor:
    """A class that deals with the Doctor operations"""

    def __init__(self, first_name, surname, speciality):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            speciality (string): Doctor`s speciality
        """

        self.__first_name = first_name
        self.__surname = surname
        self.__speciality = speciality
        self.__patients = []
        self.__appointments = []

    
    def full_name(self) :
        #ToDo1
        pass

    def get_first_name(self) :
        #ToDo2
        pass
        return self.__first_name

    def set_first_name(self, new_first_name):
        #ToDo3
        pass

    def get_surname(self) :
        #ToDo4
        pass
        return self.__surname
        

    def set_surname(self, new_surname):
        #ToDo5
        pass

    def get_speciality(self) :
        #ToDo6
        pass
        return self.__surname

    def set_speciality(self, new_speciality):
        #ToDo7
        pass

    def add_patient(self, patient):
        self.patients.append(patient)


    def __str__(self) :
        return f'{self.full_name():^30}|{self.__speciality:^15}'
