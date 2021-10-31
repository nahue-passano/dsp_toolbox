# -*- coding: utf-8 -*-
"""
Digital Signal Processing basic functions

@author: NahuePassano
"""

import numpy as np

def mov_avg(signal,M):
    """
    Parameters
    ----------
    signal : ndarray
        Signal to be averaged.
    M : int
        Size of the moving window in number of samples.

    Returns
    -------
    mavg_signal : ndarray
        Signal averaged with a window of M samples.

    """
    mavg_signal = np.zeros(len(signal))
    for  i in range(len(signal)):    
        if i == 0 : 
            mavg_signal[i] = sum(signal[i:(M+i+1)])/(M+1)       
        elif i < len(signal) - M:
            mavg_signal[i] = mavg_signal[i-1] - (signal[i-1]/(M+1)) + (signal[i+M]/(M+1))  
        else:      
            k = len(signal)-i 
            mavg_signal[i] = (mavg_signal[i-1] - (signal[i-1]/(k+1)))*((k+1)/k)  
        if i==len(signal)-1:
            mavg_signal[i]=signal[i]
    
    return mavg_signal