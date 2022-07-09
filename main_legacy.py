from cProfile import label
from unicodedata import name
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QDialog, QDialogButtonBox
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QGroupBox


import pyqtgraph as pg

from ui_main_window import Ui_MainWindow

# Only needed for access to command line arguments
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('PL Spec v0.01 beta')

        # Layouts
        layout_main = QVBoxLayout()
        layout_panel = QHBoxLayout()
        layout_spectra = QGridLayout()
        layout_mono = QGridLayout()
        layout_detector = QGridLayout()

        # Group boxes
        gbox_spectra = QGroupBox('Spectra')
        gbox_mono = QGroupBox('Mono')
        gbox_detector = QGroupBox('Detector')

        # Button widgets
        btn = QPushButton('Holder')
        self.btn_add_scan = QPushButton('Add Scan')
        self.btn_start_scan = QPushButton('Start Scan')
        self.btn_abort_scan = QPushButton('Abort Scan')
        self.btn_cont_meas = QPushButton('Continuous')

        self.btn_update = QPushButton('Update')
        self.btn_merge = QPushButton('Merge')
        self.btn_delete = QPushButton('Delete')
        self.btn_save = QPushButton('Save')
        self.btn_save_merged = QPushButton('Save Merged')

        self.btn_abort_scan.setEnabled(False)

        # Signals
        self.btn_add_scan.clicked.connect(self.add_scan_clicked)
        self.btn_start_scan.clicked.connect(self.start_scan_clicked)
        self.btn_abort_scan.clicked.connect(self.abort_scan_clicked)

        # Plots
        plot_main = pg.PlotWidget()
        plot_main.setLabel('bottom', 'Photon Energy', units='eV')
        plot_main.setLabel('left', 'PL Intensity (rel. units)')

        layout_main.addWidget(plot_main)
        layout_main.addLayout(layout_panel)

        layout_panel.addWidget(gbox_spectra)
        layout_panel.addWidget(gbox_mono)
        layout_panel.addWidget(gbox_detector)


        # Group box lyout assignment
        layout_spectra.addWidget(self.btn_add_scan, 0, 0)
        layout_spectra.addWidget(self.btn_start_scan, 1, 0)
        layout_spectra.addWidget(self.btn_abort_scan, 2, 0)
        layout_spectra.addWidget(self.btn_cont_meas, 3, 0)

        layout_spectra.addWidget(self.btn_update, 0, 2)
        layout_spectra.addWidget(self.btn_merge, 1, 2)
        layout_spectra.addWidget(self.btn_delete, 2, 2)
        layout_spectra.addWidget(self.btn_save, 3, 2)
        layout_spectra.addWidget(self.btn_save_merged, 4, 2)

        gbox_spectra.setLayout(layout_spectra)
        

        widget = QWidget()
        widget.setLayout(layout_main)
        self.setCentralWidget(widget)

    def add_scan_clicked(self, s):
        dlg = ScanSetupDialog(self)
        if dlg.exec():
            print('Scan added.')
        else:
            print('Scan adding cancelled.')

    def abort_scan_clicked(self, s):
        dlg = ScanAbortDialog(self)
        if dlg.exec():
            self.btn_start_scan.setEnabled(True)
            self.btn_add_scan.setEnabled(True)
            self.btn_cont_meas.setEnabled(True)
            self.btn_abort_scan.setEnabled(False)
            print('Scan Aborted!')
        else:
            print('Continue scanning.')

    def start_scan_clicked(self, s):
        self.btn_start_scan.setEnabled(False)
        self.btn_add_scan.setEnabled(False)
        self.btn_cont_meas.setEnabled(False)
        self.btn_abort_scan.setEnabled(True)

class ScanSetupDialog(QDialog):
    def __init__(self, parent=MainWindow):
        super().__init__(parent)

        self.setWindowTitle('Add Scan')

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel('Adding Scan')
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

class ScanAbortDialog(QDialog):
    def __init__(self, parent=MainWindow):
        super().__init__(parent)

        self.setWindowTitle('Abort Scan')

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel('Do you really want to abort the scan?\nThink twise...')
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)



# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = MainWindow()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()