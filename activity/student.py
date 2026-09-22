# add your Student class here!
class Student:

    def __init__(self, full_name, grade, classes_list):
        self.name = full_name
        self.grade = grade
        self.classes = classes_list

    def add_class(self, course):
        if course not in self.classes:
            self.classes.append(course)

        return self.classes

    def get_num_classes(self):
        return len(self.classes)


    def summary(self):
        num_classes = self.get_num_classes()

        grade_article = "an" if self.grade[0] in ["a", "e", "i", "o", "u"] else "a"
        return f"{self.name} is {grade_article} {self.grade} enrolled in {num_classes} classes"
