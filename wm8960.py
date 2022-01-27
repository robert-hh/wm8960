#
# Driver class for the WM8960 Codec to be used e.g. with MIMXRT_1xxx Boards.
# Derived from the NXP SDK drivers.
#
# Copyright (c) 2015, Freescale Semiconductor, Inc., (C-Code)
# Copyright 2016-2021 NXP, (C-Code)
# Copyright (c) 2022, Robert Hammelrath, Python transformation
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause
#


# Define the register addresses of WM8960.
WM8960_LINVOL = const(0x0)
WM8960_RINVOL = const(0x1)
WM8960_LOUT1 = const(0x2)
WM8960_ROUT1 = const(0x3)
WM8960_CLOCK1 = const(0x4)
WM8960_DACCTL1 = const(0x5)
WM8960_DACCTL2 = const(0x6)
WM8960_IFACE1 = const(0x7)
WM8960_CLOCK2 = const(0x8)
WM8960_IFACE2 = const(0x9)
WM8960_LDAC = const(0xa)
WM8960_RDAC = const(0xb)
WM8960_RESET = const(0xf)
WM8960_3D = const(0x10)
WM8960_ALC1 = const(0x11)
WM8960_ALC2 = const(0x12)
WM8960_ALC3 = const(0x13)
WM8960_NOISEG = const(0x14)
WM8960_LADC = const(0x15)
WM8960_RADC = const(0x16)
WM8960_ADDCTL1 = const(0x17)
WM8960_ADDCTL2 = const(0x18)
WM8960_POWER1 = const(0x19)
WM8960_POWER2 = const(0x1a)
WM8960_ADDCTL3 = const(0x1b)
WM8960_APOP1 = const(0x1c)
WM8960_APOP2 = const(0x1d)
WM8960_LINPATH = const(0x20)
WM8960_RINPATH = const(0x21)
WM8960_LOUTMIX = const(0x22)
WM8960_ROUTMIX = const(0x25)
WM8960_MONOMIX1 = const(0x26)
WM8960_MONOMIX2 = const(0x27)
WM8960_LOUT2 = const(0x28)
WM8960_ROUT2 = const(0x29)
WM8960_MONO = const(0x2a)
WM8960_INBMIX1 = const(0x2b)
WM8960_INBMIX2 = const(0x2c)
WM8960_BYPASS1 = const(0x2d)
WM8960_BYPASS2 = const(0x2e)
WM8960_POWER3 = const(0x2f)
WM8960_ADDCTL4 = const(0x30)
WM8960_CLASSD1 = const(0x31)
WM8960_CLASSD3 = const(0x33)
WM8960_PLL1 = const(0x34)
WM8960_PLL2 = const(0x35)
WM8960_PLL3 = const(0x36)
WM8960_PLL4 = const(0x37)

# Cache register count
WM8960_CACHEREGNUM = const(56)

# WM8960 CLOCK2 bits
WM8960_CLOCK2_BCLK_DIV_MASK =const(0x0F)

# WM8960_IFACE1 FORMAT bits
WM8960_IFACE1_FORMAT_MASK  = const(0x03)
WM8960_IFACE1_FORMAT_SHIFT = const(0x00)
WM8960_IFACE1_FORMAT_RJ    = const(0x00)
WM8960_IFACE1_FORMAT_LJ    = const(0x01)
WM8960_IFACE1_FORMAT_I2S   = const(0x02)
WM8960_IFACE1_FORMAT_DSP   = const(0x03)

# WM8960_IFACE1 WL bits
WM8960_IFACE1_WL_MASK   = const(0x0C)
WM8960_IFACE1_WL_SHIFT  = const(0x02)
WM8960_IFACE1_WL_16BITS = const(0x00)
WM8960_IFACE1_WL_20BITS = const(0x01)
WM8960_IFACE1_WL_24BITS = const(0x02)
WM8960_IFACE1_WL_32BITS = const(0x03)

# WM8960_IFACE1 LRP bit
WM8960_IFACE1_LRP_MASK         = const(0x10)
WM8960_IFACE1_LRP_SHIFT        = const(0x04)
WM8960_IFACE1_LRCLK_NORMAL_POL = const(0x00)
WM8960_IFACE1_LRCLK_INVERT_POL = const(0x01)
WM8960_IFACE1_DSP_MODEA        = const(0x00)
WM8960_IFACE1_DSP_MODEB        = const(0x01)

# WM8960_IFACE1 DLRSWAP bit
WM8960_IFACE1_DLRSWAP_MASK  = const(0x20)
WM8960_IFACE1_DLRSWAP_SHIFT = const(0x05)
WM8960_IFACE1_DACCH_NORMAL  = const(0x00)
WM8960_IFACE1_DACCH_SWAP    = const(0x01)

