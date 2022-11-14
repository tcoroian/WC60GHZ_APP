# This Python file uses the following encoding: utf-8

import threading
import time
import constants
import iio

class StatusMonitor:

    threads = list()

    LOCK_TX_EXIT = threading.Event()
    LOCK_RX_EXIT = threading.Event()
    TEMP_TX_EXIT = threading.Event()
    TEMP_RX_EXIT = threading.Event()
    POWR_TX_EXIT = threading.Event()
    POWR_RX_EXIT = threading.Event()

    def __init__(self):
        pass

    def context_search(self, window):
        added_contexts = list()
        while True:
            contexts = iio.scan_contexts()
            if contexts != None:
                # Boards are connected
                for ctx in contexts.keys():
                    if ctx.startswith("usb") and ctx not in added_contexts:
                        window.ui.cb_available_contexts.addItems([ctx])
                        added_contexts.append(ctx)
            for old_ctx in added_contexts:
                if old_ctx not in contexts:
                    added_contexts.remove(old_ctx)
                    index = window.ui.cb_available_contexts.findText(old_ctx)
                    if index > -1:
                        if window.ui.cb_available_contexts.currentIndex() == index:
                            window.ui.cb_available_contexts.setCurrentIndex(0)
                            window.reset_ui()
                        window.ui.cb_available_contexts.removeItem(index)

    def monitor_lock_mechanism_tx(self, led):
        while True:
            led.setStyleSheet(constants.style_led_green)
            time.sleep(1)
            led.setStyleSheet(constants.style_led_red)
            time.sleep(1)
            if self.LOCK_TX_EXIT.is_set():
                break
        led.setStyleSheet(constants.style_led_grey)

    def monitor_lock_mechanism_rx(self, led):
        while True:
            led.setStyleSheet(constants.style_led_green)
            time.sleep(1)
            led.setStyleSheet(constants.style_led_red)
            time.sleep(1)
            if self.LOCK_RX_EXIT.is_set():
                break
        led.setStyleSheet(constants.style_led_grey)

    def monitor_temp_tx(self, lbl):
        while True:
            lbl.setText("16 °C")
            time.sleep(1)
            lbl.setText("18 °C")
            time.sleep(1)
            if self.TEMP_TX_EXIT.is_set():
                break
        lbl.setText(constants.text_no_context)

    def monitor_temp_rx(self, lbl):
        while True:
            lbl.setText("19 °C")
            time.sleep(1)
            lbl.setText("20 °C")
            time.sleep(1)
            if self.TEMP_RX_EXIT.is_set():
                break
        lbl.setText(constants.text_no_context)

    def monitor_power_tx(self, lbl):
        while True:
            lbl.setText("221 mV")
            time.sleep(1)
            lbl.setText("259 mV")
            time.sleep(1)
            if self.POWR_TX_EXIT.is_set():
                break
        lbl.setText(constants.text_no_context)

    def monitor_power_rx(self, lbl):
        while True:
            lbl.setText("225 mV")
            time.sleep(1)
            lbl.setText("263 mV")
            time.sleep(1)
            if self.POWR_RX_EXIT.is_set():
                break
        lbl.setText(constants.text_no_context)

    def start_monitoring_lock_tx(self, led_tx):
        self.LOCK_TX_EXIT.clear()
        thread = threading.Thread(target = self.monitor_lock_mechanism_tx, args = (led_tx,), daemon = True)
        self.threads.append(thread)
        thread.start()

    def start_monitoring_lock_rx(self, led_rx):
        self.LOCK_RX_EXIT.clear()
        thread = threading.Thread(target = self.monitor_lock_mechanism_rx, args = (led_rx,), daemon = True)
        self.threads.append(thread)
        thread.start()

    def stop_monitoring_lock_tx(self):
        self.LOCK_TX_EXIT.set()

    def stop_monitoring_lock_rx(self):
        self.LOCK_RX_EXIT.set()
    def start_context_search(self, window):
        thread = threading.Thread(target = self.context_search, args = (window,), daemon = True)
        self.threads.append(thread)
        thread.start()
    def start_monitoring_temp_tx(self, lbl):
        self.TEMP_TX_EXIT.clear()
        thread = threading.Thread(target = self.monitor_temp_tx, args = (lbl,), daemon = True)
        self.threads.append(thread)
        thread.start()

    def start_monitoring_temp_rx(self, lbl):
        self.TEMP_RX_EXIT.clear()
        thread = threading.Thread(target = self.monitor_temp_rx, args = (lbl,), daemon = True)
        self.threads.append(thread)
        thread.start()

    def stop_monitoring_temp_tx(self):
        self.TEMP_TX_EXIT.set()

    def stop_monitoring_temp_rx(self):
        self.TEMP_RX_EXIT.set()

    def start_monitoring_power_tx(self, lbl):
        self.POWR_TX_EXIT.clear()
        thread = threading.Thread(target = self.monitor_power_tx, args = (lbl,), daemon = True)
        self.threads.append(thread)
        thread.start()

    def start_monitoring_power_rx(self, lbl):
        self.POWR_RX_EXIT.clear()
        thread = threading.Thread(target = self.monitor_power_rx, args = (lbl,), daemon = True)
        self.threads.append(thread)
        thread.start()

    def stop_monitoring_power_tx(self):
        self.POWR_TX_EXIT.set()

    def stop_monitoring_power_rx(self):
        self.POWR_RX_EXIT.set()
