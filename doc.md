## Context
Updated context labels and dropdown menu for the WC60GHz project.

Field description | Field type | Field ID | Remarks 
:-:|:-:|:-:|:-:
Available contexts | #label | `lbl_available_contexts` | _static_ 
Available contexts | #combo_box |  `cb_available_contexts` | Contains all the found available contexts
Hardware name | #label | `lbl_hardware_name` | _static_
Hardware name | #label_dyn | `lbl_hardware_name_dyn` | Display the device name
Vendor | #label | `lbl_vendor` | _static_
Vendor | #label_dyn | `lbl_vendor_dyn` | Display the hardware vendor
Hardware carrier | #label | `lbl_hardware_carrier` | _static_
Hardware carrier | #label_dyn | `lbl_hardware_carrier_dyn` | Display the hardware carrier
Hardware serial | #label |`lbl_hardware_serial`| _static_
Hardawre serial | #label_dyn |`lbl_hardware_serial_dyn`| Display the hardware serial
Local | #label |`lbl_local`|_static_
Local | #label_dyn | `lbl_local_dyn` | Display the local value

### Implementation details for [[#Context]]
Type | Field ID | To do
:-:|:-:| -
#field | `lbl_available_contexts` | <input type="checkbox" checked> display text "Available contexts"
#field | `cb_available_contexts` | <input type="checkbox" checked> should display only the usb contexts <br> <input type="checkbox" checked> connect `activated` signal to `ctx_canged` slot 
#slot | `ctx_changed` | <input type="checkbox" checked> disable "Select contexts..." option <br> <input type="checkbox" checked> reset user interface <br> <input type="checkbox"> check device name [`ADMV9615` or `ADMV9625`] <br> <input type="checkbox"> update all #label_dyn items in the context details <br> <input type="checkbox" checked> enable #switch for `TX` and `RX`

## Transmitter (TX)
Field description | Field type | Field ID | Remarks
:-:|:-:|:-:|:-:
Power | #label | `lbl_power_tx` | _static_
Power switch | #switch | `btn_power_tx` | Turn `ON` or `OFF` the transmitter
LO Frequency | #label | `lbl_lo_frequency_tx` | _static_
LO Frequency | #combo_box | `cb_lo_frequency_tx` | Contains all the available LO frequencies for TX
Autotuning | #check_box | `chk_autotuning_tx` | Enable/Disable autotuning for TX
Gain | #label #tunning_option| `lbl_gain_tx` | _static_
Gain | #combo_box #tunning_option| `cb_gain_tx` | Contains all the available gains for TX
RF Attenuation Index | #label #tunning_option| `lbl_rf_attn_index` | _static_
RF Attenuation Index | #combo_box #tunning_option| `cb_rf_attn_index` | Contains all the available attenuation indexes for TX
Lock detection | #label | `lbl_lock_detect_tx` | _static_ <br> part of #status_tx
Lock detection | #custom_widget | `cw_lock_detect_tx` | Colored <font style="color:green">GREEN</font> if there is a lock and <font style="color:red">RED</font> otherwise <br> part of #status_tx
Temperature | #label | `lbl_temp_tx` | _static_ <br> part of #status_tx
Temperature | #label_dyn | `lbl_temp_tx_dyn` | Display the temperature on the transmitter <br> part of #status_tx
Power usage | #label | `lbl_power_usage_tx` | _static_ <br> part of #status_tx
Power usage | #label_dyn | `lbl_power_usage_tx_dyn` | Display the power usage of the transmitter <br> part of #status_tx
Register map | #table | `tb_registers_tx` | Display the contents of the registers of `HMC6300`
Reset registers | #button | `btn_reset_regs_tx` | Reset the registers of `HMC6300` to their default values
Refresh registers | #button | `btn_refresh_regs_tx` | Read the values from the registers of `HMC6300`

