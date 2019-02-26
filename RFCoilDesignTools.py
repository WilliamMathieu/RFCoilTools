# RF Coil Design Tool Functions
__author__ = "William Mathieu"
__copyright__ = "Copyright 2019, William Mathieu"
__license__ = "MIT"
__date__ = "26Feb2019"

from math import *
from decimal import *
import sys
import numpy as np
from tkinter import *



def LoopCapacitanceCalculator():
    # Calculates the segment capacitance needed to resonate the loop at a specific frequency
    mu_0 = 4*pi*10**(-7)
    f = float(0.0)
    L_loop = float(0.0)
    Cap_number = 1
    C_equiv = float(0.0)
    C_unit = float(0.0)
    
    def close_start_window():
        CapCal_window.quit()
        CapCal_window.destroy()

    def Calculate_With_User_Inputs():
        global f, L_loop, Cap_number, C_equiv, C_unit

        f = float(Set_LarmorFreq_entry.get())*10**(6)
        L_loop = float(Set_Lloop_entry.get())*10**(-9)
        Cap_number = float(Set_CapNum_entry.get())
        
        C_equiv = (4*pi**2*(L_loop)*f**2)**(-1)
        C_unit = C_equiv*Cap_number
        C_equiv = round(C_equiv/(10**(-12)), 2)
        C_unit = round(C_unit/(10**(-12)), 2)
        
        C_total_result.config(text="C_total = " + str(C_equiv) + " pF")
        C_unit_result.config(text="C_unit = " + str(C_unit) + " pF")
        
    CapCal_window = Tk()
    CapCal_window.title('Loop Capacitance Calculator')
    CapCal_window.config(bg='white')
    
    description = ("Calculate the Capacitance Needed in a Segmented Resonant Loop.\n"
                   "    INPUTS:\n"
                   "        f: Larmor frequency (MHz)\n"
                   "        L: Inductance of wire loop (nH)\n"
                   "        n: Number of loop capacitors\n"
                   "    OUTPUTS:\n"
                   "        C_equiv: Total loop capacitance needed for resonance at Larmor (pF)\n"
                   "        C_unit: Capacitance of each capacitor on the loop (pF)\n"
                   "    EQUATIONS:\n"
                   "                C_equiv = 1/(4*pi^2*L*f^2)\n"
                   "                C_unit = n*C_equiv")
    
    Description = Label(CapCal_window, text=description, bg='lightsteelblue', justify=LEFT)
    
    Set_LarmorFreq_label = Label(CapCal_window, text="Larmor Frequency in MHz:", bg='white')
    Set_LarmorFreq_entry = Entry(CapCal_window)
    
    Set_Lloop_label = Label(CapCal_window, text="Inductance of Wire Loop in nH:", bg='white')
    Set_Lloop_entry = Entry(CapCal_window)
    
    Set_CapNum_label = Label(CapCal_window, text="Number of Loop Capacitors:", bg='white')
    Set_CapNum_entry = Entry(CapCal_window)
    
    Save_button = Button(CapCal_window, text = "Calculate", bg='white', command=Calculate_With_User_Inputs, width = 60)
    #Start_button = Button(CapCal_window, text = "Exit", bg='white', command=close_start_window, width = 30)
    
    C_total_result = Label(CapCal_window, text="C_total = " + str(C_equiv) + " pF", bg='lightsteelblue')
    C_unit_result = Label(CapCal_window, text="C_unit = " + str(C_unit) + " pF", bg='lightsteelblue')
    
    Description.grid(sticky='we', row = 0, column = 0, columnspan = 2)
    Set_LarmorFreq_label.grid(sticky='e', row = 1, column = 0)
    Set_LarmorFreq_entry.grid(sticky='w', row = 1, column = 1)
    Set_Lloop_label.grid(sticky='e', row = 2, column = 0)
    Set_Lloop_entry.grid(sticky='w', row = 2, column = 1)
    Set_CapNum_label.grid(sticky='e', row = 3, column = 0)
    Set_CapNum_entry.grid(sticky='w', row = 3, column = 1)
    Save_button.grid(sticky='e', row = 4, column = 0, columnspan = 2)
    #Start_button.grid(sticky='w', row = 4, column = 1)
    C_total_result.grid(sticky='we', row = 5, column = 0, columnspan = 2)
    C_unit_result.grid(sticky='we', row = 6, column = 0, columnspan = 2)
    
    CapCal_window.mainloop()
    
