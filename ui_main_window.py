# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFormLayout, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1369, 701)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.layout_main_v = QVBoxLayout()
        self.layout_main_v.setObjectName(u"layout_main_v")
        self.tab_main_plots = QTabWidget(self.centralwidget)
        self.tab_main_plots.setObjectName(u"tab_main_plots")
        self.tab_spec_corrected = QWidget()
        self.tab_spec_corrected.setObjectName(u"tab_spec_corrected")
        self.verticalLayout_6 = QVBoxLayout(self.tab_spec_corrected)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.layout_spec_raw_v = QVBoxLayout()
        self.layout_spec_raw_v.setObjectName(u"layout_spec_raw_v")
        self.plot_main_corrected = PlotWidget(self.tab_spec_corrected)
        self.plot_main_corrected.setObjectName(u"plot_main_corrected")

        self.layout_spec_raw_v.addWidget(self.plot_main_corrected)


        self.verticalLayout_6.addLayout(self.layout_spec_raw_v)

        self.tab_main_plots.addTab(self.tab_spec_corrected, "")
        self.tab_spec_raw = QWidget()
        self.tab_spec_raw.setObjectName(u"tab_spec_raw")
        self.verticalLayout_8 = QVBoxLayout(self.tab_spec_raw)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.layout_spec_corrected_v = QVBoxLayout()
        self.layout_spec_corrected_v.setObjectName(u"layout_spec_corrected_v")
        self.plot_main_raw = PlotWidget(self.tab_spec_raw)
        self.plot_main_raw.setObjectName(u"plot_main_raw")

        self.layout_spec_corrected_v.addWidget(self.plot_main_raw)


        self.verticalLayout_8.addLayout(self.layout_spec_corrected_v)

        self.tab_main_plots.addTab(self.tab_spec_raw, "")

        self.layout_main_v.addWidget(self.tab_main_plots)

        self.layout_panel_h = QHBoxLayout()
        self.layout_panel_h.setObjectName(u"layout_panel_h")
        self.gbox_mono = QGroupBox(self.centralwidget)
        self.gbox_mono.setObjectName(u"gbox_mono")
        self.gbox_mono.setMaximumSize(QSize(16777215, 250))
        self.gridLayout_3 = QGridLayout(self.gbox_mono)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.layout_mono_gbox_g = QGridLayout()
        self.layout_mono_gbox_g.setObjectName(u"layout_mono_gbox_g")
        self.sbox_slitin = QDoubleSpinBox(self.gbox_mono)
        self.sbox_slitin.setObjectName(u"sbox_slitin")

        self.layout_mono_gbox_g.addWidget(self.sbox_slitin, 1, 1, 1, 1)

        self.label_2 = QLabel(self.gbox_mono)
        self.label_2.setObjectName(u"label_2")

        self.layout_mono_gbox_g.addWidget(self.label_2, 1, 0, 1, 1)

        self.sbox_position = QDoubleSpinBox(self.gbox_mono)
        self.sbox_position.setObjectName(u"sbox_position")

        self.layout_mono_gbox_g.addWidget(self.sbox_position, 0, 1, 1, 1)

        self.label = QLabel(self.gbox_mono)
        self.label.setObjectName(u"label")

        self.layout_mono_gbox_g.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(self.gbox_mono)
        self.label_3.setObjectName(u"label_3")

        self.layout_mono_gbox_g.addWidget(self.label_3, 2, 0, 1, 1)

        self.sbox_slitout = QDoubleSpinBox(self.gbox_mono)
        self.sbox_slitout.setObjectName(u"sbox_slitout")

        self.layout_mono_gbox_g.addWidget(self.sbox_slitout, 2, 1, 1, 1)


        self.gridLayout_3.addLayout(self.layout_mono_gbox_g, 0, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 2, 0, 1, 1)

        self.btn_apply = QPushButton(self.gbox_mono)
        self.btn_apply.setObjectName(u"btn_apply")

        self.gridLayout_3.addWidget(self.btn_apply, 1, 0, 1, 1)


        self.layout_panel_h.addWidget(self.gbox_mono)

        self.gbox_daq = QGroupBox(self.centralwidget)
        self.gbox_daq.setObjectName(u"gbox_daq")
        self.gbox_daq.setMaximumSize(QSize(16777215, 250))
        self.gridLayout = QGridLayout(self.gbox_daq)
        self.gridLayout.setObjectName(u"gridLayout")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_4 = QLabel(self.gbox_daq)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.sbox_integration_time = QDoubleSpinBox(self.gbox_daq)
        self.sbox_integration_time.setObjectName(u"sbox_integration_time")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.sbox_integration_time)


        self.gridLayout.addLayout(self.formLayout_3, 0, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 4, 0, 1, 1)

        self.btn_cont = QPushButton(self.gbox_daq)
        self.btn_cont.setObjectName(u"btn_cont")

        self.gridLayout.addWidget(self.btn_cont, 2, 0, 1, 1)


        self.layout_panel_h.addWidget(self.gbox_daq)

        self.gbox_spectra = QGroupBox(self.centralwidget)
        self.gbox_spectra.setObjectName(u"gbox_spectra")
        self.gbox_spectra.setMaximumSize(QSize(16777215, 250))
        self.horizontalLayout_3 = QHBoxLayout(self.gbox_spectra)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.layout_spectra_h = QHBoxLayout()
        self.layout_spectra_h.setObjectName(u"layout_spectra_h")
        self.layout_spec_left_v = QVBoxLayout()
        self.layout_spec_left_v.setObjectName(u"layout_spec_left_v")
        self.btn_add_scan = QPushButton(self.gbox_spectra)
        self.btn_add_scan.setObjectName(u"btn_add_scan")

        self.layout_spec_left_v.addWidget(self.btn_add_scan)

        self.btn_redo_scan = QPushButton(self.gbox_spectra)
        self.btn_redo_scan.setObjectName(u"btn_redo_scan")

        self.layout_spec_left_v.addWidget(self.btn_redo_scan)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.layout_spec_left_v.addItem(self.verticalSpacer)

        self.btn_start_scan = QPushButton(self.gbox_spectra)
        self.btn_start_scan.setObjectName(u"btn_start_scan")

        self.layout_spec_left_v.addWidget(self.btn_start_scan)

        self.btn_abort_scan = QPushButton(self.gbox_spectra)
        self.btn_abort_scan.setObjectName(u"btn_abort_scan")

        self.layout_spec_left_v.addWidget(self.btn_abort_scan)


        self.layout_spectra_h.addLayout(self.layout_spec_left_v)

        self.table_specs = QTableWidget(self.gbox_spectra)
        if (self.table_specs.columnCount() < 8):
            self.table_specs.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_specs.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_specs.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_specs.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_specs.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_specs.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_specs.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_specs.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_specs.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        if (self.table_specs.rowCount() < 1):
            self.table_specs.setRowCount(1)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_specs.setVerticalHeaderItem(0, __qtablewidgetitem8)
        self.table_specs.setObjectName(u"table_specs")
        self.table_specs.setMinimumSize(QSize(820, 0))
        self.table_specs.setMaximumSize(QSize(1200, 400))

        self.layout_spectra_h.addWidget(self.table_specs)

        self.layout_spec_right_v = QVBoxLayout()
        self.layout_spec_right_v.setObjectName(u"layout_spec_right_v")
        self.btn_update = QPushButton(self.gbox_spectra)
        self.btn_update.setObjectName(u"btn_update")

        self.layout_spec_right_v.addWidget(self.btn_update)

        self.btn_merge = QPushButton(self.gbox_spectra)
        self.btn_merge.setObjectName(u"btn_merge")

        self.layout_spec_right_v.addWidget(self.btn_merge)

        self.btn_delete = QPushButton(self.gbox_spectra)
        self.btn_delete.setObjectName(u"btn_delete")

        self.layout_spec_right_v.addWidget(self.btn_delete)

        self.btn_save = QPushButton(self.gbox_spectra)
        self.btn_save.setObjectName(u"btn_save")

        self.layout_spec_right_v.addWidget(self.btn_save)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.layout_spec_right_v.addItem(self.verticalSpacer_2)


        self.layout_spectra_h.addLayout(self.layout_spec_right_v)


        self.horizontalLayout_3.addLayout(self.layout_spectra_h)


        self.layout_panel_h.addWidget(self.gbox_spectra)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_panel_h.addItem(self.horizontalSpacer)


        self.layout_main_v.addLayout(self.layout_panel_h)


        self.verticalLayout_2.addLayout(self.layout_main_v)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1369, 21))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.tab_main_plots.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PLSpec 0.01 beta", None))
        self.tab_main_plots.setTabText(self.tab_main_plots.indexOf(self.tab_spec_corrected), QCoreApplication.translate("MainWindow", u"Spectrum corrected", None))
        self.tab_main_plots.setTabText(self.tab_main_plots.indexOf(self.tab_spec_raw), QCoreApplication.translate("MainWindow", u"Spectrum raw", None))
        self.gbox_mono.setTitle(QCoreApplication.translate("MainWindow", u"Mono", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Slit in (mm)", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Position (nm)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Slit out (mm)", None))
        self.btn_apply.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.gbox_daq.setTitle(QCoreApplication.translate("MainWindow", u"DAQ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Integration time (s)", None))
        self.btn_cont.setText(QCoreApplication.translate("MainWindow", u"Contonuous...", None))
        self.gbox_spectra.setTitle(QCoreApplication.translate("MainWindow", u"Spectra", None))
        self.btn_add_scan.setText(QCoreApplication.translate("MainWindow", u"Add Scan", None))
        self.btn_redo_scan.setText(QCoreApplication.translate("MainWindow", u"Redo Scan...", None))
        self.btn_start_scan.setText(QCoreApplication.translate("MainWindow", u"Start Scan", None))
        self.btn_abort_scan.setText(QCoreApplication.translate("MainWindow", u"Abort Scan", None))
        ___qtablewidgetitem = self.table_specs.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"tag", None));
        ___qtablewidgetitem1 = self.table_specs.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"start (nm)", None));
        ___qtablewidgetitem2 = self.table_specs.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"stop (nm)", None));
        ___qtablewidgetitem3 = self.table_specs.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"step (nm)", None));
        ___qtablewidgetitem4 = self.table_specs.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"slit (mm)", None));
        ___qtablewidgetitem5 = self.table_specs.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"T (K)", None));
        ___qtablewidgetitem6 = self.table_specs.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"scale", None));
        ___qtablewidgetitem7 = self.table_specs.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"shift (nm)", None));
        ___qtablewidgetitem8 = self.table_specs.verticalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"1", None));
        self.btn_update.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.btn_merge.setText(QCoreApplication.translate("MainWindow", u"Merge", None))
        self.btn_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"Save...", None))
    # retranslateUi

