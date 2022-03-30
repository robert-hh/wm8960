# Driver for the WM8960 codec

This driver supports controlling a WM8960 codec. It is a literal Python translation of
the C-Code provided by NXP/Freescale for their i.MX RT series of MCUs. Almost nothing was
added, and just a few API related names were changed or added to cope with the naming style
of MicroPython.

## Features

The primary purpose of the driver is initialisation and setting operation modes of the codec.
I does not do the audio data processing for the codec. That is the task of a separate driver
built into the Operating system or firmware of a device.

## Connection

The WM8960 supports next to the audio interface the I2C interface. The connection depends on the interface used
and the number of devices in the system. For the I2C interface, SCL and SDA have to be connected, and of course
GND and Vcc. The I2C default address is 0x1a.

## Class

The driver contains the WM8960 class and quite a few name definitions.

```
wm8960=wm8960.WM8960(i2c, *,
    sample_rate=16000,
    bits=16,
    swap=SWAP_NONE,
    route=ROUTE_PLAYBACK_RECORD,
    left_input=MIC_INPUT3,
    right_input=INPUT_MIC2,
    sysclk_source=SYSCLK_MCLK,
    mclk_freq=None,
    primary=False,
    adc_sync=SYNC_DAC,
    protocol=bus_I2S,
    i2c_address=WM8960_I2C_ADDR
)
```

Only the first argument, i2c, is mandatory. All others are optional. Arguments:

- *i2c* The I2C bus object. It has be be created beforehand.
- *sample_rate* The audio sample rate. Acceptable values are 8000, 11025, 12000,
16000, 22050, 24000, 32000, 44100, 48000, 96000, 192000 and 384000. Note, that
not every I2S hardware will support all values.
- *bits* The number of bits per audio word. Acceptable value are 16, 20, 24, and 32.
- *swap* Swap the left & right channel, if set. For a list of options, see the table below.
- *route* Setting the audio path in the codec. For a list of options, see the table below.
- *left_input* Set the audio source for the left input channel. For a list of options, see the table below.
- *right_input* Set the audio source for the right input channel.For a list of options, see the table below.
- *sysclk_source* Control, whether the internal master clock called "sysclk" is directly taken from
the MCLK input or derived from it using an internal PLL. It is usually not required to change that.
- *mclk_freq* Argument for telling the mclk frequency applied to the MCLK pin of the codec If not set, default values are used.
- *primary* Let the WM8960 act as Primary or Secondary device. The default setting is False. When set to False, sample_rate and bits are controlled by the MCU.
- *adc_sync* Tell which input is used for the ADC sync signal. The default is using the DACLRC pin.
- *protocol* Setting the communication protocol. The default is I2S. For a list of options, see the table below.
- *i2c_address* The I2C address of the WM8960. The default is 0x1a or 26.

If mclk_freq is not set, the following default values are assumed:

- sysclk_source == SYSCLK_PLL: 11.2896 MHz for sample rates of 44100, 22050 and 11015 Hz, and 12.288 Mhz for sample rates < 48000, otherwise sample_rate * 256.
- sysclk_source == SYSCLK_MCLK: sample_rate * 256.

If the MCLK signal is applied using e.g. a separate oscillator, it must be specified for proper operation.

## Tables of parameter constants
**Swap Parameter**

|Value|Name|
|:---:|:-----|
|0| SWAP_NONE |
|1| SWAP_INPUT|
|2| SWAP_OUTPUT |

**Route parameter:**

|Value|Name|
|:---:|:------|
0| ROUTE_BYPASS |
1| ROUTE_PLAYBACK |
2| ROUTE_PLAYBACK_RECORD |
5| ROUTE_RECORD |

**Protocol Parameter**

|Value|Name|
|:---:|:-----|
|2| BUS_I2S |
|1| BUS_LEFT_JUSTIFIED |
|0| BUS_RIGHT_JUSTIFIED|
|3| BUS_PCMA |
|19| BUS_PCMB |

**Input Source Parameter**

|Value|Name|
|:---:|:-----|
|0| INPUT_CLOSED |
|1| INPUT_MIC1 |
|2| INPUT_MIC2|
|3| INPUT_MIC3|
|4| INPUT_LINE2_ |
|5| INPUT_LINE3 |

**Route Parameter**

|Value|Name|
|:---:|:-----|
|0| ROUTE_BYPASS |
|1| ROUTE_PLAYBACK |
|2| ROUTE_PLAYBACK_RECORD|
|5| ROUTE_RECORD |

**Master Clock Source Parameter**

|Value|Name|
|:---:|:-----|
|0| SYSCLK_MCLK |
|1| SYSCLK_PLL|

**Module Names**

|Value|Name|
|:---:|:-----|
|0| MODULE_ADC |
|1| MODULE_DAC |
|2| MODULE_VREF |
|3| MODULE_HEADPHONE |
|4| MODULE_MIC_BIAS |
|5| MODULE_MIC |
|6| MODULE_LINE_IN |
|7| MODULE_LINE_OUT|
|8| MODULE_SPEAKER|
|9| MODULE_OMIX |
|10| MODULE_MONO_OUT |

**Play Channel Names**

|Value|Name|
|:---:|:-----|
|1| PLAY_HEADPHONE_LEFT |
|2| PLAY_HEADPHONE_RIGHT|
|4| PLAY_SPEAKER_LEFT |
|8| PLAY_SPEAKER_RIGHT |

**adc_sync Parameters**

|Value|Name|
|:---:|:-----|
|0| SYNC_ADC|
|1| SYNC_DAC|


