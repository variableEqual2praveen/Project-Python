wmi in python is library file which in windows default 
toolkit which used to extract the wmic information like 
serialnumber , GPU model , Hardware spec ,Processor details 
And most importantly used to fetch remote windows clients wmi 
information

wmi libray provides plenty of classes , in which the fuctions are
used to do so.

step 1 :

intall the wmi package 

pip install wmi 


step 2 : the script can only run by the  administators

the administators must be the part of  WMI user and wmi remote should be enabled .


enabling Remote WMI for a domain user

This process allows a domain user to access WMI information remotely via a script.
This domain account will  have no other access to the servers.

In Computer Management, expand Services and Applications:
 
Right-Click WMI Control and select Properties:
 
Select the security tab, Expand Root, and select CIMV2. Click the Security button.
Click Add… and add the WMI user.
 
Highlight the WMI user, and click “Remote Enable”
 
Click OK Twice, and close Computer Management


Open a command prompt, and enable remote WMI through the firewall:
netsh firewall set service RemoteAdmin enable <enter>


Open DCOM Configuration by typing dcomcnfg at the command prompt, and hitting enter:
 
Expand “Component Services”
Expand “Computers”
Right-Click “My Computer” and select Properties.
Select the “Com Security” tab:
 
Click “Edit Limits…” under the “Launch and Activation Permissions” section (the 2nd “edit limits” button from the top):
 
Add the WMI user and give that account the “Remote Activation” permission:
 
Click OK twice and close the “Component Services” window.

Exit your command prompt, and the system is configured for remote WMI access for the WMI user, which is a Domain User account.




now run the py script as administator 
