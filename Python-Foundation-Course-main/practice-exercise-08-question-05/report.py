from medical import medical


class reportFeedback(medical):
    def bmi_result(self):
        if self.result < 18.5:
            self.msg = 'Underweight'
        elif self.result > 25:
            self.msg = 'Overweight'
        else:
            self.msg = 'Normal Weight'

        print(self.msg)


if __name__ == "__main__":
    report1 = reportFeedback('David', 83, 1.8)
    report1.bmi_result()
