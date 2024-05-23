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

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon




def recip_parameters(a0):
        GK =  (4/3)*(np.pi/a0)  
        GG = 2*GK
        GM = (2*np.pi)/(np.sqrt(3)*a0)
        KM = (2*np.pi)/(np.sqrt(3)*a0)
        KK = 2*KM
        print("Pour a0 =",str(a0)+ " A:"+'\n'
              +"\u0393K = ",str(GK)+'\n'
              +"\u0393\u0393 = ",str(GG)+'\n'
             +"\u0393M = ",str(GM)+'\n'
             +"KM = ",str(KM)+'\n'
             +"KK = ",str(KK))
        return [GK,GG,GM,KM,KK]



def plot (a,b,TMD_down,TMD_up):
  plt.rcParams['figure.figsize'] = [8, 5]
  fig,ax = plt.subplots(1)


  ax.set_aspect('equal')


  hexagon1 = RegularPolygon((0,0), numVertices=6, radius=recip_parameters(a)[0],ls='-',lw=3, alpha=.2,facecolor ='b' ,edgecolor='k',label=TMD_down)
  hexagon2 = RegularPolygon((0,0), numVertices=6, radius=recip_parameters(b)[0],ls='-', lw =2, alpha=.3, facecolor ='r',edgecolor='b',label=TMD_up)
    
  t2 = mpl.transforms.Affine2D().rotate_deg(60) + ax.transData
  t3 = mpl.transforms.Affine2D().rotate_deg(30) + ax.transData
  hexagon1.set_transform(t2)
  hexagon2.set_transform(t3)


  ax.add_patch(hexagon1)
  ax.add_patch(hexagon2)

  ax.set_xlabel("$k_{x}$ ($\AA^{-1}$)")
  ax.set_ylabel("$k_{y}$ ($\AA^{-1}$)")

  ax.text(0,0,"\u0393",fontsize = 22)

  ax.set_xlim(0,10)
  ax.set_ylim(0,3)

  #plt.axis('scaled')
  plt.autoscale(enable = True)
  #plt.axis("off")
  plt.legend()
  fig.tight_layout()




def moiree(a,b,theta,TMD_down,TMD_up):
  gamma = (a-b)/b
  lamda = a/np.sqrt(gamma*(theta**2) + gamma**2)
  ratio1 = lamda/a
  ratio2 = lamda/b
  print("==================================")
  print('Le mismatch \u03B3 vaut : '+str(np.int(gamma*100))+' %')
  print('La periodicité de moiré \u03BB vaut : '+str(np.int(lamda)))
  print(' \u03BB /'+TMD_down +' vaut : '+str(ratio1))
  print(' \u03BB /'+TMD_up +' vaut : '+str(ratio2))
  

