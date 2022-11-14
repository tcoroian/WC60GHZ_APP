# This Python file uses the following encoding: utf-8
from PySide6 import QtWidgets
from ui_alternativewindow import Ui_AlternativeWindow

import iio
import constants
import status_monitor


class MainWindow(QtWidgets.QMainWindow):

    monitors = status_monitor.StatusMonitor()

    def switch_tuning_options_tx(self, enable = True):
        self.ui.lbl_gain_tx.setEnabled(enable)
        self.ui.cb_gain_tx.setEnabled(enable)
        self.ui.lbl_rf_attn_index.setEnabled(enable)
        self.ui.cb_rf_attn_index.setEnabled(enable)

    def switch_tuning_options_rx(self, enable = True):
        self.ui.lbl_gain_rx.setEnabled(enable)
        self.ui.cb_gain_rx.setEnabled(enable)
        self.ui.lbl_bb_attn_index.setEnabled(enable)
        self.ui.cb_bb_attn_index.setEnabled(enable)

    def switch_device_options_tx(self, enable = True):
        self.ui.lbl_lo_frequency_tx.setEnabled(enable)
        self.ui.cb_lo_frequency_tx.setEnabled(enable)
        self.ui.chk_autotuning_tx.setEnabled(enable)

    def switch_device_options_rx(self, enable = True):
        self.ui.lbl_lo_frequency_rx.setEnabled(enable)
        self.ui.cb_lo_frequency_rx.setEnabled(enable)
        self.ui.chk_autotuning_rx.setEnabled(enable)

    def switch_status_options_tx(self, enable = True):
        self.ui.gb_status_tx.setEnabled(enable)

    def switch_status_options_rx(self, enable = True):
        self.ui.gb_status_rx.setEnabled(enable)

    def switch_register_map_tx(self, enable = True):
        self.ui.tb_registers_tx.setEnabled(enable)
        self.ui.btn_refresh_regs_tx.setEnabled(enable)
        self.ui.btn_reset_regs_tx.setEnabled(enable)

    def switch_register_map_rx(self, enable = True):
        self.ui.tb_registers_rx.setEnabled(enable)
        self.ui.btn_refresh_regs_rx.setEnabled(enable)
        self.ui.btn_reset_regs_rx.setEnabled(enable)

    def clear_table_tx(self):
        for i in range(self.ui.tb_registers_tx.rowCount()):
            self.ui.tb_registers_tx.setItem(i, 1, QtWidgets.QTableWidgetItem(''))

    def clear_table_rx(self):
        for i in range(self.ui.tb_registers_rx.rowCount()):
            self.ui.tb_registers_rx.setItem(i, 1, QtWidgets.QTableWidgetItem(''))

    def disable_options(self):
        self.ui.lbl_power_tx.setEnabled(False)
        self.ui.lbl_power_rx.setEnabled(False)
        self.ui.btn_power_tx.setEnabled(False)
        self.ui.btn_power_rx.setEnabled(False)

        self.switch_device_options_tx(False)
        self.switch_device_options_rx(False)
        self.switch_tuning_options_tx(False)
        self.switch_tuning_options_rx(False)
        self.switch_status_options_tx(False)
        self.switch_status_options_rx(False)
        self.switch_register_map_rx(False)
        self.switch_register_map_tx(False)

        # Disable leds for lock detection
        self.ui.cw_lock_detect_tx.setStyleSheet(constants.style_led_grey)
        self.ui.cw_lock_detect_rx.setStyleSheet(constants.style_led_grey)

    def reset_ui(self):
        self.ui.btn_power_tx.setChecked(False)
        self.ui.btn_power_rx.setChecked(False)
        self.power_switch_tx(False)
        self.power_switch_rx(False)
        self.ui.chk_autotuning_tx.setChecked(False)
        self.ui.chk_autotuning_rx.setChecked(False)
        self.disable_options()

        self.ui.lbl_hardware_name_dyn.setText(constants.text_no_context)
        self.ui.lbl_vendor_dyn.setText(constants.text_no_context)
        self.ui.lbl_hardware_carrier_dyn.setText(constants.text_no_context)
        self.ui.lbl_hardware_serial_dyn.setText(constants.text_no_context)
        self.ui.lbl_local_dyn.setText(constants.text_no_context)

        self.ui.lbl_temp_tx_dyn.setText(constants.text_no_context)
        self.ui.lbl_temp_rx_dyn.setText(constants.text_no_context)
        self.ui.lbl_power_usage_tx_dyn.setText(constants.text_no_context)
        self.ui.lbl_power_usage_rx_dyn.setText(constants.text_no_context)

        self.clear_table_tx()
        self.clear_table_rx()

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_AlternativeWindow()
        self.ui.setupUi(self)

        # Set push buttons to toggle buttons
        self.ui.btn_power_tx.setCheckable(True)
        self.ui.btn_power_rx.setCheckable(True)

        # Disable all options in TX and RX group boxes
        self.disable_options()

        # Add usb contexts to dropdown menu
        self.ui.cb_available_contexts.clear()
        self.ui.cb_available_contexts.addItems(["Select context..."])
        self.monitors.start_context_search(self)

        # Connect slot to update context labels
        self.ui.cb_available_contexts.activated.connect(self.ctx_changed)

        # Connect slots to enable/disable device configuration and monitoring
        self.ui.btn_power_tx.clicked.connect(self.power_switch_tx)
        self.ui.btn_power_rx.clicked.connect(self.power_switch_rx)

        # Connect slots to enable/disable tuning options
        self.ui.chk_autotuning_tx.clicked.connect(self.autotuning_switch_tx)
        self.ui.chk_autotuning_rx.clicked.connect(self.autotuning_switch_rx)

        # Connect slots to refresh registers buttons
        self.ui.btn_refresh_regs_tx.clicked.connect(self.read_regs_tx)
        self.ui.btn_refresh_regs_rx.clicked.connect(self.read_regs_rx)

        # Connect slots to reset registers buttons
        self.ui.btn_reset_regs_tx.clicked.connect(self.reset_regs_tx)
        self.ui.btn_reset_regs_rx.clicked.connect(self.reset_regs_rx)

    def ctx_changed(self):
        text = self.ui.cb_available_contexts.currentText()
        if not text.startswith("usb"):
            return

        # Disable "Select context..." option
        self.ui.cb_available_contexts.model().item(0).setEnabled(False)

        try:
            self.iio_ctx = iio.Context(text)
        except:
            return

        # Reset user interface after changing context
        self.reset_ui()

        # Check device type (9615 or 9625)

        # Update labels about the context
        hardware_name = "ADMV9625"
        vendor = "Analog Devices, Inc."
        hardware_carrier = "ETHERNET-MICROWAVE-EVAL Rev1.0"
        hardware_serial = "0ad9040001fbff16004f8ba6adf7"
        local = "no-OS 1.1.0-ga5b7ef51"

        self.ui.lbl_hardware_name_dyn.setText(hardware_name)
        self.ui.lbl_vendor_dyn.setText(vendor)
        self.ui.lbl_hardware_carrier_dyn.setText(hardware_carrier)
        self.ui.lbl_hardware_serial_dyn.setText(hardware_serial)
        self.ui.lbl_local_dyn.setText(local)

        # Enable TX and RX power switches
        self.ui.lbl_power_tx.setEnabled(True)
        self.ui.lbl_power_rx.setEnabled(True)
        self.ui.btn_power_tx.setEnabled(True)
        self.ui.btn_power_rx.setEnabled(True)

    def power_switch_tx(self, value):
        if value == 1:
            # Change appearance of power switch
            self.ui.btn_power_tx.setStyleSheet(constants.style_btn_on)
            self.ui.btn_power_tx.setText("Turn OFF")

            # Enable status and monitoring options
            self.switch_device_options_tx()
            autotuning = self.ui.chk_autotuning_tx.isChecked()
            self.switch_tuning_options_tx(not autotuning)
            self.switch_status_options_tx()
            self.switch_register_map_tx()
            self.read_regs_tx()

            # Start all monitoring threads
            self.monitors.start_monitoring_lock_tx(self.ui.cw_lock_detect_tx)
            self.monitors.start_monitoring_temp_tx(self.ui.lbl_temp_tx_dyn)
            self.monitors.start_monitoring_power_tx(self.ui.lbl_power_usage_tx_dyn)
        else:
            # Change appearance of power switch
            self.ui.btn_power_tx.setStyleSheet(constants.style_btn_off)
            self.ui.btn_power_tx.setText("Turn ON")

            # Disable status and monitoring options
            self.switch_device_options_tx(False)
            self.switch_tuning_options_tx(False)
            self.switch_status_options_tx(False)
            self.switch_register_map_tx(False)
            self.clear_table_tx()

            # Stop all monitoring threads
            self.monitors.stop_monitoring_lock_tx()
            self.monitors.stop_monitoring_temp_tx()
            self.monitors.stop_monitoring_power_tx()

    def power_switch_rx(self, value):
        if value == 1:
            # Change appearance of power switch
            self.ui.btn_power_rx.setStyleSheet(constants.style_btn_on)
            self.ui.btn_power_rx.setText("Turn OFF")

            # Enable status and monitoring options
            self.switch_device_options_rx()
            autotuning = self.ui.chk_autotuning_rx.isChecked()
            self.switch_tuning_options_rx(not autotuning)
            self.switch_status_options_rx()
            self.switch_register_map_rx()
            self.read_regs_rx()

            # Start all monitoring threads
            self.monitors.start_monitoring_lock_rx(self.ui.cw_lock_detect_rx)
            self.monitors.start_monitoring_temp_rx(self.ui.lbl_temp_rx_dyn)
            self.monitors.start_monitoring_power_rx(self.ui.lbl_power_usage_rx_dyn)
        else:
            # Change appearance of power switch
            self.ui.btn_power_rx.setStyleSheet(constants.style_btn_off)
            self.ui.btn_power_rx.setText("Turn ON")

            # Disable status and monitoring options
            self.switch_device_options_rx(False)
            self.switch_tuning_options_rx(False)
            self.switch_status_options_rx(False)
            self.switch_register_map_rx(False)
            self.clear_table_rx()

            # Stop all monitoring threads
            self.monitors.stop_monitoring_lock_rx()
            self.monitors.stop_monitoring_temp_rx()
            self.monitors.stop_monitoring_power_rx()

    def autotuning_switch_tx(self, state):
        self.switch_tuning_options_tx(not state)

    def autotuning_switch_rx(self, state):
        self.switch_tuning_options_rx(not state)
    def read_regs_tx(self):
        self.ui.tb_registers_tx.setItem(0, 1, QtWidgets.QTableWidgetItem("34"))
        self.ui.tb_registers_tx.setItem(1, 1, QtWidgets.QTableWidgetItem("A2"))
        self.ui.tb_registers_tx.setItem(2, 1, QtWidgets.QTableWidgetItem("8C"))
        self.ui.tb_registers_tx.setItem(3, 1, QtWidgets.QTableWidgetItem("90"))
        self.ui.tb_registers_tx.setItem(4, 1, QtWidgets.QTableWidgetItem("1F"))

    def read_regs_rx(self):
        self.ui.tb_registers_rx.setItem(0, 1, QtWidgets.QTableWidgetItem("34"))
        self.ui.tb_registers_rx.setItem(1, 1, QtWidgets.QTableWidgetItem("A2"))
        self.ui.tb_registers_rx.setItem(2, 1, QtWidgets.QTableWidgetItem("8C"))
        self.ui.tb_registers_rx.setItem(3, 1, QtWidgets.QTableWidgetItem("90"))
        self.ui.tb_registers_rx.setItem(4, 1, QtWidgets.QTableWidgetItem("1F"))
    def reset_regs_tx(self):
        btn_option = QtWidgets.QMessageBox.warning(
            self,
            "Reset TX registers",
            "Do you want to reset the registers of TX to their default values?",
            buttons = QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            defaultButton = QtWidgets.QMessageBox.No
        )

        if btn_option == QtWidgets.QMessageBox.Yes:
            print("YAY!")
        else:
            print("NAY!")

    def reset_regs_rx(self):
        btn_option = QtWidgets.QMessageBox.warning(
            self,
            "Reset RX registers",
            "Do you want to reset the registers of RX to their default values?",
            buttons = QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            defaultButton = QtWidgets.QMessageBox.No
        )

        if btn_option == QtWidgets.QMessageBox.Yes:
            print("YAY!")
        else:
            print("NAY!")
