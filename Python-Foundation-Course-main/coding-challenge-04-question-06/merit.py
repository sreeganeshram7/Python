from student import Student


class merit(Student):
    def criteria(self):
        sum = 0

        for i in self.marks:
            sum += int(i)
        avg = sum / 3

        if avg < 90:
            print(f'{self.name} with Roll No: {self.roll_no}, is not eligible.')
        else:
            print(f'Congrats! {self.name} with Roll No: {self.roll_no}, got a merit certificate.')


if __name__ == "__main__":
    input_name = input('Enter the name of the Student: ')
    input_roll_no = int(input('Enter the roll number of the Student: '))
    merit_check = merit(input_name, input_roll_no)
    input_no_of_subjects = int(input('Enter the number of Subjects: '))
    merit_check.getMarks(input_no_of_subjects)
    merit_check.criteria()
