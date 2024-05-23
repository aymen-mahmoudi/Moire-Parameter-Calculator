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

from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from PyQt5 import QtGui, QtCore
from functions import *


import sys

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from functions import *

#  import the gui :
gui_py = True

if gui_py == True:
    from gui import Ui_Form as ui
else:
    ui, _ = loadUiType('gui.ui')


class MainWindow(QWidget, ui):

    def __init__(self):
        QWidget.__init__(self)

        # self.setWindowIcon(QtGui.QIcon('logo.jpg')) choose logo from the designer
        self.setupUi(self)
        self.setUi_changes()

        # function to setup buttons
        self.HandleButtons()

    def HandleButtons(self):
        self.clickHere_pushButton.clicked.connect(self.essential_values)
        self.clickHere_pushButton.clicked.connect(self.plot)
        self.clickHere_pushButton.clicked.connect(self.set_mismatch)
        self.clickHere_pushButton.clicked.connect(self.set_lamda)
        self.clickHere_pushButton.clicked.connect(self.print_table)

    def plot_layout(self):
        self.fig = plt.figure(facecolor='#a5a6a5')
        self.canvas = FigureCanvas(self.fig)
        toolbar = NavigationToolbar(self.canvas, self)
        self.plottingSpace_verticalLayout.addWidget(toolbar)
        self.plottingSpace_verticalLayout.addWidget(self.canvas)

    def plot(self):
        self.fig.clear()
        ax = self.fig.add_subplot(111, facecolor='white')
        ax.set_aspect('equal')

        hexagon_down = RegularPolygon(
            (0, 0), numVertices=6, radius=self.a0_blue, ls='-', facecolor='blue', edgecolor='b', alpha=.7)
        t2 = mpl.transforms.Affine2D().rotate_deg(30) + ax.transData
        t3 = mpl.transforms.Affine2D().rotate_deg(30 - self.theta) + ax.transData
        hexagon_down.set_transform(t2)

        hexagon_up = RegularPolygon(
            (0, 0), numVertices=6, radius=self.a0_red, ls='-', facecolor='r', edgecolor='k', alpha=.4)

        hexagon_up.set_transform(t3)

        ax.add_patch(hexagon_down)
        ax.add_patch(hexagon_up)

        ax.hlines(0, -self.a0_blue, self.a0_blue,
                  colors='k', lw=2, linestyles='--')

        for axis in ['top', 'bottom', 'left', 'right']:
            ax.spines[axis].set_linewidth(1.5)

        ax.tick_params(which='both', direction='out', length=6, width=1, colors='k', left=True, top=True,
                       right=True, bottom=True, labelleft=True, labeltop=True, labelright=True, labelbottom=True)

        ax.set_xlabel("Real space ($\AA$)")
        ax.set_ylabel("Real space ($\AA$)")

        # plt.axis('scaled')
        plt.autoscale(enable=True)
        # plt.axis("off")

        self.fig.tight_layout()
        self.canvas.draw()

    def essential_values(self):
        # Global Varilables
        self.a0_blue = 0
        self.a0_red = 0
        self.theta = 0
        self.mismatch = 0
        self.lamda = 0

        self.a0_blue = float(self.get_a0_blue())
        self.a0_red = float(self.get_a0_red())
        self.theta = float(self.get_theta())
        self.mismatch = mismatch(self.a0_blue, self.a0_red)
        self.lamda = lamda(self.a0_red, self.mismatch, self.theta)

    def get_a0_blue(self):
        a0_blue = self.a0_blue_lineEdit.text()
        return a0_blue

    def get_a0_red(self):
        a0_red = self.a0_red_lineEdit.text()
        return a0_red

    def get_theta(self):
        theta = self.theta_lineEdit.text()
        return theta

    def set_mismatch(self):
        self.mismatch_lineEdit.setText(str(np.round(self.mismatch*100, 2)))

    def set_lamda(self):
        self.lamda_lineEdit.setText(str(np.round(self.lamda, 4)))

    def print_table(self):
        self.tableWidget_elements.setItem(0, 0, QTableWidgetItem(
            f'          {str(np.round(self.lamda/self.a0_blue,3))}'))
        self.tableWidget_elements.setItem(0, 1, QTableWidgetItem(
            f'          {str(np.round(self.lamda/self.a0_red,3))}'))
        self.tableWidget_elements.setItem(
            0, 2, QTableWidgetItem(f'          {"---"}'))

        self.tableWidget_elements.item(0, 0).setBackground(
            QtGui.QColor(0, 0, 100, 120))
        self.tableWidget_elements.item(0, 1).setBackground(
            QtGui.QColor(100, 0, 0, 120))
        self.tableWidget_elements.item(0, 2).setBackground(
            QtGui.QColor(100, 100, 100, 120))

        for i in range(4):
            self.tableWidget_elements.setItem(
                i+1, 0, QTableWidgetItem(f'          {str(np.round(recip_parameters(self.a0_blue)[i],3))}'))
            self.tableWidget_elements.setItem(
                i+1, 1, QTableWidgetItem(f'          {str(np.round(recip_parameters(self.a0_red)[i],3))}'))
            self.tableWidget_elements.setItem(
                i+1, 2, QTableWidgetItem(f'          {str(np.round(recip_parameters(self.lamda)[i],3))}'))

            self.tableWidget_elements.item(
                i+1, 0).setBackground(QtGui.QColor(0, 0, 100, 50))
            self.tableWidget_elements.item(
                i+1, 1).setBackground(QtGui.QColor(100, 0, 0, 50))
            self.tableWidget_elements.item(
                i+1, 2).setBackground(QtGui.QColor(100, 100, 100, 50))

    def setUi_changes(self):

        self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)
        # First empty plot
        self.plot_layout()
        # Table size and color
        table_row_column_size = [73, 157]
        self.tableWidget_elements.setColumnWidth(0, table_row_column_size[1])
        self.tableWidget_elements.setColumnWidth(1, table_row_column_size[1])
        self.tableWidget_elements.setColumnWidth(2, table_row_column_size[1])

        self.tableWidget_elements.setRowHeight(0, 40)
        self.tableWidget_elements.setRowHeight(1, table_row_column_size[0])
        self.tableWidget_elements.setRowHeight(2, table_row_column_size[0])
        self.tableWidget_elements.setRowHeight(3, table_row_column_size[0])
        self.tableWidget_elements.setRowHeight(4, table_row_column_size[0])
    

        #self.tableWidget_elements.item(0,0).setBackground(QtGui.QColor(0, 0, 100, 50))
        #self.tableWidget_elements.item(0,1).setBackground(QtGui.QColor(0, 0, 100, 50))
        #self.tableWidget_elements.item(0,2).setBackground(QtGui.QColor(0, 0, 100, 50))
            # self.tableWidget_elements.item(
            #     i, 1).setBackground(QtGui.QColor(100, 0, 0, 50))
            # self.tableWidget_elements.item(
            #     i, 2).setBackground(QtGui.QColor(100, 100, 100, 20))


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    # hold ui
    app.exec_()


if __name__ == "__main__":
    main()
