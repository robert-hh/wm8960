#
# Driver class for the WM8960 Codec to be used e.g. with MIMXRT_1xxx Boards.
# Derived from the NXP SDK drivers.
#
# Copyright (c) 2015, Freescale Semiconductor, Inc., (C-Code)
# Copyright 2016-2021 NXP, (C-Code)
# All rights reserved.
#
# Translated to MicroPython by Robert Hammelrath, 2022
#
# SPDX-License-Identifier: BSD-3-Clause
#

import array

# Define the register addresses of WM8960.
_WM8960_LINVOL = const(0x0)
_WM8960_RINVOL = const(0x1)
_WM8960_LOUT1 = const(0x2)
_WM8960_ROUT1 = const(0x3)
_WM8960_CLOCK1 = const(0x4)
_WM8960_DACCTL1 = const(0x5)
_WM8960_DACCTL2 = const(0x6)
_WM8960_IFACE1 = const(0x7)
_WM8960_CLOCK2 = const(0x8)
_WM8960_IFACE2 = const(0x9)
_WM8960_LDAC = const(0xA)
_WM8960_RDAC = const(0xB)
_WM8960_RESET = const(0xF)
_WM8960_3D = const(0x10)
_WM8960_ALC1 = const(0x11)
_WM8960_ALC2 = const(0x12)
_WM8960_ALC3 = const(0x13)
_WM8960_NOISEG = const(0x14)
_WM8960_LADC = const(0x15)
_WM8960_RADC = const(0x16)
_WM8960_ADDCTL1 = const(0x17)
_WM8960_ADDCTL2 = const(0x18)
_WM8960_POWER1 = const(0x19)
_WM8960_POWER2 = const(0x1A)
_WM8960_ADDCTL3 = const(0x1B)
_WM8960_APOP1 = const(0x1C)
_WM8960_APOP2 = const(0x1D)
_WM8960_LINPATH = const(0x20)
_WM8960_RINPATH = const(0x21)
_WM8960_LOUTMIX = const(0x22)
_WM8960_ROUTMIX = const(0x25)
_WM8960_MONOMIX1 = const(0x26)
_WM8960_MONOMIX2 = const(0x27)
_WM8960_LOUT2 = const(0x28)
_WM8960_ROUT2 = const(0x29)
_WM8960_MONO = const(0x2A)
_WM8960_INBMIX1 = const(0x2B)
_WM8960_INBMIX2 = const(0x2C)
_WM8960_BYPASS1 = const(0x2D)
_WM8960_BYPASS2 = const(0x2E)
_WM8960_POWER3 = const(0x2F)
_WM8960_ADDCTL4 = const(0x30)
_WM8960_CLASSD1 = const(0x31)
_WM8960_CLASSD3 = const(0x33)
_WM8960_PLL1 = const(0x34)
_WM8960_PLL2 = const(0x35)
_WM8960_PLL3 = const(0x36)
_WM8960_PLL4 = const(0x37)

# WM8960 PLLN range */
_WM8960_PLL_N_MIN_VALUE = const(6)
_WM8960_PLL_N_MAX_VALUE = const(12)

# Cache register count
_WM8960_CACHEREGNUM = const(56)

# WM8960 CLOCK2 bits
_WM8960_CLOCK2_BCLK_DIV_MASK = const(0x0F)
_WM8960_CLOCK2_DCLK_DIV_MASK = const(0x1C0)
_WM8960_CLOCK2_DCLK_DIV_SHIFT = const(0x06)

# _WM8960_IFACE1 FORMAT bits
_WM8960_IFACE1_FORMAT_MASK = const(0x03)
_WM8960_IFACE1_FORMAT_SHIFT = const(0x00)
_WM8960_IFACE1_FORMAT_RJ = const(0x00)
_WM8960_IFACE1_FORMAT_LJ = const(0x01)
_WM8960_IFACE1_FORMAT_I2S = const(0x02)
_WM8960_IFACE1_FORMAT_DSP = const(0x03)

# _WM8960_IFACE1 WL bits
_WM8960_IFACE1_WL_MASK = const(0x0C)
_WM8960_IFACE1_WL_SHIFT = const(0x02)

# _WM8960_IFACE1 LRP bit
_WM8960_IFACE1_LRP_MASK = const(0x10)
_WM8960_IFACE1_LRP_SHIFT = const(0x04)
_WM8960_IFACE1_LRCLK_NORMAL_POL = const(0x00)
_WM8960_IFACE1_LRCLK_INVERT_POL = const(0x01)
_WM8960_IFACE1_DSP_MODEA = const(0x00)
_WM8960_IFACE1_DSP_MODEB = const(0x01)

# _WM8960_IFACE1 DLRSWAP bit
_WM8960_IFACE1_DLRSWAP_MASK = const(0x20)

