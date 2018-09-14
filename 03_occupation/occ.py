#Team moBin -- Robin Han & Mohtasim Howlader
#SoftDev1 pd08
#K06 -- Stl/O: Divine your Destiny!
#2018-09-13 

import csv
import random
def chooseOccupation(d):
        #variable to match occupation with its respective weight
        i = 0
        occ = d.keys()
        weights = d.values()
        total = sum(weights)
        # generating a random number float from 0 to the total sum of the weights
        randWeight = float(random.randrange(0,total*100))/100

        for weight in weights:
                #choosing the occupation if the randWeight created lies between the range of its weight.
                randWeight -= weight
                if randWeight <= 0:
                        break
                i+=1

        return occ[i]
        
def main():
        # initialize dictionary 
        d = {}
	with open("occupations.csv") as csv_file:
		reader = csv.reader(csv_file)
                # eliminates first row of csv file
                next(reader)
                # loops through each row of csv file
                for row in reader:
                        # checks to see that the total isn't added to the dictionary
                        if row[0] != "Total":
                                d[row[0]] = float(row[1])
                        
        print(chooseOccupation(d))
                
main()
