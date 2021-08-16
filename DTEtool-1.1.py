# -*- coding: utf-8 -*-
"""
DTETool v1.1
This tool is for internal use only
The tool can pull out DICOM tag fileds and save them to xlsx file .
"""
#Imported packages


from tkinter import *
import tkinter as tk
from tkinter import filedialog
from termcolor import cprint ,colored
import pydicom
import pandas as pd
import time
import os 


class gettingDataFromDICOM:
    def DICOMData(dcmread):
        pass
    #Asking the user to choose input location
    print('Welcome to DTETool v1.1')
    

def filelocainput():
    filelocationinput = filedialog.askopenfilename()
    Data = pydicom.dcmread(filelocationinput , force = True )



    print('PatientID -',Data.PatientID)
    print('StudyID -',Data.StudyID)
    print('StudyDescription-',Data.StudyDescription)
    print('StudyDate -',Data.StudyDate)
    print('PatientName -' ,Data.PatientName)
    print('ScanOptions -' ,Data.ScanOptions)
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



              

    df = pd.DataFrame ({'PatientID ': [Data.PatientID],
                        'StudyID ': [Data.StudyID],
                        'StudyDescription':[Data.StudyDescription],
                        'StudyDate ': [Data.StudyDate],
                        'PatientName ': [Data.PatientName.given_name],
                        'ScanOptions': [Data.ScanOptions],
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


        
    class filelocaoutput:
       def SaveDatatoxlsx():
           pass
    df.to_excel ('Param.xlsx')



    cprint('xlsx file was saved secussfully', 'yellow')

time.sleep(5)

root = Tk('DTETool')
root.geometry("400x100")
title=Label(root, text='DTETool v1.1',font=('',12))
title.pack(side=TOP)
# wnp=tk.Label(root, text='Done!',font=('',10))
# wnp.place(y=70, x=250)
browse = Button(root, text='Browse',command = filelocainput)
browse.place(y=30, x=170)
# run = Button(root, text='Run')
# run.place(y=70 , x=180)
# browseBox = Entry(root)
# browseBox.place(y=50 , x=50)
root.mainloop()




#