def LoopInductanceCalculator():
    # Calculates the inductance of a conductive wire loop
    mu_0 = 4*pi*10**(-7)

    a = float(0.0)
    b = float(0.0)
    
    L = float(0.0)
    
    def close_window():
        LCal_window.quit()
        LCal_window.destroy()

    def Calculate_With_User_Inputs():
        global a, b, L

        a = ((float(Set_a_entry.get()))*10**(-3))/2
        b = ((float(Set_b_entry.get()))*10**(-3))/2
        
        L=b*mu_0*(log((8*b)/a)-2)
    
        L = round(L/(10**(-9)), 2)
        
        L_result.config(text="L = " + str(L) + " nH")

    LCal_window = Tk()
    LCal_window.title('Circular Wire Loop Inductance Calculator')
    LCal_window.config(bg='white')
    
    description = ("Calculate Circular Wire Loop Inductance \n"
                   "    INPUTS: \n"
                   "        a: Wire diameter (mm) \n"
                   "        b: Loop diameter (mm) \n"
                   "    OUTPUTS: \n"
                   "        L = Inductance value (nH) \n"
                   "    EQUATIONS:\n"
                   "                L=b*mu_0*(log((8*b)/a)-2)")
                   
    Description = Label(LCal_window, text=description, bg='lightsteelblue', justify=LEFT)
    
    Set_a_label = Label(LCal_window, text="Wire Diameter in mm:", bg='white')
    Set_a_entry = Entry(LCal_window)
    
    Set_b_label = Label(LCal_window, text="Loop Diameter in mm:", bg='white')
    Set_b_entry = Entry(LCal_window)
    
    Save_button = Button(LCal_window, text = "Calculate", bg='white', command=Calculate_With_User_Inputs, width = 60)
    #exit_button = Button(LCal_window, text = "Exit", bg='white', command=close_window, width = 30)
    
    L_result = Label(LCal_window, text="L = " + str(L) + " nH", bg='lightsteelblue')
    
    Description.grid(sticky='we', row = 0, column = 0, columnspan = 2)
    Set_a_label.grid(sticky='e', row = 1, column = 0)
    Set_a_entry.grid(sticky='w', row = 1, column = 1)
    Set_b_label.grid(sticky='e', row = 2, column = 0)
    Set_b_entry.grid(sticky='w', row = 2, column = 1)
    Save_button.grid(sticky='e', row = 3, column = 0, columnspan = 2)
    #exit_button.grid(sticky='w', row = 3, column = 1)
    L_result.grid(sticky='we', row = 4, column = 0, columnspan = 2)
   
    LCal_window.mainloop()
    
