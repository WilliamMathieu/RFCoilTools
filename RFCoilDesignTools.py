# RF Coil Design Tool Functions
__author__ = "William Mathieu"
__copyright__ = "Copyright 2019, William Mathieu"
__license__ = "MIT"
__date__ = "14Feb2019"

from math import *
from decimal import *
import sys
import numpy as np

def LoopCapacitanceCalculator():
    # Calculates the segment capacitance needed to resonate the loop at a 
    # specific frequency
    mu_0 = 4*pi*10**(-7)
    
    f = (float(input("Larmor Frequency in MHz: ")))*10**(6)
    
    L_loop = (float(input("Inductance of Wire Loop in nH: ")))*10**(-9)
    
    Cap_number = (float(input("Number of Loop Capacitors: ")))
    
    C_equiv = (4*pi**2*(L_loop)*f**2)**(-1)
    
    C_unit = C_equiv*Cap_number
    
    C_equiv = round(C_equiv/(10**(-12)), 2)
    print("C_total = " + str(C_equiv) + " pF")
    
    C_unit = round(C_unit/(10**(-12)), 2)
    print("C_unit = " + str(C_unit) + " pF")
    
    #  Exit method depending on python version
    if (sys.version_info > (3, 0)):
        input()
    else:
        raw_input()
    
def LoopInductanceCalculator():
    # Calculates the inductance of a conductive wire loop
    mu_0 = 4*pi*10**(-7)
    
    b = ((float(input("Loop Diameter in mm: ")))*10**(-3))/2
    
    a = ((float(input("Wire Diameter in mm: ")))*10**(-3))/2
    
    L=b*mu_0*(log((8*b)/a)-2)
    
    L = round(L/(10**(-9)), 2)
    print("L = " + str(L) + " nH")
    
    #  Exit method depending on python version
    if (sys.version_info > (3, 0)):
        input()
    else:
        raw_input()

def TotalCapacitanceAndResonanceCalculator():
    # Calculates the total capacitance of the loop and its resonant frequency (range)
    mu = 4*pi*10**(-7);
    f=123.25*10**6;

    #C1 = 3.5e-12:0.5e-12:27e-12;

    CapVals = list()
    num = input("Enter the number of capacitors:")
    print("Enter capacitor values in pF: ")
    for i in range(int(num)):
        n = input("C%d: "%(i))
        CapVals.append(float(n))
    print('Caps: ', CapVals)
    
    CapVals = np.asarray(CapVals)

    CapVals = CapVals*10**(-12)
    L_loop = (float(input("Inductance of Wire Loop in nH: ")))*10**(-9)
    Citot = 0.0
    for C in CapVals:
        Citot = Citot+(1/C)
    C_total = 1/Citot
    C_tot = round((1/Citot)/(10**(-12)), 2)
    print("C_total = " + str(C_tot) + " pF")


    ResonantFrequency = round((1/(2*pi*sqrt(C_total*L_loop)))/(10**6), 2)
    print("f = " + str(ResonantFrequency) + " MHz")
    #figure
    #plot(PeakFreqs./10^6,C1*10^12)
    #ylim([3.5 27])
    #vline(123.25,'k')
    #ylabel('Variable Capacitor (pF)')
    #xlabel('Peak Frequency (MHz)')

    #nums = [0, 1, 2, 3, 4]
    #squares = []
    #for x in nums:
    #    squares.append(x ** 2)
    #print(squares)