# WM8960_IFACE1 MS bit
WM8960_IFACE1_MS_MASK  = const(0x40)
WM8960_IFACE1_MS_SHIFT = const(0x06)
WM8960_IFACE1_SLAVE    = const(0x00)
WM8960_IFACE1_MASTER   = const(0x01)

# WM8960_IFACE1 BCLKINV bit
WM8960_IFACE1_BCLKINV_MASK   = const(0x80)
WM8960_IFACE1_BCLKINV_SHIFT  = const(0x07)
WM8960_IFACE1_BCLK_NONINVERT = const(0x00)
WM8960_IFACE1_BCLK_INVERT    = const(0x01)

# WM8960_IFACE1 ALRSWAP bit
WM8960_IFACE1_ALRSWAP_MASK  = const(0x100)
WM8960_IFACE1_ALRSWAP_SHIFT = const(0x08)
WM8960_IFACE1_ADCCH_NORMAL  = const(0x00)
WM8960_IFACE1_ADCCH_SWAP    = const(0x01)

# WM8960_POWER1
WM8960_POWER1_VREF_MASK  = const(0x40)
WM8960_POWER1_VREF_SHIFT = const(0x06)

WM8960_POWER1_AINL_MASK  = const(0x20)
WM8960_POWER1_AINL_SHIFT = const(0x05)

WM8960_POWER1_AINR_MASK  = const(0x10)
WM8960_POWER1_AINR_SHIFT = const(0x04)

WM8960_POWER1_ADCL_MASK  = const(0x08)
WM8960_POWER1_ADCL_SHIFT = const(0x03)

WM8960_POWER1_ADCR_MASK  = const(0x0)
WM8960_POWER1_ADCR_SHIFT = const(0x02)

WM8960_POWER1_MICB_MASK  = const(0x02)
WM8960_POWER1_MICB_SHIFT = const(0x01)

WM8960_POWER1_DIGENB_MASK  = const(0x01)
WM8960_POWER1_DIGENB_SHIFT = const(0x00)

# WM8960_POWER2
WM8960_POWER2_DACL_MASK  = const(0x100)
WM8960_POWER2_DACL_SHIFT = const(0x08)

WM8960_POWER2_DACR_MASK  = const(0x80)
WM8960_POWER2_DACR_SHIFT = const(0x07)

WM8960_POWER2_LOUT1_MASK  = const(0x40)
WM8960_POWER2_LOUT1_SHIFT = const(0x06)

WM8960_POWER2_ROUT1_MASK  = const(0x20)
WM8960_POWER2_ROUT1_SHIFT = const(0x05)

WM8960_POWER2_SPKL_MASK  = const(0x10)
WM8960_POWER2_SPKL_SHIFT = const(0x04)

WM8960_POWER2_SPKR_MASK  = const(0x08)
WM8960_POWER2_SPKR_SHIFT = const(0x03)

WM8960_POWER3_LMIC_MASK   = const(0x20)
WM8960_POWER3_LMIC_SHIFT  = const(0x05)
WM8960_POWER3_RMIC_MASK   = const(0x10)
WM8960_POWER3_RMIC_SHIFT  = const(0x04)
WM8960_POWER3_LOMIX_MASK  = const(0x08)
WM8960_POWER3_LOMIX_SHIFT = const(0x03)
WM8960_POWER3_ROMIX_MASK  = const(0x04)
WM8960_POWER3_ROMIX_SHIFT = const(0x02)

WM8960_I2C_ADDR = const(0x1a)

WM8960_I2C_BAUDRATE = const(100000)

# WM8960 maximum volume values
WM8960_ADC_MAX_VOLUME_VALUE = const(0xFF)
WM8960_DAC_MAX_VOLUME_VALUE = const(0xFF)
WM8960_HEADPHONE_MAX_VOLUME_VALUE = const(0x7F)
WM8960_HEADPHONE_MIN_VOLUME_VALUE = const(0x30)
WM8960_LINEIN_MAX_VOLUME_VALUE = const(0x3F)
WM8960_SPEAKER_MAX_VOLUME_VALUE = const(0x7F)
WM8960_SPEAKER_MIN_VOLUME_VALUE = const(0x30)

# Config symbol names
# Modules
kWM8960_ModuleADC = const(0)  # ADC module in WM8960
kWM8960_ModuleDAC = const(1)  # DAC module in WM8960
kWM8960_ModuleVREF = const(2)  # VREF module
kWM8960_ModuleHP = const(3)  # Headphone
kWM8960_ModuleMICB = const(4)  # Mic bias
kWM8960_ModuleMIC = const(5)  # Input Mic
kWM8960_ModuleLineIn = const(6)  # Analog in PGA
kWM8960_ModuleLineOut = const(7)  # Line out module
kWM8960_ModuleSpeaker = const(8)  # Speaker module
kWM8960_ModuleOMIX = const(9)  # Output mixer

