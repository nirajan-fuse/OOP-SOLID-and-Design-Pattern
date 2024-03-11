# Create a Python class to represent a University. The university should have attributes like name, location, and a list of 
# departments. Implement encapsulation to protect the internal data of the University class. Create a Department class that 
# inherits from the University class. The Department class should have attributes like department name, head of the department, 
# and a list of courses offered. Implement polymorphism by defining a common method for both the University and Department 
# classes to display their details. 

class University:
    def __init__(self, name=None, location=None, departments=[]):
        self._name = name
        self._location = location
        self._departments = departments
    
    def display_details(self):
        print("University Name:", self._name)
        print("Location:", self._location)
        print("Departments:")
        for department in self._departments:
            print("-", department)


class Department(University):
    def __init__(self, name=None, location=None, dep_name=None, hod=None, courses=[]):
        super().__init__(name, location)
        self._dep_name = dep_name
        self._hod = hod
        self._courses = courses

    def display_details(self):
        print("Department Name:", self._dep_name)
        print("Head of Department:", self._hod)
        print("Courses Offered:")
        for course in self._courses:
            print("-", course)


university = University(name="Tribhuvan University", location="Kathmandu", departments=['CSIT', 'BE'])

department = Department(name="Tribhuvan University", location="Kathmandu", dep_name="CSIT", hod="Ram Thapa", courses=['C Programming', 'Microprocessor'])

university.display_details()
print()
department.display_details()