__author__ = "William Mathieu"
__copyright__ = "Copyright 2019, William Mathieu"
__license__ = "MIT"
__date__ = "19Feb2019"

from RFCoilDesignTools import *
from RFCoilEvaluationTools import *
from tkinter import *

def start_LoopCapacitanceCalculator():
    LoopCapacitanceCalculator()
def start_LoopInductanceCalculator():
    LoopInductanceCalculator()
def start_TotalCapacitanceAndResonanceCalculator():
    TotalCapacitanceAndResonanceCalculator()
def start_SNRHeatmapGenerator():
    SNRHeatmapGenerator()

def Close_start_window():
    main_menu.quit()
    main_menu.destroy()

main_menu = Tk()
main_menu.title('RF Coil Design and Evaluation Tools')
main_menu.config(bg='lightskyblue')

LoopCapacitanceCalculator_button = Button(main_menu, text = "LoopCapacitanceCalculator", bg='white', command=start_LoopCapacitanceCalculator)
LoopInductanceCalculator_button = Button(main_menu, text = "LoopInductanceCalculator", bg='white', command=start_LoopInductanceCalculator)
TotalCapacitanceAndResonanceCalculator_button = Button(main_menu, text = "TotalCapacitanceAndResonanceCalculator", bg='white', command=start_TotalCapacitanceAndResonanceCalculator)
SNRHeatmapGenerator_button = Button(main_menu, text = "SNR Heatmap Generator", bg='white', command=start_SNRHeatmapGenerator)
blank_space = Label(main_menu, text="          ", bg='white')
DesignTitle = Label(main_menu, text="Design", bg='white')
EvaluateTitle = Label(main_menu, text="Evaluate", bg='white')
Close_start_menu = Button(main_menu, text = "GO!", bg='white', command=Close_main_menu)

DesignTitle.grid(sticky='n', row = 0, column = 0)
LoopCapacitanceCalculator_button.grid(sticky='n', row = 1, column = 0)
LoopInductanceCalculator_button.grid(sticky='n', row = 2, column = 0)
TotalCapacitanceAndResonanceCalculator_button.grid(sticky='n', row = 3, column = 0)
blank_space.grid(sticky='n', row = 4, column = 0)
Close_start_menu.grid(sticky='n', row = 5, column = 0)

EvaluateTitle.grid(sticky='n', row = 0, column = 1)
SNRHeatmapGenerator_button.grid(sticky='n', row = 1, column = 1)

main_menu.mainloop()