### Implementation details for [[#Transmitter (TX)]]
Type | Field ID | To do
:-: | :-: | -
#slot | `power_switch_tx` | **Turning ON** <br> <input type="checkbox" checked> enable `lbl_lo_frequency_tx` and `cb_lo_frequency_tx` <br> <input type="checkbox" checked> enable `chk_autotuning_tx` <br> <input type="checkbox" checked> check `chk_autoning_tx` state <ul><li>if `set` disable all #tunning_option</li><li>if not `set` enable all #tunning_option</li></ul> <input type="checkbox" checked> enable #status_tx options <br> <input type="checkbox" checked> enable `tb_registers_tx` `btn_reset_regs_tx` and `btn_refresh_regs_tx` <br> <input type="checkbox" checked> start monitoring threads <br> **Turning OFF** <br> <input type="checkbox" checked> disable all of the above <br> <input type="checkbox" checked> stop monitoring threads
#slot | `autotuning_switch_tx` | **Checked** <br> <input type="checkbox" checked> disable all #tunning_option<br> **Unchecked** <br> <input type="checkbox" checked> enable all #tunning_option

## Receiver (RX)
Field description | Field type | Field ID | Remarks
:-:|:-:|:-:|:-:
Power | #label | `lbl_power_rx` | _static_
Power switch | #switch | `btn_power_rx` | Turn `ON` or `OFF` the transmitter
LO Frequency | #label | `lbl_lo_frequency_rx` | _static_
LO Frequency | #combo_box | `cb_lo_frequency_rx` | Contains all the available LO frequencies for RX
Autotuning | #check_box | `chk_autotuning_rx` | Enable/Disable autotuning for RX
Gain | #label #tunning_option| `lbl_gain_rx` | _static_
Gain | #combo_box #tunning_option| `cb_gain_rx` | Contains all the available gains for RX
BB Attenuation Index | #label #tunning_option| `lbl_bb_attn_index` | _static_
BB Attenuation Index | #combo_box #tunning_option| `cb_bb_attn_index` | Contains all the available attenuation indexes for RX
Lock detection | #label | `lbl_lock_detect_rx` | _static_ <br> part of #status_rx 
Lock detection | #custom_widget | `cw_lock_detect_rx` | Colored <font style="color:green">GREEN</font> if there is a lock and <font style="color:red">RED</font> otherwise <br> part of #status_rx 
Temperature | #label | `lbl_temp_rx` | _static_ <br> part of #status_rx 
Temperature | #label_dyn | `lbl_temp_rx_dyn` | Display the temperature on the receiver <br> part of #status_rx 
Power usage | #label | `lbl_power_usage_rx` | _static_ <br> part of #status_rx 
Power usage | #label_dyn | `lbl_power_usage_rx_dyn` | Display the power usage of the receiver <br> part of #status_rx 
Register map | #table | `tb_registers_rx` | Display the contents of the registers of `HMC6301`
Reset registers | #button | `btn_reset_regs_rx` | Reset the registers of `HMC6301` to their default values
Refresh registers | #button | `btn_refresh_regs_rx` | Read the values from the registers of `HMC6301`

### Implementation details for [[#Receiver (RX)]]
Type | Field ID | To do
:-: | :-: | -
#slot | `power_switch_rx` | **Turning ON** <br> <input type="checkbox" checked> enable `lbl_lo_frequency_rx` and `cb_lo_frequency_rx` <br> <input type="checkbox" checked> enable `chk_autotuning_rx` <br> <input type="checkbox" checked> check `chk_autotuning_rx` state <ul><li>if `set` disable all #tunning_option</li><li>if not `set` enable all #tunning_option</li></ul><input type="checkbox" checked> enable #status_rx options <br> <input type="checkbox" checked> enable `tb_registers_rx` `btn_reset_regs_rx` and `btn_refresh_regs_rx` <br> <input type="checkbox" checked> start monitoring threads <br> **Turning OFF** <br> <input type="checkbox" checked> disable all of the above <br> <input type="checkbox" checked> stop monitoring threads
#slot | `autotuning_switch_rx` | **Checked** <br> <input type="checkbox" checked> disable all #tunning_option <br> **Unchecked** <br> <input type="checkbox" checked> enable all #tunning_option
