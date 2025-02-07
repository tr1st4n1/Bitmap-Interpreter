# FUNCTIONS
def binary_to_int(binary: int) -> int:
    binary = binary[::-1]
    final: int = 0

    for i in range(len(binary)):
        final += 2**i * int(binary[i])

    return final


def read_bitmap(bitmap: str) -> None:
    pixels_outputted: int = 0
    for i in range(0, len(bitmap), COLOUR_DEPTH):
        pixel_data = bitmap[i:i+COLOUR_DEPTH]

        print(COLOURS[pixel_data], end='')
        pixels_outputted += 1

        # Check If End Of Row
        if pixels_outputted % WIDTH == 0:
            print()


# ---------------------------------------------------------------------------------

# FILE
with open("bitmap_test.txt", 'r') as bitmap_file:
    bitmap: str = bitmap_file.read()
    bitmap_file.close()

# META DATA (stored in the first set of bits)
WIDTH: int = binary_to_int(bitmap[0:4])
HEIGHT: int = binary_to_int(bitmap[4:8])
COLOUR_DEPTH: int = 2
COLOURS: dict = {'11':'@', '00':'*', '10':'~', '01':'^'}
print(f"Height: {HEIGHT}\nWidth: {WIDTH}")

# REMOVE META DATA
bitmap = bitmap[8:] if bitmap.find('\n') == -1 else bitmap[9:]

read_bitmap(bitmap)