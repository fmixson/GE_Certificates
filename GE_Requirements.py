import pandas as pd

class GeRequirements:


    def __init__(self, degree_applicable_dict, ge_data):
        self.degree_applicable_dict = degree_applicable_dict
        self.ge_data = ge_data
        self.completed_ge_courses = {}
        self.completed_ge_units = []
        self.ge_course_list = []



    def ge_courses_completed(self, area_name):
        for i in range(len(self.ge_data[area_name])):
            for key in self.degree_applicable_dict:
                if key == self.ge_data.loc[i, area_name]:
                    if area_name not in self.completed_ge_courses:
                        if key not in self.ge_course_list:
                            self.completed_ge_courses[area_name] = {'course': key, 'units': self.degree_applicable_dict[key]['units']}
                            self.completed_ge_units.append(self.degree_applicable_dict[key])
                            ge_units_total = sum(d['units'] for d in self.completed_ge_courses.values()if d)
                            self.ge_course_list = [d['course'] for d in self.completed_ge_courses.values() if d]
        return self.completed_ge_courses