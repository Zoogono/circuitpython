USB_VID = 0x1915 # Nordic's VID
USB_PID = 0xBCDE # ABCD is the PID for when it's it bootloader mode. Not sure if we needed a different PID here.
USB_PRODUCT = "Zoog"
USB_MANUFACTURER = "Zoogono"

MCU_CHIP = nrf52840

QSPI_FLASH_FILESYSTEM = 1
EXTERNAL_FLASH_DEVICES = "GD25Q16E"

CIRCUITPY_DISPLAYIO = 0
CIRCUITPY_FRAMEBUFFERIO = 0
CIRCUITPY_FREQUENCYIO = 0
CIRCUITPY_KEYPAD = 0
CIRCUITPY_RGBMATRIX = 0
CIRCUITPY_SDCARDIO = 0
ZOOGONO = 1

FROZEN_MPY_DIRS += $(TOP)/frozen/Adafruit_CircuitPython_BLE
FROZEN_MPY_DIRS += $(TOP)/frozen/Adafruit_CircuitPython_hashlib
FROZEN_MPY_DIRS += $(TOP)/frozen/zoog-firmware
