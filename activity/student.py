# add your Student class here!
class Student:

    def __init__(self, full_name, grade, classes_list=[]):
        self.name = full_name
        self.grade = grade
        self.classes = classes_list

    def add_class(self, course):
        if course not in self.classes:
            self.classes.append(course)

    def get_num_classes(self):
        return len(self.classes)


    def summary(self):
        num_classes = self.get_num_classes()

        return f"{self.name} is a {self.grade} enrolled in {num_classes} classes"
