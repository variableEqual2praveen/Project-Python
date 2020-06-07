import wmi

con = wmi.WMI("192.168.225.61",user=r"admin", password="admin01")
#
lst = []


for i in con.Win32_BaseBoard():
  
      
      
	serialnumb = i.SerialNumber
	motherBoardBrand = i.Product
	lst.append(serialnumb)
	lst.append(motherBoardBrand)
 
  data = (("serialnumb  {}  | motherBoardBrand  {}").format(serialnumb,motherBoardBrand))
  with open("machinedetails.txt",'a') as fopen :
    fopen.write(data)
	print(i)

for os in con.Win32_Processor():
    
    
processorName = os.Name
corecount = os.NumberOfCores
lst.append(processorName)
lst.append(corecount)
data = (("{}   {}").format(processorName,corecount))
with open("machinedetails.txt",'a') as fopen :
  fopen.write(data)
print(os)

 


  # for i in lst:
	  
    
    

 
 
 
 
 
 
# for os in con.Win32_MotherboardDevice():
#     print(os)

# for os in con.Win32_BaseBoard():
#     print(os)

# for os in con.Win32_Processor():
#     print(os)
    
    
# print(con.CIM_MonitorResolution())
# for serialno in con.Win32_MotherboardDevice() :
#     print(serialno.SystemName)




# for os in con.Win32_OperatingSystem():
#     print( 'OS : ' + os.Caption + ", version " + os.Version )
# for pr in con.Win32_Processor():
#     print( 'CPU: ' + pr.Name )
# for vc in con.Win32_VideoController():
#     print( 'GPU: ' + vc.Name + "\r\n     " + vc.PNPDeviceID )


# for disk in con.Win32_LogicalDisk(["Caption", "Description"], DriveType=3):
#     print (disk)
