from activity.middle_school_student import MiddleSchoolStudent

def test_new_valid_middle_school_student_with_defaults():
    name = "Brittany"
    grade = "eighth"
    classes = ["Pre-Algebra", "Geometry"]

    brittany = MiddleSchoolStudent(name, grade, classes)

    assert brittany.name == name
    assert brittany.grade == grade
    assert brittany.classes == classes
    assert len(brittany.classes) == 2
    assert not brittany.gets_transportation

def test_new_valid_middle_school_student_gets_transportation():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]

    # Act
    ellis = MiddleSchoolStudent(name, grade, classes, gets_transportation=True)

    assert ellis.gets_transportation

def test_middle_school_student_join_club():
    # Arrange
    name = "Jonathan"
    grade = "sixth"
    classes = ["Dodgeball"]
    new_club = "Pokemon Club"

    # Act
    jon = MiddleSchoolStudent(name, grade, classes, gets_transportation=True)
    jon.join_club(new_club)

    # Assert
    assert len(jon.clubs) == 1

def test_middle_school_student_summary_with_transportation():
    name = "Tatiana"
    grade = "seventh"
    classes = ["English", "Biology", "Aerospace"]

    tatiana = MiddleSchoolStudent(name, grade, classes, gets_transportation=True)

    summary = tatiana.summary()

    assert summary == "Tatiana is a seventh grade student enrolled in 3 classes and gets transportation"

def test_middle_school_student_summary_without_transportation():
    name = "Shontai"
    grade = "sixth"
    classes = ["Social Studies", "Spanish", "Theater", "Coding"]

    shontai = MiddleSchoolStudent(name, grade, classes, gets_transportation=False)
    shontai.join_club("Ada")

    summary = shontai.summary()

    assert summary == "Shontai is a sixth grade student enrolled in 4 classes, is in 1 clubs (including Ada) and doesn't get transportation"
