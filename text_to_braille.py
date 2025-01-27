#test_to_braille.py
import louis


def text_to_braille(input_text, table="ml-in-g1.utb"):
    if not input_text:
        raise ValueError("Input text cannot be empty.")

    try:
        braille_text = louis.translateString([table], input_text)
        return braille_text
    except Exception as e:
        print(f"Input Text: {input_text}")
        print(f"Translation Table: {table}")
        raise Exception(f"Error during Braille conversion: {e}")

# Main function remains unchanged

def main():
    string = "abc"
    braille_string = text_to_braille(string)
    print(braille_string)

if __name__ == "__main__":
    main()