from tkinter import *
from Database import Database
from Admin import Admin
from Doctor import Doctor
from Patient import Patient
import json


class HMS_GUI:
    def __init__(self, admin, doctors, patients, discharged):

        self.admin = admin
        self.doctors = doctors
        self.patients = patients
        self.discharged = discharged

        self.mainWindow = Tk()
        self.mainWindow.title("Hospital Managementt System")
        self.mainWindow.geometry("1080x720")
        self.mainWindow
        self.mainFrame = Frame(self.mainWindow)
        self.mainFrame.pack()

        self.menubar = Menu(self.mainWindow)
        self.mainWindow.config(menu = self.menubar)
        
        self.doctor_menu = Menu(self.menubar, tearoff = 0)
        self.menubar.add_cascade(label ='Doctor', menu = self.doctor_menu)
        self.doctor_menu.add_command(label ='Register', command = self.registerDoctor)
        self.doctor_menu.add_command(label ='View Doctors', command = self.viewDoctors)

        self.patient_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Patient", menu=self.patient_menu)
        self.patient_menu.add_command(label="Admit New Patient", command=self.admitPatient)
        self.patient_menu.add_command(label="View Active Patients", command=self.viewPatients)
        self.patient_menu.add_command(label='View Discharged Patients', command= lambda: self.viewPatients('discharged'))

        self.settings_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Settings', menu=self.settings_menu, command=None)
        self.settings_menu.add_command(label='Admin Account', command=self.adminProfile)
        self.settings_menu.add_command(label='Generate Report', command=self.generateReport)
        self.settings_menu.add_command(label='Quit', command=lambda: self.mainWindow.destroy())

        # self.mainHeaderVar = StringVar()
        self.mainHeader = Label(self.mainFrame, text = "Hospital Managementt System")
        # self.mainHeaderVar.set("Hospital Managementt System")
        self.mainHeader.pack()

        self.isLoggedIn = False

    def clearScreen(self):
        for widget in self.mainFrame.winfo_children():
            widget.destroy()

    def home(self):

        Label(self.mainFrame, text = "HOME").pack()

        Label(self.mainFrame, text='WELCOME TO MY HOSPITAL MANAGEMENT SYSTEM', font=("Helvetica", 20)).pack()

        Label(self.mainFrame, text='BUILT WITH PYTHON AND THE TKINTER LIBRARY', font=("Helvetica", 20)).pack()

        Label(self.mainFrame, text='\n\nUse the menue bar at the top to navigate through the system... NOTE: if youre on MacOs the menue options will be at the top of your screen', wraplength=600, font=("Helvetica", 15)).pack()

        Label(self.mainFrame, text='\n\nNwando Ifezue (23115536)', font=("Helvetica", 20)).pack()
        Label(self.mainFrame, text='kingskid.ifezue@mail.bcu.ac.uk', font=("Helvetica", 20)).pack()

    def adminProfile(self):
        self.clearScreen()
        admin = self.admin.get_admin_data()
        Label(self.mainFrame, text = "ADMIN PROFILE").pack()

        profileBox = Frame(self.mainFrame, width=700)
        profileBox.pack()

        Label(profileBox, text='Username: ').grid(row=0, column=0)
        nameBox = Label(profileBox, text=admin['username']).grid(row=0, column=1)
        
        Label(profileBox, text='Address: ').grid(row=1, column=0)
        addressBox = Label(profileBox, text=admin['address']).grid(row=1, column=1)

        updateBtn = Button(profileBox, text='Update Info', command= lambda: updateInfo()).grid(row=2, column=0)
        passwordBtn = Button(profileBox, text='Change Password', command= lambda: updatePassword()).grid(row=2, column=1)

        def updateInfo():
            nonlocal nameBox, addressBox, updateBtn
            nameBox = Entry(profileBox)
            nameBox.insert(0, admin["username"])
            nameBox.grid(row=0, column=1)

            addressBox = Entry(profileBox)
            addressBox.insert(0, admin["address"])
            addressBox.grid(row=1, column=1)


            profileBox.winfo_children()[4].destroy()
            updateBtn = Button(profileBox, text='Confirm', command= lambda: processUpdate()).grid(row=2, column=0)

            def processUpdate():
                self.admin.updateAdminFromGui(nameBox.get(), addressBox.get(), admin["password"])
                Database().updateAdmin(nameBox.get(), admin["password"], addressBox.get())
                self.adminProfile()
        
        def updatePassword():
            self.clearScreen()
            Label(self.mainFrame, text = "UPDATE PASSWORD").pack()

            profileBox = Frame(self.mainFrame, width=700)
            profileBox.pack()

            Label(profileBox, text='New Password: ').grid(row=0, column=0)
            newPassword = Entry(profileBox)
            newPassword.grid(row=0, column=1)
            
            Label(profileBox, text='Confirm Password: ').grid(row=1, column=0)
            confirmPassword = Entry(profileBox)
            confirmPassword.grid(row=1, column=1)

            updateBtn = Button(profileBox, text='Confirm', command= lambda: processUpdate()).grid(row=2, column=0)

            Label(profileBox, text = "").grid(row=3, column=0)
            def processUpdate():

                if newPassword.get() != confirmPassword.get():
                    profileBox.winfo_children()[-1].destroy()
                    Label(profileBox, text = "New password and confirm password have to be the same").grid(row=3, column=0)
                    return
                if len(newPassword.get()) < 3:
                    profileBox.winfo_children()[-1].destroy()
                    Label(profileBox, text = "Password must be more than 3 characters").grid(row=3, column=0)
                    return

                self.admin.updateAdminFromGui(admin["username"], admin["address"], newPassword.get())
                Database().updateAdmin(admin["username"], newPassword.get(), admin["address"])
                self.adminProfile()


    def registerDoctor(self):
        self.clearScreen()
        Label(self.mainFrame, text = "REGISTER DOCTOR").pack()
        regFrame = Frame(self.mainFrame, width=700)
        regFrame.pack()

        Label(regFrame, text='Firstname').grid(row=0, column=0)
        firstName = Entry(regFrame)
        firstName.grid(row=0, column=1)

        Label(regFrame, text="Surname").grid(row=1, column=0)
        surname = Entry(regFrame)
        surname.grid(row=1, column=1)

        Label(regFrame, text="Speciality").grid(row=2, column=0)
        speciality = Entry(regFrame)
        speciality.grid(row=2, column=1)

        Button(regFrame, text='Register', command= lambda: processRegistration()).grid(row=3, columnspan=2)


        def processRegistration():
            self.doctors.append(Doctor(firstName.get(), surname.get(), speciality.get()))
            Database().createDoctor(firstName.get(), surname.get(), speciality.get())
            self.viewDoctors()



    def viewDoctors(self):
        self.clearScreen()
        Label(self.mainFrame, text = "DOCTORS").pack()
        tableHead = Frame(self.mainFrame, width=700)
        tableHead.pack()
        Label(tableHead, text = 'ID').grid(row=0, column=0)
        Label(tableHead, text = 'NAME').grid(row=0, column=1)
        Label(tableHead, text = 'SPECIALITY').grid(row=0, column=2)

        doc_id = 1
        for doctor in self.doctors:
            full_name = doctor.full_name()
            speciality = doctor.get_speciality()
            doc_box = Frame(self.mainFrame, bg='blue', width=700)
            doc_box.pack()
            Label(doc_box, text = doc_id).grid(row=0, column=0)
            Label(doc_box, text = full_name).grid(row=0, column=1)
            Label(doc_box, text = speciality).grid(row=0, column=2)
            Button(doc_box, text='Manage', command= lambda docId = doc_id: self.manageDoctor(docId)).grid(row=0, column=3)

            doc_id += 1


    def manageDoctor(self, doc_Id):
        self.clearScreen()
        doctor = self.doctors[doc_Id - 1]
        Label(self.mainFrame, text = "MANAGE DOCTOR").pack()
        Label(self.mainFrame, text = f'Name: {doctor.full_name()}').pack()
        Label(self.mainFrame, text = f'Speciality: {doctor.get_speciality()}').pack()

        Button(self.mainFrame, text='Update', command= lambda docId = doc_Id: update(docId)).pack()
        Button(self.mainFrame, text='Delete', command= lambda docId = doc_Id: delete(docId)).pack()

        def delete(docId):
            index = docId -1
            Database().deleteDoctor(index)
            self.doctors.pop(index)
            self.viewDoctors()

        def update(docId):
            self.clearScreen()
            index = docId -1
            doctor = self.doctors[index]
            Label(self.mainFrame, text = "UPDATE DOCTOR").pack()

            updateView = Frame(self.mainFrame, width=700)
            updateView.pack()
            
            Label(updateView, text='First Name').grid(row=0, column=0)
            f_name = Entry(updateView)
            f_name.insert(0, doctor.get_first_name())
            f_name.grid(row=0, column=1)

            Label(updateView, text='Last Name').grid(row=1, column=0)
            l_name = Entry(updateView)
            l_name.insert(0, doctor.get_surname())
            l_name.grid(row=1, column=1)

            Label(updateView, text='Speciality').grid(row=2, column=0)
            speciality = Entry(updateView)
            speciality.insert(0, doctor.get_speciality())
            speciality.grid(row=2, column=1)

            Button(updateView, text='Update', command= lambda: processUpdate() ).grid(row=3, columnspan=2)

            def processUpdate():
                doctor.set_first_name(f_name.get())
                Database().updateDoctor(index, 'first_name', f_name.get())

                doctor.set_surname(l_name.get())
                Database().updateDoctor(index, 'surname', l_name.get())

                doctor.set_speciality(speciality.get())
                Database().updateDoctor(index, 'speciality', speciality.get())
                
                self.manageDoctor(doc_Id)

        Label(self.mainFrame, text = 'Patients').pack()
        row_index = 0
        for patient in doctor.get_patients():
            pat_box = Frame(self.mainFrame, bg='blue', width=700)
            pat_box.pack()
            Label(pat_box, text = patient).grid(row=row_index, column=0)
            Button(pat_box, text="view", command= lambda: goToPatient(patient)).grid(row=row_index, column=1)
            row_index += 1

        def goToPatient(name):
            searchIndex = 1
            found = False
            for patient in self.patients:
                if name == patient.full_name():
                    found = True
                    break
                searchIndex += 1
            
            if found:
                self.managePatients(searchIndex)

        Label(self.mainFrame, text = 'Appointments:').pack()
        for appointment in doctor.get_appointments():
            Label(self.mainFrame, text = appointment).pack()
        


        addApt = Button(self.mainFrame, text='Add Appointment', command= lambda: addAppointment())
        addApt.pack()

        def addAppointment():
            nonlocal addApt
            addApt.destroy()
            addApt = Frame(self.mainFrame)
            addApt.pack()

            dayInput = Frame(addApt)
            dayInput.grid(row=0, column=0)
            Label(dayInput, text='Day: ').pack(side='left')
            day = Entry(dayInput, width=2)
            day.pack(side='left')

            
            monthInput = Frame(addApt)
            monthInput.grid(row=0, column=1)
            Label(monthInput, text='Month: ').pack(side='left')
            month = Entry(monthInput, width=2)
            month.pack(side='left')

            yearInput = Frame(addApt)
            yearInput.grid(row=0, column=2)
            Label(yearInput, text='Year: ').pack(side='left')
            year = Entry(yearInput, width=5)
            year.pack(side='left')

            Button(addApt, text='Confirm', command=lambda: confirmAppointment()).grid(row=0, column=3)
            def confirmAppointment():
                appointment = f'{day.get()}/{month.get()}/{year.get()}'
                doctor.add_appointment(appointment)
                Database().updateDoctor(doc_Id -1, 'appointments', appointment)
                self.manageDoctor(doc_Id)

    def admitPatient(self):
        self.clearScreen()
        Label(self.mainFrame, text = "ADMIT NEW PATIENT").pack()
        regFrame = Frame(self.mainFrame, width=700)
        regFrame.pack()

        Label(regFrame, text='Firstname').grid(row=0, column=0)
        firstName = Entry(regFrame)
        firstName.grid(row=0, column=1)

        Label(regFrame, text="Surname").grid(row=1, column=0)
        surname = Entry(regFrame)
        surname.grid(row=1, column=1)

        Label(regFrame, text="Age").grid(row=2, column=0)
        age = Entry(regFrame)
        age.grid(row=2, column=1)

        Label(regFrame, text="Mobile").grid(row=3, column=0)
        mobile = Entry(regFrame)
        mobile.grid(row=3, column=1)

        Label(regFrame, text="Postcode").grid(row=4, column=0)
        postcode = Entry(regFrame)
        postcode.grid(row=4, column=1)

        Button(regFrame, text='Register', command= lambda: processRegistration()).grid(row=5, columnspan=2)


        def processRegistration():
            self.patients.append(Patient(firstName.get(), surname.get(), age.get(), mobile.get(), postcode.get()))
            Database().addPatient('active', firstName.get(), surname.get(), age.get(), mobile.get(), postcode.get())
            self.managePatients(len(self.patients))



    def viewPatients(self, category = 'active'):
        self.clearScreen()
        header = 'PATIENTS'
        pat_list = self.patients
        if category == 'discharged':
            header = f'DISCHARGED {header}'
            pat_list = self.discharged
        Label(self.mainFrame, text = header).pack()
        tableHead = Frame(self.mainFrame, width=700)
        tableHead.pack()
        Label(tableHead, text = 'ID').grid(row=0, column=0)
        Label(tableHead, text = 'NAME').grid(row=0, column=1)
        # Label(tableHead, text = 'SURNAME').grid(row=0, column=2)


        pat_id = 1
        for patient in pat_list:
            full_name = patient.full_name()
            # speciality = patient.get_speciality()
            pat_box = Frame(self.mainFrame, bg='blue', width=700)
            pat_box.pack()
            Label(pat_box, text = pat_id).grid(row=0, column=0)
            Label(pat_box, text = full_name).grid(row=0, column=1)
            # Label(pat_box, text = speciality).grid(row=0, column=2)
            if category == 'active':
                Button(pat_box, text='Manage', command= lambda patId = pat_id: self.managePatients(patId)).grid(row=0, column=3)

            pat_id += 1
                
    
    def managePatients(self, pat_id):
        self.clearScreen()
        patient = self.patients[pat_id - 1]
        db_patient = patient.get_data()
        Label(self.mainFrame, text = "MANAGE PATIENT").pack()
        Label(self.mainFrame, text = f'Name: {patient.full_name()}').pack()
        Label(self.mainFrame, text = f'Age: {db_patient[2]}').pack()
        Label(self.mainFrame, text = f'Mobile: {db_patient[3]}').pack()
        Label(self.mainFrame, text = f'Postcode: {db_patient[4]}').pack()

        symptomsCont = Frame(self.mainFrame)
        symptomsCont.pack()

        symptoms = Label(symptomsCont, text=f'Symptoms: {db_patient[5]}')
        symptoms.grid(row=0, column=0)

        addBtn = Button(symptomsCont, text='Add', command= lambda: addSymptom())
        addBtn.grid(row=0, column=1)

        def addSymptom():
            nonlocal symptoms
            symptoms.destroy()
            symptoms = Entry(symptomsCont)
            symptoms.grid(row=0, column=0)

            addBtn = Button(symptomsCont, text='Confirm', command= lambda: processUpdate())
            addBtn.grid(row=0, column=1)

            def processUpdate():
                patient.add_symptoms(symptoms.get())
                Database().updatePatient(pat_id - 1, 'symptoms', symptoms.get())
                self.managePatients(pat_id)

        
        

        docContainer = Frame(self.mainFrame)
        docContainer.pack()

        Label(docContainer, text = f'Doctor: {patient.get_doctor()}').grid(row=0, column=0)

        if patient.get_doctor() != 'None':
            Button(docContainer, text='view', command= lambda: viewDoctorProfile()).grid(row=0, column=1)
            def viewDoctorProfile():
                
                for doc in self.doctors:
                    searchIndex = 1
                    if doc.full_name() == patient.get_doctor():
                        self.manageDoctor(searchIndex)
                        break
                    searchIndex += 1

        btnContainer = Frame(self.mainFrame)
        btnContainer.pack()
        Button(btnContainer, text='Assign', command= lambda: assignDoctor()).grid(row=0, column=0)
        Button(btnContainer, text='Discharge', command= lambda patId = pat_id: discharge(patId)).grid(row=0, column=1)

        def assignDoctor():
            Label(self.mainFrame, text = "DOCTORS").pack()
            tableHead = Frame(self.mainFrame, width=700)
            tableHead.pack()
            Label(tableHead, text = 'ID').grid(row=0, column=0)
            Label(tableHead, text = 'NAME').grid(row=0, column=1)
            Label(tableHead, text = 'SPECIALITY').grid(row=0, column=2)

            doc_id = 1
            for doctor in self.doctors:
                full_name = doctor.full_name()
                speciality = doctor.get_speciality()
                doc_box = Frame(self.mainFrame, bg='blue', width=700)
                doc_box.pack()
                Label(doc_box, text = doc_id).grid(row=0, column=0)
                Label(doc_box, text = full_name).grid(row=0, column=1)
                Label(doc_box, text = speciality).grid(row=0, column=2)
                Button(doc_box, text='Select', command= lambda docId = doc_id: assignToPatient(docId)).grid(row=0, column=3)

                doc_id += 1
            def assignToPatient(docId):
                doc_index = docId -1
                doctor = self.doctors[doc_index]
                patientDoc = patient.get_doctor()
                if patient.get_doctor() != "None":
                    searchIndex = 0
                    # found = False
                    for doc in self.doctors:
                        if doc.full_name() == patientDoc:
                            doc.del_patient(patient.full_name())
                            Database().updateDoctor(searchIndex, 'patients-rm', patient.full_name())
                        searchIndex += 1

                patient.link(doctor.full_name())
                doctor.add_patient(patient.full_name())
                Database().updateDoctor(doc_index, 'patients', patient.full_name())
                Database().updatePatient(pat_id - 1, 'doctor', doctor.full_name())
                self.managePatients(pat_id)

        def discharge(patId):
            index = patId -1
            Database().addPatient('discharged', db_patient[0], db_patient[1], db_patient[2], db_patient[3], db_patient[4])
            self.discharged.append(patient)
            Database().removePatient('active',index)
            self.patients.pop(index)
            self.viewPatients()

    def generateReport(self):
        self.clearScreen()
        report = self.admin.fetchReport(self.patients, self.doctors)

        Label(self.mainFrame, text='=========== HOSPITAL MANAGEMENT SYSTEM REPORT ===========\n').pack()
        Label(self.mainFrame, text='===== PERSONEL METRICS ====').pack()
        Label(self.mainFrame, text=f"Total Number Of Doctors: {report['doctors_count']}").pack()
        Label(self.mainFrame, text=f"Total Number Of Patients: {report['patients_count']}").pack()
        
        Label(self.mainFrame, text="\n\n===== ILLNESS METRICS =====").pack()
        for attr, value in report['patient_symptoms_data'].items():
            Label(self.mainFrame, text=f'{attr}: {value} patient(s)').pack()

        Label(self.mainFrame, text="\n\n===== NUMBER OF PATIENTS PER DOCTOR =====").pack()        
        for attr, value in report['patients_per_doc'].items():
            Label(self.mainFrame, text=f'{attr}: {value} patient(s)').pack()

        Label(self.mainFrame, text="\n\n========== NUMBER OF PATIENT APPOINTMENT PER MONTH PER DOCTOR ==========\n").pack()


        table = Frame(self.mainFrame)
        table.pack()

        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']

        Label(table, text='Doctor').grid(row=0, column=0)
        month_sn = 1
        for month in months:
            Label(table, text=month).grid(row=0, column=month_sn)
            month_sn += 1
        doc_sn = 1
        for docStat in report['appointments_per_month']:

            item_sn = 0
            for item in docStat:
                Label(table, text=item).grid(row=doc_sn, column=item_sn)
                item_sn += 1
            doc_sn += 1