#####Import####
import tkinter
from tkinter import *
from platform   import system as system_name  # Returns the system/OS name
import subprocess

def ping(host):
    si = subprocess.STARTUPINFO()
    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    command = 'ping' + ' -n' + ' 1' + ' ' +host
#    print("Executing "+command)
    result=subprocess.call(command, startupinfo=si)
#    print(result)
    return(result)
    # Pinging
mylist=['google.com','127.0.0.1','127.notaserver','21313123','facebook.com','yahoo.com']
reslist=[]
for i in mylist:
    if(ping(i)== 1):
        reslist.append(i+',')
	#with
#print(reslist)

root = tkinter.Tk()
iplist = tkinter.Label(root, text=reslist)
iplist.pack()
#####Extras#####
root.geometry("600x690")#The size of the box
root.wm_title("Scan result")#The name of it
root.mainloop()
