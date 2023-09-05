import pandas as pd


class Base:
    def __init__(self): 
        self.df = pd.read_csv(r"C:\Users\aniru\OneDrive\Documents\codingtemple\week6\day3\student\student-por.csv", sep=';')
        self.get_data()
    
    def get_data(self):
        self.df = self.df
        self.df.columns = self.df.columns.str.lower().str.strip()
        self.df.rename(columns={'traveltime':'travel_time','schoolsup':'school_sup','famsize':'fam_size','studytime':'study_time','freetime':'free_time','mjob':'mom_job','fjob':'dad_job'})
        return self.df


if __name__ == '__main__':
    c = Base()
    c.get_data()