__author__ = "William Mathieu"
__copyright__ = "Copyright 2019, William Mathieu"
__license__ = "MIT"
__date__ = "19Feb2019"

from RFCoilDesignTools import *

print("\
===============================================================================================\n\
PRESS 1 AND ENTER TO: \n\
  Calculate Circular Wire Loop Inductance \n\
      INPUTS: \n\
          Loop diameter (mm) \n\
          Wire diameter (mm) \n\
      OUTPUTS: \n\
          Inductance value (nH) \n\
\n\
PRESS 2 AND ENTER TO: \n\
  Calculate Capacitance Needed for Segmented Resonant Loop \n\
      INPUTS: \n\
          Larmor frequency (MHz) \n\
          Inductance of wire loop (nH) \n\
          Number of loop capacitors \n\
      OUTPUTS: \n\
          Total loop capacitance needed for resonance at Larmor (pF) \n\
          Capacitance of each capacitor on the loop (pF) \n\
\n\
PRESS 3 AND ENTER TO: \n\
  Calculate Total Capacitance of Series Capacitors and Resonant Frequency of Corresponding Loop\n\
      INPUTS: \n\
          Inductance of wire loop (nH) \n\
      OUTPUTS: \n\
          Total capacitance (pF) \n\
          Resonant frequency (MHz)\n\
===============================================================================================\n\
")

enteredinput = input()

if enteredinput == '2':
    LoopCapacitanceCalculator()
elif enteredinput == '1':
    LoopInductanceCalculator()
elif enteredinput == '3':
    TotalCapacitanceAndResonanceCalculator()
else:
    print('Bye.')
    
