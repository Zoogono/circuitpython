from intelhex import IntelHex
import crcmod
import ctypes
import sys

app_firmware = sys.argv[1]
out = sys.argv[2]

# Analyze app firmware
ih = IntelHex()
ih.loadhex(app_firmware)

# Get the binary data from IntelHex
binary_data = ih.tobinarray()

# Compute CRC16 for the binary data
crc16_func = crcmod.mkCrcFun(0x11021, rev=False, initCrc=0xFFFF)
crc16 = crc16_func(binary_data)


# Define the bootloader settings structure
# From: Adafruit_nRF52_Bootloader
# typedef struct
# {
#     uint16_t bank_0;          /**< Variable to store if bank 0 contains a valid application. */
#     uint16_t bank_0_crc;      /**< If bank is valid, this field will contain a valid CRC of the total image. */
#     uint16_t bank_1;          /**< Variable to store if bank 1 has been erased/prepared for new image. Bank 1 is only used in Banked Update scenario. */
#     uint32_t bank_0_size;     /**< Size of active image in bank0 if present, otherwise 0. */
#     uint32_t sd_image_size;   /**< Size of SoftDevice image in bank0 if bank_0 code is BANK_VALID_SD. */
#     uint32_t bl_image_size;   /**< Size of Bootloader image in bank0 if bank_0 code is BANK_VALID_SD. */
#     uint32_t app_image_size;  /**< Size of Application image in bank0 if bank_0 code is BANK_VALID_SD. */
#     uint32_t sd_image_start;  /**< Location in flash where SoftDevice image is stored for SoftDevice update. */
# } bootloader_settings_t;
class BootloaderSettings(ctypes.Structure):
    _fields_ = [
        ("bank_0", ctypes.c_uint16),  # is valid app
        ("bank_0_crc", ctypes.c_uint16),  # app crc
        ("bank_1", ctypes.c_uint16),
        ("bank_0_size", ctypes.c_int32),  # app size
        ("sd_image_size", ctypes.c_int32),
        ("bl_image_size", ctypes.c_int32),
        ("app_image_size", ctypes.c_int32),
        ("sd_image_start", ctypes.c_int32),
    ]


bootloader_settings = BootloaderSettings()
bootloader_settings.bank_0 = 0x01
bootloader_settings.bank_0_crc = crc16
bootloader_settings.bank_1 = 0xFF
bootloader_settings.bank_0_size = len(binary_data)

print("bank_0:", hex(bootloader_settings.bank_0))
print("bank_0_crc:", hex(bootloader_settings.bank_0_crc))
print("bank_1:", hex(bootloader_settings.bank_1))
print("bank_0_size:", hex(bootloader_settings.bank_0_size))

bootloader_data = ctypes.string_at(
    ctypes.byref(bootloader_settings), ctypes.sizeof(bootloader_settings)
)

# Create an IntelHex object for the bootloader settings
bootloader_hex = IntelHex()
bootloader_hex.puts(0x000FF000, bootloader_data)

# Write out the bootloader settings to a new hex file
bootloader_hex.write_hex_file(out)
