import pytest
from module.school import Classroom, Teacher, Student, TooManyStudents


# --- Fixtures ---
@pytest.fixture
def hogwarts_classroom():
    """创建一个霍格沃茨课堂，默认教师是邓布利多"""
    teacher = Teacher("Dumbledore", 115)
    students = [Student("Harry", 17), Student(
        "Hermione", 17), Student("Ron", 17)]
    return Classroom(teacher=teacher, students=students, course="Defense Against the Dark Arts")


@pytest.fixture(params=["Harry", "Hermione", "Ron"])
def gryffindor_student(request):
    """参数化 fixture，每次生成不同的格兰芬多学生"""
    return Student(request.param, 17)


# --- Tests ---
def test_add_student_success(hogwarts_classroom):
    """测试成功添加新学生"""
    new_student = Student("Neville", 17)
    hogwarts_classroom.add_student(new_student)

    assert any(s.name == "Neville" for s in hogwarts_classroom.students)


def test_add_student_too_many(hogwarts_classroom):
    """测试超过人数限制时抛出 TooManyStudents"""
    # 把人数补到 10
    for i in range(7):
        hogwarts_classroom.add_student(Student(f"Extra{i}", 16))

    with pytest.raises(TooManyStudents):
        hogwarts_classroom.add_student(Student("Draco", 17))


@pytest.mark.parametrize("student_name", ["Harry", "Hermione", "Ron"])
def test_remove_student(hogwarts_classroom, student_name):
    """测试删除不同学生"""
    hogwarts_classroom.remove_student(student_name)
    assert all(s.name != student_name for s in hogwarts_classroom.students)


def test_change_teacher(hogwarts_classroom):
    """测试换老师"""
    new_teacher = Teacher("Snape", 45)
    hogwarts_classroom.change_teacher(new_teacher)

    assert hogwarts_classroom.teacher.name == "Snape"


def test_param_fixture_add_student(hogwarts_classroom, gryffindor_student):
    """用参数化 fixture 测试添加学生"""
    hogwarts_classroom.add_student(gryffindor_student)
    assert gryffindor_student in hogwarts_classroom.students


# @pytest.mark.slow
def test_course_name(hogwarts_classroom):
    """测试课程名字（用 mark 举例，可选 slow tests）"""
    assert hogwarts_classroom.course == "Defense Against the Dark Arts"
