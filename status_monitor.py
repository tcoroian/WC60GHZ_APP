# This Python file uses the following encoding: utf-8

import threading
import time
import constants

class StatusMonitor:

    threads = list()

    LOCK_TX_EXIT = threading.Event()
    LOCK_RX_EXIT = threading.Event()

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

    def __init__(self):
        pass

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
