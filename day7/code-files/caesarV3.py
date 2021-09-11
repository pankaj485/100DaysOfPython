alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().

# pgbgyixovz


def ceaser(input_text, shift_amount, output_direction):
    output_text = ""
    for letter in input_text:
        position = alphabet.index(letter)

        if direction == "encode":
            new_position = position + shift_amount
            output_text += alphabet[new_position]
        elif direction == "decode":
            new_position = position - shift_amount
            output_text += alphabet[new_position]

    if not (direction == "encode" or direction == "decode"):
        print("right commands expected!")

    print(f"{output_direction}d text is {output_text}")


#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

ceaser(input_text=text, shift_amount=shift, output_direction=direction)
