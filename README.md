# RFCoilTools
RF Coil Design and Evaluation Tools

## Installation
Requires Python 3.
1. Click *Code* > *Download ZIP*
2. Extract the .zip file into a directory of your choice
3. In Command Prompt **cd** to the chosen directory
4. Run the command:
`py -3 setup.py install`

## Running the Application

`py -3 MAIN_MENU.py`

## Features

Tools are devided into two categories: design and evaluation. Design tools are suited for estimating the necessary electrical components before building an RF coil. Evaluation tools are used in the coil testing phase to process network and MRI image data.

### Main Menu

<p align="center">
  <img src="./screenshots/MainMenuScreenshot2.PNG">
</p>

### Loop Inductance Calculator

<p align="center">
  <img src="./screenshots/InductanceCalc.PNG">
</p>

### Loop Capacitance Calculator

<p align="center">
  <img src="./screenshots/CapCalc.PNG">
</p>

### Total Capacitance and Resonance Calculator

<p align="center">
  <img src="./screenshots/ResCalc1.PNG">
</p>
<p align="center">
  <img src="./screenshots/ResCalc2.PNG">
</p>

### Analyze Touchstone Data

<p align="center">
  <img src="./screenshots/touchstone1.PNG">
</p>
<p align="center">
  <img src="./screenshots/touchstone2.PNG">
</p>

### SNR Heatmap Generator

<p align="center">
  <img src="./screenshots/heatmap1.PNG">
</p>
<p align="center">
  <img src="./screenshots/heatmap2.PNG">
</p>

## Licenses

This software is released under the [MIT License](LICENSE).

Graphics generated from the [MNI MRI dataset](http://nist.mni.mcgill.ca/?p=935) under their [MIT License](https://github.com/WilliamMathieu/RFCoilTools/blob/master/MNI%20Dataset%20License).
