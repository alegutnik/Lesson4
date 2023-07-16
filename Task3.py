class Employer:
    instances = []

    def __init__(self, last_name, first_name, department, year_start_work):
        self.last_name = last_name
        self.first_name = first_name
        self.department = department
        self.year_start_work = year_start_work
        Employer.instances.append(self)

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        Employer.empty_value(value)
        self._last_name = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        Employer.empty_value(value)
        self._first_name = value

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, value):
        Employer.empty_value(value)
        self._department = value

    @property
    def year_start_work(self):
        return self._year_start_work

    @year_start_work.setter
    def year_start_work(self, value):
        Employer.empty_value(value)
        Employer.check_int_value(value)
        self._year_start_work = value

    @staticmethod
    def empty_value(value):
        if not value:
            raise ValueError("Параметр повинен бути заповненний!")

    @staticmethod
    def check_int_value(value):
        if not isinstance(value, int):
            raise ValueError("Рік повинен бути цілим числом!")

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.department} {self.year_start_work}"


employer_1 = Employer("Ivanov", "Ivan", "IT", 2010)
employer_2 = Employer("Petrov", "Petro", "IT", 2011)
# employer_3 = Employer("", "Sidor", "IT", 2012) # ValueError: Параметр повинен бути заповненний!
# employer_4 = Employer("Ivanov", "", "IT", 2013) # ValueError: Параметр повинен бути заповненний!
# employer_5 = Employer("Petrov", "Petro", "", 2014)  # ValueError: Параметр повинен бути заповненний!
# employer_6 = Employer("Sidorov", "Sidor", "IT", "2015") # ValueError: Рік повинен бути цілим числом!
employer_7 = Employer("Ivanov", "Ivan", "IT", 2016)
employer_8 = Employer("Petrov", "Petro", "IT", 2017)
employer_9 = Employer("Sidorov", "Sidor", "IT", 2018)
employer_10 = Employer("Ivanov", "Ivan", "IT", 2019)
# employer_10.year_start_work = "2020"    # ValueError: Рік повинен бути цілим числом!


for employer in Employer.instances:
    if employer.year_start_work > 2015:
        print(employer)
