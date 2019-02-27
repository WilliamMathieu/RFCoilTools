__author__ = "William Mathieu"
__copyright__ = "Copyright 2019, William Mathieu"
__license__ = "MIT"
__date__ = "26Feb2019"

from RFCoilDesignTools import *
from RFCoilEvaluationTools import *
from tkinter import *
import sys
from PIL import ImageTk, Image
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QGridLayout, QHBoxLayout, QGroupBox, QLabel
from PyQt5 import *
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QColor
from PyQt5.QtCore import Qt


app = QApplication([])
app.setWindowIcon(QIcon('figures/saggitalheadsnrheatmap2.png'))
window = QWidget()
window.setWindowTitle("RF Coil Design and Evaluation Tools")

p = window.palette()
p.setColor(window.backgroundRole(), QColor(255,255,255,255))
window.setPalette(p)

imLabel = QLabel()
im = QPixmap('figures/saggitalheadsnrheatmap2.png')
imLabel.setPixmap(im)

designButtonsGrid = QGridLayout()
LICbtn = QPushButton('Loop Inductance Calculator')
LICbtn.setMinimumSize(180,10)
LICbtn.clicked.connect(LoopInductanceCalculator)
LCCbtn = QPushButton('Loop Capacitance Calculator')
LCCbtn.clicked.connect(LoopCapacitanceCalculator)
TCRCbtn = QPushButton('Total Capacitance and Resonance Calculator')
TCRCbtn.clicked.connect(TotalCapacitanceAndResonanceCalculator)
designButtonsGrid.addWidget(LICbtn,0,0) # addWidget(QWidget * widget, int fromRow, int fromColumn, int rowSpan, int columnSpan, Qt::Alignment alignment = 0)
designButtonsGrid.addWidget(LCCbtn,1,0)
designButtonsGrid.addWidget(TCRCbtn,2,0)

designGroupBox = QGroupBox('DESIGN')
designGroupBox.setLayout(designButtonsGrid)

evaluateButtonsGrid = QGridLayout()
ATDbtn = QPushButton('Analyze Touchstone Data')
ATDbtn.setMinimumSize(180,10)
ATDbtn.clicked.connect(AnalyzeTouchstoneFile)
SNRbtn = QPushButton('SNR Heatmap Generator')
SNRbtn.clicked.connect(SNRHeatmapGenerator)
evaluateButtonsGrid.addWidget(ATDbtn,0,0)
evaluateButtonsGrid.addWidget(SNRbtn,1,0)

evaluateGroupBox = QGroupBox('EVALUATE')
evaluateGroupBox.setLayout(evaluateButtonsGrid)

mainGrid = QGridLayout()
mainGrid.addWidget(designGroupBox,1,0)
mainGrid.addWidget(evaluateGroupBox,1,1)
mainGrid.addWidget(imLabel,0,0,1,2)

window.setLayout(mainGrid)
window.show()
app.exec_()