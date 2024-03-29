
import csv

import datetime

#initiating lists to put all the csv data in
ManuList=[]
PricesList=[]
ServiceList=[]

#This will be a simplier way to call the functions listed below
#The sort function will allow us to go into the document itself and append it to sort the list by alphabetical order
def file1(index): # Uses the def function to sort the items by Item_ID
    return index[0]

#Adding the data to the lists from each csv file
with open("ManufacturerList.csv") as manufacture:
    man = csv.reader(manufacture,delimiter=',')
    for line in man:
        ManuList.append(line)

sorted_ManuList = sorted(ManuList, key=file1)

with open("PriceList.csv") as PriceLists:
    price = csv.reader(PriceLists,delimiter=',')
    for line in price:
        PricesList.append(line)
sorted_PriceList = sorted(PricesList, key=file1)

with open("ServiceDatesList.csv") as Services:
    service = csv.reader(Services,delimiter=',')
    for line in service:
        ServiceList.append(line)
sorted_ServiceList = sorted(ServiceList, key=file1)

# we have to sort the list and place it in order of item id, manu name, item type, price, service date and list if it is damaged.
# Sorting will result in one list which can be broken down into seperate lists
# Below will allow the document to show the entire list

complete_manufacture = sorted_ManuList
for x in range(0, len(complete_manufacture)):
    complete_manufacture[x].insert(3,sorted_PriceList[x][1])
    complete_manufacture[x].insert(4,sorted_ServiceList[x][1])

product_inventory = []
product_type = []
#creating an empty set to add to full inventory file
for x in range(0, len(complete_manufacture[x][2])): #[2] is used as this is the next set of sorted items. Realized this after doing a bunch of them as [1]
    product_inventory.append(complete_manufacture[x][2])
for x in product_inventory:
    if x not in product_type:
        product_type.append(x) #This allows any duplicated item to be removed in the item list

# Next, we still need to sort the items by their specific item_ID, manufacture name(This list above), item type (The empty product list)
# price (from the price file and list), the service date (from the service list), and if the item is damaged

def orderedletters(letters):
    return letters[1]
# This begins the process of sorting them in ABC order as well as giving outputs

def fullinventory_output(complete_manufacture):
    Full_List = (sorted(complete_manufacture, key=orderedletters)) #Printing out the report in the sorted sections
    with open('FullInventory.csv', 'w') as Full_List_File:
        new_fullinventory = csv.writer(Full_List_File)
        for Inv in Full_List:
            new_fullinventory.writerow(Inv)

fullinventory_output(complete_manufacture)
#Changes the document to an ordered list with ID, Name and alphabetical order

# Next we need the laptop information and item ID and type through the LaptopInventory.csv file
# Each row in this file will be the same as the full inventory list file
# Item ID, Name, Price, Service date and if it is damaged

def ProductTypeInventory(complete_manufacture, product_type):
    product_list = complete_manufacture
    product = product_type
    laptop_list = []
    phone_list = []
    tower_list = []
#These are the empty brackets to allow the next file to appended
    for x in range(0, len(complete_manufacture)):
        if product_list[x][2] in product[0]:
            tower_list.append(product_list[x])

        elif product_list[x][2] in type[1]:
            phone_list.append(product_list[x])

        elif product_list[x][2] in type[2]:
            laptop_list.append(product_list[x])
#This takes all the files in the given csv files and appends them according
#To the report with limits that we have created earlier

with open('LaptopInventory.csv','w') as LaptopInventory_file:
    new_LaptopInventory = csv.writer(LaptopInventory_file)
    for inventory in laptop:
        new_LaptopInventory.writerow(inventory)
#This will be similar to below where we open up our newly created documents an adding more
#items into the original csv

with open('TowerInventory.csv', 'w') as TowerInventory_file:
    new_TowerInventory = csv.writer(TowerInventory_file)
    for inventory in TowerInventory_file:
        new_TowerInventory.writerow(inventory)

with open('PhoneInventory.csv', 'w') as PhoneInventory_file:
    new_PhoneInventory = csv.writer(PhoneInventory_file)
    for inventory in PhoneInventory_file:
        new_PhoneInventory.writerow(inventory)

ProductTypeInventory(complete_manufacture, product_type)

#Next we have to order the past serviced date items, this row should contain the same
#as the items in the prior files, however, these dates will appear in the date of oldest to newest
#Keeping in mind for these files we will still be using complete_manufacture and our new sorted_ServiceList

#This report is the final list in the fullinventory file
def Past_Service_Items(complete_manufature,sorted_ServiceList):
    Servicedate_1 = []
    Servicedate_2 = []
    Servicedate_3 = []
    now = datetime.datetime.now()
    for key in complete_manufature:
        Givendate = key[4]
        firstdate = datetime.datetime.strptime(Givendate,'%m/%d/%Y') #strptime allows for the date time format to be changed
        if Givendate < now:
            Servicedate_1.append(key)
        elif Givendate > now:
            Servicedate_2.append(key)

    past_servicedate_list = Servicedate_1 + Servicedate_2

    with open('PastServiceDateInventory.csv', 'w') as pastdate_file:
        new_Givendate = csv.writer(pastdate_file)
        for inventory in past_servicedate_list:
            new_Givendate.writerow(inventory)
#This set is the same as above as we are simply editing the document in order for it to show a

Past_Service_Items(complete_manufacture,sorted_ServiceList)

#Now onto the damaged, when the damaged innventory is opened we will only see one or two items
#our job is to get that list and put it into the main inventory list

def damaged_goods(bad_items):
    return bad_items[3]
def damagedproductlist(complete_manufacture):
    damaged_list = []
    damaged_delete = []
    for x in range(0, len(complete_manufacture)): #This will delete any items that are damaged
        if complete_manufacture[x][-1] == 'damage':
            damaged_list.append(complete_manufacture[x])

    with open('DamagedInventory.csv','w') as Damaged_file:
        new_Damaged_file = csv.writer(Damaged_file)
        for key in damaged_list:
            new_Damaged_file.writerow(key)

damaged_goods(complete_manufacture)
#This is now a complete alter of the original document
    
