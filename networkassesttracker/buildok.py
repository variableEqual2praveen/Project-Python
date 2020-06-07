# import wmi
# import re 
# con = wmi.WMI()

# for i in con.Win32_BaseBoard():
#     serialnumb = i.SerialNumber
#     motherBoardBrand = i.Product
#     print("1",serialnumb)
#     data = (("serialnumber  {}  | motherBoardBrand  {} /n").format(serialnumb,motherBoardBrand))
#     with open("machinedetails.txt",'a') as fopen :
#         fopen.write(data)

# for os in con.Win32_Processor():
#     processorName = os.Name
#     corecount = os.NumberOfCores
#     data = ((" processorName -- {}   |   corecount -- {}").format(processorName,corecount))
#     with open("machinedetails.txt",'a') as fopen :
#         fopen.write(data)
# for bi in con.Win32_Bios():
#     print(bi.SerialNumber)
    
# # for p in con.Win32_MotherboardDevice() :
# #     print("SystemName --",p.SystemName)
# # p = con.Win32_LoggedOnUser

# # # print(p.Antecedent)
# # for p in con.Win32_LoggedOnUser() :
# #     print(p.Antecedent)


# # for process in con.Win32_Process(name='explorer.exe'):
# #     print (process.GetOwner())

# # for us in con.Win32_LogonSession():
# #     for user in us.references("Win32_LoggedOnUser"):
# #         print(user.Antecedent.Domain, user.Antecedent.Name, sep="\\")

# profiles = []
# lst2 = []
# for up in con.Win32_UserProfile():
#     profiles.append((up.LastUseTime, up.SID, up.LocalPath))
    


# for profile in profiles :
#     for pro in profile :
#         print(pro)
#         lst2.append(pro)
# print("this is a list",lst2)

# text = r"Users"
# for user in lst2 :
#     try:
#         if text in user :
#             print("Users",user[9:])
#     except TypeError as e:
#         pass


    
# import wmi
# import re 
# con = wmi.WMI(namespace='root/WMI')

# for i in con.Win32_DesktopMonitor() :
#     print(i)

import wmi
conn = wmi.WMI()

# convert uint16[] array to string
def cnvrt( tup ): 
    return ''.join( [chr( x ) if x else '' for x in tup] )

# this is 'universal' DesktopMonitor (no useful details for Generic PnP Monitor?)
for umn in conn.Win32_DesktopMonitor():
    print( 'UMn: Name             {}'.format( umn.Name ) )
    print( 'UMn: PNPDeviceID      {}'.format( umn.PNPDeviceID ) )

# this is 'specific' DesktopMonitor (all useful details?)
con2 =  wmi.WMI(namespace='root/WMI')
for mon in con2.WmiMonitorID():
    print( 'Mon: Active           {}'.format(        mon.Active ) )
    print( 'Mon: InstanceName     {}'.format(        mon.InstanceName ) )
    print( 'Mon: ManufacturerName {}'.format(cnvrt( mon.ManufacturerName ) ) )
    print( 'Mon: ProductCodeID    {}'.format(cnvrt( mon.ProductCodeID    ) ) )
    print( 'Mon: SerialNumberID   {}'.format(cnvrt( mon.SerialNumberID   ) ) )
    print( 'Mon: UserFriendlyName {}'.format(cnvrt( mon.UserFriendlyName ) ) )