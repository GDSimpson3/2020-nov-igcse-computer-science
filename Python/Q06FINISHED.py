#   Q6

#   Structure of sales record is
#   StaffID, First name, Last name, January sales, February sales,
#   March sales, April sales, May sales, June sales

staffSales = [
["101TGY" , "George" , "Taylor" , 6009 , 5262 , 3745 , 7075 , 1943 , 4432], # 28466
["103FCY" , "Fehlix" , "Chayne" , 8717 , 2521 , 5777 , 6189 , 5089 , 6957], # 2
["102SBY" , "Sumren" , "Bergen" , 5012 , 1063 , 7937 , 9560 , 1115 , 5499],
["104SBK" , "Samira" , "Beckle" , 1140 , 9206 , 3898 , 8544 , 5937 , 8705], # 1
["105NBT" , "Nellie" , "Bogart" , 3017 , 3342 , 5939 , 2479 , 3374 , 2297],
["106CGT" , "Cheryl" , "Grouth" , 9620 , 7160 , 5113 , 4803 , 5492 , 2195],
["107DGT" , "Danuta" , "Graunt" , 1583 , 7450 , 1026 , 7463 , 2390 , 6509],
["108JDN" , "Jaiden" , "Deckle" , 4064 , 4978 , 2984 , 3159 , 1464 , 4858],
["109JCK" , "Jimran" , "Caliks" , 6253 , 7962 , 2732 , 7504 , 2771 , 5193],
["110DDN" , "Deynar" , "Derran" , 6305 , 8817 , 5200 , 3647 , 3365 , 1256]]


#--------------------------------------------------------------------------
#   Write your code below this line
def totalSalesMadeByEachMember(dataset):
    for i in dataset:
        # totalSale = i[3] + i[4] + i[5] + i[6] + i[7] + i[8]
        totalSale = 0
        for month in range (3, len(i)):
            totalSale = totalSale + i[month]

        print(f"{i[0]}--{i[1]} {i[2]} made {totalSale} sales")

def totalSalesbyWholeTeam(dataset):
    totalSale = 0
    for i in dataset:
        individualSale = 0
        for month in range (3, len(i)):
            individualSale = individualSale + i[month]
        totalSale = totalSale + individualSale
    print(f"Total sales made by team: {totalSale}")

def topTwo(dataset):
    first = 0;
    seccond= 0;

    for i in dataset:

        individualSale = 0
        for month in range (3, len(i)):
            individualSale = individualSale + i[month]

        positionArray = [i,[individualSale]]
        if(first == 0):
            first = positionArray
        elif (seccond == 0):
            seccond = positionArray
        elif (first[1][0] < individualSale):
            first = positionArray
        elif (seccond[1][0] < individualSale):
            seccond = positionArray
    print(first[0][0])
    print(seccond[0][0])



totalSalesMadeByEachMember(staffSales)
totalSalesbyWholeTeam(staffSales)
topTwo(staffSales)
