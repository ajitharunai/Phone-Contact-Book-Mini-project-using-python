class Contact():
    def __init__(self):  # Constructor
        self.name = input("Enter Your Name: ")
        self.mobileNo = input("Enter mobile: ")

    def showInfo(self):  # Prints info
        print("name :", self.name, ", mobile no :", self.mobileNo)


first_contact = Contact()  # New instance of the class Contact, calls __init__()
first_contact.showInfo()  # Calls showInfo() on first_contact, which prints its attributes
