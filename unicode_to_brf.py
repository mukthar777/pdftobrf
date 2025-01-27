import louis
import os

def get_liblouis_table_path(table_name):
    """
    Find the full path to the LibLouis translation table.
    
    Args:
        table_name (str): Name of the translation table
    
    Returns:
        str: Full path to the translation table
    """
    # List of common LibLouis table directories
    table_dirs = [
        '/usr/share/liblouis/tables',
        '/usr/local/share/liblouis/tables',
        os.path.expanduser('~/.local/share/liblouis/tables')
    ]
    
    for directory in table_dirs:
        full_path = os.path.join(directory, table_name)
        if os.path.exists(full_path):
            return full_path
    
    raise FileNotFoundError(f"Translation table {table_name} not found in standard directories")

def unicode_braille_to_text(braille_unicode, table="en-us-g1.ctb"):
    """
    Convert Braille Unicode to readable text.
    
    Args:
        braille_unicode (str): Braille Unicode text to convert
        table (str): Translation table to use (default is US English Grade 1)
    
    Returns:
        str: Converted readable text
    """
    if not braille_unicode:
        raise ValueError("Braille Unicode text cannot be empty.")
    
    try:
        # Get the full path to the translation table
        table_path = get_liblouis_table_path(table)
        
        # Translate Braille Unicode to readable text
        normal_text = louis.translate([table_path], braille_unicode)[0]
        return normal_text
    except Exception as e:
        print(f"Braille Unicode: {braille_unicode}")
        print(f"Translation Table: {table}")
        raise Exception(f"Error converting Braille Unicode to text: {e}")

def text_to_brf(text, output_file, table="en-us-g2.ctb"):
    """
    Convert text to BRF (Braille Ready Format) file.
    
    Args:
        text (str): Text to convert to Braille
        output_file (str): Path to save the BRF file
        table (str): Translation table to use (default is US English Grade 2)
    """
    try:
        # Get the full path to the translation table
        table_path = get_liblouis_table_path(table)
        
        # Translate text to Braille
        braille_output = louis.translate([table_path], text)[0]
        
        # Write to BRF file
        with open(output_file, 'wb') as file:
            file.write(braille_output.encode('utf-8'))
        
        return braille_output
    except Exception as e:
        raise Exception(f"Error converting text to BRF: {e}")

def convert_unicode_braille_to_brf(braille_unicode, output_file, 
                                    unicode_table="en-us-g1.ctb", 
                                    brf_table="en-us-g2.ctb"):
    """
    Full conversion from Braille Unicode to BRF file.
    
    Args:
        braille_unicode (str): Braille Unicode text to convert
        output_file (str): Path to save the BRF file
        unicode_table (str): Table for Unicode to text conversion
        brf_table (str): Table for text to BRF conversion
    
    Returns:
        str: The converted text before BRF conversion
    """
    # First convert Unicode Braille to readable text
    normal_text = unicode_braille_to_text(braille_unicode, unicode_table)
    
    # Then convert text to BRF
    text_to_brf(normal_text, output_file, brf_table)
    
    return normal_text

def main():
    # Example Braille Unicode (replace with your actual input)
    braille_unicode = "⠓⠑⠇⠇⠕"  # This represents "hello"
    output_file = "output.brf"
    
    try:
        # Convert Unicode Braille to BRF
        converted_text = convert_unicode_braille_to_brf(braille_unicode, output_file)
        
        print(f"Braille Unicode: {braille_unicode}")
        print(f"Converted Text: {converted_text}")
        print(f"BRF file saved to: {output_file}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()