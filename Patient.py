class Patient:
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            address (string): address
        """

        #ToDo1
        pass
        self.__doctor = 'None'
       

    
    def full_name(self) :
        """full name is first_name and surname"""
        #ToDo2
        pass


    def get_doctor(self) :
        #ToDo3
        pass

    def link(self, doctor):
        """Args: doctor(string): the doctor full name"""
        self.__doctor = doctor

    def print_symptoms(self):
        """prints all the symptoms"""
        #ToDo4
        pass

    def __str__(self):
        return f'{self.full_name():^30}|{self.__doctor:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}'