# Route
kWM8960_RouteBypass = const(0)  # LINEIN->Headphone.
kWM8960_RoutePlayback = const(1)  #  I2SIN->DAC->Headphone.
kWM8960_RoutePlaybackandRecord = const(2)  # I2SIN->DAC->Headphone, LINEIN->ADC->I2SOUT.
kWM8960_RouteRecord = const(5)  # LINEIN->ADC->I2SOUT.

# Input
kWM8960_InputClosed = const(0)  # Input device is closed
kWM8960_InputSingleEndedMic = const(1)  # Input as single ended mic, only use L/RINPUT1
kWM8960_InputDifferentialMicInput2 = const(2)  # Input as differential mic, use L/RINPUT1 and L/RINPUT2
kWM8960_InputDifferentialMicInput3 = const(3)  # Input as differential mic, use L/RINPUT1 and L/RINPUT3
kWM8960_InputLineINPUT2 = const(4)  # Input as line input, only use L/RINPUT2
kWM8960_InputLineINPUT3 = const(5)  # Input as line input, only use L/RINPUT3

# Play source
kWM8960_PlaySourcePGA = const(1)  # wm8960 play source PGA
kWM8960_PlaySourceInput = const(2)  # wm8960 play source Input
kWM8960_PlaySourceDAC = const(4)  # wm8960 play source DAC

# Play Channel
kWM8960_HeadphoneLeft = const(1)  # wm8960 headphone left channel
kWM8960_HeadphoneRight = const(2)  # wm8960 headphone right channel
kWM8960_SpeakerLeft = const(4)  # wm8960 speaker left channel
kWM8960_SpeakerRight = const(8)  # wm8960 speaker right channel

#  Protocol type
kWM8960_BusI2S = const(2)  # I2S type
kWM8960_BusLeftJustified = const(1)  # Left justified mode
kWM8960_BusRightJustified = const(0)  # Right justified mode
kWM8960_BusPCMA = const(3)  # PCM A mode
kWM8960_BusPCMB = const(3 | (1 << 4)) # PCM B mode

# Sample Rate
kWM8960_AudioSampleRate8KHz = const(8000)  # Sample rate 8000 Hz
kWM8960_AudioSampleRate11025Hz = const(11025)  # Sample rate 11025 Hz
kWM8960_AudioSampleRate12KHz = const(12000)  # Sample rate 12000 Hz
kWM8960_AudioSampleRate16KHz = const(16000)  # Sample rate 16000 Hz
kWM8960_AudioSampleRate22050Hz = const(22050)  # Sample rate 22050 Hz
kWM8960_AudioSampleRate24KHz = const(24000)  # Sample rate 24000 Hz
kWM8960_AudioSampleRate32KHz = const(32000)  # Sample rate 32000 Hz
kWM8960_AudioSampleRate44100Hz = const(44100)  # Sample rate 44100 Hz
kWM8960_AudioSampleRate48KHz = const(48000)  # Sample rate 48000 Hz
kWM8960_AudioSampleRate96KHz = const(96000)  # Sample rate 96000 Hz
kWM8960_AudioSampleRate192KHz = const(192000)  # Sample rate 192000 Hz
kWM8960_AudioSampleRate384KHz = const(384000)  # Sample rate 384000 Hz

# Bit Width
kWM8960_AudioBitWidth16bit = const(16)  # audio bit width 16
kWM8960_AudioBitWidth20bit = const(20)  # audio bit width 20
kWM8960_AudioBitWidth24bit = const(24)  # audio bit width 24
kWM8960_AudioBitWidth32bit = const(32)  # audio bit width 32

# Clock Source
kWM8960_SysClkSourceMclk = const(0)  # sysclk source from external MCLK
kWM8960_SysClkSourceInternalPLL = const(1)  # sysclk source from internal PLL

