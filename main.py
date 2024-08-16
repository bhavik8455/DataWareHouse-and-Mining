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

# Color =Red TYPE =SUV ORIGIN =Domestic STOLEN =Yes

#Calculated Probability of Stolen=Yes and Color=Red
ProbYesRed = len([row for row in data if row[1] == 'Red' and row[4] == 'Yes'])/len([row for row in data if row[1]=='Red'])
ProbRed= len([row for row in data if row[1] == 'Red'])/len(data)
ProbYes= len([row for row in data if row[4]=='Yes'])/len(data)

ProbRed_Yes = ProbYesRed*ProbRed/ProbYes

#Calculated Probability of Stolen=Yes and Tpe=SUV
ProbYesSuv = len([row for row in data if row[2]=='Suv' and row[4]=='Yes'])/len([row for row in data if row[2]=='Suv'])
ProbSuv = len([row for row in data if row[2]=='Suv'])/len(data)

ProbSuv_Yes = ProbYesSuv*ProbSuv/ProbYes


#Calculated Probability of Stolen=Yes and Origin=Domestic
ProbDomesYes = len([row for row in data if row[3]=='Domestic' and row[4]=='Yes'])/len([row for row in data if row[3]=='Domestic'])
ProbDomes = len([row for row in data if row[3]=='Domestic'])/len(data)

ProbDom_Yes = ProbDomesYes*ProbDomes/ProbYes

#Calculated Probability of Stolen=Yes Over X = {(Color="Red", Type="SUV"; and Origin="Domestic") }
ProbX_Yes = ProbRed_Yes * ProbSuv_Yes * ProbDom_Yes

print("The Probability of X over Stolen = Yes is : ",ProbX_Yes)






