# RF Coil Evaluation Tool Functions
__author__ = "William Mathieu"
__copyright__ = "Copyright 2019, William Mathieu"
__license__ = "MIT"
__date__ = "26Feb2019"

from math import *
from decimal import *
import sys
import numpy as np

import nibabel as nib
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
from matplotlib.patches import Circle
import tkinter as tk
from tkinter.filedialog import askopenfilename
from skrf import Network

def AnalyzeTouchstoneFile():

    root = tk.Tk()
    root.withdraw()
    root.filename = askopenfilename(initialdir = "./Touchstone_Files", title = "Select Touchstone file", filetypes = (("Touchstone files","*.s1p *.s2p *.s*p"),("all files","*.*")))
    TSFilePath = root.filename
    
    Sm = 1
    Sn = 1
    
    def setSParam(mm, nn):
        global Sm, Sn
        Sm = mm
        Sn = nn
        Close_start_menu.config(state=tk.NORMAL)
        Close_start_menu.config(bg='lime')
    def getSParam():
        global Sm, Sn
        return Sm, Sn
    def close_start_window():
        start_window.quit()
        start_window.destroy()

    start_window = tk.Tk()
    start_window.title('Select S-Parameter')
    start_window.config(bg='white')
    S11_button = tk.Button(start_window, text = "S11", bg='white', command= lambda: setSParam(1, 1), height = 1, width = 20)
    S21_button = tk.Button(start_window, text = "S21", bg='white', command= lambda: setSParam(2, 1), height = 1, width = 20)
    S12_button = tk.Button(start_window, text = "S12", bg='white', command= lambda: setSParam(1, 2), height = 1, width = 20)
    S22_button = tk.Button(start_window, text = "S22", bg='white', command= lambda: setSParam(2, 2), height = 1, width = 20)
    blank_space = tk.Label(start_window, text="          ", bg='white')
    Close_start_menu = tk.Button(start_window, text = "GO!", bg='white', command=close_start_window)
    Close_start_menu.config(state=tk.DISABLED)
    
    S11_button.grid(sticky='we', row = 0, column = 0)
    S21_button.grid(sticky='we', row = 1, column = 0)
    S12_button.grid(sticky='we', row = 0, column = 1)
    S22_button.grid(sticky='we', row = 1, column = 1)
    blank_space.grid(sticky='we', row = 2, column = 0)
    Close_start_menu.grid(sticky='we', row = 3, column = 0, columnspan = 2)
    start_window.mainloop()
    
    Sm, Sn = getSParam()
    
    #fig, axarr = plt.subplots(1,2, sharex=True)
    #plot1 = axarr[0]
    #plot2 = axarr[1]
    plt.figure()
    #plt.title('Scattering Parameter Results')
    s_plot = Network(TSFilePath)
    s_plot.frequency.unit = 'mhz'
    s_plot.plot_s_db(m=Sm-1,n=Sn-1)#, label = "Tuned and Matched")
    #s_plot.plot_s_smith(m=Sm-1,n=Sn-1, ax=plot2, draw_labels=True)
    
    #plot1.set_title('Magnetude')
    plt.legend(loc='best')
    plt.grid(color='lightgray', linestyle='-', linewidth=1)
    
    #plot2.set_title('Smith Chart')
    #plot2.legend(loc='lower center', ncol=2)
    #plot2.grid(color='lightgray', linestyle='-', linewidth=2)
    
    plt.tight_layout()
    plt.show()

