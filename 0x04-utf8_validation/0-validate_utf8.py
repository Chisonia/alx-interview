#!/usr/bin/python3
"""UTF-8 Validation module"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Parameters:
    data (list): A list of integers representing bytes.

    Returns:
    bool: True if data is a valid UTF-8 encoding, False otherwise.
    """
    num_bytes = 0

    for byte in data:
        # Get the last 8 bits of the byte
        byte &= 0xFF

        if num_bytes == 0:
            # Determine the number of bytes for this character
            if (byte >> 7) == 0b0:  # 1-byte character
                continue
            elif (byte >> 5) == 0b110:  # 2-byte character
                num_bytes = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character
                num_bytes = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character
                num_bytes = 3
            else:  # Invalid starting byte
                return False
        else:
            # Check continuation bytes
            if (byte >> 6) != 0b10:  # Valid continuation byte starts with 10
                return False
            num_bytes -= 1

    return num_bytes == 0  # All bytes must be accounted for


# Example usage
if __name__ == "__main__":
    data = [65]
    print(validUTF8(data))  # True

    data = [
        80,
        121,
        116,
        104,
        111,
        110,
        32,
        105,
        115,
        32,
        99,
        111,
        111,
        108,
        33
        ]
    print(validUTF8(data))  # True

    data = [229, 65, 127, 256]
    print(validUTF8(data))  # False
