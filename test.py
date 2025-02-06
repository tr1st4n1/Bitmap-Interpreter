def binary_to_int(binary: int) -> int:
    binary = binary[::-1] # Reverse Binary String

    final: int = 0
    for i in range(len(binary)):
        final += 2**i * int(binary[i]) # Add current binary bit's value

    return final


def read_bitmap(bitmap: str) -> None: 
    for i in range(0, len(bitmap), COLOUR_DEPTH):
        bit = bitmap[i:i+COLOUR_DEPTH]
        print(bit, end='')



# Extract Binary from Bitmap File
with open("bitmap_test.txt", 'r') as bitmap_file:
    bitmap: str = bitmap_file.read()
    bitmap_file.close()

# Meta Data, Stored in the first set of bits
WIDTH: int = binary_to_int(bitmap[0:4])
HEIGHT: int = binary_to_int(bitmap[4:8])
COLOUR_DEPTH: int = binary_to_int(bitmap[8:12])
print(f"Height: {HEIGHT}\nWidth: {WIDTH}\nColour Depth: {COLOUR_DEPTH}")

# Remove Bitmap Meta Data
bitmap = bitmap[12:] if bitmap.find('\n') == -1 else bitmap[13:]

read_bitmap(bitmap)