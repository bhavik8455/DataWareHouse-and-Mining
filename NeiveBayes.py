import csv

with open('data.csv', 'w') as csv_file:
    writer = csv.writer(csv_file , delimiter='|', lineterminator='\n')

    writer.writerow(['Example No.','Color','Type','Origin','Stolen'])

    data = [
        ['1','Red','Sports','Domestic','Yes'],
        ['2','Red','Sports','Domestic','No'],
        ['3','Red','Sports','Domestic','Yes'],
        ['4','Yellow','Sports','Domestic','No'],
        ['5','Yellow','Sports','Imported','Yes'],
        ['6','Yellow','Suv','Imported','No'],
        ['7','Yellow','Suv','Imported','Yes'],
        ['8','Yellow','Suv','Domestic','No'],
        ['9','Red','Suv','Imported','No'],
        ['10','Red','Sports','Imported','Yes'],
        
    ]

    writer.writerows(data)

#Initilize  Mendatory Variable
ProbRed= len([row for row in data if row[1] == 'Red'])/len(data)
ProbYellow= len([row for row in data if row[1] == 'Yellow'])/len(data)

ProbYes= len([row for row in data if row[4]=='Yes'])/len(data)
ProbNo= len([row for row in data if row[4]=='No'])/len(data)

ProbSuv = len([row for row in data if row[2]=='Suv'])/len(data)
ProbSports = len([row for row in data if row[2]=='Sports'])/len(data)

ProbDomes = len([row for row in data if row[3]=='Domestic'])/len(data) 
ProbImported = len([row for row in data if row[3]=='Imported'])/len(data) 


#Calculated Probability of Stolen=Yes  , Stolen = No and Color=Red
ProbYesRed = len([row for row in data if row[1] == 'Red' and row[4] == 'Yes'])/len([row for row in data if row[1]=='Red'])
ProbRed_Yes = ProbYesRed*ProbRed/ProbYes
ProbNoRed  = len([row for row in data if row[1] == 'Red' and row[4] == 'No'])/len([row for row in data if row[1]=='Red'])


#Calculated Probability of Stolen=Yes and Tpe=SUV
ProbYesSuv = len([row for row in data if row[2]=='Suv' and row[4]=='Yes'])/len([row for row in data if row[2]=='Suv'])
ProbNoSuv = len([row for row in data if row[2]=='Suv' and row[4]=='No'])/len([row for row in data if row[2]=='Suv'])
ProbSuv_Yes = ProbYesSuv*ProbSuv/ProbYes


#Calculated Probability of Stolen=Yes and Origin=Domestic
ProbYesDomes = len([row for row in data if row[3]=='Domestic' and row[4]=='Yes'])/len([row for row in data if row[3]=='Domestic'])
ProbNoDomes = len([row for row in data if row[3]=='Domestic' and row[4]=='No'])/len([row for row in data if row[3]=='Domestic'])
ProbDom_Yes = ProbYesDomes*ProbDomes/ProbYes

#Calculated Probability of Stolen=Yes Over X = {(Color="Red", Type="SUV"; and Origin="Domestic") }
ProbX_Yes = ProbRed_Yes * ProbSuv_Yes * ProbDom_Yes
ProbX_No =  (ProbNoRed*ProbRed/ProbNo) * (ProbNoSuv*ProbSuv/ProbNo) *(ProbNoDomes*ProbDomes/ProbNo)


#---------------------print dataset------------
print("---------------------print dataset------------")
print("The dataset is  : ")
for row in data :
    print(row)

# print no. of rows and columns of dataset..
print("-------print no. of rows and columns of dataset-----------")
print("No. of Rows is  : ",len([row for row in data]))
print("No. of Columns is",len(data[0]))

# print the individual class probability of Yes..
print("-----print the individual class probability of Yes----------")

print("The Probabiliy of Red | Yes ",ProbRed_Yes)
print("The Probabiliy of Suv | Yes ",ProbSuv_Yes)
print("The Probabiliy of Domestic | Yes ",ProbDom_Yes)

# print the individual  class probability of No..
print("-----print the individual  class probability of No----------")

print("The Probabiliy of Red | No ",(ProbNoRed*ProbRed/ProbNo))
print("The Probabiliy of Suv | No ",round((ProbNoSuv*ProbSuv/ProbNo),1))
print("The Probabiliy of Domestic | No ",(ProbNoDomes*ProbDomes/ProbNo))

# probabiliy of individual values of attribute..
print("-----probabiliy of individual values of attribute----------")
print("The Probabiliy of Red  ",ProbRed)
print("The Probabiliy of Yellow   ",ProbYellow)
print("The Probabiliy of Suv   ",ProbSuv)
print("The Probabiliy of Sports   ",ProbSports)
print("The Probabiliy of Domestic   ",ProbDomes)
print("The Probabiliy of Imported   ",ProbImported)
print("The Probabiliy of Yes   ",ProbYes)
print("The Probabiliy of No   ",ProbNo)



#print new Tuple for Classification..
print("-----print new Tuple for Classification----------")
print("X = { Color : Red , Type : SUV , Origin : Domestic} ")

#print class
print("----------print class---------------")

if ProbX_Yes > ProbX_No:
     print("Class is YES" )
else: print(" Class is NO ")




print("The Probability of X over Stolen = Yes is : ",ProbX_Yes)
print("The Probability of X over Stolen = No is : ",round(ProbX_No,3))