# _WM8960_IFACE1 MS bit
_WM8960_IFACE1_MS_MASK = const(0x40)
_WM8960_IFACE1_MS_SHIFT = const(0x06)
_WM8960_IFACE1_SLAVE = const(0x00)
_WM8960_IFACE1_MASTER = const(0x01)

# _WM8960_IFACE1 BCLKINV bit
_WM8960_IFACE1_BCLKINV_MASK = const(0x80)
_WM8960_IFACE1_BCLKINV_SHIFT = const(0x07)
_WM8960_IFACE1_BCLK_NONINVERT = const(0x00)
_WM8960_IFACE1_BCLK_INVERT = const(0x01)

# _WM8960_IFACE1 ALRSWAP bit
_WM8960_IFACE1_ALRSWAP_MASK = const(0x100)
_WM8960_IFACE1_ALRSWAP_SHIFT = const(0x08)
_WM8960_IFACE1_ADCCH_NORMAL = const(0x00)
_WM8960_IFACE1_ADCCH_SWAP = const(0x01)

# _WM8960_POWER1
_WM8960_POWER1_VREF_MASK = const(0x40)
_WM8960_POWER1_VREF_SHIFT = const(0x06)

_WM8960_POWER1_AINL_MASK = const(0x20)
_WM8960_POWER1_AINL_SHIFT = const(0x05)

_WM8960_POWER1_AINR_MASK = const(0x10)
_WM8960_POWER1_AINR_SHIFT = const(0x04)

_WM8960_POWER1_ADCL_MASK = const(0x08)
_WM8960_POWER1_ADCL_SHIFT = const(0x03)

_WM8960_POWER1_ADCR_MASK = const(0x0)
_WM8960_POWER1_ADCR_SHIFT = const(0x02)

_WM8960_POWER1_MICB_MASK = const(0x02)
_WM8960_POWER1_MICB_SHIFT = const(0x01)

_WM8960_POWER1_DIGENB_MASK = const(0x01)
_WM8960_POWER1_DIGENB_SHIFT = const(0x00)

# _WM8960_POWER2
_WM8960_POWER2_DACL_MASK = const(0x100)
_WM8960_POWER2_DACL_SHIFT = const(0x08)

_WM8960_POWER2_DACR_MASK = const(0x80)
_WM8960_POWER2_DACR_SHIFT = const(0x07)

_WM8960_POWER2_LOUT1_MASK = const(0x40)
_WM8960_POWER2_LOUT1_SHIFT = const(0x06)

_WM8960_POWER2_ROUT1_MASK = const(0x20)
_WM8960_POWER2_ROUT1_SHIFT = const(0x05)

_WM8960_POWER2_SPKL_MASK = const(0x10)
_WM8960_POWER2_SPKL_SHIFT = const(0x04)

_WM8960_POWER2_SPKR_MASK = const(0x08)
_WM8960_POWER2_SPKR_SHIFT = const(0x03)

_WM8960_POWER3_LMIC_MASK = const(0x20)
_WM8960_POWER3_LMIC_SHIFT = const(0x05)
_WM8960_POWER3_RMIC_MASK = const(0x10)
_WM8960_POWER3_RMIC_SHIFT = const(0x04)
_WM8960_POWER3_LOMIX_MASK = const(0x08)
_WM8960_POWER3_LOMIX_SHIFT = const(0x03)
_WM8960_POWER3_ROMIX_MASK = const(0x04)
_WM8960_POWER3_ROMIX_SHIFT = const(0x02)

# _WM8960_DACCTL1 and 2
_WM8960_DACCTL1_MONOMIX_MASK = const(0x10)
_WM8960_DACCTL1_MONOMIX_SHIFT = const(0x4)
_WM8960_DACCTL1_DACMU_MASK = const(0x08)
_WM8960_DACCTL2_DACSMM_MASK = const(0x08)
_WM8960_DACCTL2_DACMR_MASK = const(0x04)


_WM8960_I2C_ADDR = const(0x1A)

# WM8960 maximum volume values
_WM8960_ADC_MAX_VOLUME = const(0xFF)
_WM8960_DAC_MAX_VOLUME = const(0xFF)
_WM8960_HEADPHONE_MAX_VOLUME = const(0x7F)
_WM8960_LINEIN_MAX_VOLUME = const(0x3F)
_WM8960_SPEAKER_MAX_VOLUME = const(0x7F)

# Config symbol names
# Modules
module_ADC = const(0)  # ADC module in WM8960
module_DAC = const(1)  # DAC module in WM8960
module_VREF = const(2)  # VREF module
module_headphone = const(3)  # Headphone
module_mic_bias = const(4)  # Mic bias
module_mic = const(5)  # Input Mic
module_line_in = const(6)  # Analog in PGA
module_line_out = const(7)  # Line out module
module_speaker = const(8)  # Speaker module
module_omix = const(9)  # Output mixer
module_mono = const(10)  # Mono mix

