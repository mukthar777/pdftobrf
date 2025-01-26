import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from pdf_to_text import pdf_to_text
from text_to_braille import text_to_braille
from unicode_to_brf import convert_unicode_braille_to_brf, unicode_braille_to_text  # Import your function

def upload_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        text_window.delete("1.0", tk.END)
        text_window.insert(tk.END, file_path)

def convert_to_braille():
    file_path = text_window.get("1.0", tk.END).strip()
    if file_path:
        try:
            # Simulated PDF-to-text and text-to-Braille conversion
            extracted_text = pdf_to_text(file_path) # Replace with pdf_to_text(file_path)
            print(extracted_text)
            braille_text = text_to_braille(extracted_text)
            braille_window.delete("1.0", tk.END)
            braille_window.insert(tk.END, braille_text)
            messagebox.showinfo("Conversion Complete", "Braille Output displayed below.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to convert: {e}")

def convert_braille_to_text():
    braille_unicode = braille_window.get("1.0", tk.END).strip()
    if not braille_unicode:
        messagebox.showwarning("Warning", "No Braille content to convert.")
        return  # Exit if no Braille content is present

    try:
        # Convert Braille Unicode to text
        converted_text = unicode_braille_to_text(braille_unicode)
        
        # Clear the converted text window and display the result
        converted_text_window.delete("1.0", tk.END)  
        converted_text_window.insert(tk.END, converted_text)  
        
        messagebox.showinfo("Conversion Complete", "Text Output displayed below.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to convert Braille to text: {e}")

def download_brf():
    braille_unicode = braille_window.get("1.0", tk.END).strip()
    if not braille_unicode:
        messagebox.showwarning("Warning", "No Braille content to save.")
        return

    output_file = filedialog.asksaveasfilename(
        defaultextension=".brf",
        filetypes=[("Braille Ready Format", "*.brf")],
        title="Save BRF File"
    )
    if output_file:
        try:
            # Convert Unicode Braille to BRF and save
            convert_unicode_braille_to_brf(braille_unicode, output_file)
            messagebox.showinfo("Success", f"BRF file saved to: {output_file}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save BRF file: {e}")

# Create the main window
root = tk.Tk()
root.title("PDF to Braille Converter")
root.geometry("600x650")
root.configure(bg="#e6f7ff")

# Set up fonts and colors
font = ("Arial", 12)
button_font = ("Arial", 12, "bold")
bg_color = "#e6f7ff"  # Soft blue background
button_color = "#4CAF50"  # Green for buttons
button_hover_color = "#45a049"  # Darker green on hover
text_bg_color = "#f8f9fa"  # Light gray background for textboxes
braille_bg_color = "#fff3e6"  # Soft orange for Braille output
converted_text_bg_color = "#f0f8ff"  # Light blue background for converted text

# Frame for Upload and Convert section
frame_1 = tk.Frame(root, bg=bg_color)
frame_1.pack(pady=20, padx=20, fill="x")

upload_button = ttk.Button(frame_1, text="Upload PDF", command=upload_pdf)
upload_button.pack(side="left", padx=10)

# Frame for Text Window Section
frame_2 = tk.Frame(root, bg=bg_color)
frame_2.pack(pady=10, padx=20, fill="x")

text_label = tk.Label(frame_2, text="PDF File Path:", font=font, bg=bg_color)
text_label.pack(pady=5, anchor="w")

text_window = tk.Text(frame_2, height=2, width=50, font=font, bg=text_bg_color)
text_window.pack(pady=5)

convert_button = ttk.Button(frame_2, text="Convert to Braille", command=convert_to_braille)
convert_button.pack(pady=10)

# Frame for Braille Output Section
frame_3 = tk.Frame(root, bg=bg_color)
frame_3.pack(pady=10, padx=20, fill="x")

braille_label = tk.Label(frame_3, text="Braille Output:", font=font, bg=bg_color)
braille_label.pack(pady=5, anchor="w")

braille_window = tk.Text(frame_3, height=10, width=60, font=font, bg=braille_bg_color)
braille_window.pack(pady=5)

# Frame for Converted Text Section
frame_5 = tk.Frame(root, bg=bg_color)
frame_5.pack(pady=10, padx=20, fill="x")

converted_text_label = tk.Label(frame_5, text="Converted Text Output:", font=font, bg=bg_color)
converted_text_label.pack(pady=5, anchor="w")

converted_text_window = tk.Text(frame_5, height=10, width=60, font=font, bg=converted_text_bg_color)
converted_text_window.pack(pady=5)

# Frame for Download Section
frame_4 = tk.Frame(root, bg=bg_color)
frame_4.pack(pady=10, padx=20, fill="x")

download_button = ttk.Button(frame_4, text="Download as BRF", command=download_brf)
download_button.pack(pady=10)

# Frame for Convert Braille to Text Section
frame_6 = tk.Frame(root, bg=bg_color)
frame_6.pack(pady=10, padx=20, fill="x")

convert_braille_button = ttk.Button(frame_6, text="Convert Braille to Text", command=convert_braille_to_text)
convert_braille_button.pack(pady=10)

# Style for buttons
style = ttk.Style()
style.configure("TButton",
                font=button_font,
                padding=10,
                background=button_color,
                relief="flat")

style.map("TButton",
          background=[("active", button_hover_color)])

# Run the application
root.mainloop()
