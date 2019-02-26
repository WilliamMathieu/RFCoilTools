__author__ = "William Mathieu"
__copyright__ = "Copyright 2019, William Mathieu"
__license__ = "MIT"
__date__ = "26Feb2019"

from RFCoilDesignTools import *
from RFCoilEvaluationTools import *
from tkinter import *
import sys
from PIL import ImageTk, Image

def start_LoopCapacitanceCalculator():
    LoopCapacitanceCalculator()
def start_LoopInductanceCalculator():
    LoopInductanceCalculator()
def start_TotalCapacitanceAndResonanceCalculator():
    TotalCapacitanceAndResonanceCalculator()
def start_AnalyzeTouchstoneFile():
    AnalyzeTouchstoneFile()
def start_SNRHeatmapGenerator():
    SNRHeatmapGenerator()

def close_main_menu():
    main_menu.quit()
    main_menu.destroy()
    sys.exit()

main_menu = Tk()
# width x height + x_offset + y_offset:
#main_menu.geometry("800x200+30+30")
main_menu.resizable(width=False, height=False)
main_menu.title('RF Coil Design and Evaluation Tools')
main_menu.config(bg='white')
imagepath = "figures/saggitalheadsnrheatmap.png"

SNRimg = ImageTk.PhotoImage((Image.open(imagepath)).resize((300, 252), Image.ANTIALIAS)) #(height, width)

APPTitle = Label(main_menu, text="RF Coil Design and Evaluation Tools", bg='white', font=("Microsoft Sans Serif", 22))
ImagePanel = Label(main_menu, image = SNRimg, bg='white')
LoopInductanceCalculator_button = Button(main_menu, text = "Loop Inductance Calculator", bg='white', command=start_LoopInductanceCalculator, height = 1, width = 40)
LoopCapacitanceCalculator_button = Button(main_menu, text = "Loop Capacitance Calculator", bg='white', command=start_LoopCapacitanceCalculator, height = 1, width = 40)
TotalCapacitanceAndResonanceCalculator_button = Button(main_menu, text = "Total Capacitance and Resonance Calculator", bg='white', command=start_TotalCapacitanceAndResonanceCalculator, height = 1, width = 40)
AnalyzeTouchstoneFile_button = Button(main_menu, text = "Analyze Touchstone Data", bg='white', command=start_AnalyzeTouchstoneFile, height = 1, width = 40)
SNRHeatmapGenerator_button = Button(main_menu, text = "SNR Heatmap Generator", bg='white', command=start_SNRHeatmapGenerator, height = 1, width = 40)
DesignTitle = Label(main_menu, text="DESIGN", bg='white', font=("Microsoft Sans Serif", 12))
EvaluateTitle = Label(main_menu, text="EVALUATE", bg='white', font=("Microsoft Sans Serif", 12))
blackspace = Label(main_menu, text="                ", bg='white')
Close_start_menu = Button(main_menu, text = "Exit", bg='white', command=close_main_menu, height = 1, width = 20)


APPTitle.grid(row = 0, column = 0, columnspan = 2, sticky=(N, S, E, W))
ImagePanel.grid(row = 1, column = 0, columnspan = 2, sticky=(N, S, E, W))
blackspace.grid(row = 6, column = 0, columnspan = 2, sticky=(N, S, E, W))
Close_start_menu.grid(row = 7, column = 0, columnspan = 2)

DesignTitle.grid(row = 2, column = 0, sticky=(N, S, E, W))
LoopInductanceCalculator_button.grid(row = 3, column = 0, sticky=(N, S, E, W))
LoopCapacitanceCalculator_button.grid(row = 4, column = 0, sticky=(N, S, E, W))
TotalCapacitanceAndResonanceCalculator_button.grid(row = 5, column = 0, sticky=(N, S, E, W))


EvaluateTitle.grid(row = 2, column = 1, sticky=(N, S, E, W))
AnalyzeTouchstoneFile_button.grid(row = 3, column = 1, sticky=(N, S, E, W))
SNRHeatmapGenerator_button.grid(row = 4, column = 1, sticky=(N, S, E, W))

main_menu.mainloop()