# Route
route_bypass = const(0)  # LINEIN->Headphone.
route_playback = const(1)  #  I2SIN->DAC->Headphone.
route_playback_record = const(2)  # I2SIN->DAC->Headphone, LINEIN->ADC->I2SOUT.
route_record = const(5)  # LINEIN->ADC->I2SOUT.

# Input
input_closed = const(0)  # Input device is closed
input_mic1 = const(1)  # Input as single ended mic, only use L/RINPUT1
input_mic2 = const(2)  # Input as diff. mic, use L/RINPUT1 and L/RINPUT2
input_mic3 = const(3)  # Input as diff. mic, use L/RINPUT1 and L/RINPUT3
input_line2 = const(4)  # Input as line input, only use L/RINPUT2
input_line3 = const(5)  # Input as line input, only use L/RINPUT3

# Play source
# source_PGA = const(1)  # wm8960 play source PGA
# source_input = const(2)  # wm8960 play source Input
# source_DAC = const(4)  # wm8960 play source DAC

# Play Channel
# play_headphone_left = const(1)  # wm8960 headphone left channel
# play_headphone_right = const(2)  # wm8960 headphone right channel
# play_speaker_left = const(4)  # wm8960 speaker left channel
# play_speaker_right = const(8)  # wm8960 speaker right channel

# ADC sync input
sync_adc = const(0)  # Use ADCLRC pin for ADC sync
sync_dac = const(1)  # used DACLRC pin for ADC sync

# Protocol type
bus_I2S = const(2)  # I2S type
bus_left_justified = const(1)  # Left justified mode
bus_right_justified = const(0)  # Right justified mode
bus_PCMA = const(3)  # PCM A mode
bus_PCMB = const(3 | (1 << 4))  # PCM B mode

# Channel swap
swap_none = const(0)
swap_input = const(1)
swap_output = const(2)

# Mute settings
mute_fast = const(0)
mute_slow = const(1)

# Sample Rate symbolic names dropped

# Bit Width symbolic names dropped

# Clock Source
sysclk_mclk = const(0)  # sysclk source from external MCLK
sysclk_PLL = const(1)  # sysclk source from internal PLL


