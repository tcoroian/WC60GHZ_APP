# This Python file uses the following encoding: utf-8
from PySide6 import QtWidgets
from ui_alternativewindow import Ui_AlternativeWindow

import iio
import constants
import status_monitor


class MainWindow(QtWidgets.QMainWindow):

    iio_ctx = iio.Context()
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

    def disable_options(self):
        self.ui.lbl_power_tx.setEnabled(False)
        self.ui.lbl_power_rx.setEnabled(False)
        self.ui.slider_power_tx.setEnabled(False)
        self.ui.slider_power_rx.setEnabled(False)

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

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_AlternativeWindow()
        self.ui.setupUi(self)

        # Disable all options in TX and RX group boxes
        self.disable_options()

        # Add usb contexts to dropdown menu
        contexts = iio.scan_contexts()
        self.ui.cb_available_contexts.clear()
        self.ui.cb_available_contexts.addItems(["Select context..."])
        if contexts != None:
            # Boards are connected
            for ctx in contexts.keys():
                if ctx.startswith("usb"):
                    self.ui.cb_available_contexts.addItems([ctx])

        # Connect slot to update context labels
        self.ui.cb_available_contexts.activated.connect(self.ctx_changed)

        # Connect slots to enable/disable device configuration and monitoring
        self.ui.slider_power_tx.valueChanged.connect(self.power_switch_tx)
        self.ui.slider_power_rx.valueChanged.connect(self.power_switch_rx)

        # Connect slots to enable/disable tuning options
        self.ui.chk_autotuning_tx.stateChanged.connect(self.autotuning_switch_tx)
        self.ui.chk_autotuning_rx.stateChanged.connect(self.autotuning_switch_rx)

    def ctx_changed(self):
        text = self.ui.cb_available_contexts.currentText()

        if not text.startswith("usb"):
            return

        self.ui.cb_available_contexts.model().item(0).setEnabled(False)

        self.iio_ctx = iio.Context(text)

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
        self.ui.slider_power_tx.setEnabled(True)
        self.ui.slider_power_rx.setEnabled(True)

    def power_switch_tx(self, value):
        if value == 1:
            self.switch_device_options_tx()
            autotuning = self.ui.chk_autotuning_tx.isChecked()
            self.switch_tuning_options_tx(not autotuning)
            self.switch_status_options_tx()
            self.switch_register_map_tx()
            self.monitors.start_monitoring_lock_tx(self.ui.cw_lock_detect_tx)
        else:
            self.switch_device_options_tx(False)
            self.switch_tuning_options_tx(False)
            self.switch_status_options_tx(False)
            self.switch_register_map_tx(False)
            self.monitors.stop_monitoring_lock_tx()

    def power_switch_rx(self, value):
        if value == 1:
            self.switch_device_options_rx()
            autotuning = self.ui.chk_autotuning_rx.isChecked()
            self.switch_tuning_options_rx(not autotuning)
            self.switch_status_options_rx()
            self.switch_register_map_rx()
            self.monitors.start_monitoring_lock_rx(self.ui.cw_lock_detect_rx)
        else:
            self.switch_device_options_rx(False)
            self.switch_tuning_options_rx(False)
            self.switch_status_options_rx(False)
            self.switch_register_map_rx(False)
            self.monitors.stop_monitoring_lock_rx()

    def autotuning_switch_tx(self, state):
        self.switch_tuning_options_tx(not state)

    def autotuning_switch_rx(self, state):
        self.switch_tuning_options_rx(not state)
