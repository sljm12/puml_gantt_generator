"""
This is 
"""
from enum import Enum
import calendar



    

class Quarter(Enum):
    """
    This is
    """
    Q1 = "Q1"
    Q2 = "Q2"
    Q3 = "Q3"
    Q4 = "Q4"

    def print(self):
        return self.value
    
    def get_date_end(self, year):
        match self.value:
            case "Q1":                
                return self.form_last_day(year, 4)
            case "Q2":
                return self.form_last_day(year, 7)
            case "Q3":
                return self.form_last_day(year, 10)
            case "Q4":
                return self.form_last_day(year, 1)
            case _:
                return ""

    def get_date_start(self, year):
        match self.value:
            case "Q1":
                return self.form_date(year, 4, 1)
            case "Q2":
                return self.form_date(year, 7, 1)
            case "Q3":
                return self.form_date(year, 10, 1)
            case "Q4":
                return self.form_date(year, 1, 1)
            case _:
                return ""
   
    def form_date(self, year, month, last_day):
        return "-".join([str(year), str(month), str(last_day)])

    def form_last_day(self, year, month):
        return self.form_date(year, month, calendar.monthrange(year, month)[1])

class QuarterYear:
    def __init__(self, quarter, year):
        self.quarter = quarter
        self.year = year
        
    def start_date(self):
        return self.quarter.get_date_start(self.year)
    
    def end_date(self):
        return self.quarter.get_end_date(self.year)

class Task:
    def __init__(self, taskname: str, quarter: QuarterYear, start_time = None, end_time = None):
        self.color = None
        self.start_time = start_time
        self.taskname = taskname
        self.end_time = end_time
        self.quarter = quarter
    
    
a = Quarter.Q1

print(a.get_date_start(2024), a.get_date_end(2024))

q1 = QuarterYear(a, 2024)
Task(taskname = "GIS", quarter=q1)


