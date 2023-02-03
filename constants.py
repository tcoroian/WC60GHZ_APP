# This Python file uses the following encoding: utf-8

style_led_green = """
    color: white;
    border-radius: 10;
    background-color: qlineargradient(spread:pad, x1:0.145, y1:0.16, x2:1, y2:1, stop:0 rgba(20, 252, 7, 255), stop:1 rgba(25, 134, 5, 255))
"""

style_led_red = """
    color: white;
    border-radius: 10;
    background-color: qlineargradient(spread:pad, x1:0.145, y1:0.16, x2:1, y2:1, stop:0 rgba(252, 20, 7, 255), stop:1 rgba(134, 25, 5, 255))
"""

style_led_grey = """
    color: white;
    border-radius: 10;
    background-color: qlineargradient(spread:pad, x1:0.145, y1:0.16, x2:1, y2:1, stop:0 rgba(200, 200, 200, 255), stop:1 rgba(134, 134, 134, 255))
"""

style_default_label = "color: black"
style_error_label = "color: red"

style_btn_on = "background-color: lightgreen"
style_btn_off = "background-color: lightgrey"

text_no_context = "No context"
text_not_iio = "Not an IIO device"

# IIO attribute names

dev_MWC = "mwc"

dev_HMC6300 = "hmc6300"
dev_HMC6301 = "hmc6301"
dev_PHY = "adin1300"
dev_SERIAL = ""

ctx_HW_MODEL = "hw_model"
ctx_FW_VERSION = "fw_version"

dev_attr_LO_FREQ = "vco"
dev_attr_LO_FREQ_AVB = "vco_available"
dev_attr_ENABLED = "enabled"
dev_attr_RESET = "tx_rx_reset"

chn_TEMP = "temp"
chn_attr_RAW = "raw"
