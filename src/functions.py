##############################################################################
##
# This file is part of Moiré parameter project
##
# Copyright 2023 / AYMEN MAHMOUDI, FRANCE
##
# The files of this project are free and open source: you can redistribute them and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
##
# This project is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
##
##############################################################################

__author__ = ["Aymen Mahmoudi"]
__license__ = "GPL"
__date__ = "26/03/2023"




import numpy as np



def recip_parameters(a0):
        GK =  (4/3)*(np.pi/a0)  
        GM = (2*np.pi)/(np.sqrt(3)*a0)
        GG = 2*GM
        KM = (2*np.pi)/(np.sqrt(3)*a0)
        KK = 2*KM
        return [GK,GG,GM,KK]


def mismatch(a,b):
    m = np.abs(a-b)/a
    return m


def lamda_ref(a,m,t):
    l = a*(1+m)/np.sqrt(2*(1+m)*(1-np.cos(t)) + m**2)
    return l

def lamda(a,m,t):
    t = np.deg2rad(t)
    l = a/np.sqrt(m*(t**2) + m**2)
    return l
















