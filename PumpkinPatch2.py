#You are on the Great Pumpkin Ranch and your job is to create 
#a report of the sales to the stores in time for Halloween.  
#You are to create a program to create the report requested.



def main():
    moreData = "y"
    pumpkinFile = init()
    while(moreData == 'y'):
        iStoreName = getStoreName()
        iPatchID = getPatchID()
        iQuantity = getQuantity()
        iPrice = getPrice()
        output(iStoreName,iPatchID,iQuantity,iPrice, pumpkinFile)
        moreData = input("Would you like to enter another order? y/n: ")
    closing(pumpkinFile)

def closing(pumpkinFile):
    pumpkinFile.close()

def output(iStoreName, iPatchID, iQuantity,iPrice, pumpkinFile):
    pumpkinFile.write(format(iStoreName, '10s') +
                      format(iPatchID, '1s') + 
                      format(iQuantity, '03d')+
                      format(iPrice, '0.2f') + "\n")

def getPrice():
    valid = False
    while not valid:
        try:
            iPrice = float(input("Enter the price per each: "))
            if iPrice > 0 and iPrice < 10:
                valid = True
            else:
                print("Error - Enter a valid price greater than 0 and less than 10: ")
        except:
            print("Error - Enter a valid price greater than 0 and less than 10: ")
    return iPrice

def getQuantity():
    valid = False
    while not valid:
        iQuantity = int(input("Enter the number of pumpkins purchased: "))
        if iQuantity > 0:
            valid = True
        else:
            print("Enter a valid quantity greater than 0: ")
    return iQuantity

def getPatchID():
    valid = False
    while not valid:
        iPatchID = input("Enter the character for Patch ID: N - North, S - Skunk Creek, B - Back 40""Enter Patch ID: ")
        iPatchID = iPatchID.strip()
        x = len(iPatchID)
        if x == 1:
            valid = True
        else:
            print("A valid Patch ID is required")
    return iPatchID

def getStoreName():
    valid = False
    while not valid:
        iStoreName = input("Enter store name: ")
        iStoreName = iStoreName.strip()
        if len(iStoreName) > 0:
            valid = True
        else:
            print("Error - store name is required")
    return iStoreName

def init():
    pumpkinFile = open(r'pumpkinData\pumpkin.dat','a')
    return pumpkinFile

main()