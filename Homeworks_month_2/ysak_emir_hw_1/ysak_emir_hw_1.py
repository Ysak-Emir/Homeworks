class Person:

    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f"Fullname: {self.fullname}\n"
              f"Age: {self.age}\n"
              f"Is married: {self.is_married}\n")
    def output(self):
        return f"fullname: {self.fullname}\n" \
               f"Age: {self.age}\n" \
               f"Is married: {self.is_married}\n"

class Student(Person):

    def __init__(self, marks, fullname, age, is_married):
        super().__init__(fullname, age, is_married)
        self.marks = marks  # Эта фигная словарик)))


class Teacher(Person):
    salary = 30000

    def __init__(self, fullname, age, is_married, experience=3):
        Person.__init__(self. fullname, age, is_married, experience)
        self.fullname = fullname
        self.age = age
        self.is_married = is_married
        self.experience = experience

    def the_salary(self, experience, salary):
        global procent_experience
        self.experience = experience
        self.salary = salary

    def Teacher_salary(self):
        if self.experience >= 3:
            new_salary = self.salary + ((self.salary/100*5) * (self.experience-3))
            return new_salary
    def results(self, experience, salary):
        Person.introduce_myself()
        self.experience = experience
        self.salary = salary
        teacher_esen = Teacher(name="Esenbek")
        print(teacher_esen)


def create_students(st1, st2, st3):
        st1 = Student(fullname="Кореш", age=98, is_married=False, marks={
            'math': 0,
            'russian': 0,
            'english': 0,
            'informatics': 0,
            'geography': 0,
            'biology': 0,
            'story': 0,
            'liters': 0,
            'chemistry': 0,
            'geometry': 0,
            'physics': 0,
            'physical_culture': 0
        })
        st2 = Student(fullname="Сыч", age=7, is_married=False, marks={
            'math': 0,
            'russian': 0,
            'english': 0,
            'informatics': 0,
            'geography': 0,
            'biology': 0,
            'story': 0,
            'liters': 0,
            'chemistry': 0,
            'geometry': 0,
            'physics': 0,
            'physical_culture': 0
        })
        st3 = Student(fullname="Димоооооооооооон", age=27, is_married=False, marks={
            'math': 0,
            'russian': 0,
            'english': 0,
            'informatics': 0,
            'geography': 0,
            'biology': 0,
            'story': 0,
            'liters': 0,
            'chemistry': 0,
            'geometry': 0,
            'physics': 0,
            'physical_culture': 0
        })


        create_students = [st1, st2, st3]
        return create_students

        students = create_students()
        for i in students:
            studentsss = []
            for marks in i.marks.values:
                studentsss.append(marks)
            print(f"Имя: {i.fullname}\n"
                f"Возраст: {i.age}\n"
                f"Женат?: {i.is_married}"
                f"Средние баллы: {sum(studentsss)/len(studentsss)}\n")

