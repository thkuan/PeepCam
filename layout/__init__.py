# -*- coding: utf-8 -*-
from Tkinter import *
class peepCamLayout(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        objLvl = 0
#remote ip field
        self.rmtIpLbl = Label(self)
        self.rmtIpLbl["text"] = "Remote  IP"
        self.rmtIpLbl.grid(row=objLvl, column=0)
        self.rmtIpField = Entry(self)
        self.rmtIpField["width"] = 50
        self.rmtIpField.grid(row=objLvl, column=1, columnspan=6)
        objLvl += 1

#host ip field
        self.hostIpLbl = Label(self)
        self.hostIpLbl["text"] = "Host IP"
        self.hostIpLbl.grid(row=objLvl, column=0)
        self.hostIpField = Entry(self)
        self.hostIpField["width"] = 50
        self.hostIpField.grid(row=objLvl, column=1, columnspan=6)
        objLvl += 1
#capture snapshotsCapture Snapshots
        self.capBut = Button(self)
        self.capBut["text"] = "Capture Snapshots"
        self.capBut.grid(row=objLvl, column=0, columnspan=3)
#starts video recording
        self.recBut = Button(self)
        self.recBut["text"] = "Record video"
        self.recBut.grid(row=objLvl, column=3, columnspan=3)
        objLvl += 1
#network state
        self.netStatLbl = Label(self)
        self.netStatLbl["text"] = "Network State"
        self.netStatLbl.grid(row=objLvl, column=0)
        self.netStatField = Entry(self)
        self.netStatField["width"] = 30
        self.netStatField.grid(row=objLvl, column=1, columnspan=3)
        objLvl += 1
#File Saved Directory
        self.directoryRouteLbl = Label(self)
        self.directoryRouteLbl["text"] = "File Directory"
        self.directoryRouteLbl.grid(row=objLvl, column=0)
        self.directoryRouteField = Entry(self)
        self.directoryRouteField["width"] = 60
        self.directoryRouteField.grid(row=objLvl, column=1, columnspan=6)
        objLvl += 1
#remote file list
        self.rmtFileLbl = Label(self)
        self.rmtFileLbl["text"] = "Remote File List"
        self.rmtFileLbl.grid(row=objLvl, column=0, columnspan=6)
        objLvl += 1
        self.rmtFileLstBox = Listbox(self)
        self.rmtFileLstBox.grid(row=objLvl, column=0, columnspan=6)
        objLvl += 1
#transfering file list
        self.tsfFileLbl = Label(self)
        self.tsfFileLbl["text"] = "Remote File List"
        self.tsfFileLbl.grid(row=objLvl, column=0, columnspan=6)
        objLvl += 1
        self.tsfFileLstBox = Listbox(self)
        self.tsfFileLstBox.grid(row=objLvl, column=0, columnspan=6)
        objLvl += 1
#Log List
        self.logLbl = Label(self)
        self.logLbl["text"] = "Remote File List"
        self.logLbl.grid(row=objLvl, column=0, columnspan=6)
        objLvl += 1
        self.logLstBox = Listbox(self)
        self.logLstBox.grid(row=objLvl, column=0, columnspan=6)


if __name__ == '__main__':
    root = Tk()
    root.title("PeepCam")
    app = peepCamLayout(master=root)
    app.mainloop()

