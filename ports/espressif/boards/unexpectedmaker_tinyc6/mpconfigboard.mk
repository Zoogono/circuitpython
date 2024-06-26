CIRCUITPY_CREATOR_ID = 0xB0B00000
CIRCUITPY_CREATION_ID = 0x00C60001

IDF_TARGET = esp32c6

CIRCUITPY_ESP_FLASH_MODE = qio
CIRCUITPY_ESP_FLASH_FREQ = 80m
CIRCUITPY_ESP_FLASH_SIZE = 8MB

# Include these Python libraries in firmware.
FROZEN_MPY_DIRS += $(TOP)/frozen/Adafruit_CircuitPython_NeoPixel
