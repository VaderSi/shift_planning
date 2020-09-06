#import numpy as np
#import matplotlib.pyplot as plt
import xlrd
import pandas as pd
#import os
#import csv

#

#Finding the roots
#cwd = os.getcwd()
#dir_list = os.listdir(cwd)

Data_File = "C:/Users/Simon/Documents/Projekte/Stammdaten.xlsx"
#Sd_xlsx_d = (cwd + "\Stammdaten.xlsx")

#Opening hours
day = pd.read_excel(Data_File, sheet_name = "allg. Beschränkungen", index_col="Tag", na_filter =False).iloc[:7]
hours_per_day = day["Anzahl h"]

#employee capacity
empl_data = pd.read_excel(Data_File, sheet_name ="Mitarbeiter", index_col="Name", na_filter =False)
empl_maxHours = empl_data["week hours"]


#employee competence
empl_comp = empl_data["competence"]
workers_for_Bar = []
workers_for_Service = []
workers_for_Kueche = []

#calculations
sum_openHours = sum(hours_per_day)
sum_emplHours = sum(empl_maxHours)


#print(empl_data)
#print(day)
#print(empl_comp)
#print(sum_emplHours)
#print(sum_hours)
#print(hours_per_day)

#print(openings.head())


#with open(cwd + "\ " + Sd_sheets[0] + ".csv", mode="r") as csv_file:
#csv_employee = csv.DictReader(csv_file, delimiter=",")






#Combining roots with specific files (DO NOT CHANGE)
#Sd_xlsx_d = (cwd + "\Stammdaten.xlsx")
#Sd_sheets = "Mitarbeiter", "Zeitplanung", "allg. Beschränkungen"