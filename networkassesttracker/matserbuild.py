import wmi
import re 
con = wmi.WMI("192.168.225.117", user=r"192.168.225.117\admin", password="admin01")   #FILL WITH THE REMOTE MACHINE NAME 
#vm1 = "192.168.225.90",user=r'admin',password='admin01'
###serialnumber && motherBoardBrand ###
for i in con.Win32_BaseBoard():
    serialnumb = i.SerialNumber
    motherBoardBrand = i.Product
    print("1",serialnumb)
    data = (("serialnumber  {}  | motherBoardBrand  {} /n").format(serialnumb,motherBoardBrand))
    with open("machinedetails.txt",'a') as fopen :
        fopen.write(data)

###processorName & corecount###
for os in con.Win32_Processor():
    processorName = os.Name
    corecount = os.NumberOfCores
    data = ((" processorName -- {}   |   corecount -- {}").format(processorName,corecount))
    with open("machinedetails.txt",'a') as fopen :
        fopen.write(data)
for bi in con.Win32_Bios():
    print(bi.SerialNumber)

###extract the no .of users
profiles = []
lst2 = []
for up in con.Win32_UserProfile():
    profiles.append((up.LastUseTime, up.SID, up.LocalPath))

for profile in profiles :
    for pro in profile :
        # print(pro)
        lst2.append(pro)
text = r"Users"
for user in lst2 :
    try:
        if text in user :
            print("Users",user[9:])
    except TypeError as e:
        pass
    
###machine name###
for p in con.Win32_MotherboardDevice() :
    print("Machine Name --",p.SystemName)
p = con.Win32_LoggedOnUser


