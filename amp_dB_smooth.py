# -*- coding: utf-8 -*-
"""
Digital Signal Processing basic functions

@author: NahuePassano
"""

import numpy as np

def smooth(f,amp,n_oct):
    """   
    Parameters
    ----------
    f : ndarray
        Frequency array.
    amp : ndarray
        Amplitude array in dB .
    n_oct : int
        Octave division of the smooth.

    Returns
    -------
    smoothed : ndarray
        Amplitude array smoothed in 1/n_oct octave division.
    """
    smoothed = np.empty(len(amp))
    for i in np.arange(1,len(f)):
        f_inf = f[i]*2**(-1/(2*n_oct))
        f_sup = f[i]*2**(1/(2*n_oct))
        
        index_inf = len(np.asarray((np.where(f-f_inf<0)))[0]-1)-1
        index_sup = len(np.asarray((np.where(f-f_sup<0)))[0]-1)-1
        
        if f_sup > max(f):
            f_sup=max(f)
            index_sup = np.argmax(f)
            
        
        amps_i = amp[index_inf:index_sup+1]
        smoothed[i] = 10*np.log10(sum(pow(10,amps_i*0.1))/(len(amps_i)))

    return smoothed
