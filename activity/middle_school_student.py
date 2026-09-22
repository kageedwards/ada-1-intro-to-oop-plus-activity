from .student import Student

class MiddleSchoolStudent(Student):
    def __init__(self, name, grade, classes, gets_transportation=False, clubs=None):
        super().__init__(name, grade, classes)
        self.gets_transportation = gets_transportation
        self.clubs = [] if clubs is None else clubs

    def join_club(self, club):
        if club not in self.clubs:
            self.clubs.append(club)

        return self.clubs

    def get_num_clubs(self):
        return len(self.clubs)

    def display_clubs(self):
        if not self.clubs:
            return ""

        clubs = ", ".join(self.clubs)
        return f", is in {self.get_num_clubs()} clubs (including {clubs})"

    def display_gets_transportation(self):
        return "gets transportation" if self.gets_transportation else "doesn't get transportation"

    def summary(self):
        grade_article = "an" if self.grade[0] in "aeiou" else "a"
        gen_summary = f"{self.name} is {grade_article} {self.grade} grade student enrolled in {self.get_num_classes()} classes"
        club_summary = self.display_clubs()
        gets_transportation = self.display_gets_transportation()
        return gen_summary + club_summary + f" and {gets_transportation}"