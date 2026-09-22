from .student import Student

class HighSchoolStudent(Student):
    def __init__(self, name, grade, classes, has_parking_privileges=False, clubs=[]):
        super().__init__(self, name, grade, classes)
        self.has_parking_privileges = has_parking_privileges
        self.clubs = clubs

    def join_club(self, club):
        if club not in self.clubs:
            self.clubs.append(club)

        return self.clubs

    def get_num_clubs(self):
        return len(self.clubs)

    def display_parking_privileges(self):
        return "has parking privileges" if self.has_parking_privileges else "doesn't have parking privileges"

    def display_clubs(self):
        return ", ".join(self.clubs)

    def summary(self):
        gen_summary = super().summary()
        parking_perm = self.display_parking_privileges()
        return gen_summary + f" , is in {self.get_num_clubs()} (including {self.display_clubs()}), and {parking_perm}"