def SNRHeatmapGenerator():
    NoiseROIradius0 = 10
    NoiseROIxGap0 = 5 #158
    NoiseROIyGap0 = 5 #195
    
    # Loads .nii that user chooses calculates SNR pixel-wise and displays the volume's center slice. SNR values window can be adjusted with sliders.
    root = tk.Tk()
    root.withdraw()
    root.filename = askopenfilename(initialdir = "./NIfTI_Files", title = "Select NIfTI file", filetypes = (("NIfTI files","*.nii *.nii.gz"),("all files","*.*")))
    img = nib.load(root.filename)

    img_data = img.get_fdata()
    img_shape = img_data.shape

    slice_0 = img_data[int(img_shape[0]/2), :, :] #Sagittal
    slice_1 = img_data[:, int(img_shape[1]/2), :] #Coronal
    slice_2 = img_data[:, :, int(img_shape[2]/2)] #Axial
    
    target_slice = slice_0
    def selectOrientation(slice):
        global target_slice
        target_slice = slice
        Close_start_menu.config(state=tk.NORMAL)
        Close_start_menu.config(bg='lime')
    def getOrientation():
        global target_slice
        return target_slice
    def getNoiseROIParams():
        global NoiseROIradius0, NoiseROIxGap0, NoiseROIyGap0
        return NoiseROIradius0, NoiseROIxGap0, NoiseROIyGap0
    def close_start_window():
        global NoiseROIradius0, NoiseROIxGap0, NoiseROIyGap0
        NoiseROIradius0 = int(Set_ROIradius_entry.get())
        NoiseROIxGap0 = int(Set_xgap_entry.get())
        NoiseROIyGap0 = int(Set_ygap_entry.get())
        start_window.quit()
        start_window.destroy()

    start_window = tk.Tk()
    start_window.title('Select Orientation and Noise ROI Location')
    start_window.config(bg='white')
    
    Orientation_label = tk.Label(start_window, text="Select plane:", bg='white')
    Sagittal_button = tk.Button(start_window, text = "Sagittal", bg='white', command= lambda: selectOrientation(slice_0), height = 1, width = 15)
    Coronal_button = tk.Button(start_window, text = "Coronal", bg='white', command= lambda: selectOrientation(slice_1), height = 1, width = 15)
    Axial_button = tk.Button(start_window, text = "Axial", bg='white', command= lambda: selectOrientation(slice_2), height = 1, width = 15)

    Set_ROIradius_label = tk.Label(start_window, text="Noise ROI Radius:", bg='white')
    Set_ROIradius_entry = tk.Entry(start_window, width = 15)
    Set_ROIradius_entry.insert(0, str(NoiseROIradius0))
    
    Set_xgap_label = tk.Label(start_window, text="ROI distance from y-axis:", bg='white')
    Set_xgap_entry = tk.Entry(start_window, width = 15)
    Set_xgap_entry.insert(0, str(NoiseROIxGap0))
    
    Set_ygap_label = tk.Label(start_window, text="ROI distance from x-axis:", bg='white')
    Set_ygap_entry = tk.Entry(start_window, width = 15)
    Set_ygap_entry.insert(0, str(NoiseROIyGap0))
    
    Close_start_menu = tk.Button(start_window, text = "GO!", bg='lightgray', command=close_start_window)
    Close_start_menu.config(state=tk.DISABLED)
    
    Orientation_label.grid(sticky='e', row = 0, column = 0)
    Sagittal_button.grid(sticky='we', row = 0, column = 1)
    Coronal_button.grid(sticky='we', row = 0, column = 2)
    Axial_button.grid(sticky='we', row = 0, column = 3)
    Set_ROIradius_label.grid(sticky='e', row = 1, column = 0)
    Set_ROIradius_entry.grid(sticky='we', row = 1, column = 1)
    Set_xgap_label.grid(sticky='e', row = 2, column = 0)
    Set_xgap_entry.grid(sticky='we', row = 2, column = 1)
    Set_ygap_label.grid(sticky='e', row = 3, column = 0)
    Set_ygap_entry.grid(sticky='we', row = 3, column = 1)
    Close_start_menu.grid(sticky='we', row = 4, column = 0, columnspan = 4)
    
    start_window.mainloop()
    
    
    target_slice = getOrientation()
    NoiseROIradius1, NoiseROIxGap1, NoiseROIyGap1 = getNoiseROIParams()
    
    def calculateSNRHeatmap(slice, NoiseROIradius, NoiseROIxGap, NoiseROIyGap):
        target_slice = slice
        xMax = target_slice.shape[1]
        yMax = target_slice.shape[0]

        x = np.arange(0, xMax)
        y = np.arange(0, yMax)

        xCentre = NoiseROIxGap+NoiseROIradius
        yCentre = len(target_slice) - NoiseROIyGap - NoiseROIradius
        mask = (x[np.newaxis,:]-xCentre)**2 + (y[:,np.newaxis]-yCentre)**2 < NoiseROIradius**2

        noise_ROI_values = target_slice[mask]

        ROI_noise_mean = np.mean(noise_ROI_values)
        ROI_noise_std = np.std(noise_ROI_values)
        IM_pixel_mean = np.mean(target_slice)
        IM_pixel_std = np.std(target_slice)
        print("Mean Pixel Intensity: "+str(IM_pixel_mean))
        print("STD Pixel Intensity: "+str(IM_pixel_std))
        print("Noise Mean: "+str(ROI_noise_mean))
        print("Noise STD: "+str(ROI_noise_std))

        # Calculate SNR of image using SNR=A_pixel/STD_noise
        slice_SNR = np.true_divide(target_slice, ROI_noise_std)
        return slice_SNR, xCentre, yCentre, NoiseROIradius
    
    slice_SNRHeatmap, xCentre, yCentre, NoiseROIradius = calculateSNRHeatmap(target_slice, NoiseROIradius1, NoiseROIxGap1, NoiseROIyGap1)
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    fig.subplots_adjust(left=0.20, bottom=0.25)
    im = slice_SNRHeatmap
    im1 = ax.imshow(im, cmap="nipy_spectral")
    min0 = 0
    max0 = np.amax(slice_SNRHeatmap)
    plt.suptitle("SNR Heatmap of Center Slice")
    fig.colorbar(im1, label='SNR (Absolute Value)')

    circ = Circle((xCentre,yCentre), NoiseROIradius, fill=False, facecolor=None, edgecolor='white')
    ax.add_patch(circ)
    #plt.text(xCentre, xCentre, str(ROI_noise_std), fontsize=12)

    axcolor = 'lightgray'
    
    axNoiseROIradius = fig.add_axes([0.25, 0.17, 0.65, 0.02], facecolor=axcolor)
    axNoiseROIxCenter = fig.add_axes([0.25, 0.14, 0.65, 0.02], facecolor=axcolor)
    axNoiseROIyCenter = fig.add_axes([0.25, 0.11, 0.65, 0.02], facecolor=axcolor)
    axmax  = fig.add_axes([0.25, 0.08, 0.65, 0.02], facecolor=axcolor)
    axmin = fig.add_axes([0.25, 0.05, 0.65, 0.02], facecolor=axcolor)
    
    sNoiseROIradius = Slider(axNoiseROIradius, 'Noise ROI Radius', 1, 50, valinit=10)
    sNoiseROIxCenter = Slider(axNoiseROIxCenter, 'Noise ROI x-pos', 0, target_slice.shape[1]-2*NoiseROIradius1, valinit=NoiseROIxGap1)
    sNoiseROIyCenter = Slider(axNoiseROIyCenter, 'Noise ROI y-pos', 0, target_slice.shape[0]-2*NoiseROIradius1, valinit=NoiseROIyGap1)
    smax = Slider(axmax, 'SNR Max', 0, np.amax(slice_SNRHeatmap), valinit=max0)
    smin = Slider(axmin, 'SNR Min', 0, np.amax(slice_SNRHeatmap), valinit=min0)
    
    def update(val):
        im1.set_data(calculateSNRHeatmap(target_slice, sNoiseROIradius.val, sNoiseROIxCenter.val, sNoiseROIyCenter.val)[0])
        circ.set_radius(sNoiseROIradius.val)
        circ.center = calculateSNRHeatmap(target_slice, sNoiseROIradius.val, sNoiseROIxCenter.val, sNoiseROIyCenter.val)[1], calculateSNRHeatmap(target_slice, sNoiseROIradius.val, sNoiseROIxCenter.val, sNoiseROIyCenter.val)[2]
        smax.valmax = np.amax(calculateSNRHeatmap(target_slice, sNoiseROIradius.val, sNoiseROIxCenter.val, sNoiseROIyCenter.val)[0])
        im1.set_clim([smin.val,smax.val])
        fig.canvas.draw()
    smin.on_changed(update)
    smax.on_changed(update)
    sNoiseROIradius.on_changed(update)
    sNoiseROIxCenter.on_changed(update)
    sNoiseROIyCenter.on_changed(update)
    
    plt.show()