from cProfile import label
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QDialog, QDialogButtonBox
from PySide6.QtWidgets import QLabel


import pyqtgraph as pg

import mono

# Only needed for access to command line arguments
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('PL Spec v0.01 beta')

        # Layouts
        layout_main = QHBoxLayout()
        layout_right = QVBoxLayout()
        layout_bottom = QHBoxLayout()

        # Button widgets
        btn = QPushButton('Holder')
        self.btn_add_scan = QPushButton('Add Scan')
        self.btn_start_scan = QPushButton('Start Scan')
        btn_abort_scan = QPushButton('Abort Scan')
        self.btn_cont_meas = QPushButton('Continuous')

        # Signals
        self.btn_add_scan.clicked.connect(self.add_scan_clicked)
        self.btn_start_scan.clicked.connect(self.start_scan_clicked)
        btn_abort_scan.clicked.connect(self.abort_scan_clicked)

        # Plots
        plot_main = pg.PlotWidget()
        plot_main.setLabel('bottom', 'Photon Energy', units='eV')
        plot_main.setLabel('left', 'PL Intensity (rel. units)')

        layout_main.addWidget(btn)
        layout_main.addLayout(layout_right)
        layout_right.addLayout(layout_bottom)
        layout_right.addWidget(plot_main)
        layout_bottom.addWidget(self.btn_add_scan)
        layout_bottom.addWidget(self.btn_start_scan)
        layout_bottom.addWidget(btn_abort_scan)
        layout_bottom.addWidget(self.btn_cont_meas)

        widget = QWidget()
        widget.setLayout(layout_main)
        self.setCentralWidget(widget)

    def add_scan_clicked(self, s):
        dlg = ScanSetupDialog(self)
        if dlg.exec():
            print('Success!')
        else:
            print('Cancel!')

    def abort_scan_clicked(self, s):
        dlg = ScanAbortDialog(self)
        if dlg.exec():
            print('Scan Aborted!')
            self.btn_start_scan.setEnabled(True)
            self.btn_add_scan.setEnabled(True)
            self.btn_cont_meas.setEnabled(True)
        else:
            print('Continue scanning!')

    def start_scan_clicked(self, s):
        self.btn_start_scan.setEnabled(False)
        self.btn_add_scan.setEnabled(False)
        self.btn_cont_meas.setEnabled(False)

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