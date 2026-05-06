class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def getMarks(self, no_of_subjects):
        self.marks = []
        for i in range(1, no_of_subjects + 1):
            input_marks = input(f'Enter marks{i}: ')
            self.marks.append(input_marks)


if __name__ == "__main__":
    input_name = input('Enter the name of the Student: ')
    input_roll_no = int(input('Enter the roll number of the Student: '))
    student_1 = Student(input_name, input_roll_no)
    input_no_of_subjects = int(input('Enter the number of Subjects: '))
    student_1.getMarks(input_no_of_subjects)
