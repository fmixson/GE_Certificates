from easygui import fileopenbox
import pandas as pd
from Student_ID import StudentID
from dataframe import EnrollmentHistoryDataFrame
from Student_Info import StudentInfo
from Course_Info import CourseInfo
from Term_Info import TermInfo
from GE_Requirements import GeRequirements
from Social_Behavioral_Areas import SocialBehavAreas
from GE_Dataframe import GeDataframe
Plan_C_list = ['Comp', 'Crit_Think', 'Oral_Comm', 'Math', 'Arts', 'Hum', 'Arts_Hum','Soc_Behav1', 'Soc_Behav2', 'Soc_Behav3',
               'Phys_Sci', 'Bio_Sci', 'Sci_Labs']






enrollment_history_file = fileopenbox('Upload Ernollment Histories', filetypes='*.csv')
e = EnrollmentHistoryDataFrame(enrollment_history_file=enrollment_history_file)
enrollment_history_df = e.create_dataframe()
sid = StudentID(enrollment_history_df=enrollment_history_df)
student_ids_list = sid.student_ids()
for id in student_ids_list:
    sinfo = StudentInfo(student_id=id, enrollment_history_df=enrollment_history_df)
    degree_applicable_courses = sinfo.completed_courses()
    crsinfo = CourseInfo(student_id=id, enrollment_history_df=enrollment_history_df)
    crsinfo.current_courses()
    terminfo = TermInfo(student_id=id, enrollment_history_df=enrollment_history_df)
    terminfo.first_term()
    ge_df = GeDataframe(ge_plan='PlanC_GE.csv')
    ge_data = ge_df.construct_ge_dataframe()
    ge_requirements = GeRequirements(degree_applicable_dict=degree_applicable_courses, ge_data=ge_data)
    soc_behav_requirements = SocialBehavAreas(degree_applicable_dict=degree_applicable_courses, ge_data=ge_data)
    for area in Plan_C_list:
        if area == 'Soc_Behav1' or area == 'Soc_Behav2' or area == 'Soc_Behav3':
            soc_behav_requirements.ge_courses_completed(area_name=area, ge_courses_completed=ge_courses_completed)
        else:
            ge_courses_completed = ge_requirements.ge_courses_completed(area_name=area)
            print('after else', ge_courses_completed)







