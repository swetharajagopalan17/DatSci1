"""
QUESTION 1: Which car brands have the most gas-operated cars? Which car brands have the least? Represent the number of gas and diesel-operated cars for each brand on a bar graph.
REASON: Greenhouse gas emissions from automobiles is a major cause of global warming. Compared to diesel, gas is a more environmentally-friendly fuel because it releases fewer and less harmful emissions.
I chose this question so that I could analyze which car brands use what proportion of a more environmentally-friendly fuel (gas in this case). This can help people make better choices when they buy cars.
FINDINGS: From the bar graph, we can see that Toyota has the most gas-operated cars (29) and Mercury has the least gas-operated cars (1). We also see that Chevrolet has the most diesel-operated cars (5)
and BMW and Isuzu have the least diesel-operated cars (1). 
"""
def carbrand_gas():
    import matplotlib.pyplot as plot
    import numpy as numpy
    
    f = open("automobile.csv","r")
    data = f.readlines()
    f.close()
    mydict = {}
    mydict2 = {}
    for dataline in data:
        pieces = dataline.split(",")
        if pieces[3] == "gas" and pieces[2] not in mydict:
            mydict[pieces[2]] = 1
        elif pieces[3] == "gas" and pieces[2] in mydict:
            mydict[pieces[2]] += 1
        if pieces[3] == "diesel" and pieces[2] not in mydict2:
            mydict2[pieces[2]] = 1
        elif pieces[3] == "diesel" and pieces[2] in mydict2:
            mydict2[pieces[2]] += 1

    brand1 = []
    num1 = []
    brand2 = []
    num2 = []
    
    for brand,val in mydict.items():
        brand1.append(brand)
        num1.append(val)

    for brand,val in mydict2.items():
        brand2.append(brand)
        num2.append(val)
        
    
    index = numpy.arange(len(brand1))
    index2 = numpy.arange(len(brand2))
    
    g1 = plot.bar(index + 0.00, num1, color = "purple", width = 0.3, label = "Gas-operated cars")
    plot.xlabel("CAR BRAND", fontsize = 5)
    plot.ylabel("NUMBER OF CARS", fontsize = 5)
    plot.xticks(index,brand1, fontsize = 5, rotation = 35)
    plot.title("Graph showing number of\n gas-operated cars for each brand", color = "black")
    plot.show()
carbrand_gas()


        
