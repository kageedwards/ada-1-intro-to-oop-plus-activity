from .student import Student

class HighSchoolStudent(Student):

    def __init__(self, name, grade, classes, has_parking_privileges=False, clubs=None):
        super().__init__(name, grade, classes)
        self.has_parking_privileges = has_parking_privileges
        self.clubs = [] if clubs is None else clubs

    def join_club(self, club):
        if club not in self.clubs:
            self.clubs.append(club)

        return self.clubs

    def get_num_clubs(self):
        return len(self.clubs)

    def display_parking_privileges(self):
        return "has parking privileges" if self.has_parking_privileges else "doesn't have parking privileges"

    def display_clubs(self):
            if not self.clubs:
                return ""
    
            clubs = ", ".join(self.clubs)
            return f", is in {self.get_num_clubs()} clubs (including {clubs})"

    def summary(self):
        gen_summary = f"{self.name} is a {self.grade} enrolled in {self.get_num_classes()} classes"
        club_summary = self.display_clubs()
        parking_perm = self.display_parking_privileges()
        return gen_summary + club_summary + f" and {parking_perm}"