def TotalCapacitanceAndResonanceCalculator():
    # Calculates the total capacitance of the loop and its resonant frequency (range)
    mu = 4*pi*10**(-7);
    #f=123.25*10**6;
    CapNum = 0
    L_loop = 0.0
    C_tot = 0.0
    ResonantFrequency = 0.0
    
    def getCapNumANDLloop():
        global CapNum, L_loop
        return CapNum, L_loop
    def setVals_and_closeStartWindow():
        global CapNum, L_loop
        CapNum = int(Set_capnum_entry.get())
        L_loop = (float(Set_Lloop_entry.get()))*(10**(-9))
        start_window.quit()
        start_window.destroy()
    

    start_window = Tk()
    start_window.title('Parameters')
    start_window.config(bg='white')
    
    Set_capnum_label = Label(start_window, text="Enter the number of capacitors:", bg='white')
    Set_capnum_entry = Entry(start_window)
    Set_Lloop_label = Label(start_window, text="Inductance of wire loop in nH:", bg='white')
    Set_Lloop_entry = Entry(start_window)
    Next_button = Button(start_window, text = "Next", bg='white', command=setVals_and_closeStartWindow)
    
    Set_capnum_label.grid(sticky='we', row = 0, column = 0)
    Set_capnum_entry.grid(sticky='we', row = 0, column = 1)
    Set_Lloop_label.grid(sticky='we', row = 1, column = 0)
    Set_Lloop_entry.grid(sticky='we', row = 1, column = 1)
    Next_button.grid(sticky='we', row = 2, column = 0, columnspan=2)
    
    start_window.mainloop()
    
    num, L_loop = getCapNumANDLloop()
    
    #MAIN Window
    def getCapEntries():
        global cap_entries0
        return cap_entries0
    def setVals_and_closeWindow():
        global L_loop
        cap_entries = []
        for i in range(num):
            cap_entries.append((entries[i].get()))
        npa_cap_entries = np.asarray(cap_entries, dtype=np.float32)
        npa_cap_entries = npa_cap_entries*(10**(-12))
        Citot = 0.0
        for C in npa_cap_entries:
            Citot = Citot+(1/C)
        C_total = 1/Citot
        C_tot = round((1/Citot)/(10**(-12)), 2)

        ResonantFrequency = round((1/(2*pi*sqrt(C_total*L_loop)))/(10**6), 2)
        
        C_tot_result.config(text="C_total = " + str(C_tot) + " pF")
        ResonantFrequency_result.config(text="f = " + str(ResonantFrequency) + " MHz")
    
    caps_window = Tk()
    caps_window.title('Total Capacitance and Resonance Calculator')
    caps_window.config(bg='white')
    
    description = ("Calculate Total Capacitance of Series Capacitors and Resonant Frequency of Corresponding Loop \n"
                   "    INPUTS: \n"
                   "        n : Total number of series capacitors\n"
                   "        L: Inductance of wire loop (nH) \n"
                   "    OUTPUTS: \n"
                   "        C_total = Total capacitance (pF) \n"
                   "        f = Resonant frequency (MHz) \n"
                   "    EQUATIONS:\n"
                   "                f=1/(2*pi*sqrt(C_total*L)) \n"
                   "                C_total = 1/(1/C1+1/C2/+1/C3+...)")
    
    Description = Label(caps_window, text=description, bg='lightsteelblue', justify=LEFT)
    Description.grid(sticky='we', row = 0, column = 0, columnspan = 3)
    
    entries = []
    for n in range(num):
        # create left side info labels
        Label(caps_window, text="C%2d: " % n, bg='white').grid(sticky='e', row=n+1, column=0)
        Label(caps_window, text="pF", bg='white').grid(sticky='w', row=n+1, column=2)
        # create entries list
        entries.append(Entry(caps_window, bg='white', width=20))
        # grid layout the entries
        entries[n].grid(row=n+1, column=1)
        # create pF labels

    go_button = Button(caps_window, text = "Calculate", bg='white', command=setVals_and_closeWindow, width = 60)
    go_button.grid(sticky='we', row = num+2, column = 0, columnspan = 3)
    
    C_tot_result = Label(caps_window, text="C_total = " + str(C_tot) + " pF", bg='lightsteelblue')
    ResonantFrequency_result = Label(caps_window, text="f = " + str(ResonantFrequency) + " MHz", bg='lightsteelblue')
    C_tot_result.grid(sticky='we', row = num+3, column = 0, columnspan = 3)
    ResonantFrequency_result.grid(sticky='we', row = num+4, column = 0, columnspan = 3)
    caps_window.mainloop()