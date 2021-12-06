from Student_Info import StudentInfo

class TermInfo(StudentInfo):

    def first_term(self):
        current_term = 1219
        semester = ''
        for i in range(len(self.enrollment_history_df)):
            if self.student_id == self.enrollment_history_df.loc[i, "ID"]:
                if self.enrollment_history_df.loc[i, 'Term'] != 800:
                    if self.enrollment_history_df.loc[i, 'Term'] <= current_term:
                        current_term = self.enrollment_history_df.loc[i, 'Term']
                        semester = self.enrollment_history_df.loc[i, 'Term Description']
        print(semester)
        return semester