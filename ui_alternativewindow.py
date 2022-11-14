# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'alternativewindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_AlternativeWindow(object):
    def setupUi(self, AlternativeWindow):
        if not AlternativeWindow.objectName():
            AlternativeWindow.setObjectName(u"AlternativeWindow")
        AlternativeWindow.resize(984, 506)
        self.centralwidget = QWidget(AlternativeWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 981, 461))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.verticalLayoutWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setBaseSize(QSize(20, 20))
        self.transceiver_tab = QWidget()
        self.transceiver_tab.setObjectName(u"transceiver_tab")
        self.layoutWidget = QWidget(self.transceiver_tab)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 964, 419))
        self.verticalLayout_14 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_available_contexts = QLabel(self.layoutWidget)
        self.lbl_available_contexts.setObjectName(u"lbl_available_contexts")

        self.horizontalLayout_2.addWidget(self.lbl_available_contexts)

        self.cb_available_contexts = QComboBox(self.layoutWidget)
        self.cb_available_contexts.addItem("")
        self.cb_available_contexts.addItem("")
        self.cb_available_contexts.setObjectName(u"cb_available_contexts")

        self.horizontalLayout_2.addWidget(self.cb_available_contexts)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.lbl_hardware_name = QLabel(self.layoutWidget)
        self.lbl_hardware_name.setObjectName(u"lbl_hardware_name")

        self.horizontalLayout_22.addWidget(self.lbl_hardware_name)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_8)

        self.lbl_hardware_name_dyn = QLabel(self.layoutWidget)
        self.lbl_hardware_name_dyn.setObjectName(u"lbl_hardware_name_dyn")
        font = QFont()
        font.setFamilies([u"Ubuntu Mono"])
        font.setBold(True)
        self.lbl_hardware_name_dyn.setFont(font)

        self.horizontalLayout_22.addWidget(self.lbl_hardware_name_dyn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_22)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.line = QFrame(self.layoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_5.addWidget(self.line)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.lbl_vendor = QLabel(self.layoutWidget)
        self.lbl_vendor.setObjectName(u"lbl_vendor")

        self.horizontalLayout_23.addWidget(self.lbl_vendor)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_4)

        self.lbl_vendor_dyn = QLabel(self.layoutWidget)
        self.lbl_vendor_dyn.setObjectName(u"lbl_vendor_dyn")
        self.lbl_vendor_dyn.setFont(font)

        self.horizontalLayout_23.addWidget(self.lbl_vendor_dyn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.lbl_hardware_carrier = QLabel(self.layoutWidget)
        self.lbl_hardware_carrier.setObjectName(u"lbl_hardware_carrier")

        self.horizontalLayout_24.addWidget(self.lbl_hardware_carrier)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_5)

        self.lbl_hardware_carrier_dyn = QLabel(self.layoutWidget)
        self.lbl_hardware_carrier_dyn.setObjectName(u"lbl_hardware_carrier_dyn")
        self.lbl_hardware_carrier_dyn.setFont(font)

        self.horizontalLayout_24.addWidget(self.lbl_hardware_carrier_dyn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_24)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.line_2 = QFrame(self.layoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_2)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.lbl_hardware_serial = QLabel(self.layoutWidget)
        self.lbl_hardware_serial.setObjectName(u"lbl_hardware_serial")

        self.horizontalLayout_25.addWidget(self.lbl_hardware_serial)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_6)

        self.lbl_hardware_serial_dyn = QLabel(self.layoutWidget)
        self.lbl_hardware_serial_dyn.setObjectName(u"lbl_hardware_serial_dyn")
        self.lbl_hardware_serial_dyn.setFont(font)

        self.horizontalLayout_25.addWidget(self.lbl_hardware_serial_dyn)


        self.verticalLayout_15.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.lbl_local = QLabel(self.layoutWidget)
        self.lbl_local.setObjectName(u"lbl_local")

        self.horizontalLayout_26.addWidget(self.lbl_local)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_7)

        self.lbl_local_dyn = QLabel(self.layoutWidget)
        self.lbl_local_dyn.setObjectName(u"lbl_local_dyn")
        self.lbl_local_dyn.setFont(font)

        self.horizontalLayout_26.addWidget(self.lbl_local_dyn)


        self.verticalLayout_15.addLayout(self.horizontalLayout_26)


        self.horizontalLayout_3.addLayout(self.verticalLayout_15)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)


        self.verticalLayout_14.addLayout(self.horizontalLayout_5)

        self.line_3 = QFrame(self.layoutWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_14.addWidget(self.line_3)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.gb_transmitter = QGroupBox(self.layoutWidget)
        self.gb_transmitter.setObjectName(u"gb_transmitter")
        self.verticalLayout_12 = QVBoxLayout(self.gb_transmitter)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lbl_power_tx = QLabel(self.gb_transmitter)
        self.lbl_power_tx.setObjectName(u"lbl_power_tx")

        self.horizontalLayout_6.addWidget(self.lbl_power_tx)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_9)

        self.btn_power_tx = QPushButton(self.gb_transmitter)
        self.btn_power_tx.setObjectName(u"btn_power_tx")

        self.horizontalLayout_6.addWidget(self.btn_power_tx)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lbl_lo_frequency_tx = QLabel(self.gb_transmitter)
        self.lbl_lo_frequency_tx.setObjectName(u"lbl_lo_frequency_tx")

        self.horizontalLayout_11.addWidget(self.lbl_lo_frequency_tx)

        self.cb_lo_frequency_tx = QComboBox(self.gb_transmitter)
        self.cb_lo_frequency_tx.addItem("")
        self.cb_lo_frequency_tx.addItem("")
        self.cb_lo_frequency_tx.setObjectName(u"cb_lo_frequency_tx")

        self.horizontalLayout_11.addWidget(self.cb_lo_frequency_tx)


        self.verticalLayout_4.addLayout(self.horizontalLayout_11)

        self.chk_autotuning_tx = QCheckBox(self.gb_transmitter)
        self.chk_autotuning_tx.setObjectName(u"chk_autotuning_tx")

        self.verticalLayout_4.addWidget(self.chk_autotuning_tx)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lbl_gain_tx = QLabel(self.gb_transmitter)
        self.lbl_gain_tx.setObjectName(u"lbl_gain_tx")

        self.horizontalLayout_10.addWidget(self.lbl_gain_tx)

        self.cb_gain_tx = QComboBox(self.gb_transmitter)
        self.cb_gain_tx.addItem("")
        self.cb_gain_tx.addItem("")
        self.cb_gain_tx.setObjectName(u"cb_gain_tx")

        self.horizontalLayout_10.addWidget(self.cb_gain_tx)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lbl_rf_attn_index = QLabel(self.gb_transmitter)
        self.lbl_rf_attn_index.setObjectName(u"lbl_rf_attn_index")

        self.horizontalLayout_7.addWidget(self.lbl_rf_attn_index)

        self.cb_rf_attn_index = QComboBox(self.gb_transmitter)
        self.cb_rf_attn_index.addItem("")
        self.cb_rf_attn_index.addItem("")
        self.cb_rf_attn_index.setObjectName(u"cb_rf_attn_index")

        self.horizontalLayout_7.addWidget(self.cb_rf_attn_index)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)


        self.verticalLayout_7.addLayout(self.verticalLayout_4)

        self.gb_status_tx = QGroupBox(self.gb_transmitter)
        self.gb_status_tx.setObjectName(u"gb_status_tx")
        self.horizontalLayout_9 = QHBoxLayout(self.gb_status_tx)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_lock_detect_tx = QLabel(self.gb_status_tx)
        self.lbl_lock_detect_tx.setObjectName(u"lbl_lock_detect_tx")

        self.horizontalLayout.addWidget(self.lbl_lock_detect_tx)

        self.cw_lock_detect_tx = QWidget(self.gb_status_tx)
        self.cw_lock_detect_tx.setObjectName(u"cw_lock_detect_tx")
        self.cw_lock_detect_tx.setMinimumSize(QSize(20, 20))
        self.cw_lock_detect_tx.setMaximumSize(QSize(20, 20))
        self.cw_lock_detect_tx.setBaseSize(QSize(20, 20))
        self.cw_lock_detect_tx.setAutoFillBackground(False)
        self.cw_lock_detect_tx.setStyleSheet(u"color: white;\n"
"border-radius: 10;\n"
"background-color: qlineargradient(spread:pad, x1:0.145, y1:0.16, x2:1, y2:1, stop:0 rgba(20, 252, 7, 255), stop:1 rgba(25, 134, 5, 255))")

        self.horizontalLayout.addWidget(self.cw_lock_detect_tx)


        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lbl_temp_tx = QLabel(self.gb_status_tx)
        self.lbl_temp_tx.setObjectName(u"lbl_temp_tx")

        self.horizontalLayout_8.addWidget(self.lbl_temp_tx)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.lbl_temp_tx_dyn = QLabel(self.gb_status_tx)
        self.lbl_temp_tx_dyn.setObjectName(u"lbl_temp_tx_dyn")

        self.horizontalLayout_8.addWidget(self.lbl_temp_tx_dyn)


        self.verticalLayout_6.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.lbl_power_usage_tx = QLabel(self.gb_status_tx)
        self.lbl_power_usage_tx.setObjectName(u"lbl_power_usage_tx")

        self.horizontalLayout_29.addWidget(self.lbl_power_usage_tx)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_12)

        self.lbl_power_usage_tx_dyn = QLabel(self.gb_status_tx)
        self.lbl_power_usage_tx_dyn.setObjectName(u"lbl_power_usage_tx_dyn")

        self.horizontalLayout_29.addWidget(self.lbl_power_usage_tx_dyn)


        self.verticalLayout_6.addLayout(self.horizontalLayout_29)


        self.horizontalLayout_9.addLayout(self.verticalLayout_6)


        self.verticalLayout_7.addWidget(self.gb_status_tx)


        self.horizontalLayout_12.addLayout(self.verticalLayout_7)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tb_registers_tx = QTableWidget(self.gb_transmitter)
        if (self.tb_registers_tx.columnCount() < 2):
            self.tb_registers_tx.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_registers_tx.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_registers_tx.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tb_registers_tx.rowCount() < 28):
            self.tb_registers_tx.setRowCount(28)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_registers_tx.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_registers_tx.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tb_registers_tx.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tb_registers_tx.setVerticalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tb_registers_tx.setVerticalHeaderItem(4, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tb_registers_tx.setVerticalHeaderItem(5, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tb_registers_tx.setVerticalHeaderItem(6, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tb_registers_tx.setVerticalHeaderItem(7, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tb_registers_tx.setVerticalHeaderItem(8, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tb_registers_tx.setVerticalHeaderItem(9, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tb_registers_tx.setVerticalHeaderItem(10, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tb_registers_tx.setVerticalHeaderItem(11, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tb_registers_tx.setVerticalHeaderItem(12, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tb_registers_tx.setVerticalHeaderItem(13, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tb_registers_tx.setVerticalHeaderItem(14, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tb_registers_tx.setVerticalHeaderItem(15, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tb_registers_tx.setVerticalHeaderItem(16, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tb_registers_tx.setVerticalHeaderItem(17, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tb_registers_tx.setVerticalHeaderItem(18, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tb_registers_tx.setVerticalHeaderItem(19, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tb_registers_tx.setVerticalHeaderItem(20, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tb_registers_tx.setVerticalHeaderItem(21, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tb_registers_tx.setVerticalHeaderItem(22, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tb_registers_tx.setVerticalHeaderItem(23, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tb_registers_tx.setVerticalHeaderItem(24, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tb_registers_tx.setVerticalHeaderItem(25, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tb_registers_tx.setVerticalHeaderItem(26, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tb_registers_tx.setVerticalHeaderItem(27, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tb_registers_tx.setItem(0, 0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tb_registers_tx.setItem(0, 1, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tb_registers_tx.setItem(1, 0, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tb_registers_tx.setItem(1, 1, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tb_registers_tx.setItem(2, 0, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tb_registers_tx.setItem(2, 1, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tb_registers_tx.setItem(3, 0, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tb_registers_tx.setItem(3, 1, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tb_registers_tx.setItem(4, 0, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tb_registers_tx.setItem(4, 1, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tb_registers_tx.setItem(5, 0, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tb_registers_tx.setItem(5, 1, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tb_registers_tx.setItem(6, 0, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tb_registers_tx.setItem(6, 1, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tb_registers_tx.setItem(7, 0, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tb_registers_tx.setItem(7, 1, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tb_registers_tx.setItem(8, 0, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tb_registers_tx.setItem(8, 1, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tb_registers_tx.setItem(9, 0, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tb_registers_tx.setItem(9, 1, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tb_registers_tx.setItem(10, 0, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tb_registers_tx.setItem(10, 1, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tb_registers_tx.setItem(11, 0, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.tb_registers_tx.setItem(11, 1, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.tb_registers_tx.setItem(12, 0, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.tb_registers_tx.setItem(12, 1, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.tb_registers_tx.setItem(13, 0, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.tb_registers_tx.setItem(13, 1, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.tb_registers_tx.setItem(14, 0, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.tb_registers_tx.setItem(14, 1, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.tb_registers_tx.setItem(15, 0, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.tb_registers_tx.setItem(15, 1, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.tb_registers_tx.setItem(16, 0, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.tb_registers_tx.setItem(16, 1, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.tb_registers_tx.setItem(17, 0, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.tb_registers_tx.setItem(17, 1, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.tb_registers_tx.setItem(18, 0, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.tb_registers_tx.setItem(18, 1, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.tb_registers_tx.setItem(19, 0, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.tb_registers_tx.setItem(19, 1, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.tb_registers_tx.setItem(20, 0, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.tb_registers_tx.setItem(20, 1, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.tb_registers_tx.setItem(21, 0, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.tb_registers_tx.setItem(21, 1, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.tb_registers_tx.setItem(22, 0, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.tb_registers_tx.setItem(22, 1, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.tb_registers_tx.setItem(23, 0, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.tb_registers_tx.setItem(23, 1, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.tb_registers_tx.setItem(24, 0, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        self.tb_registers_tx.setItem(24, 1, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.tb_registers_tx.setItem(25, 0, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.tb_registers_tx.setItem(25, 1, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        self.tb_registers_tx.setItem(26, 0, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        self.tb_registers_tx.setItem(26, 1, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        self.tb_registers_tx.setItem(27, 0, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        self.tb_registers_tx.setItem(27, 1, __qtablewidgetitem85)
        self.tb_registers_tx.setObjectName(u"tb_registers_tx")
        self.tb_registers_tx.setMaximumSize(QSize(221, 581))
        self.tb_registers_tx.verticalHeader().setVisible(False)

        self.verticalLayout_5.addWidget(self.tb_registers_tx)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.btn_reset_regs_tx = QPushButton(self.gb_transmitter)
        self.btn_reset_regs_tx.setObjectName(u"btn_reset_regs_tx")

        self.horizontalLayout_27.addWidget(self.btn_reset_regs_tx)

        self.btn_refresh_regs_tx = QPushButton(self.gb_transmitter)
        self.btn_refresh_regs_tx.setObjectName(u"btn_refresh_regs_tx")

        self.horizontalLayout_27.addWidget(self.btn_refresh_regs_tx)


        self.verticalLayout_5.addLayout(self.horizontalLayout_27)


        self.horizontalLayout_12.addLayout(self.verticalLayout_5)


        self.verticalLayout_12.addLayout(self.horizontalLayout_12)


        self.horizontalLayout_21.addWidget(self.gb_transmitter)

        self.gb_receiver = QGroupBox(self.layoutWidget)
        self.gb_receiver.setObjectName(u"gb_receiver")
        self.verticalLayout_13 = QVBoxLayout(self.gb_receiver)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.lbl_power_rx = QLabel(self.gb_receiver)
        self.lbl_power_rx.setObjectName(u"lbl_power_rx")

        self.horizontalLayout_28.addWidget(self.lbl_power_rx)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_11)

        self.btn_power_rx = QPushButton(self.gb_receiver)
        self.btn_power_rx.setObjectName(u"btn_power_rx")

        self.horizontalLayout_28.addWidget(self.btn_power_rx)


        self.verticalLayout_9.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.lbl_lo_frequency_rx = QLabel(self.gb_receiver)
        self.lbl_lo_frequency_rx.setObjectName(u"lbl_lo_frequency_rx")

        self.horizontalLayout_15.addWidget(self.lbl_lo_frequency_rx)

        self.cb_lo_frequency_rx = QComboBox(self.gb_receiver)
        self.cb_lo_frequency_rx.addItem("")
        self.cb_lo_frequency_rx.addItem("")
        self.cb_lo_frequency_rx.setObjectName(u"cb_lo_frequency_rx")

        self.horizontalLayout_15.addWidget(self.cb_lo_frequency_rx)


        self.verticalLayout_9.addLayout(self.horizontalLayout_15)

        self.chk_autotuning_rx = QCheckBox(self.gb_receiver)
        self.chk_autotuning_rx.setObjectName(u"chk_autotuning_rx")

        self.verticalLayout_9.addWidget(self.chk_autotuning_rx)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.lbl_gain_rx = QLabel(self.gb_receiver)
        self.lbl_gain_rx.setObjectName(u"lbl_gain_rx")

        self.horizontalLayout_16.addWidget(self.lbl_gain_rx)

        self.cb_gain_rx = QComboBox(self.gb_receiver)
        self.cb_gain_rx.addItem("")
        self.cb_gain_rx.addItem("")
        self.cb_gain_rx.setObjectName(u"cb_gain_rx")

        self.horizontalLayout_16.addWidget(self.cb_gain_rx)


        self.verticalLayout_9.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.lbl_bb_attn_index = QLabel(self.gb_receiver)
        self.lbl_bb_attn_index.setObjectName(u"lbl_bb_attn_index")

        self.horizontalLayout_17.addWidget(self.lbl_bb_attn_index)

        self.cb_bb_attn_index = QComboBox(self.gb_receiver)
        self.cb_bb_attn_index.addItem("")
        self.cb_bb_attn_index.addItem("")
        self.cb_bb_attn_index.setObjectName(u"cb_bb_attn_index")

        self.horizontalLayout_17.addWidget(self.cb_bb_attn_index)


        self.verticalLayout_9.addLayout(self.horizontalLayout_17)


        self.verticalLayout_8.addLayout(self.verticalLayout_9)

        self.gb_status_rx = QGroupBox(self.gb_receiver)
        self.gb_status_rx.setObjectName(u"gb_status_rx")
        self.horizontalLayout_18 = QHBoxLayout(self.gb_status_rx)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.lbl_lock_detect_rx = QLabel(self.gb_status_rx)
        self.lbl_lock_detect_rx.setObjectName(u"lbl_lock_detect_rx")

        self.horizontalLayout_19.addWidget(self.lbl_lock_detect_rx)

        self.cw_lock_detect_rx = QWidget(self.gb_status_rx)
        self.cw_lock_detect_rx.setObjectName(u"cw_lock_detect_rx")
        self.cw_lock_detect_rx.setMinimumSize(QSize(20, 20))
        self.cw_lock_detect_rx.setMaximumSize(QSize(20, 20))
        self.cw_lock_detect_rx.setBaseSize(QSize(20, 20))
        self.cw_lock_detect_rx.setAutoFillBackground(False)
        self.cw_lock_detect_rx.setStyleSheet(u"color: white;\n"
"border-radius: 10;\n"
"background-color: qlineargradient(spread:pad, x1:0.145, y1:0.16, x2:1, y2:1, stop:0 rgba(252, 20, 7, 255), stop:1 rgba(134, 25, 5, 255))")

        self.horizontalLayout_19.addWidget(self.cw_lock_detect_rx)


        self.verticalLayout_10.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.lbl_temp_rx = QLabel(self.gb_status_rx)
        self.lbl_temp_rx.setObjectName(u"lbl_temp_rx")

        self.horizontalLayout_20.addWidget(self.lbl_temp_rx)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_3)

        self.lbl_temp_rx_dyn = QLabel(self.gb_status_rx)
        self.lbl_temp_rx_dyn.setObjectName(u"lbl_temp_rx_dyn")

        self.horizontalLayout_20.addWidget(self.lbl_temp_rx_dyn)


        self.verticalLayout_10.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.lbl_power_usage_rx = QLabel(self.gb_status_rx)
        self.lbl_power_usage_rx.setObjectName(u"lbl_power_usage_rx")

        self.horizontalLayout_30.addWidget(self.lbl_power_usage_rx)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_13)

        self.lbl_power_usage_rx_dyn = QLabel(self.gb_status_rx)
        self.lbl_power_usage_rx_dyn.setObjectName(u"lbl_power_usage_rx_dyn")

        self.horizontalLayout_30.addWidget(self.lbl_power_usage_rx_dyn)


        self.verticalLayout_10.addLayout(self.horizontalLayout_30)


        self.horizontalLayout_18.addLayout(self.verticalLayout_10)


        self.verticalLayout_8.addWidget(self.gb_status_rx)


        self.horizontalLayout_13.addLayout(self.verticalLayout_8)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.tb_registers_rx = QTableWidget(self.gb_receiver)
        if (self.tb_registers_rx.columnCount() < 2):
            self.tb_registers_rx.setColumnCount(2)
        __qtablewidgetitem86 = QTableWidgetItem()
        self.tb_registers_rx.setHorizontalHeaderItem(0, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        self.tb_registers_rx.setHorizontalHeaderItem(1, __qtablewidgetitem87)
        if (self.tb_registers_rx.rowCount() < 28):
            self.tb_registers_rx.setRowCount(28)
        __qtablewidgetitem88 = QTableWidgetItem()
        self.tb_registers_rx.setVerticalHeaderItem(0, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        self.tb_registers_rx.setVerticalHeaderItem(1, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        self.tb_registers_rx.setVerticalHeaderItem(2, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        self.tb_registers_rx.setVerticalHeaderItem(3, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        self.tb_registers_rx.setVerticalHeaderItem(4, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        self.tb_registers_rx.setVerticalHeaderItem(5, __qtablewidgetitem93)
        __qtablewidgetitem94 = QTableWidgetItem()
        self.tb_registers_rx.setVerticalHeaderItem(6, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        self.tb_registers_rx.setVerticalHeaderItem(7, __qtablewidgetitem95)
        __qtablewidgetitem96 = QTableWidgetItem()
        self.tb_registers_rx.setVerticalHeaderItem(8, __qtablewidgetitem96)
        __qtablewidgetitem97 = QTableWidgetItem()
        self.tb_registers_rx.setVerticalHeaderItem(9, __qtablewidgetitem97)
        __qtablewidgetitem98 = QTableWidgetItem()
        self.tb_registers_rx.setVerticalHeaderItem(10, __qtablewidgetitem98)
        __qtablewidgetitem99 = QTableWidgetItem()
        self.tb_registers_rx.setVerticalHeaderItem(11, __qtablewidgetitem99)
        __qtablewidgetitem100 = QTableWidgetItem()
        self.tb_registers_rx.setVerticalHeaderItem(12, __qtablewidgetitem100)
        __qtablewidgetitem101 = QTableWidgetItem()
        self.tb_registers_rx.setVerticalHeaderItem(13, __qtablewidgetitem101)
        __qtablewidgetitem102 = QTableWidgetItem()
        self.tb_registers_rx.setVerticalHeaderItem(14, __qtablewidgetitem102)
        __qtablewidgetitem103 = QTableWidgetItem()
        self.tb_registers_rx.setVerticalHeaderItem(15, __qtablewidgetitem103)
        __qtablewidgetitem104 = QTableWidgetItem()
        self.tb_registers_rx.setVerticalHeaderItem(16, __qtablewidgetitem104)
        __qtablewidgetitem105 = QTableWidgetItem()
        self.tb_registers_rx.setVerticalHeaderItem(17, __qtablewidgetitem105)
        __qtablewidgetitem106 = QTableWidgetItem()
        self.tb_registers_rx.setVerticalHeaderItem(18, __qtablewidgetitem106)
        __qtablewidgetitem107 = QTableWidgetItem()
        self.tb_registers_rx.setVerticalHeaderItem(19, __qtablewidgetitem107)
        __qtablewidgetitem108 = QTableWidgetItem()
        self.tb_registers_rx.setVerticalHeaderItem(20, __qtablewidgetitem108)
        __qtablewidgetitem109 = QTableWidgetItem()
        self.tb_registers_rx.setVerticalHeaderItem(21, __qtablewidgetitem109)
        __qtablewidgetitem110 = QTableWidgetItem()
        self.tb_registers_rx.setVerticalHeaderItem(22, __qtablewidgetitem110)
        __qtablewidgetitem111 = QTableWidgetItem()
        self.tb_registers_rx.setVerticalHeaderItem(23, __qtablewidgetitem111)
        __qtablewidgetitem112 = QTableWidgetItem()
        self.tb_registers_rx.setVerticalHeaderItem(24, __qtablewidgetitem112)
        __qtablewidgetitem113 = QTableWidgetItem()
        self.tb_registers_rx.setVerticalHeaderItem(25, __qtablewidgetitem113)
        __qtablewidgetitem114 = QTableWidgetItem()
        self.tb_registers_rx.setVerticalHeaderItem(26, __qtablewidgetitem114)
        __qtablewidgetitem115 = QTableWidgetItem()
        self.tb_registers_rx.setVerticalHeaderItem(27, __qtablewidgetitem115)
        __qtablewidgetitem116 = QTableWidgetItem()
        self.tb_registers_rx.setItem(0, 0, __qtablewidgetitem116)
        __qtablewidgetitem117 = QTableWidgetItem()
        self.tb_registers_rx.setItem(0, 1, __qtablewidgetitem117)
        __qtablewidgetitem118 = QTableWidgetItem()
        self.tb_registers_rx.setItem(1, 0, __qtablewidgetitem118)
        __qtablewidgetitem119 = QTableWidgetItem()
        self.tb_registers_rx.setItem(1, 1, __qtablewidgetitem119)
        __qtablewidgetitem120 = QTableWidgetItem()
        self.tb_registers_rx.setItem(2, 0, __qtablewidgetitem120)
        __qtablewidgetitem121 = QTableWidgetItem()
        self.tb_registers_rx.setItem(2, 1, __qtablewidgetitem121)
        __qtablewidgetitem122 = QTableWidgetItem()
        self.tb_registers_rx.setItem(3, 0, __qtablewidgetitem122)
        __qtablewidgetitem123 = QTableWidgetItem()
        self.tb_registers_rx.setItem(3, 1, __qtablewidgetitem123)
        __qtablewidgetitem124 = QTableWidgetItem()
        self.tb_registers_rx.setItem(4, 0, __qtablewidgetitem124)
        __qtablewidgetitem125 = QTableWidgetItem()
        self.tb_registers_rx.setItem(4, 1, __qtablewidgetitem125)
        __qtablewidgetitem126 = QTableWidgetItem()
        self.tb_registers_rx.setItem(5, 0, __qtablewidgetitem126)
        __qtablewidgetitem127 = QTableWidgetItem()
        self.tb_registers_rx.setItem(5, 1, __qtablewidgetitem127)
        __qtablewidgetitem128 = QTableWidgetItem()
        self.tb_registers_rx.setItem(6, 0, __qtablewidgetitem128)
        __qtablewidgetitem129 = QTableWidgetItem()
        self.tb_registers_rx.setItem(6, 1, __qtablewidgetitem129)
        __qtablewidgetitem130 = QTableWidgetItem()
        self.tb_registers_rx.setItem(7, 0, __qtablewidgetitem130)
        __qtablewidgetitem131 = QTableWidgetItem()
        self.tb_registers_rx.setItem(7, 1, __qtablewidgetitem131)
        __qtablewidgetitem132 = QTableWidgetItem()
        self.tb_registers_rx.setItem(8, 0, __qtablewidgetitem132)
        __qtablewidgetitem133 = QTableWidgetItem()
        self.tb_registers_rx.setItem(8, 1, __qtablewidgetitem133)
        __qtablewidgetitem134 = QTableWidgetItem()
        self.tb_registers_rx.setItem(9, 0, __qtablewidgetitem134)
        __qtablewidgetitem135 = QTableWidgetItem()
        self.tb_registers_rx.setItem(9, 1, __qtablewidgetitem135)
        __qtablewidgetitem136 = QTableWidgetItem()
        self.tb_registers_rx.setItem(10, 0, __qtablewidgetitem136)
        __qtablewidgetitem137 = QTableWidgetItem()
        self.tb_registers_rx.setItem(10, 1, __qtablewidgetitem137)
        __qtablewidgetitem138 = QTableWidgetItem()
        self.tb_registers_rx.setItem(11, 0, __qtablewidgetitem138)
        __qtablewidgetitem139 = QTableWidgetItem()
        self.tb_registers_rx.setItem(11, 1, __qtablewidgetitem139)
        __qtablewidgetitem140 = QTableWidgetItem()
        self.tb_registers_rx.setItem(12, 0, __qtablewidgetitem140)
        __qtablewidgetitem141 = QTableWidgetItem()
        self.tb_registers_rx.setItem(12, 1, __qtablewidgetitem141)
        __qtablewidgetitem142 = QTableWidgetItem()
        self.tb_registers_rx.setItem(13, 0, __qtablewidgetitem142)
        __qtablewidgetitem143 = QTableWidgetItem()
        self.tb_registers_rx.setItem(13, 1, __qtablewidgetitem143)
        __qtablewidgetitem144 = QTableWidgetItem()
        self.tb_registers_rx.setItem(14, 0, __qtablewidgetitem144)
        __qtablewidgetitem145 = QTableWidgetItem()
        self.tb_registers_rx.setItem(14, 1, __qtablewidgetitem145)
        __qtablewidgetitem146 = QTableWidgetItem()
        self.tb_registers_rx.setItem(15, 0, __qtablewidgetitem146)
        __qtablewidgetitem147 = QTableWidgetItem()
        self.tb_registers_rx.setItem(15, 1, __qtablewidgetitem147)
        __qtablewidgetitem148 = QTableWidgetItem()
        self.tb_registers_rx.setItem(16, 0, __qtablewidgetitem148)
        __qtablewidgetitem149 = QTableWidgetItem()
        self.tb_registers_rx.setItem(16, 1, __qtablewidgetitem149)
        __qtablewidgetitem150 = QTableWidgetItem()
        self.tb_registers_rx.setItem(17, 0, __qtablewidgetitem150)
        __qtablewidgetitem151 = QTableWidgetItem()
        self.tb_registers_rx.setItem(17, 1, __qtablewidgetitem151)
        __qtablewidgetitem152 = QTableWidgetItem()
        self.tb_registers_rx.setItem(18, 0, __qtablewidgetitem152)
        __qtablewidgetitem153 = QTableWidgetItem()
        self.tb_registers_rx.setItem(18, 1, __qtablewidgetitem153)
        __qtablewidgetitem154 = QTableWidgetItem()
        self.tb_registers_rx.setItem(19, 0, __qtablewidgetitem154)
        __qtablewidgetitem155 = QTableWidgetItem()
        self.tb_registers_rx.setItem(19, 1, __qtablewidgetitem155)
        __qtablewidgetitem156 = QTableWidgetItem()
        self.tb_registers_rx.setItem(20, 0, __qtablewidgetitem156)
        __qtablewidgetitem157 = QTableWidgetItem()
        self.tb_registers_rx.setItem(20, 1, __qtablewidgetitem157)
        __qtablewidgetitem158 = QTableWidgetItem()
        self.tb_registers_rx.setItem(21, 0, __qtablewidgetitem158)
        __qtablewidgetitem159 = QTableWidgetItem()
        self.tb_registers_rx.setItem(21, 1, __qtablewidgetitem159)
        __qtablewidgetitem160 = QTableWidgetItem()
        self.tb_registers_rx.setItem(22, 0, __qtablewidgetitem160)
        __qtablewidgetitem161 = QTableWidgetItem()
        self.tb_registers_rx.setItem(22, 1, __qtablewidgetitem161)
        __qtablewidgetitem162 = QTableWidgetItem()
        self.tb_registers_rx.setItem(23, 0, __qtablewidgetitem162)
        __qtablewidgetitem163 = QTableWidgetItem()
        self.tb_registers_rx.setItem(23, 1, __qtablewidgetitem163)
        __qtablewidgetitem164 = QTableWidgetItem()
        self.tb_registers_rx.setItem(24, 0, __qtablewidgetitem164)
        __qtablewidgetitem165 = QTableWidgetItem()
        self.tb_registers_rx.setItem(24, 1, __qtablewidgetitem165)
        __qtablewidgetitem166 = QTableWidgetItem()
        self.tb_registers_rx.setItem(25, 0, __qtablewidgetitem166)
        __qtablewidgetitem167 = QTableWidgetItem()
        self.tb_registers_rx.setItem(25, 1, __qtablewidgetitem167)
        __qtablewidgetitem168 = QTableWidgetItem()
        self.tb_registers_rx.setItem(26, 0, __qtablewidgetitem168)
        __qtablewidgetitem169 = QTableWidgetItem()
        self.tb_registers_rx.setItem(26, 1, __qtablewidgetitem169)
        __qtablewidgetitem170 = QTableWidgetItem()
        self.tb_registers_rx.setItem(27, 0, __qtablewidgetitem170)
        __qtablewidgetitem171 = QTableWidgetItem()
        self.tb_registers_rx.setItem(27, 1, __qtablewidgetitem171)
        self.tb_registers_rx.setObjectName(u"tb_registers_rx")
        self.tb_registers_rx.setMaximumSize(QSize(221, 581))
        self.tb_registers_rx.verticalHeader().setVisible(False)

        self.verticalLayout_11.addWidget(self.tb_registers_rx)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_reset_regs_rx = QPushButton(self.gb_receiver)
        self.btn_reset_regs_rx.setObjectName(u"btn_reset_regs_rx")

        self.horizontalLayout_4.addWidget(self.btn_reset_regs_rx)

        self.btn_refresh_regs_rx = QPushButton(self.gb_receiver)
        self.btn_refresh_regs_rx.setObjectName(u"btn_refresh_regs_rx")

        self.horizontalLayout_4.addWidget(self.btn_refresh_regs_rx)


        self.verticalLayout_11.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_13.addLayout(self.verticalLayout_11)


        self.verticalLayout_13.addLayout(self.horizontalLayout_13)


        self.horizontalLayout_21.addWidget(self.gb_receiver)


        self.verticalLayout_14.addLayout(self.horizontalLayout_21)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.transceiver_tab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.layoutWidget_2 = QWidget(self.tab_3)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 10, 221, 411))
        self.verticalLayout_16 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_3 = QTableWidget(self.layoutWidget_2)
        if (self.tableWidget_3.columnCount() < 2):
            self.tableWidget_3.setColumnCount(2)
        __qtablewidgetitem172 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem172)
        __qtablewidgetitem173 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem173)
        if (self.tableWidget_3.rowCount() < 28):
            self.tableWidget_3.setRowCount(28)
        __qtablewidgetitem174 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, __qtablewidgetitem174)
        __qtablewidgetitem175 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(1, __qtablewidgetitem175)
        __qtablewidgetitem176 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(2, __qtablewidgetitem176)
        __qtablewidgetitem177 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(3, __qtablewidgetitem177)
        __qtablewidgetitem178 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(4, __qtablewidgetitem178)
        __qtablewidgetitem179 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(5, __qtablewidgetitem179)
        __qtablewidgetitem180 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(6, __qtablewidgetitem180)
        __qtablewidgetitem181 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(7, __qtablewidgetitem181)
        __qtablewidgetitem182 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(8, __qtablewidgetitem182)
        __qtablewidgetitem183 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(9, __qtablewidgetitem183)
        __qtablewidgetitem184 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(10, __qtablewidgetitem184)
        __qtablewidgetitem185 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(11, __qtablewidgetitem185)
        __qtablewidgetitem186 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(12, __qtablewidgetitem186)
        __qtablewidgetitem187 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(13, __qtablewidgetitem187)
        __qtablewidgetitem188 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(14, __qtablewidgetitem188)
        __qtablewidgetitem189 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(15, __qtablewidgetitem189)
        __qtablewidgetitem190 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(16, __qtablewidgetitem190)
        __qtablewidgetitem191 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(17, __qtablewidgetitem191)
        __qtablewidgetitem192 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(18, __qtablewidgetitem192)
        __qtablewidgetitem193 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(19, __qtablewidgetitem193)
        __qtablewidgetitem194 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(20, __qtablewidgetitem194)
        __qtablewidgetitem195 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(21, __qtablewidgetitem195)
        __qtablewidgetitem196 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(22, __qtablewidgetitem196)
        __qtablewidgetitem197 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(23, __qtablewidgetitem197)
        __qtablewidgetitem198 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(24, __qtablewidgetitem198)
        __qtablewidgetitem199 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(25, __qtablewidgetitem199)
        __qtablewidgetitem200 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(26, __qtablewidgetitem200)
        __qtablewidgetitem201 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(27, __qtablewidgetitem201)
        __qtablewidgetitem202 = QTableWidgetItem()
        self.tableWidget_3.setItem(0, 0, __qtablewidgetitem202)
        __qtablewidgetitem203 = QTableWidgetItem()
        self.tableWidget_3.setItem(0, 1, __qtablewidgetitem203)
        __qtablewidgetitem204 = QTableWidgetItem()
        self.tableWidget_3.setItem(1, 0, __qtablewidgetitem204)
        __qtablewidgetitem205 = QTableWidgetItem()
        self.tableWidget_3.setItem(1, 1, __qtablewidgetitem205)
        __qtablewidgetitem206 = QTableWidgetItem()
        self.tableWidget_3.setItem(2, 0, __qtablewidgetitem206)
        __qtablewidgetitem207 = QTableWidgetItem()
        self.tableWidget_3.setItem(2, 1, __qtablewidgetitem207)
        __qtablewidgetitem208 = QTableWidgetItem()
        self.tableWidget_3.setItem(3, 0, __qtablewidgetitem208)
        __qtablewidgetitem209 = QTableWidgetItem()
        self.tableWidget_3.setItem(3, 1, __qtablewidgetitem209)
        __qtablewidgetitem210 = QTableWidgetItem()
        self.tableWidget_3.setItem(4, 0, __qtablewidgetitem210)
        __qtablewidgetitem211 = QTableWidgetItem()
        self.tableWidget_3.setItem(4, 1, __qtablewidgetitem211)
        __qtablewidgetitem212 = QTableWidgetItem()
        self.tableWidget_3.setItem(5, 0, __qtablewidgetitem212)
        __qtablewidgetitem213 = QTableWidgetItem()
        self.tableWidget_3.setItem(5, 1, __qtablewidgetitem213)
        __qtablewidgetitem214 = QTableWidgetItem()
        self.tableWidget_3.setItem(6, 0, __qtablewidgetitem214)
        __qtablewidgetitem215 = QTableWidgetItem()
        self.tableWidget_3.setItem(6, 1, __qtablewidgetitem215)
        __qtablewidgetitem216 = QTableWidgetItem()
        self.tableWidget_3.setItem(7, 0, __qtablewidgetitem216)
        __qtablewidgetitem217 = QTableWidgetItem()
        self.tableWidget_3.setItem(7, 1, __qtablewidgetitem217)
        __qtablewidgetitem218 = QTableWidgetItem()
        self.tableWidget_3.setItem(8, 0, __qtablewidgetitem218)
        __qtablewidgetitem219 = QTableWidgetItem()
        self.tableWidget_3.setItem(8, 1, __qtablewidgetitem219)
        __qtablewidgetitem220 = QTableWidgetItem()
        self.tableWidget_3.setItem(9, 0, __qtablewidgetitem220)
        __qtablewidgetitem221 = QTableWidgetItem()
        self.tableWidget_3.setItem(9, 1, __qtablewidgetitem221)
        __qtablewidgetitem222 = QTableWidgetItem()
        self.tableWidget_3.setItem(10, 0, __qtablewidgetitem222)
        __qtablewidgetitem223 = QTableWidgetItem()
        self.tableWidget_3.setItem(10, 1, __qtablewidgetitem223)
        __qtablewidgetitem224 = QTableWidgetItem()
        self.tableWidget_3.setItem(11, 0, __qtablewidgetitem224)
        __qtablewidgetitem225 = QTableWidgetItem()
        self.tableWidget_3.setItem(11, 1, __qtablewidgetitem225)
        __qtablewidgetitem226 = QTableWidgetItem()
        self.tableWidget_3.setItem(12, 0, __qtablewidgetitem226)
        __qtablewidgetitem227 = QTableWidgetItem()
        self.tableWidget_3.setItem(12, 1, __qtablewidgetitem227)
        __qtablewidgetitem228 = QTableWidgetItem()
        self.tableWidget_3.setItem(13, 0, __qtablewidgetitem228)
        __qtablewidgetitem229 = QTableWidgetItem()
        self.tableWidget_3.setItem(13, 1, __qtablewidgetitem229)
        __qtablewidgetitem230 = QTableWidgetItem()
        self.tableWidget_3.setItem(14, 0, __qtablewidgetitem230)
        __qtablewidgetitem231 = QTableWidgetItem()
        self.tableWidget_3.setItem(14, 1, __qtablewidgetitem231)
        __qtablewidgetitem232 = QTableWidgetItem()
        self.tableWidget_3.setItem(15, 0, __qtablewidgetitem232)
        __qtablewidgetitem233 = QTableWidgetItem()
        self.tableWidget_3.setItem(15, 1, __qtablewidgetitem233)
        __qtablewidgetitem234 = QTableWidgetItem()
        self.tableWidget_3.setItem(16, 0, __qtablewidgetitem234)
        __qtablewidgetitem235 = QTableWidgetItem()
        self.tableWidget_3.setItem(16, 1, __qtablewidgetitem235)
        __qtablewidgetitem236 = QTableWidgetItem()
        self.tableWidget_3.setItem(17, 0, __qtablewidgetitem236)
        __qtablewidgetitem237 = QTableWidgetItem()
        self.tableWidget_3.setItem(17, 1, __qtablewidgetitem237)
        __qtablewidgetitem238 = QTableWidgetItem()
        self.tableWidget_3.setItem(18, 0, __qtablewidgetitem238)
        __qtablewidgetitem239 = QTableWidgetItem()
        self.tableWidget_3.setItem(18, 1, __qtablewidgetitem239)
        __qtablewidgetitem240 = QTableWidgetItem()
        self.tableWidget_3.setItem(19, 0, __qtablewidgetitem240)
        __qtablewidgetitem241 = QTableWidgetItem()
        self.tableWidget_3.setItem(19, 1, __qtablewidgetitem241)
        __qtablewidgetitem242 = QTableWidgetItem()
        self.tableWidget_3.setItem(20, 0, __qtablewidgetitem242)
        __qtablewidgetitem243 = QTableWidgetItem()
        self.tableWidget_3.setItem(20, 1, __qtablewidgetitem243)
        __qtablewidgetitem244 = QTableWidgetItem()
        self.tableWidget_3.setItem(21, 0, __qtablewidgetitem244)
        __qtablewidgetitem245 = QTableWidgetItem()
        self.tableWidget_3.setItem(21, 1, __qtablewidgetitem245)
        __qtablewidgetitem246 = QTableWidgetItem()
        self.tableWidget_3.setItem(22, 0, __qtablewidgetitem246)
        __qtablewidgetitem247 = QTableWidgetItem()
        self.tableWidget_3.setItem(22, 1, __qtablewidgetitem247)
        __qtablewidgetitem248 = QTableWidgetItem()
        self.tableWidget_3.setItem(23, 0, __qtablewidgetitem248)
        __qtablewidgetitem249 = QTableWidgetItem()
        self.tableWidget_3.setItem(23, 1, __qtablewidgetitem249)
        __qtablewidgetitem250 = QTableWidgetItem()
        self.tableWidget_3.setItem(24, 0, __qtablewidgetitem250)
        __qtablewidgetitem251 = QTableWidgetItem()
        self.tableWidget_3.setItem(24, 1, __qtablewidgetitem251)
        __qtablewidgetitem252 = QTableWidgetItem()
        self.tableWidget_3.setItem(25, 0, __qtablewidgetitem252)
        __qtablewidgetitem253 = QTableWidgetItem()
        self.tableWidget_3.setItem(25, 1, __qtablewidgetitem253)
        __qtablewidgetitem254 = QTableWidgetItem()
        self.tableWidget_3.setItem(26, 0, __qtablewidgetitem254)
        __qtablewidgetitem255 = QTableWidgetItem()
        self.tableWidget_3.setItem(26, 1, __qtablewidgetitem255)
        __qtablewidgetitem256 = QTableWidgetItem()
        self.tableWidget_3.setItem(27, 0, __qtablewidgetitem256)
        __qtablewidgetitem257 = QTableWidgetItem()
        self.tableWidget_3.setItem(27, 1, __qtablewidgetitem257)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setMaximumSize(QSize(221, 581))
        self.tableWidget_3.verticalHeader().setVisible(False)

        self.verticalLayout_16.addWidget(self.tableWidget_3)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.pushButton_8 = QPushButton(self.layoutWidget_2)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.horizontalLayout_31.addWidget(self.pushButton_8)

        self.pushButton_13 = QPushButton(self.layoutWidget_2)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.horizontalLayout_31.addWidget(self.pushButton_13)


        self.verticalLayout_16.addLayout(self.horizontalLayout_31)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.layoutWidget_3 = QWidget(self.tab_2)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(10, 10, 221, 411))
        self.verticalLayout_17 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_4 = QTableWidget(self.layoutWidget_3)
        if (self.tableWidget_4.columnCount() < 2):
            self.tableWidget_4.setColumnCount(2)
        __qtablewidgetitem258 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem258)
        __qtablewidgetitem259 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem259)
        if (self.tableWidget_4.rowCount() < 28):
            self.tableWidget_4.setRowCount(28)
        __qtablewidgetitem260 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(0, __qtablewidgetitem260)
        __qtablewidgetitem261 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(1, __qtablewidgetitem261)
        __qtablewidgetitem262 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(2, __qtablewidgetitem262)
        __qtablewidgetitem263 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(3, __qtablewidgetitem263)
        __qtablewidgetitem264 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(4, __qtablewidgetitem264)
        __qtablewidgetitem265 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(5, __qtablewidgetitem265)
        __qtablewidgetitem266 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(6, __qtablewidgetitem266)
        __qtablewidgetitem267 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(7, __qtablewidgetitem267)
        __qtablewidgetitem268 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(8, __qtablewidgetitem268)
        __qtablewidgetitem269 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(9, __qtablewidgetitem269)
        __qtablewidgetitem270 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(10, __qtablewidgetitem270)
        __qtablewidgetitem271 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(11, __qtablewidgetitem271)
        __qtablewidgetitem272 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(12, __qtablewidgetitem272)
        __qtablewidgetitem273 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(13, __qtablewidgetitem273)
        __qtablewidgetitem274 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(14, __qtablewidgetitem274)
        __qtablewidgetitem275 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(15, __qtablewidgetitem275)
        __qtablewidgetitem276 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(16, __qtablewidgetitem276)
        __qtablewidgetitem277 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(17, __qtablewidgetitem277)
        __qtablewidgetitem278 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(18, __qtablewidgetitem278)
        __qtablewidgetitem279 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(19, __qtablewidgetitem279)
        __qtablewidgetitem280 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(20, __qtablewidgetitem280)
        __qtablewidgetitem281 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(21, __qtablewidgetitem281)
        __qtablewidgetitem282 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(22, __qtablewidgetitem282)
        __qtablewidgetitem283 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(23, __qtablewidgetitem283)
        __qtablewidgetitem284 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(24, __qtablewidgetitem284)
        __qtablewidgetitem285 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(25, __qtablewidgetitem285)
        __qtablewidgetitem286 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(26, __qtablewidgetitem286)
        __qtablewidgetitem287 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(27, __qtablewidgetitem287)
        __qtablewidgetitem288 = QTableWidgetItem()
        self.tableWidget_4.setItem(0, 0, __qtablewidgetitem288)
        __qtablewidgetitem289 = QTableWidgetItem()
        self.tableWidget_4.setItem(0, 1, __qtablewidgetitem289)
        __qtablewidgetitem290 = QTableWidgetItem()
        self.tableWidget_4.setItem(1, 0, __qtablewidgetitem290)
        __qtablewidgetitem291 = QTableWidgetItem()
        self.tableWidget_4.setItem(1, 1, __qtablewidgetitem291)
        __qtablewidgetitem292 = QTableWidgetItem()
        self.tableWidget_4.setItem(2, 0, __qtablewidgetitem292)
        __qtablewidgetitem293 = QTableWidgetItem()
        self.tableWidget_4.setItem(2, 1, __qtablewidgetitem293)
        __qtablewidgetitem294 = QTableWidgetItem()
        self.tableWidget_4.setItem(3, 0, __qtablewidgetitem294)
        __qtablewidgetitem295 = QTableWidgetItem()
        self.tableWidget_4.setItem(3, 1, __qtablewidgetitem295)
        __qtablewidgetitem296 = QTableWidgetItem()
        self.tableWidget_4.setItem(4, 0, __qtablewidgetitem296)
        __qtablewidgetitem297 = QTableWidgetItem()
        self.tableWidget_4.setItem(4, 1, __qtablewidgetitem297)
        __qtablewidgetitem298 = QTableWidgetItem()
        self.tableWidget_4.setItem(5, 0, __qtablewidgetitem298)
        __qtablewidgetitem299 = QTableWidgetItem()
        self.tableWidget_4.setItem(5, 1, __qtablewidgetitem299)
        __qtablewidgetitem300 = QTableWidgetItem()
        self.tableWidget_4.setItem(6, 0, __qtablewidgetitem300)
        __qtablewidgetitem301 = QTableWidgetItem()
        self.tableWidget_4.setItem(6, 1, __qtablewidgetitem301)
        __qtablewidgetitem302 = QTableWidgetItem()
        self.tableWidget_4.setItem(7, 0, __qtablewidgetitem302)
        __qtablewidgetitem303 = QTableWidgetItem()
        self.tableWidget_4.setItem(7, 1, __qtablewidgetitem303)
        __qtablewidgetitem304 = QTableWidgetItem()
        self.tableWidget_4.setItem(8, 0, __qtablewidgetitem304)
        __qtablewidgetitem305 = QTableWidgetItem()
        self.tableWidget_4.setItem(8, 1, __qtablewidgetitem305)
        __qtablewidgetitem306 = QTableWidgetItem()
        self.tableWidget_4.setItem(9, 0, __qtablewidgetitem306)
        __qtablewidgetitem307 = QTableWidgetItem()
        self.tableWidget_4.setItem(9, 1, __qtablewidgetitem307)
        __qtablewidgetitem308 = QTableWidgetItem()
        self.tableWidget_4.setItem(10, 0, __qtablewidgetitem308)
        __qtablewidgetitem309 = QTableWidgetItem()
        self.tableWidget_4.setItem(10, 1, __qtablewidgetitem309)
        __qtablewidgetitem310 = QTableWidgetItem()
        self.tableWidget_4.setItem(11, 0, __qtablewidgetitem310)
        __qtablewidgetitem311 = QTableWidgetItem()
        self.tableWidget_4.setItem(11, 1, __qtablewidgetitem311)
        __qtablewidgetitem312 = QTableWidgetItem()
        self.tableWidget_4.setItem(12, 0, __qtablewidgetitem312)
        __qtablewidgetitem313 = QTableWidgetItem()
        self.tableWidget_4.setItem(12, 1, __qtablewidgetitem313)
        __qtablewidgetitem314 = QTableWidgetItem()
        self.tableWidget_4.setItem(13, 0, __qtablewidgetitem314)
        __qtablewidgetitem315 = QTableWidgetItem()
        self.tableWidget_4.setItem(13, 1, __qtablewidgetitem315)
        __qtablewidgetitem316 = QTableWidgetItem()
        self.tableWidget_4.setItem(14, 0, __qtablewidgetitem316)
        __qtablewidgetitem317 = QTableWidgetItem()
        self.tableWidget_4.setItem(14, 1, __qtablewidgetitem317)
        __qtablewidgetitem318 = QTableWidgetItem()
        self.tableWidget_4.setItem(15, 0, __qtablewidgetitem318)
        __qtablewidgetitem319 = QTableWidgetItem()
        self.tableWidget_4.setItem(15, 1, __qtablewidgetitem319)
        __qtablewidgetitem320 = QTableWidgetItem()
        self.tableWidget_4.setItem(16, 0, __qtablewidgetitem320)
        __qtablewidgetitem321 = QTableWidgetItem()
        self.tableWidget_4.setItem(16, 1, __qtablewidgetitem321)
        __qtablewidgetitem322 = QTableWidgetItem()
        self.tableWidget_4.setItem(17, 0, __qtablewidgetitem322)
        __qtablewidgetitem323 = QTableWidgetItem()
        self.tableWidget_4.setItem(17, 1, __qtablewidgetitem323)
        __qtablewidgetitem324 = QTableWidgetItem()
        self.tableWidget_4.setItem(18, 0, __qtablewidgetitem324)
        __qtablewidgetitem325 = QTableWidgetItem()
        self.tableWidget_4.setItem(18, 1, __qtablewidgetitem325)
        __qtablewidgetitem326 = QTableWidgetItem()
        self.tableWidget_4.setItem(19, 0, __qtablewidgetitem326)
        __qtablewidgetitem327 = QTableWidgetItem()
        self.tableWidget_4.setItem(19, 1, __qtablewidgetitem327)
        __qtablewidgetitem328 = QTableWidgetItem()
        self.tableWidget_4.setItem(20, 0, __qtablewidgetitem328)
        __qtablewidgetitem329 = QTableWidgetItem()
        self.tableWidget_4.setItem(20, 1, __qtablewidgetitem329)
        __qtablewidgetitem330 = QTableWidgetItem()
        self.tableWidget_4.setItem(21, 0, __qtablewidgetitem330)
        __qtablewidgetitem331 = QTableWidgetItem()
        self.tableWidget_4.setItem(21, 1, __qtablewidgetitem331)
        __qtablewidgetitem332 = QTableWidgetItem()
        self.tableWidget_4.setItem(22, 0, __qtablewidgetitem332)
        __qtablewidgetitem333 = QTableWidgetItem()
        self.tableWidget_4.setItem(22, 1, __qtablewidgetitem333)
        __qtablewidgetitem334 = QTableWidgetItem()
        self.tableWidget_4.setItem(23, 0, __qtablewidgetitem334)
        __qtablewidgetitem335 = QTableWidgetItem()
        self.tableWidget_4.setItem(23, 1, __qtablewidgetitem335)
        __qtablewidgetitem336 = QTableWidgetItem()
        self.tableWidget_4.setItem(24, 0, __qtablewidgetitem336)
        __qtablewidgetitem337 = QTableWidgetItem()
        self.tableWidget_4.setItem(24, 1, __qtablewidgetitem337)
        __qtablewidgetitem338 = QTableWidgetItem()
        self.tableWidget_4.setItem(25, 0, __qtablewidgetitem338)
        __qtablewidgetitem339 = QTableWidgetItem()
        self.tableWidget_4.setItem(25, 1, __qtablewidgetitem339)
        __qtablewidgetitem340 = QTableWidgetItem()
        self.tableWidget_4.setItem(26, 0, __qtablewidgetitem340)
        __qtablewidgetitem341 = QTableWidgetItem()
        self.tableWidget_4.setItem(26, 1, __qtablewidgetitem341)
        __qtablewidgetitem342 = QTableWidgetItem()
        self.tableWidget_4.setItem(27, 0, __qtablewidgetitem342)
        __qtablewidgetitem343 = QTableWidgetItem()
        self.tableWidget_4.setItem(27, 1, __qtablewidgetitem343)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.setMaximumSize(QSize(221, 581))
        self.tableWidget_4.verticalHeader().setVisible(False)

        self.verticalLayout_17.addWidget(self.tableWidget_4)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.pushButton_14 = QPushButton(self.layoutWidget_3)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.horizontalLayout_32.addWidget(self.pushButton_14)

        self.pushButton_15 = QPushButton(self.layoutWidget_3)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.horizontalLayout_32.addWidget(self.pushButton_15)


        self.verticalLayout_17.addLayout(self.horizontalLayout_32)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        AlternativeWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(AlternativeWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 984, 22))
        AlternativeWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(AlternativeWindow)
        self.statusbar.setObjectName(u"statusbar")
        AlternativeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AlternativeWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(AlternativeWindow)
    # setupUi

    def retranslateUi(self, AlternativeWindow):
        AlternativeWindow.setWindowTitle(QCoreApplication.translate("AlternativeWindow", u"MainWindow", None))
        self.lbl_available_contexts.setText(QCoreApplication.translate("AlternativeWindow", u"Available contexts", None))
        self.cb_available_contexts.setItemText(0, QCoreApplication.translate("AlternativeWindow", u"usb:2.3.1", None))
        self.cb_available_contexts.setItemText(1, QCoreApplication.translate("AlternativeWindow", u"usb:3.1.5", None))

        self.lbl_hardware_name.setText(QCoreApplication.translate("AlternativeWindow", u"Hardware name:", None))
        self.lbl_hardware_name_dyn.setText(QCoreApplication.translate("AlternativeWindow", u"No context", None))
        self.lbl_vendor.setText(QCoreApplication.translate("AlternativeWindow", u"Vendor:", None))
        self.lbl_vendor_dyn.setText(QCoreApplication.translate("AlternativeWindow", u"No context", None))
        self.lbl_hardware_carrier.setText(QCoreApplication.translate("AlternativeWindow", u"Hardware carrier:", None))
        self.lbl_hardware_carrier_dyn.setText(QCoreApplication.translate("AlternativeWindow", u"No context", None))
        self.lbl_hardware_serial.setText(QCoreApplication.translate("AlternativeWindow", u"Hardware serial:", None))
        self.lbl_hardware_serial_dyn.setText(QCoreApplication.translate("AlternativeWindow", u"No context", None))
        self.lbl_local.setText(QCoreApplication.translate("AlternativeWindow", u"Local:", None))
        self.lbl_local_dyn.setText(QCoreApplication.translate("AlternativeWindow", u"No context", None))
        self.gb_transmitter.setTitle(QCoreApplication.translate("AlternativeWindow", u"Transmitter (TX)", None))
        self.lbl_power_tx.setText(QCoreApplication.translate("AlternativeWindow", u"Power", None))
        self.btn_power_tx.setText(QCoreApplication.translate("AlternativeWindow", u"Turn ON", None))
        self.lbl_lo_frequency_tx.setText(QCoreApplication.translate("AlternativeWindow", u"LO Frequency", None))
        self.cb_lo_frequency_tx.setItemText(0, QCoreApplication.translate("AlternativeWindow", u"value1", None))
        self.cb_lo_frequency_tx.setItemText(1, QCoreApplication.translate("AlternativeWindow", u"value2", None))

        self.chk_autotuning_tx.setText(QCoreApplication.translate("AlternativeWindow", u"Autotuning", None))
        self.lbl_gain_tx.setText(QCoreApplication.translate("AlternativeWindow", u"Gain", None))
        self.cb_gain_tx.setItemText(0, QCoreApplication.translate("AlternativeWindow", u"value1", None))
        self.cb_gain_tx.setItemText(1, QCoreApplication.translate("AlternativeWindow", u"value2", None))

        self.lbl_rf_attn_index.setText(QCoreApplication.translate("AlternativeWindow", u"RF Attn Index", None))
        self.cb_rf_attn_index.setItemText(0, QCoreApplication.translate("AlternativeWindow", u"value1", None))
        self.cb_rf_attn_index.setItemText(1, QCoreApplication.translate("AlternativeWindow", u"value2", None))

        self.gb_status_tx.setTitle(QCoreApplication.translate("AlternativeWindow", u"Status", None))
        self.lbl_lock_detect_tx.setText(QCoreApplication.translate("AlternativeWindow", u"Lock Detect", None))
        self.lbl_temp_tx.setText(QCoreApplication.translate("AlternativeWindow", u"Temperature:", None))
        self.lbl_temp_tx_dyn.setText(QCoreApplication.translate("AlternativeWindow", u"15 \u00b0C", None))
        self.lbl_power_usage_tx.setText(QCoreApplication.translate("AlternativeWindow", u"Power:", None))
        self.lbl_power_usage_tx_dyn.setText(QCoreApplication.translate("AlternativeWindow", u"200 mV", None))
        ___qtablewidgetitem = self.tb_registers_tx.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AlternativeWindow", u"Address", None));
        ___qtablewidgetitem1 = self.tb_registers_tx.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("AlternativeWindow", u"Data", None));
        ___qtablewidgetitem2 = self.tb_registers_tx.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("AlternativeWindow", u"0", None));
        ___qtablewidgetitem3 = self.tb_registers_tx.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("AlternativeWindow", u"1", None));
        ___qtablewidgetitem4 = self.tb_registers_tx.verticalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("AlternativeWindow", u"2", None));
        ___qtablewidgetitem5 = self.tb_registers_tx.verticalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("AlternativeWindow", u"3", None));
        ___qtablewidgetitem6 = self.tb_registers_tx.verticalHeaderItem(4)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("AlternativeWindow", u"4", None));
        ___qtablewidgetitem7 = self.tb_registers_tx.verticalHeaderItem(5)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("AlternativeWindow", u"5", None));
        ___qtablewidgetitem8 = self.tb_registers_tx.verticalHeaderItem(6)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("AlternativeWindow", u"6", None));
        ___qtablewidgetitem9 = self.tb_registers_tx.verticalHeaderItem(7)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("AlternativeWindow", u"7", None));
        ___qtablewidgetitem10 = self.tb_registers_tx.verticalHeaderItem(8)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("AlternativeWindow", u"8", None));
        ___qtablewidgetitem11 = self.tb_registers_tx.verticalHeaderItem(9)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("AlternativeWindow", u"9", None));
        ___qtablewidgetitem12 = self.tb_registers_tx.verticalHeaderItem(10)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("AlternativeWindow", u"10", None));
        ___qtablewidgetitem13 = self.tb_registers_tx.verticalHeaderItem(11)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("AlternativeWindow", u"11", None));
        ___qtablewidgetitem14 = self.tb_registers_tx.verticalHeaderItem(12)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("AlternativeWindow", u"12", None));
        ___qtablewidgetitem15 = self.tb_registers_tx.verticalHeaderItem(13)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("AlternativeWindow", u"13", None));
        ___qtablewidgetitem16 = self.tb_registers_tx.verticalHeaderItem(14)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("AlternativeWindow", u"14", None));
        ___qtablewidgetitem17 = self.tb_registers_tx.verticalHeaderItem(15)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("AlternativeWindow", u"15", None));
        ___qtablewidgetitem18 = self.tb_registers_tx.verticalHeaderItem(16)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("AlternativeWindow", u"16", None));
        ___qtablewidgetitem19 = self.tb_registers_tx.verticalHeaderItem(17)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("AlternativeWindow", u"17", None));
        ___qtablewidgetitem20 = self.tb_registers_tx.verticalHeaderItem(18)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("AlternativeWindow", u"18", None));
        ___qtablewidgetitem21 = self.tb_registers_tx.verticalHeaderItem(19)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("AlternativeWindow", u"19", None));
        ___qtablewidgetitem22 = self.tb_registers_tx.verticalHeaderItem(20)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("AlternativeWindow", u"20", None));
        ___qtablewidgetitem23 = self.tb_registers_tx.verticalHeaderItem(21)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("AlternativeWindow", u"21", None));
        ___qtablewidgetitem24 = self.tb_registers_tx.verticalHeaderItem(22)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("AlternativeWindow", u"22", None));
        ___qtablewidgetitem25 = self.tb_registers_tx.verticalHeaderItem(23)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("AlternativeWindow", u"23", None));
        ___qtablewidgetitem26 = self.tb_registers_tx.verticalHeaderItem(24)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("AlternativeWindow", u"24", None));
        ___qtablewidgetitem27 = self.tb_registers_tx.verticalHeaderItem(25)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("AlternativeWindow", u"25", None));
        ___qtablewidgetitem28 = self.tb_registers_tx.verticalHeaderItem(26)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("AlternativeWindow", u"26", None));
        ___qtablewidgetitem29 = self.tb_registers_tx.verticalHeaderItem(27)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("AlternativeWindow", u"27", None));

        __sortingEnabled = self.tb_registers_tx.isSortingEnabled()
        self.tb_registers_tx.setSortingEnabled(False)
        ___qtablewidgetitem30 = self.tb_registers_tx.item(0, 0)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("AlternativeWindow", u"0x00", None));
        ___qtablewidgetitem31 = self.tb_registers_tx.item(0, 1)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("AlternativeWindow", u"34", None));
        ___qtablewidgetitem32 = self.tb_registers_tx.item(1, 0)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("AlternativeWindow", u"0x01", None));
        ___qtablewidgetitem33 = self.tb_registers_tx.item(1, 1)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("AlternativeWindow", u"4A", None));
        ___qtablewidgetitem34 = self.tb_registers_tx.item(2, 0)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("AlternativeWindow", u"0x02", None));
        ___qtablewidgetitem35 = self.tb_registers_tx.item(2, 1)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("AlternativeWindow", u"32", None));
        ___qtablewidgetitem36 = self.tb_registers_tx.item(3, 0)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("AlternativeWindow", u"0x03", None));
        ___qtablewidgetitem37 = self.tb_registers_tx.item(3, 1)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("AlternativeWindow", u"43", None));
        ___qtablewidgetitem38 = self.tb_registers_tx.item(4, 0)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("AlternativeWindow", u"0x04", None));
        ___qtablewidgetitem39 = self.tb_registers_tx.item(4, 1)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("AlternativeWindow", u"9F", None));
        ___qtablewidgetitem40 = self.tb_registers_tx.item(5, 0)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("AlternativeWindow", u"0x05", None));
        ___qtablewidgetitem41 = self.tb_registers_tx.item(5, 1)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("AlternativeWindow", u"BF", None));
        ___qtablewidgetitem42 = self.tb_registers_tx.item(6, 0)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("AlternativeWindow", u"0x06", None));
        ___qtablewidgetitem43 = self.tb_registers_tx.item(6, 1)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("AlternativeWindow", u"6D", None));
        ___qtablewidgetitem44 = self.tb_registers_tx.item(7, 0)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("AlternativeWindow", u"0x07", None));
        ___qtablewidgetitem45 = self.tb_registers_tx.item(7, 1)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("AlternativeWindow", u"90", None));
        ___qtablewidgetitem46 = self.tb_registers_tx.item(8, 0)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("AlternativeWindow", u"0x08", None));
        ___qtablewidgetitem47 = self.tb_registers_tx.item(8, 1)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("AlternativeWindow", u"40", None));
        ___qtablewidgetitem48 = self.tb_registers_tx.item(9, 0)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("AlternativeWindow", u"0x09", None));
        ___qtablewidgetitem49 = self.tb_registers_tx.item(9, 1)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("AlternativeWindow", u"36", None));
        ___qtablewidgetitem50 = self.tb_registers_tx.item(10, 0)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("AlternativeWindow", u"0x0A", None));
        ___qtablewidgetitem51 = self.tb_registers_tx.item(10, 1)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("AlternativeWindow", u"BB", None));
        ___qtablewidgetitem52 = self.tb_registers_tx.item(11, 0)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("AlternativeWindow", u"0x0B", None));
        ___qtablewidgetitem53 = self.tb_registers_tx.item(11, 1)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("AlternativeWindow", u"46", None));
        ___qtablewidgetitem54 = self.tb_registers_tx.item(12, 0)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("AlternativeWindow", u"0x0C", None));
        ___qtablewidgetitem55 = self.tb_registers_tx.item(12, 1)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("AlternativeWindow", u"02", None));
        ___qtablewidgetitem56 = self.tb_registers_tx.item(13, 0)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("AlternativeWindow", u"0x0D", None));
        ___qtablewidgetitem57 = self.tb_registers_tx.item(13, 1)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("AlternativeWindow", u"1D", None));
        ___qtablewidgetitem58 = self.tb_registers_tx.item(14, 0)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("AlternativeWindow", u"0x0E", None));
        ___qtablewidgetitem59 = self.tb_registers_tx.item(14, 1)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("AlternativeWindow", u"12", None));
        ___qtablewidgetitem60 = self.tb_registers_tx.item(15, 0)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("AlternativeWindow", u"0x0F", None));
        ___qtablewidgetitem61 = self.tb_registers_tx.item(15, 1)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("AlternativeWindow", u"05", None));
        ___qtablewidgetitem62 = self.tb_registers_tx.item(16, 0)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("AlternativeWindow", u"0x10", None));
        ___qtablewidgetitem63 = self.tb_registers_tx.item(16, 1)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("AlternativeWindow", u"62", None));
        ___qtablewidgetitem64 = self.tb_registers_tx.item(17, 0)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("AlternativeWindow", u"0x11", None));
        ___qtablewidgetitem65 = self.tb_registers_tx.item(17, 1)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("AlternativeWindow", u"C1", None));
        ___qtablewidgetitem66 = self.tb_registers_tx.item(18, 0)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("AlternativeWindow", u"0x12", None));
        ___qtablewidgetitem67 = self.tb_registers_tx.item(18, 1)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("AlternativeWindow", u"1D", None));
        ___qtablewidgetitem68 = self.tb_registers_tx.item(19, 0)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("AlternativeWindow", u"0x13", None));
        ___qtablewidgetitem69 = self.tb_registers_tx.item(19, 1)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("AlternativeWindow", u"41", None));
        ___qtablewidgetitem70 = self.tb_registers_tx.item(20, 0)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("AlternativeWindow", u"0x14", None));
        ___qtablewidgetitem71 = self.tb_registers_tx.item(20, 1)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("AlternativeWindow", u"32", None));
        ___qtablewidgetitem72 = self.tb_registers_tx.item(21, 0)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("AlternativeWindow", u"0x15", None));
        ___qtablewidgetitem73 = self.tb_registers_tx.item(21, 1)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("AlternativeWindow", u"9B", None));
        ___qtablewidgetitem74 = self.tb_registers_tx.item(22, 0)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("AlternativeWindow", u"0x16", None));
        ___qtablewidgetitem75 = self.tb_registers_tx.item(22, 1)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("AlternativeWindow", u"BF", None));
        ___qtablewidgetitem76 = self.tb_registers_tx.item(23, 0)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("AlternativeWindow", u"0x17", None));
        ___qtablewidgetitem77 = self.tb_registers_tx.item(23, 1)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("AlternativeWindow", u"51", None));
        ___qtablewidgetitem78 = self.tb_registers_tx.item(24, 0)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("AlternativeWindow", u"0x18", None));
        ___qtablewidgetitem79 = self.tb_registers_tx.item(24, 1)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("AlternativeWindow", u"24", None));
        ___qtablewidgetitem80 = self.tb_registers_tx.item(25, 0)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("AlternativeWindow", u"0x19", None));
        ___qtablewidgetitem81 = self.tb_registers_tx.item(25, 1)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("AlternativeWindow", u"71", None));
        ___qtablewidgetitem82 = self.tb_registers_tx.item(26, 0)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("AlternativeWindow", u"0x1A", None));
        ___qtablewidgetitem83 = self.tb_registers_tx.item(26, 1)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("AlternativeWindow", u"C5", None));
        ___qtablewidgetitem84 = self.tb_registers_tx.item(27, 0)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("AlternativeWindow", u"0x1B", None));
        ___qtablewidgetitem85 = self.tb_registers_tx.item(27, 1)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("AlternativeWindow", u"23", None));
        self.tb_registers_tx.setSortingEnabled(__sortingEnabled)

        self.btn_reset_regs_tx.setText(QCoreApplication.translate("AlternativeWindow", u"Reset", None))
        self.btn_refresh_regs_tx.setText(QCoreApplication.translate("AlternativeWindow", u"Refresh", None))
        self.gb_receiver.setTitle(QCoreApplication.translate("AlternativeWindow", u"Receiver (RX)", None))
        self.lbl_power_rx.setText(QCoreApplication.translate("AlternativeWindow", u"Power", None))
        self.btn_power_rx.setText(QCoreApplication.translate("AlternativeWindow", u"Turn ON", None))
        self.lbl_lo_frequency_rx.setText(QCoreApplication.translate("AlternativeWindow", u"LO Frequency", None))
        self.cb_lo_frequency_rx.setItemText(0, QCoreApplication.translate("AlternativeWindow", u"value1", None))
        self.cb_lo_frequency_rx.setItemText(1, QCoreApplication.translate("AlternativeWindow", u"value2", None))

        self.chk_autotuning_rx.setText(QCoreApplication.translate("AlternativeWindow", u"Autotuning", None))
        self.lbl_gain_rx.setText(QCoreApplication.translate("AlternativeWindow", u"Gain", None))
        self.cb_gain_rx.setItemText(0, QCoreApplication.translate("AlternativeWindow", u"value1", None))
        self.cb_gain_rx.setItemText(1, QCoreApplication.translate("AlternativeWindow", u"value2", None))

        self.lbl_bb_attn_index.setText(QCoreApplication.translate("AlternativeWindow", u"BB Attn Index", None))
        self.cb_bb_attn_index.setItemText(0, QCoreApplication.translate("AlternativeWindow", u"value1", None))
        self.cb_bb_attn_index.setItemText(1, QCoreApplication.translate("AlternativeWindow", u"value2", None))

        self.gb_status_rx.setTitle(QCoreApplication.translate("AlternativeWindow", u"Status", None))
        self.lbl_lock_detect_rx.setText(QCoreApplication.translate("AlternativeWindow", u"Lock Detect", None))
        self.lbl_temp_rx.setText(QCoreApplication.translate("AlternativeWindow", u"Temperature:", None))
        self.lbl_temp_rx_dyn.setText(QCoreApplication.translate("AlternativeWindow", u"15 \u00b0C", None))
        self.lbl_power_usage_rx.setText(QCoreApplication.translate("AlternativeWindow", u"Power:", None))
        self.lbl_power_usage_rx_dyn.setText(QCoreApplication.translate("AlternativeWindow", u"255 mV", None))
        ___qtablewidgetitem86 = self.tb_registers_rx.horizontalHeaderItem(0)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("AlternativeWindow", u"Address", None));
        ___qtablewidgetitem87 = self.tb_registers_rx.horizontalHeaderItem(1)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("AlternativeWindow", u"Data", None));
        ___qtablewidgetitem88 = self.tb_registers_rx.verticalHeaderItem(0)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("AlternativeWindow", u"0", None));
        ___qtablewidgetitem89 = self.tb_registers_rx.verticalHeaderItem(1)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("AlternativeWindow", u"1", None));
        ___qtablewidgetitem90 = self.tb_registers_rx.verticalHeaderItem(2)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("AlternativeWindow", u"2", None));
        ___qtablewidgetitem91 = self.tb_registers_rx.verticalHeaderItem(3)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("AlternativeWindow", u"3", None));
        ___qtablewidgetitem92 = self.tb_registers_rx.verticalHeaderItem(4)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("AlternativeWindow", u"4", None));
        ___qtablewidgetitem93 = self.tb_registers_rx.verticalHeaderItem(5)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("AlternativeWindow", u"5", None));
        ___qtablewidgetitem94 = self.tb_registers_rx.verticalHeaderItem(6)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("AlternativeWindow", u"6", None));
        ___qtablewidgetitem95 = self.tb_registers_rx.verticalHeaderItem(7)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("AlternativeWindow", u"7", None));
        ___qtablewidgetitem96 = self.tb_registers_rx.verticalHeaderItem(8)
        ___qtablewidgetitem96.setText(QCoreApplication.translate("AlternativeWindow", u"8", None));
        ___qtablewidgetitem97 = self.tb_registers_rx.verticalHeaderItem(9)
        ___qtablewidgetitem97.setText(QCoreApplication.translate("AlternativeWindow", u"9", None));
        ___qtablewidgetitem98 = self.tb_registers_rx.verticalHeaderItem(10)
        ___qtablewidgetitem98.setText(QCoreApplication.translate("AlternativeWindow", u"10", None));
        ___qtablewidgetitem99 = self.tb_registers_rx.verticalHeaderItem(11)
        ___qtablewidgetitem99.setText(QCoreApplication.translate("AlternativeWindow", u"11", None));
        ___qtablewidgetitem100 = self.tb_registers_rx.verticalHeaderItem(12)
        ___qtablewidgetitem100.setText(QCoreApplication.translate("AlternativeWindow", u"12", None));
        ___qtablewidgetitem101 = self.tb_registers_rx.verticalHeaderItem(13)
        ___qtablewidgetitem101.setText(QCoreApplication.translate("AlternativeWindow", u"13", None));
        ___qtablewidgetitem102 = self.tb_registers_rx.verticalHeaderItem(14)
        ___qtablewidgetitem102.setText(QCoreApplication.translate("AlternativeWindow", u"14", None));
        ___qtablewidgetitem103 = self.tb_registers_rx.verticalHeaderItem(15)
        ___qtablewidgetitem103.setText(QCoreApplication.translate("AlternativeWindow", u"15", None));
        ___qtablewidgetitem104 = self.tb_registers_rx.verticalHeaderItem(16)
        ___qtablewidgetitem104.setText(QCoreApplication.translate("AlternativeWindow", u"16", None));
        ___qtablewidgetitem105 = self.tb_registers_rx.verticalHeaderItem(17)
        ___qtablewidgetitem105.setText(QCoreApplication.translate("AlternativeWindow", u"17", None));
        ___qtablewidgetitem106 = self.tb_registers_rx.verticalHeaderItem(18)
        ___qtablewidgetitem106.setText(QCoreApplication.translate("AlternativeWindow", u"18", None));
        ___qtablewidgetitem107 = self.tb_registers_rx.verticalHeaderItem(19)
        ___qtablewidgetitem107.setText(QCoreApplication.translate("AlternativeWindow", u"19", None));
        ___qtablewidgetitem108 = self.tb_registers_rx.verticalHeaderItem(20)
        ___qtablewidgetitem108.setText(QCoreApplication.translate("AlternativeWindow", u"20", None));
        ___qtablewidgetitem109 = self.tb_registers_rx.verticalHeaderItem(21)
        ___qtablewidgetitem109.setText(QCoreApplication.translate("AlternativeWindow", u"21", None));
        ___qtablewidgetitem110 = self.tb_registers_rx.verticalHeaderItem(22)
        ___qtablewidgetitem110.setText(QCoreApplication.translate("AlternativeWindow", u"22", None));
        ___qtablewidgetitem111 = self.tb_registers_rx.verticalHeaderItem(23)
        ___qtablewidgetitem111.setText(QCoreApplication.translate("AlternativeWindow", u"23", None));
        ___qtablewidgetitem112 = self.tb_registers_rx.verticalHeaderItem(24)
        ___qtablewidgetitem112.setText(QCoreApplication.translate("AlternativeWindow", u"24", None));
        ___qtablewidgetitem113 = self.tb_registers_rx.verticalHeaderItem(25)
        ___qtablewidgetitem113.setText(QCoreApplication.translate("AlternativeWindow", u"25", None));
        ___qtablewidgetitem114 = self.tb_registers_rx.verticalHeaderItem(26)
        ___qtablewidgetitem114.setText(QCoreApplication.translate("AlternativeWindow", u"26", None));
        ___qtablewidgetitem115 = self.tb_registers_rx.verticalHeaderItem(27)
        ___qtablewidgetitem115.setText(QCoreApplication.translate("AlternativeWindow", u"27", None));

        __sortingEnabled1 = self.tb_registers_rx.isSortingEnabled()
        self.tb_registers_rx.setSortingEnabled(False)
        ___qtablewidgetitem116 = self.tb_registers_rx.item(0, 0)
        ___qtablewidgetitem116.setText(QCoreApplication.translate("AlternativeWindow", u"0x00", None));
        ___qtablewidgetitem117 = self.tb_registers_rx.item(0, 1)
        ___qtablewidgetitem117.setText(QCoreApplication.translate("AlternativeWindow", u"34", None));
        ___qtablewidgetitem118 = self.tb_registers_rx.item(1, 0)
        ___qtablewidgetitem118.setText(QCoreApplication.translate("AlternativeWindow", u"0x01", None));
        ___qtablewidgetitem119 = self.tb_registers_rx.item(1, 1)
        ___qtablewidgetitem119.setText(QCoreApplication.translate("AlternativeWindow", u"4A", None));
        ___qtablewidgetitem120 = self.tb_registers_rx.item(2, 0)
        ___qtablewidgetitem120.setText(QCoreApplication.translate("AlternativeWindow", u"0x02", None));
        ___qtablewidgetitem121 = self.tb_registers_rx.item(2, 1)
        ___qtablewidgetitem121.setText(QCoreApplication.translate("AlternativeWindow", u"32", None));
        ___qtablewidgetitem122 = self.tb_registers_rx.item(3, 0)
        ___qtablewidgetitem122.setText(QCoreApplication.translate("AlternativeWindow", u"0x03", None));
        ___qtablewidgetitem123 = self.tb_registers_rx.item(3, 1)
        ___qtablewidgetitem123.setText(QCoreApplication.translate("AlternativeWindow", u"43", None));
        ___qtablewidgetitem124 = self.tb_registers_rx.item(4, 0)
        ___qtablewidgetitem124.setText(QCoreApplication.translate("AlternativeWindow", u"0x04", None));
        ___qtablewidgetitem125 = self.tb_registers_rx.item(4, 1)
        ___qtablewidgetitem125.setText(QCoreApplication.translate("AlternativeWindow", u"9F", None));
        ___qtablewidgetitem126 = self.tb_registers_rx.item(5, 0)
        ___qtablewidgetitem126.setText(QCoreApplication.translate("AlternativeWindow", u"0x05", None));
        ___qtablewidgetitem127 = self.tb_registers_rx.item(5, 1)
        ___qtablewidgetitem127.setText(QCoreApplication.translate("AlternativeWindow", u"BF", None));
        ___qtablewidgetitem128 = self.tb_registers_rx.item(6, 0)
        ___qtablewidgetitem128.setText(QCoreApplication.translate("AlternativeWindow", u"0x06", None));
        ___qtablewidgetitem129 = self.tb_registers_rx.item(6, 1)
        ___qtablewidgetitem129.setText(QCoreApplication.translate("AlternativeWindow", u"6D", None));
        ___qtablewidgetitem130 = self.tb_registers_rx.item(7, 0)
        ___qtablewidgetitem130.setText(QCoreApplication.translate("AlternativeWindow", u"0x07", None));
        ___qtablewidgetitem131 = self.tb_registers_rx.item(7, 1)
        ___qtablewidgetitem131.setText(QCoreApplication.translate("AlternativeWindow", u"90", None));
        ___qtablewidgetitem132 = self.tb_registers_rx.item(8, 0)
        ___qtablewidgetitem132.setText(QCoreApplication.translate("AlternativeWindow", u"0x08", None));
        ___qtablewidgetitem133 = self.tb_registers_rx.item(8, 1)
        ___qtablewidgetitem133.setText(QCoreApplication.translate("AlternativeWindow", u"40", None));
        ___qtablewidgetitem134 = self.tb_registers_rx.item(9, 0)
        ___qtablewidgetitem134.setText(QCoreApplication.translate("AlternativeWindow", u"0x09", None));
        ___qtablewidgetitem135 = self.tb_registers_rx.item(9, 1)
        ___qtablewidgetitem135.setText(QCoreApplication.translate("AlternativeWindow", u"36", None));
        ___qtablewidgetitem136 = self.tb_registers_rx.item(10, 0)
        ___qtablewidgetitem136.setText(QCoreApplication.translate("AlternativeWindow", u"0x0A", None));
        ___qtablewidgetitem137 = self.tb_registers_rx.item(10, 1)
        ___qtablewidgetitem137.setText(QCoreApplication.translate("AlternativeWindow", u"BB", None));
        ___qtablewidgetitem138 = self.tb_registers_rx.item(11, 0)
        ___qtablewidgetitem138.setText(QCoreApplication.translate("AlternativeWindow", u"0x0B", None));
        ___qtablewidgetitem139 = self.tb_registers_rx.item(11, 1)
        ___qtablewidgetitem139.setText(QCoreApplication.translate("AlternativeWindow", u"46", None));
        ___qtablewidgetitem140 = self.tb_registers_rx.item(12, 0)
        ___qtablewidgetitem140.setText(QCoreApplication.translate("AlternativeWindow", u"0x0C", None));
        ___qtablewidgetitem141 = self.tb_registers_rx.item(12, 1)
        ___qtablewidgetitem141.setText(QCoreApplication.translate("AlternativeWindow", u"02", None));
        ___qtablewidgetitem142 = self.tb_registers_rx.item(13, 0)
        ___qtablewidgetitem142.setText(QCoreApplication.translate("AlternativeWindow", u"0x0D", None));
        ___qtablewidgetitem143 = self.tb_registers_rx.item(13, 1)
        ___qtablewidgetitem143.setText(QCoreApplication.translate("AlternativeWindow", u"1D", None));
        ___qtablewidgetitem144 = self.tb_registers_rx.item(14, 0)
        ___qtablewidgetitem144.setText(QCoreApplication.translate("AlternativeWindow", u"0x0E", None));
        ___qtablewidgetitem145 = self.tb_registers_rx.item(14, 1)
        ___qtablewidgetitem145.setText(QCoreApplication.translate("AlternativeWindow", u"12", None));
        ___qtablewidgetitem146 = self.tb_registers_rx.item(15, 0)
        ___qtablewidgetitem146.setText(QCoreApplication.translate("AlternativeWindow", u"0x0F", None));
        ___qtablewidgetitem147 = self.tb_registers_rx.item(15, 1)
        ___qtablewidgetitem147.setText(QCoreApplication.translate("AlternativeWindow", u"05", None));
        ___qtablewidgetitem148 = self.tb_registers_rx.item(16, 0)
        ___qtablewidgetitem148.setText(QCoreApplication.translate("AlternativeWindow", u"0x10", None));
        ___qtablewidgetitem149 = self.tb_registers_rx.item(16, 1)
        ___qtablewidgetitem149.setText(QCoreApplication.translate("AlternativeWindow", u"62", None));
        ___qtablewidgetitem150 = self.tb_registers_rx.item(17, 0)
        ___qtablewidgetitem150.setText(QCoreApplication.translate("AlternativeWindow", u"0x11", None));
        ___qtablewidgetitem151 = self.tb_registers_rx.item(17, 1)
        ___qtablewidgetitem151.setText(QCoreApplication.translate("AlternativeWindow", u"C1", None));
        ___qtablewidgetitem152 = self.tb_registers_rx.item(18, 0)
        ___qtablewidgetitem152.setText(QCoreApplication.translate("AlternativeWindow", u"0x12", None));
        ___qtablewidgetitem153 = self.tb_registers_rx.item(18, 1)
        ___qtablewidgetitem153.setText(QCoreApplication.translate("AlternativeWindow", u"1D", None));
        ___qtablewidgetitem154 = self.tb_registers_rx.item(19, 0)
        ___qtablewidgetitem154.setText(QCoreApplication.translate("AlternativeWindow", u"0x13", None));
        ___qtablewidgetitem155 = self.tb_registers_rx.item(19, 1)
        ___qtablewidgetitem155.setText(QCoreApplication.translate("AlternativeWindow", u"41", None));
        ___qtablewidgetitem156 = self.tb_registers_rx.item(20, 0)
        ___qtablewidgetitem156.setText(QCoreApplication.translate("AlternativeWindow", u"0x14", None));
        ___qtablewidgetitem157 = self.tb_registers_rx.item(20, 1)
        ___qtablewidgetitem157.setText(QCoreApplication.translate("AlternativeWindow", u"32", None));
        ___qtablewidgetitem158 = self.tb_registers_rx.item(21, 0)
        ___qtablewidgetitem158.setText(QCoreApplication.translate("AlternativeWindow", u"0x15", None));
        ___qtablewidgetitem159 = self.tb_registers_rx.item(21, 1)
        ___qtablewidgetitem159.setText(QCoreApplication.translate("AlternativeWindow", u"9B", None));
        ___qtablewidgetitem160 = self.tb_registers_rx.item(22, 0)
        ___qtablewidgetitem160.setText(QCoreApplication.translate("AlternativeWindow", u"0x16", None));
        ___qtablewidgetitem161 = self.tb_registers_rx.item(22, 1)
        ___qtablewidgetitem161.setText(QCoreApplication.translate("AlternativeWindow", u"BF", None));
        ___qtablewidgetitem162 = self.tb_registers_rx.item(23, 0)
        ___qtablewidgetitem162.setText(QCoreApplication.translate("AlternativeWindow", u"0x17", None));
        ___qtablewidgetitem163 = self.tb_registers_rx.item(23, 1)
        ___qtablewidgetitem163.setText(QCoreApplication.translate("AlternativeWindow", u"51", None));
        ___qtablewidgetitem164 = self.tb_registers_rx.item(24, 0)
        ___qtablewidgetitem164.setText(QCoreApplication.translate("AlternativeWindow", u"0x18", None));
        ___qtablewidgetitem165 = self.tb_registers_rx.item(24, 1)
        ___qtablewidgetitem165.setText(QCoreApplication.translate("AlternativeWindow", u"24", None));
        ___qtablewidgetitem166 = self.tb_registers_rx.item(25, 0)
        ___qtablewidgetitem166.setText(QCoreApplication.translate("AlternativeWindow", u"0x19", None));
        ___qtablewidgetitem167 = self.tb_registers_rx.item(25, 1)
        ___qtablewidgetitem167.setText(QCoreApplication.translate("AlternativeWindow", u"71", None));
        ___qtablewidgetitem168 = self.tb_registers_rx.item(26, 0)
        ___qtablewidgetitem168.setText(QCoreApplication.translate("AlternativeWindow", u"0x1A", None));
        ___qtablewidgetitem169 = self.tb_registers_rx.item(26, 1)
        ___qtablewidgetitem169.setText(QCoreApplication.translate("AlternativeWindow", u"C5", None));
        ___qtablewidgetitem170 = self.tb_registers_rx.item(27, 0)
        ___qtablewidgetitem170.setText(QCoreApplication.translate("AlternativeWindow", u"0x1B", None));
        ___qtablewidgetitem171 = self.tb_registers_rx.item(27, 1)
        ___qtablewidgetitem171.setText(QCoreApplication.translate("AlternativeWindow", u"23", None));
        self.tb_registers_rx.setSortingEnabled(__sortingEnabled1)

        self.btn_reset_regs_rx.setText(QCoreApplication.translate("AlternativeWindow", u"Reset", None))
        self.btn_refresh_regs_rx.setText(QCoreApplication.translate("AlternativeWindow", u"Refresh", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.transceiver_tab), QCoreApplication.translate("AlternativeWindow", u"Transceiver", None))
        ___qtablewidgetitem172 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem172.setText(QCoreApplication.translate("AlternativeWindow", u"Address", None));
        ___qtablewidgetitem173 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem173.setText(QCoreApplication.translate("AlternativeWindow", u"Data", None));
        ___qtablewidgetitem174 = self.tableWidget_3.verticalHeaderItem(0)
        ___qtablewidgetitem174.setText(QCoreApplication.translate("AlternativeWindow", u"0", None));
        ___qtablewidgetitem175 = self.tableWidget_3.verticalHeaderItem(1)
        ___qtablewidgetitem175.setText(QCoreApplication.translate("AlternativeWindow", u"1", None));
        ___qtablewidgetitem176 = self.tableWidget_3.verticalHeaderItem(2)
        ___qtablewidgetitem176.setText(QCoreApplication.translate("AlternativeWindow", u"2", None));
        ___qtablewidgetitem177 = self.tableWidget_3.verticalHeaderItem(3)
        ___qtablewidgetitem177.setText(QCoreApplication.translate("AlternativeWindow", u"3", None));
        ___qtablewidgetitem178 = self.tableWidget_3.verticalHeaderItem(4)
        ___qtablewidgetitem178.setText(QCoreApplication.translate("AlternativeWindow", u"4", None));
        ___qtablewidgetitem179 = self.tableWidget_3.verticalHeaderItem(5)
        ___qtablewidgetitem179.setText(QCoreApplication.translate("AlternativeWindow", u"5", None));
        ___qtablewidgetitem180 = self.tableWidget_3.verticalHeaderItem(6)
        ___qtablewidgetitem180.setText(QCoreApplication.translate("AlternativeWindow", u"6", None));
        ___qtablewidgetitem181 = self.tableWidget_3.verticalHeaderItem(7)
        ___qtablewidgetitem181.setText(QCoreApplication.translate("AlternativeWindow", u"7", None));
        ___qtablewidgetitem182 = self.tableWidget_3.verticalHeaderItem(8)
        ___qtablewidgetitem182.setText(QCoreApplication.translate("AlternativeWindow", u"8", None));
        ___qtablewidgetitem183 = self.tableWidget_3.verticalHeaderItem(9)
        ___qtablewidgetitem183.setText(QCoreApplication.translate("AlternativeWindow", u"9", None));
        ___qtablewidgetitem184 = self.tableWidget_3.verticalHeaderItem(10)
        ___qtablewidgetitem184.setText(QCoreApplication.translate("AlternativeWindow", u"10", None));
        ___qtablewidgetitem185 = self.tableWidget_3.verticalHeaderItem(11)
        ___qtablewidgetitem185.setText(QCoreApplication.translate("AlternativeWindow", u"11", None));
        ___qtablewidgetitem186 = self.tableWidget_3.verticalHeaderItem(12)
        ___qtablewidgetitem186.setText(QCoreApplication.translate("AlternativeWindow", u"12", None));
        ___qtablewidgetitem187 = self.tableWidget_3.verticalHeaderItem(13)
        ___qtablewidgetitem187.setText(QCoreApplication.translate("AlternativeWindow", u"13", None));
        ___qtablewidgetitem188 = self.tableWidget_3.verticalHeaderItem(14)
        ___qtablewidgetitem188.setText(QCoreApplication.translate("AlternativeWindow", u"14", None));
        ___qtablewidgetitem189 = self.tableWidget_3.verticalHeaderItem(15)
        ___qtablewidgetitem189.setText(QCoreApplication.translate("AlternativeWindow", u"15", None));
        ___qtablewidgetitem190 = self.tableWidget_3.verticalHeaderItem(16)
        ___qtablewidgetitem190.setText(QCoreApplication.translate("AlternativeWindow", u"16", None));
        ___qtablewidgetitem191 = self.tableWidget_3.verticalHeaderItem(17)
        ___qtablewidgetitem191.setText(QCoreApplication.translate("AlternativeWindow", u"17", None));
        ___qtablewidgetitem192 = self.tableWidget_3.verticalHeaderItem(18)
        ___qtablewidgetitem192.setText(QCoreApplication.translate("AlternativeWindow", u"18", None));
        ___qtablewidgetitem193 = self.tableWidget_3.verticalHeaderItem(19)
        ___qtablewidgetitem193.setText(QCoreApplication.translate("AlternativeWindow", u"19", None));
        ___qtablewidgetitem194 = self.tableWidget_3.verticalHeaderItem(20)
        ___qtablewidgetitem194.setText(QCoreApplication.translate("AlternativeWindow", u"20", None));
        ___qtablewidgetitem195 = self.tableWidget_3.verticalHeaderItem(21)
        ___qtablewidgetitem195.setText(QCoreApplication.translate("AlternativeWindow", u"21", None));
        ___qtablewidgetitem196 = self.tableWidget_3.verticalHeaderItem(22)
        ___qtablewidgetitem196.setText(QCoreApplication.translate("AlternativeWindow", u"22", None));
        ___qtablewidgetitem197 = self.tableWidget_3.verticalHeaderItem(23)
        ___qtablewidgetitem197.setText(QCoreApplication.translate("AlternativeWindow", u"23", None));
        ___qtablewidgetitem198 = self.tableWidget_3.verticalHeaderItem(24)
        ___qtablewidgetitem198.setText(QCoreApplication.translate("AlternativeWindow", u"24", None));
        ___qtablewidgetitem199 = self.tableWidget_3.verticalHeaderItem(25)
        ___qtablewidgetitem199.setText(QCoreApplication.translate("AlternativeWindow", u"25", None));
        ___qtablewidgetitem200 = self.tableWidget_3.verticalHeaderItem(26)
        ___qtablewidgetitem200.setText(QCoreApplication.translate("AlternativeWindow", u"26", None));
        ___qtablewidgetitem201 = self.tableWidget_3.verticalHeaderItem(27)
        ___qtablewidgetitem201.setText(QCoreApplication.translate("AlternativeWindow", u"27", None));

        __sortingEnabled2 = self.tableWidget_3.isSortingEnabled()
        self.tableWidget_3.setSortingEnabled(False)
        ___qtablewidgetitem202 = self.tableWidget_3.item(0, 0)
        ___qtablewidgetitem202.setText(QCoreApplication.translate("AlternativeWindow", u"0x00", None));
        ___qtablewidgetitem203 = self.tableWidget_3.item(0, 1)
        ___qtablewidgetitem203.setText(QCoreApplication.translate("AlternativeWindow", u"34", None));
        ___qtablewidgetitem204 = self.tableWidget_3.item(1, 0)
        ___qtablewidgetitem204.setText(QCoreApplication.translate("AlternativeWindow", u"0x01", None));
        ___qtablewidgetitem205 = self.tableWidget_3.item(1, 1)
        ___qtablewidgetitem205.setText(QCoreApplication.translate("AlternativeWindow", u"4A", None));
        ___qtablewidgetitem206 = self.tableWidget_3.item(2, 0)
        ___qtablewidgetitem206.setText(QCoreApplication.translate("AlternativeWindow", u"0x02", None));
        ___qtablewidgetitem207 = self.tableWidget_3.item(2, 1)
        ___qtablewidgetitem207.setText(QCoreApplication.translate("AlternativeWindow", u"32", None));
        ___qtablewidgetitem208 = self.tableWidget_3.item(3, 0)
        ___qtablewidgetitem208.setText(QCoreApplication.translate("AlternativeWindow", u"0x03", None));
        ___qtablewidgetitem209 = self.tableWidget_3.item(3, 1)
        ___qtablewidgetitem209.setText(QCoreApplication.translate("AlternativeWindow", u"43", None));
        ___qtablewidgetitem210 = self.tableWidget_3.item(4, 0)
        ___qtablewidgetitem210.setText(QCoreApplication.translate("AlternativeWindow", u"0x04", None));
        ___qtablewidgetitem211 = self.tableWidget_3.item(4, 1)
        ___qtablewidgetitem211.setText(QCoreApplication.translate("AlternativeWindow", u"9F", None));
        ___qtablewidgetitem212 = self.tableWidget_3.item(5, 0)
        ___qtablewidgetitem212.setText(QCoreApplication.translate("AlternativeWindow", u"0x05", None));
        ___qtablewidgetitem213 = self.tableWidget_3.item(5, 1)
        ___qtablewidgetitem213.setText(QCoreApplication.translate("AlternativeWindow", u"BF", None));
        ___qtablewidgetitem214 = self.tableWidget_3.item(6, 0)
        ___qtablewidgetitem214.setText(QCoreApplication.translate("AlternativeWindow", u"0x06", None));
        ___qtablewidgetitem215 = self.tableWidget_3.item(6, 1)
        ___qtablewidgetitem215.setText(QCoreApplication.translate("AlternativeWindow", u"6D", None));
        ___qtablewidgetitem216 = self.tableWidget_3.item(7, 0)
        ___qtablewidgetitem216.setText(QCoreApplication.translate("AlternativeWindow", u"0x07", None));
        ___qtablewidgetitem217 = self.tableWidget_3.item(7, 1)
        ___qtablewidgetitem217.setText(QCoreApplication.translate("AlternativeWindow", u"90", None));
        ___qtablewidgetitem218 = self.tableWidget_3.item(8, 0)
        ___qtablewidgetitem218.setText(QCoreApplication.translate("AlternativeWindow", u"0x08", None));
        ___qtablewidgetitem219 = self.tableWidget_3.item(8, 1)
        ___qtablewidgetitem219.setText(QCoreApplication.translate("AlternativeWindow", u"40", None));
        ___qtablewidgetitem220 = self.tableWidget_3.item(9, 0)
        ___qtablewidgetitem220.setText(QCoreApplication.translate("AlternativeWindow", u"0x09", None));
        ___qtablewidgetitem221 = self.tableWidget_3.item(9, 1)
        ___qtablewidgetitem221.setText(QCoreApplication.translate("AlternativeWindow", u"36", None));
        ___qtablewidgetitem222 = self.tableWidget_3.item(10, 0)
        ___qtablewidgetitem222.setText(QCoreApplication.translate("AlternativeWindow", u"0x0A", None));
        ___qtablewidgetitem223 = self.tableWidget_3.item(10, 1)
        ___qtablewidgetitem223.setText(QCoreApplication.translate("AlternativeWindow", u"BB", None));
        ___qtablewidgetitem224 = self.tableWidget_3.item(11, 0)
        ___qtablewidgetitem224.setText(QCoreApplication.translate("AlternativeWindow", u"0x0B", None));
        ___qtablewidgetitem225 = self.tableWidget_3.item(11, 1)
        ___qtablewidgetitem225.setText(QCoreApplication.translate("AlternativeWindow", u"46", None));
        ___qtablewidgetitem226 = self.tableWidget_3.item(12, 0)
        ___qtablewidgetitem226.setText(QCoreApplication.translate("AlternativeWindow", u"0x0C", None));
        ___qtablewidgetitem227 = self.tableWidget_3.item(12, 1)
        ___qtablewidgetitem227.setText(QCoreApplication.translate("AlternativeWindow", u"02", None));
        ___qtablewidgetitem228 = self.tableWidget_3.item(13, 0)
        ___qtablewidgetitem228.setText(QCoreApplication.translate("AlternativeWindow", u"0x0D", None));
        ___qtablewidgetitem229 = self.tableWidget_3.item(13, 1)
        ___qtablewidgetitem229.setText(QCoreApplication.translate("AlternativeWindow", u"1D", None));
        ___qtablewidgetitem230 = self.tableWidget_3.item(14, 0)
        ___qtablewidgetitem230.setText(QCoreApplication.translate("AlternativeWindow", u"0x0E", None));
        ___qtablewidgetitem231 = self.tableWidget_3.item(14, 1)
        ___qtablewidgetitem231.setText(QCoreApplication.translate("AlternativeWindow", u"12", None));
        ___qtablewidgetitem232 = self.tableWidget_3.item(15, 0)
        ___qtablewidgetitem232.setText(QCoreApplication.translate("AlternativeWindow", u"0x0F", None));
        ___qtablewidgetitem233 = self.tableWidget_3.item(15, 1)
        ___qtablewidgetitem233.setText(QCoreApplication.translate("AlternativeWindow", u"05", None));
        ___qtablewidgetitem234 = self.tableWidget_3.item(16, 0)
        ___qtablewidgetitem234.setText(QCoreApplication.translate("AlternativeWindow", u"0x10", None));
        ___qtablewidgetitem235 = self.tableWidget_3.item(16, 1)
        ___qtablewidgetitem235.setText(QCoreApplication.translate("AlternativeWindow", u"62", None));
        ___qtablewidgetitem236 = self.tableWidget_3.item(17, 0)
        ___qtablewidgetitem236.setText(QCoreApplication.translate("AlternativeWindow", u"0x11", None));
        ___qtablewidgetitem237 = self.tableWidget_3.item(17, 1)
        ___qtablewidgetitem237.setText(QCoreApplication.translate("AlternativeWindow", u"C1", None));
        ___qtablewidgetitem238 = self.tableWidget_3.item(18, 0)
        ___qtablewidgetitem238.setText(QCoreApplication.translate("AlternativeWindow", u"0x12", None));
        ___qtablewidgetitem239 = self.tableWidget_3.item(18, 1)
        ___qtablewidgetitem239.setText(QCoreApplication.translate("AlternativeWindow", u"1D", None));
        ___qtablewidgetitem240 = self.tableWidget_3.item(19, 0)
        ___qtablewidgetitem240.setText(QCoreApplication.translate("AlternativeWindow", u"0x13", None));
        ___qtablewidgetitem241 = self.tableWidget_3.item(19, 1)
        ___qtablewidgetitem241.setText(QCoreApplication.translate("AlternativeWindow", u"41", None));
        ___qtablewidgetitem242 = self.tableWidget_3.item(20, 0)
        ___qtablewidgetitem242.setText(QCoreApplication.translate("AlternativeWindow", u"0x14", None));
        ___qtablewidgetitem243 = self.tableWidget_3.item(20, 1)
        ___qtablewidgetitem243.setText(QCoreApplication.translate("AlternativeWindow", u"32", None));
        ___qtablewidgetitem244 = self.tableWidget_3.item(21, 0)
        ___qtablewidgetitem244.setText(QCoreApplication.translate("AlternativeWindow", u"0x15", None));
        ___qtablewidgetitem245 = self.tableWidget_3.item(21, 1)
        ___qtablewidgetitem245.setText(QCoreApplication.translate("AlternativeWindow", u"9B", None));
        ___qtablewidgetitem246 = self.tableWidget_3.item(22, 0)
        ___qtablewidgetitem246.setText(QCoreApplication.translate("AlternativeWindow", u"0x16", None));
        ___qtablewidgetitem247 = self.tableWidget_3.item(22, 1)
        ___qtablewidgetitem247.setText(QCoreApplication.translate("AlternativeWindow", u"BF", None));
        ___qtablewidgetitem248 = self.tableWidget_3.item(23, 0)
        ___qtablewidgetitem248.setText(QCoreApplication.translate("AlternativeWindow", u"0x17", None));
        ___qtablewidgetitem249 = self.tableWidget_3.item(23, 1)
        ___qtablewidgetitem249.setText(QCoreApplication.translate("AlternativeWindow", u"51", None));
        ___qtablewidgetitem250 = self.tableWidget_3.item(24, 0)
        ___qtablewidgetitem250.setText(QCoreApplication.translate("AlternativeWindow", u"0x18", None));
        ___qtablewidgetitem251 = self.tableWidget_3.item(24, 1)
        ___qtablewidgetitem251.setText(QCoreApplication.translate("AlternativeWindow", u"24", None));
        ___qtablewidgetitem252 = self.tableWidget_3.item(25, 0)
        ___qtablewidgetitem252.setText(QCoreApplication.translate("AlternativeWindow", u"0x19", None));
        ___qtablewidgetitem253 = self.tableWidget_3.item(25, 1)
        ___qtablewidgetitem253.setText(QCoreApplication.translate("AlternativeWindow", u"71", None));
        ___qtablewidgetitem254 = self.tableWidget_3.item(26, 0)
        ___qtablewidgetitem254.setText(QCoreApplication.translate("AlternativeWindow", u"0x1A", None));
        ___qtablewidgetitem255 = self.tableWidget_3.item(26, 1)
        ___qtablewidgetitem255.setText(QCoreApplication.translate("AlternativeWindow", u"C5", None));
        ___qtablewidgetitem256 = self.tableWidget_3.item(27, 0)
        ___qtablewidgetitem256.setText(QCoreApplication.translate("AlternativeWindow", u"0x1B", None));
        ___qtablewidgetitem257 = self.tableWidget_3.item(27, 1)
        ___qtablewidgetitem257.setText(QCoreApplication.translate("AlternativeWindow", u"23", None));
        self.tableWidget_3.setSortingEnabled(__sortingEnabled2)

        self.pushButton_8.setText(QCoreApplication.translate("AlternativeWindow", u"Reset", None))
        self.pushButton_13.setText(QCoreApplication.translate("AlternativeWindow", u"Refresh", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("AlternativeWindow", u"PHY", None))
        ___qtablewidgetitem258 = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem258.setText(QCoreApplication.translate("AlternativeWindow", u"Address", None));
        ___qtablewidgetitem259 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem259.setText(QCoreApplication.translate("AlternativeWindow", u"Data", None));
        ___qtablewidgetitem260 = self.tableWidget_4.verticalHeaderItem(0)
        ___qtablewidgetitem260.setText(QCoreApplication.translate("AlternativeWindow", u"0", None));
        ___qtablewidgetitem261 = self.tableWidget_4.verticalHeaderItem(1)
        ___qtablewidgetitem261.setText(QCoreApplication.translate("AlternativeWindow", u"1", None));
        ___qtablewidgetitem262 = self.tableWidget_4.verticalHeaderItem(2)
        ___qtablewidgetitem262.setText(QCoreApplication.translate("AlternativeWindow", u"2", None));
        ___qtablewidgetitem263 = self.tableWidget_4.verticalHeaderItem(3)
        ___qtablewidgetitem263.setText(QCoreApplication.translate("AlternativeWindow", u"3", None));
        ___qtablewidgetitem264 = self.tableWidget_4.verticalHeaderItem(4)
        ___qtablewidgetitem264.setText(QCoreApplication.translate("AlternativeWindow", u"4", None));
        ___qtablewidgetitem265 = self.tableWidget_4.verticalHeaderItem(5)
        ___qtablewidgetitem265.setText(QCoreApplication.translate("AlternativeWindow", u"5", None));
        ___qtablewidgetitem266 = self.tableWidget_4.verticalHeaderItem(6)
        ___qtablewidgetitem266.setText(QCoreApplication.translate("AlternativeWindow", u"6", None));
        ___qtablewidgetitem267 = self.tableWidget_4.verticalHeaderItem(7)
        ___qtablewidgetitem267.setText(QCoreApplication.translate("AlternativeWindow", u"7", None));
        ___qtablewidgetitem268 = self.tableWidget_4.verticalHeaderItem(8)
        ___qtablewidgetitem268.setText(QCoreApplication.translate("AlternativeWindow", u"8", None));
        ___qtablewidgetitem269 = self.tableWidget_4.verticalHeaderItem(9)
        ___qtablewidgetitem269.setText(QCoreApplication.translate("AlternativeWindow", u"9", None));
        ___qtablewidgetitem270 = self.tableWidget_4.verticalHeaderItem(10)
        ___qtablewidgetitem270.setText(QCoreApplication.translate("AlternativeWindow", u"10", None));
        ___qtablewidgetitem271 = self.tableWidget_4.verticalHeaderItem(11)
        ___qtablewidgetitem271.setText(QCoreApplication.translate("AlternativeWindow", u"11", None));
        ___qtablewidgetitem272 = self.tableWidget_4.verticalHeaderItem(12)
        ___qtablewidgetitem272.setText(QCoreApplication.translate("AlternativeWindow", u"12", None));
        ___qtablewidgetitem273 = self.tableWidget_4.verticalHeaderItem(13)
        ___qtablewidgetitem273.setText(QCoreApplication.translate("AlternativeWindow", u"13", None));
        ___qtablewidgetitem274 = self.tableWidget_4.verticalHeaderItem(14)
        ___qtablewidgetitem274.setText(QCoreApplication.translate("AlternativeWindow", u"14", None));
        ___qtablewidgetitem275 = self.tableWidget_4.verticalHeaderItem(15)
        ___qtablewidgetitem275.setText(QCoreApplication.translate("AlternativeWindow", u"15", None));
        ___qtablewidgetitem276 = self.tableWidget_4.verticalHeaderItem(16)
        ___qtablewidgetitem276.setText(QCoreApplication.translate("AlternativeWindow", u"16", None));
        ___qtablewidgetitem277 = self.tableWidget_4.verticalHeaderItem(17)
        ___qtablewidgetitem277.setText(QCoreApplication.translate("AlternativeWindow", u"17", None));
        ___qtablewidgetitem278 = self.tableWidget_4.verticalHeaderItem(18)
        ___qtablewidgetitem278.setText(QCoreApplication.translate("AlternativeWindow", u"18", None));
        ___qtablewidgetitem279 = self.tableWidget_4.verticalHeaderItem(19)
        ___qtablewidgetitem279.setText(QCoreApplication.translate("AlternativeWindow", u"19", None));
        ___qtablewidgetitem280 = self.tableWidget_4.verticalHeaderItem(20)
        ___qtablewidgetitem280.setText(QCoreApplication.translate("AlternativeWindow", u"20", None));
        ___qtablewidgetitem281 = self.tableWidget_4.verticalHeaderItem(21)
        ___qtablewidgetitem281.setText(QCoreApplication.translate("AlternativeWindow", u"21", None));
        ___qtablewidgetitem282 = self.tableWidget_4.verticalHeaderItem(22)
        ___qtablewidgetitem282.setText(QCoreApplication.translate("AlternativeWindow", u"22", None));
        ___qtablewidgetitem283 = self.tableWidget_4.verticalHeaderItem(23)
        ___qtablewidgetitem283.setText(QCoreApplication.translate("AlternativeWindow", u"23", None));
        ___qtablewidgetitem284 = self.tableWidget_4.verticalHeaderItem(24)
        ___qtablewidgetitem284.setText(QCoreApplication.translate("AlternativeWindow", u"24", None));
        ___qtablewidgetitem285 = self.tableWidget_4.verticalHeaderItem(25)
        ___qtablewidgetitem285.setText(QCoreApplication.translate("AlternativeWindow", u"25", None));
        ___qtablewidgetitem286 = self.tableWidget_4.verticalHeaderItem(26)
        ___qtablewidgetitem286.setText(QCoreApplication.translate("AlternativeWindow", u"26", None));
        ___qtablewidgetitem287 = self.tableWidget_4.verticalHeaderItem(27)
        ___qtablewidgetitem287.setText(QCoreApplication.translate("AlternativeWindow", u"27", None));

        __sortingEnabled3 = self.tableWidget_4.isSortingEnabled()
        self.tableWidget_4.setSortingEnabled(False)
        ___qtablewidgetitem288 = self.tableWidget_4.item(0, 0)
        ___qtablewidgetitem288.setText(QCoreApplication.translate("AlternativeWindow", u"0x00", None));
        ___qtablewidgetitem289 = self.tableWidget_4.item(0, 1)
        ___qtablewidgetitem289.setText(QCoreApplication.translate("AlternativeWindow", u"34", None));
        ___qtablewidgetitem290 = self.tableWidget_4.item(1, 0)
        ___qtablewidgetitem290.setText(QCoreApplication.translate("AlternativeWindow", u"0x01", None));
        ___qtablewidgetitem291 = self.tableWidget_4.item(1, 1)
        ___qtablewidgetitem291.setText(QCoreApplication.translate("AlternativeWindow", u"4A", None));
        ___qtablewidgetitem292 = self.tableWidget_4.item(2, 0)
        ___qtablewidgetitem292.setText(QCoreApplication.translate("AlternativeWindow", u"0x02", None));
        ___qtablewidgetitem293 = self.tableWidget_4.item(2, 1)
        ___qtablewidgetitem293.setText(QCoreApplication.translate("AlternativeWindow", u"32", None));
        ___qtablewidgetitem294 = self.tableWidget_4.item(3, 0)
        ___qtablewidgetitem294.setText(QCoreApplication.translate("AlternativeWindow", u"0x03", None));
        ___qtablewidgetitem295 = self.tableWidget_4.item(3, 1)
        ___qtablewidgetitem295.setText(QCoreApplication.translate("AlternativeWindow", u"43", None));
        ___qtablewidgetitem296 = self.tableWidget_4.item(4, 0)
        ___qtablewidgetitem296.setText(QCoreApplication.translate("AlternativeWindow", u"0x04", None));
        ___qtablewidgetitem297 = self.tableWidget_4.item(4, 1)
        ___qtablewidgetitem297.setText(QCoreApplication.translate("AlternativeWindow", u"9F", None));
        ___qtablewidgetitem298 = self.tableWidget_4.item(5, 0)
        ___qtablewidgetitem298.setText(QCoreApplication.translate("AlternativeWindow", u"0x05", None));
        ___qtablewidgetitem299 = self.tableWidget_4.item(5, 1)
        ___qtablewidgetitem299.setText(QCoreApplication.translate("AlternativeWindow", u"BF", None));
        ___qtablewidgetitem300 = self.tableWidget_4.item(6, 0)
        ___qtablewidgetitem300.setText(QCoreApplication.translate("AlternativeWindow", u"0x06", None));
        ___qtablewidgetitem301 = self.tableWidget_4.item(6, 1)
        ___qtablewidgetitem301.setText(QCoreApplication.translate("AlternativeWindow", u"6D", None));
        ___qtablewidgetitem302 = self.tableWidget_4.item(7, 0)
        ___qtablewidgetitem302.setText(QCoreApplication.translate("AlternativeWindow", u"0x07", None));
        ___qtablewidgetitem303 = self.tableWidget_4.item(7, 1)
        ___qtablewidgetitem303.setText(QCoreApplication.translate("AlternativeWindow", u"90", None));
        ___qtablewidgetitem304 = self.tableWidget_4.item(8, 0)
        ___qtablewidgetitem304.setText(QCoreApplication.translate("AlternativeWindow", u"0x08", None));
        ___qtablewidgetitem305 = self.tableWidget_4.item(8, 1)
        ___qtablewidgetitem305.setText(QCoreApplication.translate("AlternativeWindow", u"40", None));
        ___qtablewidgetitem306 = self.tableWidget_4.item(9, 0)
        ___qtablewidgetitem306.setText(QCoreApplication.translate("AlternativeWindow", u"0x09", None));
        ___qtablewidgetitem307 = self.tableWidget_4.item(9, 1)
        ___qtablewidgetitem307.setText(QCoreApplication.translate("AlternativeWindow", u"36", None));
        ___qtablewidgetitem308 = self.tableWidget_4.item(10, 0)
        ___qtablewidgetitem308.setText(QCoreApplication.translate("AlternativeWindow", u"0x0A", None));
        ___qtablewidgetitem309 = self.tableWidget_4.item(10, 1)
        ___qtablewidgetitem309.setText(QCoreApplication.translate("AlternativeWindow", u"BB", None));
        ___qtablewidgetitem310 = self.tableWidget_4.item(11, 0)
        ___qtablewidgetitem310.setText(QCoreApplication.translate("AlternativeWindow", u"0x0B", None));
        ___qtablewidgetitem311 = self.tableWidget_4.item(11, 1)
        ___qtablewidgetitem311.setText(QCoreApplication.translate("AlternativeWindow", u"46", None));
        ___qtablewidgetitem312 = self.tableWidget_4.item(12, 0)
        ___qtablewidgetitem312.setText(QCoreApplication.translate("AlternativeWindow", u"0x0C", None));
        ___qtablewidgetitem313 = self.tableWidget_4.item(12, 1)
        ___qtablewidgetitem313.setText(QCoreApplication.translate("AlternativeWindow", u"02", None));
        ___qtablewidgetitem314 = self.tableWidget_4.item(13, 0)
        ___qtablewidgetitem314.setText(QCoreApplication.translate("AlternativeWindow", u"0x0D", None));
        ___qtablewidgetitem315 = self.tableWidget_4.item(13, 1)
        ___qtablewidgetitem315.setText(QCoreApplication.translate("AlternativeWindow", u"1D", None));
        ___qtablewidgetitem316 = self.tableWidget_4.item(14, 0)
        ___qtablewidgetitem316.setText(QCoreApplication.translate("AlternativeWindow", u"0x0E", None));
        ___qtablewidgetitem317 = self.tableWidget_4.item(14, 1)
        ___qtablewidgetitem317.setText(QCoreApplication.translate("AlternativeWindow", u"12", None));
        ___qtablewidgetitem318 = self.tableWidget_4.item(15, 0)
        ___qtablewidgetitem318.setText(QCoreApplication.translate("AlternativeWindow", u"0x0F", None));
        ___qtablewidgetitem319 = self.tableWidget_4.item(15, 1)
        ___qtablewidgetitem319.setText(QCoreApplication.translate("AlternativeWindow", u"05", None));
        ___qtablewidgetitem320 = self.tableWidget_4.item(16, 0)
        ___qtablewidgetitem320.setText(QCoreApplication.translate("AlternativeWindow", u"0x10", None));
        ___qtablewidgetitem321 = self.tableWidget_4.item(16, 1)
        ___qtablewidgetitem321.setText(QCoreApplication.translate("AlternativeWindow", u"62", None));
        ___qtablewidgetitem322 = self.tableWidget_4.item(17, 0)
        ___qtablewidgetitem322.setText(QCoreApplication.translate("AlternativeWindow", u"0x11", None));
        ___qtablewidgetitem323 = self.tableWidget_4.item(17, 1)
        ___qtablewidgetitem323.setText(QCoreApplication.translate("AlternativeWindow", u"C1", None));
        ___qtablewidgetitem324 = self.tableWidget_4.item(18, 0)
        ___qtablewidgetitem324.setText(QCoreApplication.translate("AlternativeWindow", u"0x12", None));
        ___qtablewidgetitem325 = self.tableWidget_4.item(18, 1)
        ___qtablewidgetitem325.setText(QCoreApplication.translate("AlternativeWindow", u"1D", None));
        ___qtablewidgetitem326 = self.tableWidget_4.item(19, 0)
        ___qtablewidgetitem326.setText(QCoreApplication.translate("AlternativeWindow", u"0x13", None));
        ___qtablewidgetitem327 = self.tableWidget_4.item(19, 1)
        ___qtablewidgetitem327.setText(QCoreApplication.translate("AlternativeWindow", u"41", None));
        ___qtablewidgetitem328 = self.tableWidget_4.item(20, 0)
        ___qtablewidgetitem328.setText(QCoreApplication.translate("AlternativeWindow", u"0x14", None));
        ___qtablewidgetitem329 = self.tableWidget_4.item(20, 1)
        ___qtablewidgetitem329.setText(QCoreApplication.translate("AlternativeWindow", u"32", None));
        ___qtablewidgetitem330 = self.tableWidget_4.item(21, 0)
        ___qtablewidgetitem330.setText(QCoreApplication.translate("AlternativeWindow", u"0x15", None));
        ___qtablewidgetitem331 = self.tableWidget_4.item(21, 1)
        ___qtablewidgetitem331.setText(QCoreApplication.translate("AlternativeWindow", u"9B", None));
        ___qtablewidgetitem332 = self.tableWidget_4.item(22, 0)
        ___qtablewidgetitem332.setText(QCoreApplication.translate("AlternativeWindow", u"0x16", None));
        ___qtablewidgetitem333 = self.tableWidget_4.item(22, 1)
        ___qtablewidgetitem333.setText(QCoreApplication.translate("AlternativeWindow", u"BF", None));
        ___qtablewidgetitem334 = self.tableWidget_4.item(23, 0)
        ___qtablewidgetitem334.setText(QCoreApplication.translate("AlternativeWindow", u"0x17", None));
        ___qtablewidgetitem335 = self.tableWidget_4.item(23, 1)
        ___qtablewidgetitem335.setText(QCoreApplication.translate("AlternativeWindow", u"51", None));
        ___qtablewidgetitem336 = self.tableWidget_4.item(24, 0)
        ___qtablewidgetitem336.setText(QCoreApplication.translate("AlternativeWindow", u"0x18", None));
        ___qtablewidgetitem337 = self.tableWidget_4.item(24, 1)
        ___qtablewidgetitem337.setText(QCoreApplication.translate("AlternativeWindow", u"24", None));
        ___qtablewidgetitem338 = self.tableWidget_4.item(25, 0)
        ___qtablewidgetitem338.setText(QCoreApplication.translate("AlternativeWindow", u"0x19", None));
        ___qtablewidgetitem339 = self.tableWidget_4.item(25, 1)
        ___qtablewidgetitem339.setText(QCoreApplication.translate("AlternativeWindow", u"71", None));
        ___qtablewidgetitem340 = self.tableWidget_4.item(26, 0)
        ___qtablewidgetitem340.setText(QCoreApplication.translate("AlternativeWindow", u"0x1A", None));
        ___qtablewidgetitem341 = self.tableWidget_4.item(26, 1)
        ___qtablewidgetitem341.setText(QCoreApplication.translate("AlternativeWindow", u"C5", None));
        ___qtablewidgetitem342 = self.tableWidget_4.item(27, 0)
        ___qtablewidgetitem342.setText(QCoreApplication.translate("AlternativeWindow", u"0x1B", None));
        ___qtablewidgetitem343 = self.tableWidget_4.item(27, 1)
        ___qtablewidgetitem343.setText(QCoreApplication.translate("AlternativeWindow", u"23", None));
        self.tableWidget_4.setSortingEnabled(__sortingEnabled3)

        self.pushButton_14.setText(QCoreApplication.translate("AlternativeWindow", u"Reset", None))
        self.pushButton_15.setText(QCoreApplication.translate("AlternativeWindow", u"Refresh", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("AlternativeWindow", u"Parallel/Serial", None))
    # retranslateUi

