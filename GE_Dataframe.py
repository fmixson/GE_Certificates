import pandas as pd


class GeDataframe:
    def __init__(self, ge_plan):
        self.ge_plan = ge_plan
        print(self.ge_plan)
    def construct_ge_dataframe(self):
        ge_dataframe = pd.read_csv(self.ge_plan)
        return ge_dataframe