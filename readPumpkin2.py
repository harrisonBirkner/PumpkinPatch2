#Read in data and display

#import
import datetime


#Globals Definitions
pumpkinFile = ''
cPctr = 0
cLctr = 0
oDate = ''
GtQuantity = 0
GtStoreCost = 0
MjQuantity = 0
MjStoreCost = 0
hStoreName = ""
iStoreName = ""

def main():
    global hStoreName
    iRec, iStoreName, hStoreName = init()
    while iRec !="":
        if hStoreName != iStoreName: #check for control break
            majorSubtotals(MjStoreCost, hStoreName, cLctr)
        MjQuantity, MjStoreCost, cStoreCost = calcs(iRec)
        output(iRec,cStoreCost,cLctr)
        iRec = read()
    closing()

def closing():
    majorSubtotals(MjStoreCost, hStoreName, cLctr)
    print()
    print(format("","1s"),"Grand Totals",format("","26s"),format(GtQuantity,'6,d'), format("","20s"),format(GtStoreCost,'10,.2f'))
    pumpkinFile.close()

def output(iRec,cStoreCost,cLctr):
    global hStoreName
    iStoreName = iRec[0:10]
    if iStoreName != hStoreName:
        hStoreName = iStoreName
    iPatchID = iRec[10:11]
    iQuantity = iRec[11:14]
    iPrice = iRec[14:19]
    if iPatchID =="N":
        iPatchID = "North"
    elif iPatchID =="S":
        iPatchID ="Skunk Creek"
    else:
        iPatchID ="Back 40"
    oQuantity = int(iQuantity)
    oPrice = float(iPrice)
    print(format(iStoreName,"18s"),format(iPatchID,"25s"),format(oQuantity,"3d"),format(" ", "9s"),
          format(oPrice,'4.2f'),format(" ", "7s"),(f'{cStoreCost:>8,.2f}')) 
    print()
    cLctr = cLctr + 1
    if cLctr >=50:
        headings()
    return iStoreName
 

def calcs(iRec): #calculate store cost, major quantity, major cost
    global MjQuantity
    global MjStoreCost
    quantity = iRec[11:14]
    cQuantity = int(quantity)
    MjQuantity = MjQuantity + cQuantity
    cost = float(iRec[14:19])
    MjStoreCost = MjStoreCost + (cQuantity * cost)
    cStoreCost = cQuantity * cost
    return MjQuantity, MjStoreCost, cStoreCost

#move and print major subtotals, add to totals(counters and accumulators),
#zero out major counters and accumulators, move break field to hold field
def majorSubtotals(MjStoreCost, hStoreName, cLctr):
    global GtQuantity
    global GtStoreCost
    global MjQuantity
    print(format(hStoreName,"12s"),format("","1s"),"SUBTOTALS",format("","16s"),format(MjQuantity,"6,d"),format("","22s"),format(MjStoreCost,"8,.2f"))
    print()
    cLctr = cLctr + 2
    if cLctr >=50:
        headings()
    GtQuantity = GtQuantity + MjQuantity
    GtStoreCost = GtStoreCost + MjStoreCost
    MjQuantity = 0
    MjStoreCost = 0
    hStoreName = iStoreName


def init():
    global oDate
    global pumpkinFile
    global hStoreName
    global iStorename
    try:
        pumpkinFile = open(r'pumpkinData\pumpkin.dat','r')
    except IOError:
        print("File error.  Program terminated")
        exit(0)
    oDate = datetime.datetime.today().strftime('%m/%d/%Y')
    cLctr = headings()
    iRec = read()
    hStoreName = iStoreName #move break field to hold field
    return iRec, iStoreName, hStoreName

def headings():
    global oDate
    global cPctr
    global cLctr
    cPctr = cPctr + 1
    oDate = datetime.datetime.today().strftime('%m/%d/%Y')
    print("    0         1         2         3          4         5         6         7")
    print("12345678901234567890123456789012345678901234567890123456789012345678901234567890")
    print("DATE:",oDate, format(" ","11s"), "GREAT PUMPKIN RANCH", format(" ","21s"), "PAGE:", format(cPctr,"3d"))
    print(format(" ","32s"),"SALES REPORT")
    print()
    print("STORE NAME", format(" ","7s"), "PATCH NAME",format(" ","9s"),"QUANTITY",
         format(" ","8s"),"PRICE", format(" ","5s"),"STORE COST")
    print()
    cLctr = 5
    return cLctr

def read():
    iRec = pumpkinFile.readline()
    return iRec

main()