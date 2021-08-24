from tkinter import *
from tkinter import Scale
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from termcolor import cprint ,colored
import pydicom
import pandas as pd
import os



 


        
   
print('Welcome to DTETool v1.1')
    

#Asking the user to choose input location

def filelocainput():
    global Data
    filelocationinput = filedialog.askopenfilename()
    Data = pydicom.dcmread(filelocationinput , force = True )
    if Data is None:
         Data = 1
         
   
    
    class CheckboxState():
     def cPID():
         if(CheckBoxPID.get(Data.PatientID)==1):
          Scale.config(state=ACTIVE)
         elif Data.PatientID.get() == 0:
          Scale.config(state=DISABLED)
    
  


    print('PatientID -',Data.PatientID)
    print('StudyID -',Data.StudyID)
    print('StudyDescription-',Data.StudyDescription)
    print('StudyDate -',Data.StudyDate)
    print('PatientName -' ,Data.PatientName)
    print('ScanOptions -' ,Data.ScanOptions)
    print('TotalCollimationWidth -',Data.TotalCollimationWidth)
    print('SeriesDescription',Data.SeriesDescription)
    print('SeriesNumber -',Data.SeriesNumber)
    print('PatientSex -' ,Data.PatientSex)
    print('SliceThickness -' ,Data.SliceThickness)
    print('ProtocolName -',Data.ProtocolName)
    print('BodyPartExamined -' ,Data.BodyPartExamined)
    print('Exposure -' ,Data.Exposure)
    print('FilterType - ' ,Data.FilterType)
    print('InstitutionAddress -',Data.InstitutionAddress)
    print('KVP -'  ,Data.KVP)
    print('ManufacturerModelName -' ,Data.ManufacturerModelName)
   

    


    df = pd.DataFrame ({
        
        
        
                        'PatientID ': [Data.PatientID],
                        'StudyID ': [Data.StudyID],
                        'StudyDescription':[Data.StudyDescription],
                        'StudyDate ': [Data.StudyDate],
                        'PatientName ': [Data.PatientName.given_name],
                        'ScanOptions': [Data.ScanOptions],
                        'TotalCollimationWidth': [str([Data.TotalCollimationWidth])],
                        'SeriesDescription':[Data.SeriesDescription],
                        'SeriesNumber':[Data.SeriesNumber.original_string],
                        'PatientSex' : [Data.PatientSex],
                        'SliceThickness' : [Data.SliceThickness.original_string],
                        'ProtocolName ' :[Data.ProtocolName],
                        'BodyPartExamined': [Data.BodyPartExamined],
                        'Exposure ' :[Data.Exposure.original_string],
                        'FilterType ':[Data.FilterType],
                        'InstitutionAddress':[Data.InstitutionAddress],
                        'KVP':[Data.KVP.original_string],
                        'ManufacturerModelName':[Data.ManufacturerModelName],
                        
                        

        })


     #Asking the user to choose output location   
    class filelocaoutput:
       def SaveDatatoxlsx():
           pass
       filelocaloutput = filedialog.asksaveasfilename(defaultextension = 'xlsx')
       df.to_excel (filelocaloutput)



  


       
root = Tk()
root.geometry("600x500")
Scallbtn = ttk.Button(root , text = 'Select All')
Scallbtn.place(y=450 , x=430)
Run_btn = ttk.Button(root, text='Run',command = filelocainput)
Run_btn.place(y=450, x=520)
# MainWindowbg = PhotoImage(file="BG.png")
# MainWindowbg_label = Label(root , image=MainWindowbg)
# MainWindowbg_label.place(y=0,x=0 , relwidth =1 , relheight=1)
CreatedBy = ttk.Label(root , text = 'Created By : Noam.Asulin@Philips.com')
CreatedBy.config(font=("Ariel", 7))
CreatedBy.place(y=450 , x=20)
PhilipsMedicalSystems = ttk.Label(root , text='Philips Medical Systems ')
PhilipsMedicalSystems.place(y=460 , x=20)
PhilipsMedicalSystems.config(font=("Ariel", 7))


     
cPID = IntVar()
CheckBoxPID = Checkbutton(root , 
                            text = 'PatientID',variable = cPID,
                            onvalue = 1 , offvalue = 0 , command=cPID,
                       )
CheckBoxPID.place(y=20 , x=20)






root.mainloop()
