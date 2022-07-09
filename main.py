from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWidgets import QDialog, QDialogButtonBox, QLabel, QVBoxLayout
from ui_main_window import Ui_MainWindow


from spectrum import Spectrum
import sys

class UI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Data
        self.spectral_data = [Spectrum()]


        self.ui.plot_main_corrected.setLabel('bottom', 'Photon Energy', units='eV')
        self.ui.plot_main_corrected.setLabel('left', 'PL Intensity (rel. units)')

        self.ui.plot_main_raw.setLabel('bottom', 'Wavelength (nm)')
        self.ui.plot_main_raw.setLabel('left', 'Counts per second')

        # Signals
        self.ui.btn_add_scan.clicked.connect(self.add_scan_clicked)
        self.ui.btn_start_scan.clicked.connect(self.start_scan_clicked)
        self.ui.btn_abort_scan.clicked.connect(self.abort_scan_clicked)
        self.ui.btn_delete.clicked.connect(self.delete_scan_clicked)


    def add_scan_clicked(self, s):
        dlg = ScanSetupDialog(self)
        if dlg.exec():
            nrows = self.ui.table_specs.rowCount()
            self.ui.table_specs.insertRow(nrows)
            self.spectral_data.append(Spectrum())
            print(len(self.spectral_data))
            print('Scan added.')
        else:
            print('Scan adding cancelled.')

    def abort_scan_clicked(self, s):
        dlg = ScanAbortDialog(self)
        if dlg.exec():
            self.ui.btn_start_scan.setEnabled(True)
            self.ui.btn_add_scan.setEnabled(True)
            self.ui.btn_cont.setEnabled(True)
            self.ui.btn_apply.setEnabled(True)
            self.ui.btn_abort_scan.setEnabled(False)
            print('Scan Aborted!')
        else:
            print('Continue scanning.')

    def start_scan_clicked(self, s):
        self.ui.btn_start_scan.setEnabled(False)
        self.ui.btn_add_scan.setEnabled(False)
        self.ui.btn_apply.setEnabled(False)
        self.ui.btn_cont.setEnabled(False)
        self.ui.btn_abort_scan.setEnabled(True)

    def delete_scan_clicked(self, s):
        row_selected = self.ui.table_specs.currentRow()
        dlg = ScanAbortDialog(self)
        if dlg.exec():
            self.ui.table_specs.removeRow(row_selected)
            print('Scan #{:1.0f} Deleted!'.format(row_selected))
        

class ScanSetupDialog(QDialog):
    def __init__(self, parent=UI):
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
    def __init__(self, parent=UI):
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

class ScanDeleteDialog(QDialog):
    def __init__(self, parent=UI):
        super().__init__(parent)

        self.setWindowTitle('Delete Scan')

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel('Delete selected the scan?\nThe measurement will be lost!\nThink twise...')
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = UI()
    win.show()
    app.exec()