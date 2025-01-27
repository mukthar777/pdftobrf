import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pdf_to_text import pdf_to_text
from text_to_braille import text_to_braille
from unicode_to_brf import convert_unicode_braille_to_brf, unicode_braille_to_text

# Modern color scheme
DARK_BG = "#2d2d2d"
LIGHT_TEXT = "#ffffff"
ACCENT_COLOR = "#4a9cff"
SECONDARY_BG = "#3d3d3d"
TEXT_AREA_BG = "#1e1e1e"

def create_scrollable_text(parent, height):
    frame = ttk.Frame(parent)
    scrollbar = ttk.Scrollbar(frame)
    text_widget = tk.Text(
        frame, 
        height=height, 
        wrap=tk.WORD,
        yscrollcommand=scrollbar.set,
        bg=TEXT_AREA_BG,
        fg=LIGHT_TEXT,
        insertbackground=LIGHT_TEXT,
        font=("Segoe UI", 10)
    )
    scrollbar.config(command=text_widget.yview)
    text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    return frame, text_widget

def upload_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        text_window.delete("1.0", tk.END)
        text_window.insert(tk.END, file_path)

def convert_to_braille():
    file_path = text_window.get("1.0", tk.END).strip()
    if not file_path:
        messagebox.showwarning("Warning", "Please select a PDF file first")
        return

    try:
        extracted_text = pdf_to_text(file_path)
        braille_text = text_to_braille(extracted_text)
        braille_window.delete("1.0", tk.END)
        braille_window.insert(tk.END, braille_text)
        messagebox.showinfo("Conversion Complete", "Braille output generated successfully")
    except Exception as e:
        messagebox.showerror("Error", f"Conversion failed: {str(e)}")

def convert_braille_to_text():
    braille_unicode = braille_window.get("1.0", tk.END).strip()
    if not braille_unicode:
        messagebox.showwarning("Warning", "No Braille content to convert")
        return

    try:
        converted_text = unicode_braille_to_text(braille_unicode)
        converted_text_window.delete("1.0", tk.END)
        converted_text_window.insert(tk.END, converted_text)
        messagebox.showinfo("Conversion Complete", "Text conversion successful")
    except Exception as e:
        messagebox.showerror("Error", f"Conversion failed: {str(e)}")

def download_brf():
    braille_unicode = braille_window.get("1.0", tk.END).strip()
    if not braille_unicode:
        messagebox.showwarning("Warning", "No Braille content to save")
        return

    output_file = filedialog.asksaveasfilename(
        defaultextension=".brf",
        filetypes=[("Braille Ready Format", "*.brf")],
        title="Save BRF File"
    )
    if output_file:
        try:
            convert_unicode_braille_to_brf(braille_unicode, output_file)
            messagebox.showinfo("Success", f"File saved successfully:\n{output_file}")
        except Exception as e:
            messagebox.showerror("Error", f"Save failed: {str(e)}")

# Main window setup
root = tk.Tk()
root.title("PDF to Braille Converter")
root.geometry("1280x800")
root.configure(bg=DARK_BG)
root.minsize(1000, 700)

# Configure styles
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Segoe UI", 10), padding=6, background=ACCENT_COLOR, foreground=LIGHT_TEXT)
style.map("TButton", background=[("active", "#3d7cc4")])
style.configure("TFrame", background=DARK_BG)
style.configure("TLabel", background=DARK_BG, foreground=LIGHT_TEXT, font=("Segoe UI", 10, "bold"))

# Main container
main_frame = ttk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# File input section
input_frame = ttk.Frame(main_frame)
input_frame.pack(fill=tk.X, pady=10)

ttk.Label(input_frame, text="PDF File:").pack(side=tk.LEFT, padx=5)
text_window_frame, text_window = create_scrollable_text(input_frame, 2)
text_window_frame.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
ttk.Button(input_frame, text="Browse", command=upload_pdf).pack(side=tk.LEFT, padx=5)

# Conversion buttons
button_frame = ttk.Frame(main_frame)
button_frame.pack(fill=tk.X, pady=10)
ttk.Button(button_frame, text="Convert to Braille", command=convert_to_braille).pack(side=tk.LEFT, padx=5)
ttk.Button(button_frame, text="Convert Braille to Text", command=convert_braille_to_text).pack(side=tk.LEFT, padx=5)
ttk.Button(button_frame, text="Export BRF", command=download_brf).pack(side=tk.RIGHT, padx=5)

# Braille output section
ttk.Label(main_frame, text="Braille Output").pack(anchor=tk.W, pady=(10, 0))
braille_window_frame, braille_window = create_scrollable_text(main_frame, 15)
braille_window_frame.pack(fill=tk.BOTH, expand=True, pady=5)

# Converted text section
ttk.Label(main_frame, text="Converted Text").pack(anchor=tk.W, pady=(10, 0))
converted_text_frame, converted_text_window = create_scrollable_text(main_frame, 15)
converted_text_frame.pack(fill=tk.BOTH, expand=True, pady=5)

root.mainloop()