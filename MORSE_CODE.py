class MorseCodeConverter:
    def __init__(self):
        self.morse_code_dict = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
            'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
            'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..',
            '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
            '8': '---..', '9': '----.', '0': '-----',
            '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
            ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
            '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
        }

        self.reverse_morse_code_dict = {value: key for key, value in self.morse_code_dict.items()}

    def text_to_morse(self, text):
        morse_code = ''
        for char in text.upper():
            if char in self.morse_code_dict:
                morse_code += self.morse_code_dict[char] + ' '
        return morse_code.strip()

    def morse_to_text(self, morse_code):
        morse_code = morse_code.split(' ')
        text = ''
        for code in morse_code:
            if code in self.reverse_morse_code_dict:
                text += self.reverse_morse_code_dict[code]
            else:
                text += ' '
        return text.capitalize()


if __name__ == "__main__":
    converter = MorseCodeConverter()
    print("Choose conversion:")
    print("1. Text to Morse Code")
    print("2. Morse Code to Text")

    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        text_input = input("Enter the text to convert to Morse Code: ")
        morse_code_output = converter.text_to_morse(text_input)
        print("Morse Code:", morse_code_output)
    elif choice == 2:
        morse_input = input("Enter the Morse Code to convert to Text: ")
        text_output = converter.morse_to_text(morse_input)
        print("Text:", text_output)
    else:
        print("Invalid choice. Please choose 1 or 2.")