_bitClockDividerDict = {
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

# Just a simple class that populates the config data type.
class WM8960_Config:

    def __init__(self,
                 route = kWM8960_RoutePlaybackandRecord,
                 bus = kWM8960_BusI2S,
                 formatMclkHz = 12000000,
                 formatSampleRate = kWM8960_AudioSampleRate16KHz,
                 formatBitWidth = kWM8960_AudioBitWidth16bit,
                 master_slave = True,
                 enableSpeaker = False,
                 leftInputSource = kWM8960_InputDifferentialMicInput3,
                 rightInputSource = kWM8960_InputDifferentialMicInput2,
                 playSource = kWM8960_PlaySourceDAC,
                 masterClockSource = kWM8960_SysClkSourceInternalPLL,
                 masterClockFreq = 12288000,
                ):

        self.route = route  # Audio data route.
        self.bus = bus  # Audio transfer protocol
        self.formatMclkHz = formatMclkHz  # Audio format
        self.formatSampleRate = formatSampleRate  # Audio format
        self.formatBitWidth = formatBitWidth  # Audio format
        self.master_slave = master_slave  # Master or slave.
        self.enableSpeaker = enableSpeaker  # True means enable class D speaker as output, False means no
        self.leftInputSource = leftInputSource  # Left input source for WM8960
        self.rightInputSource = rightInputSource  # Right input source for wm8960
        self.playSource = playSource  # play source
        self.masterClockSource = masterClockSource  # master clock configurations
        self.masterClockFreq = masterClockFreq  # master clock configurations


class WM8960:

    wm8960_reg = [
        0x0097, 0x0097, 0x0000, 0x0000, 0x0000, 0x0008, 0x0000,
        0x000a, 0x01c0, 0x0000, 0x00ff, 0x00ff, 0x0000, 0x0000,
        0x0000, 0x0000, 0x0000, 0x007b, 0x0100, 0x0032, 0x0000,
        0x00c3, 0x00c3, 0x01c0, 0x0000, 0x0000, 0x0000, 0x0000,
        0x0000, 0x0000, 0x0000, 0x0000, 0x0100, 0x0100, 0x0050,
        0x0050, 0x0050, 0x0050, 0x0000, 0x0000, 0x0000, 0x0000,
        0x0040, 0x0000, 0x0000, 0x0050, 0x0050, 0x0000, 0x0002,
        0x0037, 0x004d, 0x0080, 0x0008, 0x0031, 0x0026, 0x00e9
    ]

    def __init__(self, config, i2c, i2c_address = WM8960_I2C_ADDR):
        self.i2c = i2c
        self.i2c_address = i2c_address
        self.value_buffer = bytearray(1)

        sysclk = config.formatMclkHz

        # Reset the codec
        self.WM8960_WriteReg(WM8960_RESET, 0x00)
        #
        # VMID=50K, Enable VREF, AINL, AINR, ADCL and ADCR
        # I2S_IN (bit 0), I2S_OUT (bit 1), DAP (bit 4), DAC (bit 5), ADC (bit 6) are powered on

        self.WM8960_WriteReg(WM8960_POWER1, 0xFE)
        #
        # Enable DACL, DACR, LOUT1, ROUT1, PLL down, SPKL, SPKR
        self.WM8960_WriteReg(WM8960_POWER2, 0x1F8)
        #
        # Enable left and right channel input PGA, left and right output mixer
        self.WM8960_WriteReg(WM8960_POWER3, 0x3C)
        # ADC and DAC uses same clock
        self.WM8960_WriteReg(WM8960_IFACE2, 0x40)
        # set data route
        self.WM8960_SetDataRoute(config.route)
        # set data protocol
        self.WM8960_SetProtocol(config.bus)

        if config.masterClockSource == kWM8960_SysClkSourceInternalPLL:
            self.WM8960_SetInternalPllConfig(config.formatMclkHz, config.masterClockFreq,
                config.formatSampleRate, config.formatBitWidth)
            sysclk = config.masterClockFreq

        # set master or slave
        if config.master_slave:
            self.WM8960_SetMasterClock(sysclk, config.formatSampleRate, config.formatBitWidth)

        self.WM8960_SetMasterSlave(config.master_slave)
        # select left input
        self.WM8960_SetLeftInput(config.leftInputSource)
        # select right input
        self.WM8960_SetRightInput(config.rightInputSource)
        # speaker power
        if config.enableSpeaker:
            self.WM8960_SetModule(kWM8960_ModuleSpeaker, True)

        self.WM8960_WriteReg(WM8960_ADDCTL1, 0x0C0)
        self.WM8960_WriteReg(WM8960_ADDCTL4, 0x40)

        self.WM8960_WriteReg(WM8960_BYPASS1, 0x0)
        self.WM8960_WriteReg(WM8960_BYPASS2, 0x0)
        #
        # ADC volume, 0dB
        self.WM8960_WriteReg(WM8960_LADC, 0x1C3)
        self.WM8960_WriteReg(WM8960_RADC, 0x1C3)
        #
        # Digital DAC volume, 0dB
        self.WM8960_WriteReg(WM8960_LDAC, 0x1E0)
        self.WM8960_WriteReg(WM8960_RDAC, 0x1E0)
        #
        # Headphone volume, LOUT1 and ROUT1, 0dB
        self.WM8960_WriteReg(WM8960_LOUT1, 0x16F)
        self.WM8960_WriteReg(WM8960_ROUT1, 0x16F)
        #
        # speaker volume 6dB
        self.WM8960_WriteReg(WM8960_LOUT2, 0x1ff)
        self.WM8960_WriteReg(WM8960_ROUT2, 0x1ff)
        #
        # enable class D output
        self.WM8960_WriteReg(WM8960_CLASSD1, 0xf7)
        #
        # Unmute DAC.
        self.WM8960_WriteReg(WM8960_DACCTL1, 0x0000)
        self.WM8960_WriteReg(WM8960_LINVOL, 0x117)
        self.WM8960_WriteReg(WM8960_RINVOL, 0x117)

        self.WM8960_ConfigDataFormat(sysclk, config.formatSampleRate, config.formatBitWidth)


    def deinit(self):

        self.WM8960_SetModule(kWM8960_ModuleADC, False)
        self.WM8960_SetModule(kWM8960_ModuleDAC, False)
        self.WM8960_SetModule(kWM8960_ModuleVREF, False)
        self.WM8960_SetModule(kWM8960_ModuleLineIn, False)
        self.WM8960_SetModule(kWM8960_ModuleLineOut, False)
        self.WM8960_SetModule(kWM8960_ModuleSpeaker, False)


    def WM8960_SetInternalPllConfig(self, inputMclk, outputClk, sampleRate, bitWidth):
        pllF2 = outputClk * 4
        pllPrescale = 0
        sysclkDiv = 1
        pllR = 0
        pllN = 0
        pllK = 0
        fracMode = 0

        # disable PLL power
        self.WM8960_ModifyReg(WM8960_POWER2, 1, 0)
        self.WM8960_ModifyReg(WM8960_CLOCK1, 7, 0)

        pllN = pllF2 // inputMclk
        if pllN < WM8960_PLL_N_MIN_VALUE:
            inputMclk >>= 1
            pllPrescale = 1
            pllN = pllF2 // inputMclk
            if pllN < WM8960_PLL_N_MIN_VALUE:
                sysclkDiv = 2
                pllN = pllF2 // inputMclk * sysclkDiv

        if (pllN < WM8960_PLL_N_MIN_VALUE) or (pllN > WM8960_PLL_N_MAX_VALUE):
            raise ValueError('Invalid Argument')

        pllR = pllF2 // (inputMclk // 1000) * sysclkDiv
        pllK = ((1 << 24) * (pllR - pllN * 1000)) // 1000
        if pllK != 0:
            fracMode = 1

        self.WM8960_WriteReg(WM8960_PLL1,
                        (fracMode << 5) | (pllPrescale << 4) | (pllN & 0x0F))
        self.WM8960_WriteReg(WM8960_PLL2, (pllK >> 16) & 0xFF)
        self.WM8960_WriteReg(WM8960_PLL3, (pllK >> 8) & 0xFF)
        self.WM8960_WriteReg(WM8960_PLL4, pllK & 0xFF)
        # enable PLL power
        self.WM8960_ModifyReg(WM8960_POWER2, 1, 1)
        self.WM8960_ModifyReg(WM8960_CLOCK1, 7, ((0 if sysclkDiv == 1 else sysclkDiv) << 1) | 1)


    def WM8960_SetMasterClock(self, sysclk, sampleRate, bitWidth):
        bitClockDivider = (sysclk * 2) // (sampleRate * bitWidth * 2)
        regDivider = _bitClockDividerDict[bitClockDivider]
        # configure the master bit clock divider will be better
        self.WM8960_ModifyReg(WM8960_CLOCK2, WM8960_CLOCK2_BCLK_DIV_MASK, regDivider)


    def WM8960_SetMasterSlave(self, master):
        if master:
            self.WM8960_ModifyReg(WM8960_IFACE1, WM8960_IFACE1_MS_MASK,
                ((WM8960_IFACE1_MASTER << WM8960_IFACE1_MS_SHIFT) & WM8960_IFACE1_MS_MASK))

        else:
            self.WM8960_ModifyReg(WM8960_IFACE1, WM8960_IFACE1_MS_MASK,
                ((WM8960_IFACE1_SLAVE << WM8960_IFACE1_MS_SHIFT) & WM8960_IFACE1_MS_MASK))


    def WM8960_SetModule(self, module, isEnabled):

            if module == kWM8960_ModuleADC:

                self.WM8960_ModifyReg(WM8960_POWER1, WM8960_POWER1_ADCL_MASK,
                    (isEnabled << WM8960_POWER1_ADCL_SHIFT))
                self.WM8960_ModifyReg(WM8960_POWER1, WM8960_POWER1_ADCR_MASK,
                    (isEnabled << WM8960_POWER1_ADCR_SHIFT))

            elif module ==  kWM8960_ModuleDAC:

                self.WM8960_ModifyReg(WM8960_POWER2, WM8960_POWER2_DACL_MASK,
                    (isEnabled << WM8960_POWER2_DACL_SHIFT))
                self.WM8960_ModifyReg(WM8960_POWER2, WM8960_POWER2_DACR_MASK,
                    (isEnabled << WM8960_POWER2_DACR_SHIFT))

            elif module ==  kWM8960_ModuleVREF:

                self.WM8960_ModifyReg(WM8960_POWER1, WM8960_POWER1_VREF_MASK,
                    (isEnabled << WM8960_POWER1_VREF_SHIFT))

            elif module ==  kWM8960_ModuleLineIn:

                self.WM8960_ModifyReg(WM8960_POWER1, WM8960_POWER1_AINL_MASK,
                    (isEnabled << WM8960_POWER1_AINL_SHIFT))
                self.WM8960_ModifyReg(WM8960_POWER1, WM8960_POWER1_AINR_MASK,
                    (isEnabled << WM8960_POWER1_AINR_SHIFT))
                self.WM8960_ModifyReg(WM8960_POWER3, WM8960_POWER3_LMIC_MASK,
                    (isEnabled << WM8960_POWER3_LMIC_SHIFT))
                self.WM8960_ModifyReg(WM8960_POWER3, WM8960_POWER3_RMIC_MASK,
                    (isEnabled << WM8960_POWER3_RMIC_SHIFT))

            elif module ==  kWM8960_ModuleLineOut:

                self.WM8960_ModifyReg(WM8960_POWER2, WM8960_POWER2_LOUT1_MASK,
                    (isEnabled << WM8960_POWER2_LOUT1_SHIFT))
                self.WM8960_ModifyReg(WM8960_POWER2, WM8960_POWER2_ROUT1_MASK,
                    (isEnabled << WM8960_POWER2_ROUT1_SHIFT))

            elif module ==  kWM8960_ModuleMICB:

                self.WM8960_ModifyReg(WM8960_POWER1, WM8960_POWER1_MICB_MASK,
                    (isEnabled << WM8960_POWER1_MICB_SHIFT))

            elif module ==  kWM8960_ModuleSpeaker:

                self.WM8960_ModifyReg(WM8960_POWER2, WM8960_POWER2_SPKL_MASK,
                    (isEnabled << WM8960_POWER2_SPKL_SHIFT))
                self.WM8960_ModifyReg(WM8960_POWER2, WM8960_POWER2_SPKR_MASK,
                    (isEnabled << WM8960_POWER2_SPKR_SHIFT))
                self.WM8960_WriteReg(WM8960_CLASSD1, 0xF7)

            elif module ==  kWM8960_ModuleOMIX:

                self.WM8960_ModifyReg(WM8960_POWER3, WM8960_POWER3_LOMIX_MASK,
                    (isEnabled << WM8960_POWER3_LOMIX_SHIFT))
                self.WM8960_ModifyReg(WM8960_POWER3, WM8960_POWER3_ROMIX_MASK,
                    (isEnabled << WM8960_POWER3_ROMIX_SHIFT))
            else:
                raise ValueError('Invalid Argument')


    def WM8960_SetDataRoute(self, route):
        if route ==  kWM8960_RouteBypass:
            # Bypass means from line-in to HP
            # Left LINPUT3 to left output mixer, LINPUT3 left output mixer volume = 0dB
            self.WM8960_WriteReg(WM8960_LOUTMIX, 0x80)
            # Right RINPUT3 to right output mixer, RINPUT3 right output mixer volume = 0dB
            self.WM8960_WriteReg(WM8960_ROUTMIX, 0x80)

        elif route ==  kWM8960_RoutePlayback:
            # Data route I2S_IN-> DAC-> HP
            #
            # Left DAC to left output mixer, LINPUT3 left output mixer volume = 0dB
            self.WM8960_WriteReg(WM8960_LOUTMIX, 0x100)
            # Right DAC to right output mixer, RINPUT3 right output mixer volume = 0dB
            self.WM8960_WriteReg(WM8960_ROUTMIX, 0x100)
            self.WM8960_WriteReg(WM8960_POWER3, 0x0C)
            # Set power for DAC
            self.WM8960_SetModule(kWM8960_ModuleDAC, True)
            self.WM8960_SetModule(kWM8960_ModuleOMIX, True)
            self.WM8960_SetModule(kWM8960_ModuleLineOut, True)

        elif route ==  kWM8960_RoutePlaybackandRecord:
            #
            # Left DAC to left output mixer, LINPUT3 left output mixer volume = 0dB
            self.WM8960_WriteReg(WM8960_LOUTMIX, 0x100)
            # Right DAC to right output mixer, RINPUT3 right output mixer volume = 0dB
            self.WM8960_WriteReg(WM8960_ROUTMIX, 0x100)
            self.WM8960_WriteReg(WM8960_POWER3, 0x3C)
            self.WM8960_SetModule(kWM8960_ModuleDAC, True)
            self.WM8960_SetModule(kWM8960_ModuleADC, True)
            self.WM8960_SetModule(kWM8960_ModuleLineIn, True)
            self.WM8960_SetModule(kWM8960_ModuleOMIX, True)
            self.WM8960_SetModule(kWM8960_ModuleLineOut, True)

        elif route ==  kWM8960_RouteRecord:
            # LINE_IN->ADC->I2S_OUT
            # Left and right input boost, LIN3BOOST and RIN3BOOST = 0dB
            self.WM8960_WriteReg(WM8960_POWER3, 0x30)
            # Power up ADC and AIN
            self.WM8960_SetModule(kWM8960_ModuleLineIn, True)
            self.WM8960_SetModule(kWM8960_ModuleADC, True)

        else:
            raise ValueError('Invalid Argument')


    def WM8960_SetLeftInput(self, input):

        if input ==  kWM8960_InputClosed:
            val = self.WM8960_ReadReg(WM8960_POWER1)
            val &= ~(WM8960_POWER1_AINL_MASK | WM8960_POWER1_ADCL_MASK)
            self.WM8960_WriteReg(WM8960_POWER1, val)

        elif input ==  kWM8960_InputSingleEndedMic:
            # Only LMN1 enabled, LMICBOOST to 13db, LMIC2B enabled
            val = self.WM8960_ReadReg(WM8960_POWER1)
            val |= (WM8960_POWER1_AINL_MASK | WM8960_POWER1_ADCL_MASK | WM8960_POWER1_MICB_MASK)
            self.WM8960_WriteReg(WM8960_POWER1, val)
            self.WM8960_WriteReg(WM8960_LINPATH, 0x138)
            self.WM8960_WriteReg(WM8960_LINVOL, 0x117)

        elif input ==  kWM8960_InputDifferentialMicInput2:
            val = self.WM8960_ReadReg(WM8960_POWER1)
            val |= (WM8960_POWER1_AINL_MASK | WM8960_POWER1_ADCL_MASK | WM8960_POWER1_MICB_MASK)
            self.WM8960_WriteReg(WM8960_POWER1, val)
            self.WM8960_WriteReg(WM8960_LINPATH, 0x178)
            self.WM8960_WriteReg(WM8960_LINVOL, 0x117)

        elif input ==  kWM8960_InputDifferentialMicInput3:
            val = self.WM8960_ReadReg(WM8960_POWER1)
            val |= (WM8960_POWER1_AINL_MASK | WM8960_POWER1_ADCL_MASK | WM8960_POWER1_MICB_MASK)
            self.WM8960_WriteReg(WM8960_POWER1, val)
            self.WM8960_WriteReg(WM8960_LINPATH, 0x1B8)
            self.WM8960_WriteReg(WM8960_LINVOL, 0x117)

        elif input ==  kWM8960_InputLineINPUT2:
            val = self.WM8960_ReadReg(WM8960_POWER1)
            val |= (WM8960_POWER1_AINL_MASK | WM8960_POWER1_ADCL_MASK)
            self.WM8960_WriteReg(WM8960_POWER1, val)
            val = self.WM8960_ReadReg(WM8960_INBMIX1)
            val |= 0xE
            self.WM8960_WriteReg(WM8960_INBMIX1, val)

        elif input ==  kWM8960_InputLineINPUT3:
            val = self.WM8960_ReadReg(WM8960_POWER1)
            val |= (WM8960_POWER1_AINL_MASK | WM8960_POWER1_ADCL_MASK)
            self.WM8960_WriteReg(WM8960_POWER1, val)
            val = self.WM8960_ReadReg(WM8960_INBMIX1)
            val |= 0x70
            self.WM8960_WriteReg(WM8960_INBMIX1, val)

        else:
            raise ValueError('Invalid Argument')


    def WM8960_SetRightInput(self, input):

        if input ==  kWM8960_InputClosed:
            val = self.WM8960_ReadReg(WM8960_POWER1)
            val &= ~(WM8960_POWER1_AINR_MASK | WM8960_POWER1_ADCR_MASK)
            self.WM8960_WriteReg(WM8960_POWER1, val)

        elif input ==  kWM8960_InputSingleEndedMic:
            # Only LMN1 enabled, LMICBOOST to 13db, LMIC2B enabled
            val = self.WM8960_ReadReg(WM8960_POWER1)
            val |= (WM8960_POWER1_AINR_MASK | WM8960_POWER1_ADCR_MASK | WM8960_POWER1_MICB_MASK)
            self.WM8960_WriteReg(WM8960_POWER1, val)
            self.WM8960_WriteReg(WM8960_RINPATH, 0x138)
            self.WM8960_WriteReg(WM8960_RINVOL, 0x117)

        elif input ==  kWM8960_InputDifferentialMicInput2:
            val = self.WM8960_ReadReg(WM8960_POWER1)
            val |= (WM8960_POWER1_AINR_MASK | WM8960_POWER1_ADCR_MASK | WM8960_POWER1_MICB_MASK)
            self.WM8960_WriteReg(WM8960_POWER1, val)
            self.WM8960_WriteReg(WM8960_RINPATH, 0x178)
            self.WM8960_WriteReg(WM8960_RINVOL, 0x117)

        elif input ==  kWM8960_InputDifferentialMicInput3:
            val = self.WM8960_ReadReg(WM8960_POWER1)
            val |= (WM8960_POWER1_AINR_MASK | WM8960_POWER1_ADCR_MASK | WM8960_POWER1_MICB_MASK)
            self.WM8960_WriteReg(WM8960_POWER1, val)
            self.WM8960_WriteReg(WM8960_RINPATH, 0x1B8)
            self.WM8960_WriteReg(WM8960_RINVOL, 0x117)

        elif input ==  kWM8960_InputLineINPUT2:
            val = self.WM8960_ReadReg(WM8960_POWER1)
            val |= (WM8960_POWER1_AINR_MASK | WM8960_POWER1_ADCR_MASK)
            self.WM8960_WriteReg(WM8960_POWER1, val)
            val = self.WM8960_ReadReg(WM8960_INBMIX2)
            val |= 0xE
            self.WM8960_WriteReg(WM8960_INBMIX2, val)

        elif input ==  kWM8960_InputLineINPUT3:
            val = self.WM8960_ReadReg(WM8960_POWER1)
            val |= (WM8960_POWER1_AINR_MASK | WM8960_POWER1_ADCR_MASK)
            self.WM8960_WriteReg(WM8960_POWER1, val)
            val = self.WM8960_ReadReg(WM8960_INBMIX2)
            val |= 0x70
            self.WM8960_WriteReg(WM8960_INBMIX2, val)

        else:
            raise ValueError('Invalid Argument')


    def WM8960_SetProtocol(self, protocol):
        self.WM8960_ModifyReg(WM8960_IFACE1, WM8960_IFACE1_FORMAT_MASK | WM8960_IFACE1_LRP_MASK,
            protocol)


    def WM8960_ConfigDataFormat(self, sysclk, sample_rate, bits):

        #  Compute sample rate divider, dac and adc are the same sample rate
        divider = sysclk // sample_rate
        if divider == 256:
            val = 0
        elif divider > 256:
            val = (uint16_t)(((divider // 256) << 6) | ((divider // 256) << 3))
        else:
            raise ValueError('Invalid Argument')

        self.WM8960_ModifyReg(WM8960_CLOCK1, 0x1F8, val)

        # Slave mode (MS = 0), LRP = 0, 32bit WL, left justified (FORMAT[1:0]=0b01)
        if bits == 16:
            self.WM8960_ModifyReg(WM8960_IFACE1, WM8960_IFACE1_WL_MASK,
                (((WM8960_IFACE1_WL_16BITS) << WM8960_IFACE1_WL_SHIFT) & WM8960_IFACE1_WL_MASK))

        elif bits ==  20:
            self.WM8960_ModifyReg(WM8960_IFACE1, WM8960_IFACE1_WL_MASK,
                (((WM8960_IFACE1_WL_20BITS) << WM8960_IFACE1_WL_SHIFT) & WM8960_IFACE1_WL_MASK))

        elif bits ==  24:
            self.WM8960_ModifyReg(WM8960_IFACE1, WM8960_IFACE1_WL_MASK,
                (((WM8960_IFACE1_WL_24BITS) << WM8960_IFACE1_WL_SHIFT) & WM8960_IFACE1_WL_MASK))

        elif bits ==  32:
            self.WM8960_ModifyReg(WM8960_IFACE1, WM8960_IFACE1_WL_MASK,
                (((WM8960_IFACE1_WL_24BITS) << WM8960_IFACE1_WL_SHIFT) & WM8960_IFACE1_WL_MASK))

        else:
            raise ValueError('Invalid Argument')


    # write a command and cache the result
    def WM8960_WriteReg(self, reg, value):

        self.value_buffer[0] = value & 0xff
        self.wm8960_reg[reg] = value
        reg = (reg << 1) | ((value >> 8) & 0x01)
        self.i2c.writeto_mem(self.i2c_address, reg, self.value_buffer)

    # read a value back from the register cache
    def WM8960_ReadReg(self, reg):

        if reg < WM8960_CACHEREGNUM:
            return self.wm8960_reg[reg]
        else:
            raise ValueError('Invalid register number %d' % reg)


    def WM8960_ModifyReg(reg, mask, val):

        reg_val = self.WM8960_ReadReg(reg)
        reg_val &= (~mask) & 0xffff
        reg_val |= val
        self.WM8960_WriteReg(reg, reg_val)