## Methods

Next to the initialisation, the driver provides some useful methods for
controlling the operation:

### set_left_input(input source)

Specify the source for the left input. The input source names are listed above.

### set_right_input(input source)

Specify the source for the left input. For a list of suitable parameter values, see
the table above.

### volume(module [, value_l [, value_r]])

Sets or get the volume of a certain module. If not value is supplied, the
actual volume is returned. If two values are given, the first one is used
for the left channel, the second for the right channel. The value range is normalized
to 0.0-100.0 with a logarithmic scale.
For a list of suitable modules and db/step, see the table below.

**Module Names and dB steps**

|dB/Step|Name|
|:---:|:-----|
|1.28| MODULE_ADC |
|1.28| MODULE_DAC |
|0.8| MODULE_HEADPHONE |
|0.475| MODULE_LINE_IN |
|0.8| MODULE_SPEAKER |


### mute(module, enable, soft=True, ramp=wm8960.mute_fast)

Mute or unmute the output. If **enable** is True, the output is muted, if False
it is unmuted. 
If **soft** is True, mute will happen as a soft transition. The time for
the transistion is defined by **ramp**, which is either mute_fast or mute_slow.


### set_data_route(route)

Set the audio data route. For the parameter value/names, look at the table above.


### set_module(module, True|False)

Enable or disable a module. For the list of module names, look at the table above.
Note that enabling module_mono_out is different from the mono() method. The first
enables output 3, while the mono method sends a mono mix to the left and right output.

### enable_module(module, True|False)

Enable a module. For the list of module names, look at the table above.

### disable_module(module, True|False)

Disable a module. For the list of module names, look at the table above.

### expand_3d(level)

Enable Stereo 3d exansion. Level is a number between 0 and 15. A value of 0
disables the expansion.

### mono(True | False)

If set to True, a Mono mix is sent to the left and right output channel.  This
is different from enabling module_mono_mix, which enables output 3.

### alc_mode(channel, mode=ALC_MODE)

Enables or disables ALC mode. Parameters are:  

**channel** Enable and set the channel for ALC. The parameter values are:  

  - ALC_OFF:   Switch ALC off
  - ALS_RIGHT:  Use the right input channel
  - ALC_LEFT:   Use the left input channel
  - ALC_STEREO: Use both input channels.  

**mode** Set the ALC mode. Input values are  

  - ALC_MODE:   act as ALC
  - ALC_LIMITER: act as limiter. 


### alc_gain(target=-12, max_gain=30, min_gain=-17.25, noise_gate=-78)

Set the target level, highest and lowest gain levels and the noise gate as dB level.
Permitted ranges are:  

- target: -22.5 to -1.5 dB
- max_gain: -12 to 30 dB
- min_gain: -17 to 25 dB
- noise_gate: -78 to -30 dB

Excess values are limited to the permitted ranges.  A value of -78 or less 
for **noise_gate** disables the noise gate function.

### alc_time(attack=24, decay=192, hold=0)

Set the dynamic characteristic of ALC. The times are given as ms values. Permitted ranges are:

- attack: 6 to 6140
- decay: 24 to 24580
- hold: 0 to 43000

Excess values are limited within the permitted ranges.

### deemphasis(True | False)

Enables or disables a deemphasis filter for playback. This filter is applied only for
sample rates of 32000, 44100 and 48000. For other sample rates, the filter setting
is silently ignored.

### deinit()

Disable all modules.


# Example Code

```
# Micro_python WM8960 Codec driver
#
# Setting the codec to secondary mode using the default settings
#
from machine import Pin, I2C
import wm8960

i2c = I2C(0)
wm=wm8960.WM8960(i2c)
```

```
# Micro_python WM8960 Codec driver
#
# Setting the codec to primary mode using specific audio format settings
#
from machine import Pin, I2C
import wm8960

i2c = I2C(0)
wm=wm8960.WM8960(i2c, primary=True, sample_rate=16000, bits=32)
```


Record with a Sparkfun WM8960 breakout board with Teensy in secondary mode(default):
```
# Micro_python WM8960 Codec driver
#
# The breakout board uses a fixed 24MHz MCLK. Therefore the internal
# PLL must be used as sysclk, which is the master audio clock.
# The Sparkfun board has the WS pins for RX and TX connected on the
# board. Therefore adc_sync must be set to SYNC_ADC, to configure
# it's ADCLRC pin as input.
#
from machine import Pin, I2C
import wm8960
i2c = I2C(0)
wm=wm8960.WM8960(i2c, sample_rate=16_000,
    adc_sync=wm8960.SYNC_ADC,
    sysclk_source=wm8960.SYSCLK_PLL,
    mclk_freq=24_000_000,
    left_input=wm8960.INPUT_MIC1,
    right_input=wm8960.INPUT_CLOSED)
```

Play with a Sparkfun WM8960 breakout board with Teensy in secondary mode(default)::
```
# The breakout board uses a fixed 24MHz MCLK. Therefore the internal
# PLL must be used as sysclk, which is the master audio clock.
# The Sparkfun board has the WS pins for RX and TX connected on the
# board. Therefore adc_sync must be set to SYNC_ADC, to configure
# it's ADCLRC pin as input.

from machine import I2C
i2c=I2C(0)
import wm8960
wm=wm8960.WM8960(i2c, sample_rate=44_100,
    adc_sync=wm8960.SYNC_ADC,
    sysclk_source=wm8960.SYSCLK_PLL,
    mclk_freq=24_000_000)
wm.set_volume(wm8960.MODULE_HEADPHONE, 100)
```
