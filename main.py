# Functions
def binary_to_int(binary: str) -> int:
    binary = binary[::-1]
    final: int = 0

    for i in range(len(binary)):
        final += 2**i * int(binary[i])

    return final


def find_rgb(binary: str) -> int:
    binary_coefficient: int = int(255/(2**len(binary)-1))
    return binary_to_int(binary)*binary_coefficient


def read_bitmap(bitmap: str, _COLOUR_DEPTH) -> None:
    pixels_outputted: int = 0
    for i in range(0, len(bitmap), _COLOUR_DEPTH):
        pixel_data = bitmap[i:i+_COLOUR_DEPTH]

        print(  find_rgb(pixel_data[:int(_COLOUR_DEPTH/3)]),
                find_rgb(pixel_data[int(_COLOUR_DEPTH/3):int(_COLOUR_DEPTH/3*2)]),
                find_rgb(pixel_data[int(_COLOUR_DEPTH/3*2):int(_COLOUR_DEPTH)]),
                end=' | ')
        pixels_outputted += 1

        # Check If End Of Row
        if pixels_outputted % WIDTH == 0:
            print()



# ---------------------------------------------------------------------------------

with open("bitmap_test.txt", 'r') as bitmap_file:
    bitmap: str = bitmap_file.read().replace(' ', '').replace('\n', '')
    bitmap_file.close()

WIDTH: int = binary_to_int(bitmap[0:4])
HEIGHT: int = binary_to_int(bitmap[4:8])
COLOUR_DEPTH: int = binary_to_int(bitmap[8:12])
print(f"Height: {HEIGHT} | Width: {WIDTH} | Colour Depth: {COLOUR_DEPTH}")

# Remove Meta Data
bitmap = bitmap[12:]

read_bitmap(bitmap, COLOUR_DEPTH)