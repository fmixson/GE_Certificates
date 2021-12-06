from Student_Info import StudentInfo


class CourseInfo(StudentInfo):

    def current_courses(self):
        current_term = 1219
        self.enrolled_courses = []

        for i in range(len(self.enrollment_history_df)):
            if self.student_id == self.enrollment_history_df.loc[i, "ID"]:
                if self.enrollment_history_df.loc[i, "Term"] == current_term:
                    if self.enrollment_history_df.loc[i, "Course"] not in self.enrolled_courses:
                        if self.enrollment_history_df.loc[i, 'Enrollment Drop Date'] == 0:
                            self.enrolled_courses.append(self.enrollment_history_df.loc[i, "Course"])
        print(self.enrolled_courses)
        return self.enrolled_courses