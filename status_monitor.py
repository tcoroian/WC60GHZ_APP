# This Python file uses the following encoding: utf-8
from PySide6.QtSerialPort import QSerialPortInfo

import threading
import time
import constants as ct
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

    # def context_search(self, window):
    #     added_contexts = list()
    #     while True:
    #         contexts = iio.scan_contexts()
    #         if contexts != None:
    #             # Boards are connected
    #             for ctx in contexts.keys():
    #                 if ctx.startswith("usb") and ctx not in added_contexts:
    #                     window.ui.cb_available_contexts.addItems([ctx])
    #                     added_contexts.append(ctx)
    #         for old_ctx in added_contexts:
    #             if old_ctx not in contexts:
    #                 added_contexts.remove(old_ctx)
    #                 index = window.ui.cb_available_contexts.findText(old_ctx)
    #                 if index > -1:
    #                     if window.ui.cb_available_contexts.currentIndex() == index:
    #                         window.ui.cb_available_contexts.setCurrentIndex(0)
    #                         window.reset_ui()
    #                     window.ui.cb_available_contexts.removeItem(index)
    
    def context_search(self, window):
        while True:
            cb = window.ui.cb_available_contexts
            available_ports = QSerialPortInfo.availablePorts()
            ports = [port.portName() for port in available_ports]
            options_in_cb = [cb.itemText(i) for i in range(1, cb.count())]
            # print(ports)
            for port in ports:
                index = cb.findText(port)
                if index <= 0:
                    cb.addItems([port])
                    
            # Check if the selected device is still connected
            if (cb.currentIndex() > 0):
                try:
                    ctx = iio.Context("serial:" + cb.currentText() + ",57600,8n1n")
                    ctx = None
                except Exception as e:
                    if str(e).__contains__("[Errno 2]"):
                        # cb.setItemText(cb.currentIndex(), "Device disconected")
                        print(e)
                        cb.currentIndexChanged.emit(cb.currentIndex())
                    else:
                        pass
                    
            for port in options_in_cb:
                if port not in ports:
                    index = cb.findText(port)
                    cb.removeItem(index)
            
            time.sleep(5)

    def monitor_lock_mechanism_tx(self, led):
        while True:
            led.setStyleSheet(ct.style_led_green)
            time.sleep(1)
            led.setStyleSheet(ct.style_led_red)
            time.sleep(1)
            if self.LOCK_TX_EXIT.is_set():
                break
        led.setStyleSheet(ct.style_led_grey)

    def monitor_lock_mechanism_rx(self, led):
        while True:
            led.setStyleSheet(ct.style_led_green)
            time.sleep(1)
            led.setStyleSheet(ct.style_led_red)
            time.sleep(1)
            if self.LOCK_RX_EXIT.is_set():
                break
        led.setStyleSheet(ct.style_led_grey)

    def monitor_temp_tx(self, lbl, ctx):
        while True:
            temp = ctx.find_device(ct.dev_HMC6300).find_channel(ct.chn_TEMP).attrs.get(ct.chn_attr_RAW).value
            lbl.setText(str(temp) + " °C")
            time.sleep(5)
            lbl.setText("18 °C")
            time.sleep(1)
            if self.TEMP_TX_EXIT.is_set():
                break
        lbl.setText(ct.text_no_context)

    def monitor_temp_rx(self, lbl, ctx):
        while True:
            temp = ctx.find_device(ct.dev_HMC6301).find_channel(ct.chn_TEMP).attrs.get(ct.chn_attr_RAW).value
            lbl.setText(str(temp) + " °C")
            time.sleep(5)
            lbl.setText("20 °C")
            time.sleep(1)
            if self.TEMP_RX_EXIT.is_set():
                break
        lbl.setText(ct.text_no_context)

    def monitor_power_tx(self, lbl):
        while True:
            lbl.setText("221 mV")
            time.sleep(1)
            lbl.setText("259 mV")
            time.sleep(1)
            if self.POWR_TX_EXIT.is_set():
                break
        lbl.setText(ct.text_no_context)

    def monitor_power_rx(self, lbl):
        while True:
            lbl.setText("225 mV")
            time.sleep(1)
            lbl.setText("263 mV")
            time.sleep(1)
            if self.POWR_RX_EXIT.is_set():
                break
        lbl.setText(ct.text_no_context)

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
    def start_monitoring_temp_tx(self, lbl, ctx):
        self.TEMP_TX_EXIT.clear()
        thread = threading.Thread(target = self.monitor_temp_tx, args = (lbl, ctx,), daemon = True)
        self.threads.append(thread)
        thread.start()

    def start_monitoring_temp_rx(self, lbl, ctx):
        self.TEMP_RX_EXIT.clear()
        thread = threading.Thread(target = self.monitor_temp_rx, args = (lbl, ctx,), daemon = True)
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