class WM8960:

    # register cache of 56 register. Since registers cannot be read back, they are
    # kept in the table for modification
    # fmt: off
    reg = [
        0x0097, 0x0097, 0x0000, 0x0000, 0x0000, 0x0008, 0x0000,
        0x000a, 0x01c0, 0x0000, 0x00ff, 0x00ff, 0x0000, 0x0000,
        0x0000, 0x0000, 0x0000, 0x007b, 0x0100, 0x0032, 0x0000,
        0x00c3, 0x00c3, 0x01c0, 0x0000, 0x0000, 0x0000, 0x0000,
        0x0000, 0x0000, 0x0000, 0x0000, 0x0100, 0x0100, 0x0050,
        0x0050, 0x0050, 0x0050, 0x0000, 0x0000, 0x0000, 0x0000,
        0x0040, 0x0000, 0x0000, 0x0050, 0x0050, 0x0000, 0x0002,
        0x0037, 0x004d, 0x0080, 0x0008, 0x0031, 0x0026, 0x00e9
    ]
    # ftm: on

    _bit_clock_divider_table = {
        2: 0,
        3: 1,
        4: 2,
        6: 3,
        8: 4,
        11: 5,
        12: 6,
        16: 7,
        22: 8,
        24: 9,
        32: 10,
        44: 11,
        48: 12,
    }

    _dac_divider_table = {
        1.0 * 256: 0b000,
        1.5 * 256: 0b001,
        2 * 256: 0b010,
        3 * 256: 0b011,
        4 * 256: 0b100,
        5.5 * 256: 0b101,
        6 * 256: 0b110,
    }

    _audio_word_length_table = {
        16: 0b00,
        20: 0b01,
        24: 0b10,
        32: 0b11,
    }

    def __init__(
        self,
        i2c,
        sample_rate=16000,
        bits=16,
        swap=swap_none,
        route=route_playback_record,
        left_input=input_mic3,
        right_input=input_mic2,
        sysclk_source=sysclk_mclk,
        mclk_freq=None,
        primary=False,
        adc_sync=sync_dac,
        protocol=bus_I2S,
        i2c_address=_WM8960_I2C_ADDR,
    ):
        self.i2c = i2c
        self.i2c_address = i2c_address
        self.value_buffer = bytearray(2)
        self.sample_rate = sample_rate

        # check parameter consistency and set the sysclk value
        if sysclk_source == sysclk_PLL:
            if sample_rate in (11025, 22050, 44100):
                sysclk = 11289600
            else:
                sysclk = 12288000
            if sysclk < sample_rate * 256:
                sysclk = sample_rate * 256
            if mclk_freq is None:
                mclk_freq = sysclk
        else:  # sysclk_source == sysclk_mclk
            if mclk_freq is None:
                mclk_freq = sample_rate * 256
            sysclk = mclk_freq

        # Reset the codec
        self.write_reg(_WM8960_RESET, 0x00)
        #
        # VMID=50K, Enable VREF, AINL, AINR, ADCL and ADCR
        # I2S_IN (bit 0), I2S_OUT (bit 1), DAP (bit 4), DAC (bit 5), ADC (bit 6) are powered on
        self.write_reg(_WM8960_POWER1, 0xFE)
        #
        # Enable DACL, DACR, LOUT1, ROUT1, PLL down, SPKL, SPKR
        self.write_reg(_WM8960_POWER2, 0x1F8)
        #
        # Enable left and right channel input PGA, left and right output mixer
        self.write_reg(_WM8960_POWER3, 0x3C)

        if adc_sync == sync_adc:
            # ADC and DAC use different Frame Clock Pins
            self.write_reg(_WM8960_IFACE2, 0x00)  # ADCLRC 0x00:Input 0x40:output.
        else:
            # ADC and DAC use the same Frame Clock Pin
            self.write_reg(_WM8960_IFACE2, 0x40)  # ADCLRC 0x00:Input 0x40:output.
        # set data route
        self.set_data_route(route)
        # set data protocol
        self.set_protocol(protocol)

        if sysclk_source == sysclk_PLL:
            self.set_internal_pll_config(mclk_freq, sysclk)
        # set master or slave
        if primary:
            self.set_master_clock(sysclk, sample_rate, bits)

        self.set_primary(primary)
        # set speaker clock
        self.set_speaker_clock(sysclk)

        # swap channels
        if swap & swap_input:
            self.modify_reg(
                _WM8960_IFACE1,
                _WM8960_IFACE1_ALRSWAP_MASK,
                _WM8960_IFACE1 << _WM8960_IFACE1_ALRSWAP_SHIFT
            )
        if swap & swap_output:
            self.modify_reg(
                _WM8960_IFACE1,
                _WM8960_IFACE1_DLRSWAP_MASK,
                _WM8960_IFACE1 << _MM8960_IFACE1_DLRSWAP_SHIFT
            )

        # select left input
        self.set_left_input(left_input)
        # select right input
        self.set_right_input(right_input)

        self.write_reg(_WM8960_ADDCTL1, 0x0C0)
        self.write_reg(_WM8960_ADDCTL4, 0x60)  # Set GPIO1 to 0.

        self.write_reg(_WM8960_BYPASS1, 0x0)
        self.write_reg(_WM8960_BYPASS2, 0x0)
        #
        # ADC volume, 0dB
        self.write_reg(_WM8960_LADC, 0x1C3)
        self.write_reg(_WM8960_RADC, 0x1C3)
        #
        # Digital DAC volume, 0dB
        self.write_reg(_WM8960_LDAC, 0x1E0)
        self.write_reg(_WM8960_RDAC, 0x1E0)
        #
        # Headphone volume, LOUT1 and ROUT1, 0dB
        self.write_reg(_WM8960_LOUT1, 0x16F)
        self.write_reg(_WM8960_ROUT1, 0x16F)
        #
        # speaker volume 6dB
        self.write_reg(_WM8960_LOUT2, 0x1FF)
        self.write_reg(_WM8960_ROUT2, 0x1FF)
        #
        # enable class D output
        self.write_reg(_WM8960_CLASSD1, 0xF7)
        #
        # Unmute DAC.
        self.write_reg(_WM8960_DACCTL1, 0x0000)
        #
        # Input PGA volume 0 dB
        self.write_reg(_WM8960_LINVOL, 0x117)
        self.write_reg(_WM8960_RINVOL, 0x117)

        self.config_data_format(sysclk, sample_rate, bits)

    def deinit(self):

        self.set_module(module_ADC, False)
        self.set_module(module_DAC, False)
        self.set_module(module_VREF, False)
        self.set_module(module_line_in, False)
        self.set_module(module_line_out, False)
        self.set_module(module_speaker, False)

    def set_internal_pll_config(self, input_mclk, output_clk):
        pllF2 = output_clk * 4
        pll_prescale = 0
        sysclk_div = 1
        frac_mode = 0

        # disable PLL power
        self.modify_reg(_WM8960_POWER2, 1, 0)
        self.modify_reg(_WM8960_CLOCK1, 7, 0)

        pllN = pllF2 // input_mclk
        if pllN < _WM8960_PLL_N_MIN_VALUE:
            input_mclk //= 2
            pll_prescale = 1
            pllN = pllF2 // input_mclk
            if pllN < _WM8960_PLL_N_MIN_VALUE:
                sysclk_div = 2
                pllF2 *= 2
                pllN = pllF2 // input_mclk

        if (pllN < _WM8960_PLL_N_MIN_VALUE) or (pllN > _WM8960_PLL_N_MAX_VALUE):
            raise ValueError("Invalid MCLK vs. sysclk ratio")

        pllK = ((pllF2 % input_mclk) * (1 << 24)) // input_mclk
        if pllK != 0:
            frac_mode = 1

        self.write_reg(_WM8960_PLL1, (frac_mode << 5) | (pll_prescale << 4) | (pllN & 0x0F))
        self.write_reg(_WM8960_PLL2, (pllK >> 16) & 0xFF)
        self.write_reg(_WM8960_PLL3, (pllK >> 8) & 0xFF)
        self.write_reg(_WM8960_PLL4, pllK & 0xFF)
        # enable PLL power
        self.modify_reg(_WM8960_POWER2, 1, 1)
        self.modify_reg(_WM8960_CLOCK1, 7, ((0 if sysclk_div == 1 else sysclk_div) << 1) | 1)

    def set_master_clock(self, sysclk, sample_rate, bit_width):
        bit_clock_divider = sysclk // (sample_rate * bit_width * 2)
        try:
            reg_divider = self._bit_clock_divider_table[bit_clock_divider]
        except:
            raise ValueError("Invalid ratio of sysclk sample rate and bits")
        # configure the master bit clock divider will be better
        self.modify_reg(_WM8960_CLOCK2, _WM8960_CLOCK2_BCLK_DIV_MASK, reg_divider)

    def set_speaker_clock(self, sysclk):
        speaker_divider_table = (1.5, 2, 3, 4, 6, 8, 12, 16)
        for val in range(8):
            divider = speaker_divider_table[val]
            f = sysclk / divider
            if (500_000 < f < 1_000_000):
                break
        else:
            val = 7
        self.modify_reg(
            _WM8960_CLOCK2,
            _WM8960_CLOCK2_DCLK_DIV_MASK,
            val << _WM8960_CLOCK2_DCLK_DIV_SHIFT)

    def set_primary(self, master):
        if master:
            self.modify_reg(
                _WM8960_IFACE1,
                _WM8960_IFACE1_MS_MASK,
                _WM8960_IFACE1_MASTER << _WM8960_IFACE1_MS_SHIFT
            )

        else:
            self.modify_reg(
                _WM8960_IFACE1, _WM8960_IFACE1_MS_MASK, _WM8960_IFACE1_SLAVE << _WM8960_IFACE1_MS_SHIFT
            )

    def set_module(self, module, is_enabled):

        is_enabled = 1 if is_enabled else 0

        if module == module_ADC:

            self.modify_reg(
                _WM8960_POWER1, _WM8960_POWER1_ADCL_MASK, (is_enabled << _WM8960_POWER1_ADCL_SHIFT)
            )
            self.modify_reg(
                _WM8960_POWER1, _WM8960_POWER1_ADCR_MASK, (is_enabled << _WM8960_POWER1_ADCR_SHIFT)
            )

        elif module == module_DAC:

            self.modify_reg(
                _WM8960_POWER2, _WM8960_POWER2_DACL_MASK, (is_enabled << _WM8960_POWER2_DACL_SHIFT)
            )
            self.modify_reg(
                _WM8960_POWER2, _WM8960_POWER2_DACR_MASK, (is_enabled << _WM8960_POWER2_DACR_SHIFT)
            )

        elif module == module_VREF:

            self.modify_reg(
                _WM8960_POWER1, _WM8960_POWER1_VREF_MASK, (is_enabled << _WM8960_POWER1_VREF_SHIFT)
            )

        elif module == module_line_in:

            self.modify_reg(
                _WM8960_POWER1, _WM8960_POWER1_AINL_MASK, (is_enabled << _WM8960_POWER1_AINL_SHIFT)
            )
            self.modify_reg(
                _WM8960_POWER1, _WM8960_POWER1_AINR_MASK, (is_enabled << _WM8960_POWER1_AINR_SHIFT)
            )
            self.modify_reg(
                _WM8960_POWER3, _WM8960_POWER3_LMIC_MASK, (is_enabled << _WM8960_POWER3_LMIC_SHIFT)
            )
            self.modify_reg(
                _WM8960_POWER3, _WM8960_POWER3_RMIC_MASK, (is_enabled << _WM8960_POWER3_RMIC_SHIFT)
            )

        elif module == module_line_out:

            self.modify_reg(
                _WM8960_POWER2, _WM8960_POWER2_LOUT1_MASK, (is_enabled << _WM8960_POWER2_LOUT1_SHIFT)
            )
            self.modify_reg(
                _WM8960_POWER2, _WM8960_POWER2_ROUT1_MASK, (is_enabled << _WM8960_POWER2_ROUT1_SHIFT)
            )

        elif module == module_mic_bias:

            self.modify_reg(
                _WM8960_POWER1, _WM8960_POWER1_MICB_MASK, (is_enabled << _WM8960_POWER1_MICB_SHIFT)
            )

        elif module == module_speaker:

            self.modify_reg(
                _WM8960_POWER2, _WM8960_POWER2_SPKL_MASK, (is_enabled << _WM8960_POWER2_SPKL_SHIFT)
            )
            self.modify_reg(
                _WM8960_POWER2, _WM8960_POWER2_SPKR_MASK, (is_enabled << _WM8960_POWER2_SPKR_SHIFT)
            )
            self.write_reg(_WM8960_CLASSD1, 0xF7)

        elif module == module_omix:

            self.modify_reg(
                _WM8960_POWER3, _WM8960_POWER3_LOMIX_MASK, (is_enabled << _WM8960_POWER3_LOMIX_SHIFT)
            )
            self.modify_reg(
                _WM8960_POWER3, _WM8960_POWER3_ROMIX_MASK, (is_enabled << _WM8960_POWER3_ROMIX_SHIFT)
            )

        elif module == module_mono_out:

            self.write_reg(_WM8960_MONOMIX1, (is_enabled << 7))
            self.write_reg(_WM8960_MONOMIX2, (is_enabled << 7))
            self.write_reg(_WM8960_MONO, (is_enabled << 6))

        else:
            raise ValueError("Invalid module")

    def enable_module(self, module):
        self.set_module(module, True)

    def disable_module(self, module):
        self.set_module(module, False)

    def set_data_route(self, route):
        if route == route_bypass:
            # Bypass means from line-in to HP
            # Left LINPUT3 to left output mixer, LINPUT3 left output mixer volume = 0dB
            self.write_reg(_WM8960_LOUTMIX, 0x80)
            # Right RINPUT3 to right output mixer, RINPUT3 right output mixer volume = 0dB
            self.write_reg(_WM8960_ROUTMIX, 0x80)

        elif route == route_playback:
            # Data route I2S_IN-> DAC-> HP
            #
            # Left DAC to left output mixer, LINPUT3 left output mixer volume = 0dB
            self.write_reg(_WM8960_LOUTMIX, 0x100)
            # Right DAC to right output mixer, RINPUT3 right output mixer volume = 0dB
            self.write_reg(_WM8960_ROUTMIX, 0x100)
            self.write_reg(_WM8960_POWER3, 0x0C)
            # Set power for DAC
            self.set_module(module_DAC, True)
            self.set_module(module_omix, True)
            self.set_module(module_line_out, True)

        elif route == route_playback_record:
            #
            # Left DAC to left output mixer, LINPUT3 left output mixer volume = 0dB
            self.write_reg(_WM8960_LOUTMIX, 0x100)
            # Right DAC to right output mixer, RINPUT3 right output mixer volume = 0dB
            self.write_reg(_WM8960_ROUTMIX, 0x100)
            self.write_reg(_WM8960_POWER3, 0x3C)
            self.set_module(module_DAC, True)
            self.set_module(module_ADC, True)
            self.set_module(module_line_in, True)
            self.set_module(module_omix, True)
            self.set_module(module_line_out, True)

        elif route == route_record:
            # LINE_IN->ADC->I2S_OUT
            # Left and right input boost, LIN3BOOST and RIN3BOOST = 0dB
            self.write_reg(_WM8960_POWER3, 0x30)
            # Power up ADC and AIN
            self.set_module(module_line_in, True)
            self.set_module(module_ADC, True)

        else:
            raise ValueError("Invalid route")

    def set_left_input(self, input):

        if input == input_closed:
            # Disable the input
            val = self.read_reg(_WM8960_POWER1)
            val &= ~(_WM8960_POWER1_AINL_MASK | _WM8960_POWER1_ADCL_MASK)
            self.write_reg(_WM8960_POWER1, val)

        elif input == input_mic1:
            # Only LMN1 enabled, LMICBOOST to 13db, LMIC2B enabled
            val = self.read_reg(_WM8960_POWER1)
            val |= _WM8960_POWER1_AINL_MASK | _WM8960_POWER1_ADCL_MASK | _WM8960_POWER1_MICB_MASK
            self.write_reg(_WM8960_POWER1, val)
            self.write_reg(_WM8960_LINPATH, 0x138)
            self.write_reg(_WM8960_LINVOL, 0x117)

        elif input == input_mic2:
            val = self.read_reg(_WM8960_POWER1)
            val |= _WM8960_POWER1_AINL_MASK | _WM8960_POWER1_ADCL_MASK | _WM8960_POWER1_MICB_MASK
            self.write_reg(_WM8960_POWER1, val)
            self.write_reg(_WM8960_LINPATH, 0x178)
            self.write_reg(_WM8960_LINVOL, 0x117)

        elif input == input_mic3:
            val = self.read_reg(_WM8960_POWER1)
            val |= _WM8960_POWER1_AINL_MASK | _WM8960_POWER1_ADCL_MASK | _WM8960_POWER1_MICB_MASK
            self.write_reg(_WM8960_POWER1, val)
            self.write_reg(_WM8960_LINPATH, 0x1B8)
            self.write_reg(_WM8960_LINVOL, 0x117)

        elif input == input_line2:
            val = self.read_reg(_WM8960_POWER1)
            val |= _WM8960_POWER1_AINL_MASK | _WM8960_POWER1_ADCL_MASK
            self.write_reg(_WM8960_POWER1, val)
            val = self.read_reg(_WM8960_INBMIX1)
            val |= 0xE
            self.write_reg(_WM8960_INBMIX1, val)

        elif input == input_line3:
            val = self.read_reg(_WM8960_POWER1)
            val |= _WM8960_POWER1_AINL_MASK | _WM8960_POWER1_ADCL_MASK
            self.write_reg(_WM8960_POWER1, val)
            val = self.read_reg(_WM8960_INBMIX1)
            val |= 0x70
            self.write_reg(_WM8960_INBMIX1, val)

        else:
            raise ValueError("Invalid input name")

    def set_right_input(self, input):

        if input == input_closed:
            # Disable the input
            val = self.read_reg(_WM8960_POWER1)
            val &= ~(_WM8960_POWER1_AINR_MASK | _WM8960_POWER1_ADCR_MASK)
            self.write_reg(_WM8960_POWER1, val)

        elif input == input_mic1:
            # Only LMN1 enabled, LMICBOOST to 13db, LMIC2B enabled
            val = self.read_reg(_WM8960_POWER1)
            val |= _WM8960_POWER1_AINR_MASK | _WM8960_POWER1_ADCR_MASK | _WM8960_POWER1_MICB_MASK
            self.write_reg(_WM8960_POWER1, val)
            self.write_reg(_WM8960_RINPATH, 0x138)
            self.write_reg(_WM8960_RINVOL, 0x117)

        elif input == input_mic2:
            val = self.read_reg(_WM8960_POWER1)
            val |= _WM8960_POWER1_AINR_MASK | _WM8960_POWER1_ADCR_MASK | _WM8960_POWER1_MICB_MASK
            self.write_reg(_WM8960_POWER1, val)
            self.write_reg(_WM8960_RINPATH, 0x178)
            self.write_reg(_WM8960_RINVOL, 0x117)

        elif input == input_mic3:
            val = self.read_reg(_WM8960_POWER1)
            val |= _WM8960_POWER1_AINR_MASK | _WM8960_POWER1_ADCR_MASK | _WM8960_POWER1_MICB_MASK
            self.write_reg(_WM8960_POWER1, val)
            self.write_reg(_WM8960_RINPATH, 0x1B8)
            self.write_reg(_WM8960_RINVOL, 0x117)

        elif input == input_line2:
            val = self.read_reg(_WM8960_POWER1)
            val |= _WM8960_POWER1_AINR_MASK | _WM8960_POWER1_ADCR_MASK
            self.write_reg(_WM8960_POWER1, val)
            val = self.read_reg(_WM8960_INBMIX2)
            val |= 0xE
            self.write_reg(_WM8960_INBMIX2, val)

        elif input == input_line3:
            val = self.read_reg(_WM8960_POWER1)
            val |= _WM8960_POWER1_AINR_MASK | _WM8960_POWER1_ADCR_MASK
            self.write_reg(_WM8960_POWER1, val)
            val = self.read_reg(_WM8960_INBMIX2)
            val |= 0x70
            self.write_reg(_WM8960_INBMIX2, val)

        else:
            raise ValueError("Invalid input name")

    def set_protocol(self, protocol):
        self.modify_reg(
            _WM8960_IFACE1, _WM8960_IFACE1_FORMAT_MASK | _WM8960_IFACE1_LRP_MASK, protocol
        )

    def config_data_format(self, sysclk, sample_rate, bits):
        #  Compute sample rate divider, dac and adc are the same sample rate
        try:
            divider = self._dac_divider_table[sysclk // sample_rate]
            wl = self._audio_word_length_table[bits]
        except:
            raise ValueError("Invalid ratio sysclk/sample_rate or invalid bit length")

        self.modify_reg(_WM8960_CLOCK1, 0x1F8, divider << 6 | divider << 3)
        self.modify_reg(_WM8960_IFACE1, _WM8960_IFACE1_WL_MASK,wl << _WM8960_IFACE1_WL_SHIFT)

    def set_volume(self, module, volume, volume_r=None):

        if volume_r is None:
            volume_r = volume

        if module == module_ADC:
            if volume <= _WM8960_ADC_MAX_VOLUME:
                self.write_reg(_WM8960_LADC, volume)
                self.write_reg(_WM8960_RADC, volume_r)
                # Update volume
                volume |= 0x100
                self.write_reg(_WM8960_LADC, volume)
                self.write_reg(_WM8960_RADC, volume_r)

        elif module == module_DAC:
            if volume <= _WM8960_DAC_MAX_VOLUME:
                self.write_reg(_WM8960_LDAC, volume)
                self.write_reg(_WM8960_RDAC, volume_r)
                volume |= 0x100
                self.write_reg(_WM8960_LDAC, volume)
                self.write_reg(_WM8960_RDAC, volume_r)

        elif module == module_headphone:
            if volume <= _WM8960_HEADPHONE_MAX_VOLUME:
                self.write_reg(_WM8960_LOUT1, volume)
                self.write_reg(_WM8960_ROUT1, volume_r)
                volume |= 0x100
                self.write_reg(_WM8960_LOUT1, volume)
                self.write_reg(_WM8960_ROUT1, volume_r)

        elif module == module_line_in:
            if volume <= _WM8960_LINEIN_MAX_VOLUME:
                self.write_reg(_WM8960_LINVOL, volume)
                self.write_reg(_WM8960_RINVOL, volume_r)
                volume |= 0x100
                self.write_reg(_WM8960_LINVOL, volume)
                self.write_reg(_WM8960_RINVOL, volume_r)

        elif module == module_speaker:
            if volume <= _WM8960_SPEAKER_MAX_VOLUME:
                self.write_reg(_WM8960_LOUT2, volume)
                self.write_reg(_WM8960_ROUT2, volume_r)
                volume |= 0x100
                self.write_reg(_WM8960_LOUT2, volume)
                self.write_reg(_WM8960_ROUT2, volume_r)
        else:
            raise ValueError("Invalid module")

    def get_volume(self, module):

        if module == module_ADC:
            vol_l = self.read_reg(_WM8960_LADC)
            vol_r = self.read_reg(_WM8960_RADC)

        elif module == module_DAC:
            vol_l = self.read_reg(_WM8960_LDAC)
            vol_r = self.read_reg(_WM8960_RDAC)

        elif module == module_headphone:
            vol_l = self.read_reg(_WM8960_LOUT1)
            vol_r = self.read_reg(_WM8960_ROUT1)

        elif module == module_line_out:
            vol_l = self.read_reg(_WM8960_LINVOL)
            vol_r = self.read_reg(_WM8960_RINVOL)

        else:
            vol_l = vol_r = 0

        return (vol_l & 0xFF, vol_r & 0xFF)

    def volume(self, module, volume_l=None, volume_r=None):
        if volume_l is None:
            return self.get_volume(module)
        else:
            self.set_volume(module, volume_l, volume_r)

    def mute(self, enable, soft=True, ramp=mute_fast):
        enable = _WM8960_DACCTL1_DACMU_MASK if enable else 0
        soft = _WM8960_DACCTL2_DACSMM_MASK if soft else 0
        ramp = _WM8960_DACCTL2_DACMR_MASK if ramp == mute_slow else 0
        self.modify_reg(_WM8960_DACCTL1, _WM8960_DACCTL1_DACMU_MASK, enable)
        self.modify_reg(
            _WM8960_DACCTL2, _WM8960_DACCTL2_DACSMM_MASK | _WM8960_DACCTL2_DACMR_MASK, soft | ramp
        )

    def expand_3d(self, depth=0):
        if depth > 15:
            depth = 15
        cutoff = 0 if self.sample_rate >= 32000 else 0b1100000
        self.write_reg(_WM8960_3D, cutoff | depth << 1 | (1 if depth > 0 else 0))

    def mono(self, enable):
        enable = 1 if enable else 0
        self.modify_reg(
            _WM8960_DACCTL1, _WM8960_DACCTL1_MONOMIX_MASK, enable << _WM8960_DACCTL1_MONOMIX_SHIFT
        )

    # write a command and cache the result
    def write_reg(self, reg, value):

        self.reg[reg] = value
        self.value_buffer[0] = (reg << 1) | ((value >> 8) & 0x01)
        self.value_buffer[1] = value & 0xFF
        self.i2c.writeto(self.i2c_address, self.value_buffer)

    # read a value back from the register cache
    def read_reg(self, reg):

        if reg < _WM8960_CACHEREGNUM:
            return self.reg[reg]
        else:
            raise ValueError("Invalid register number %d" % reg)

    def modify_reg(self, reg, mask, val):

        reg_val = self.read_reg(reg)
        reg_val &= (~mask) & 0xFFFF
        reg_val |= val & mask
        self.write_reg(reg, reg_val)
