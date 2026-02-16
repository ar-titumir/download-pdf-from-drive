import os
import shlex
import tkinter as tk
from tkinter import filedialog, messagebox

from scraper import create_driver, run_scraper
import logging
from utils import (
    ensure_pdf_name,
    timestamp_name,
    ensure_directory,
    notify,
    setup_logging,
)


class PDFDownloaderGUI:

    def __init__(self, root):
        setup_logging()
        logging.info("GUI initialized")
        self.root = root
        self.root.title("PDF file maker from Google Drive link")
        self.root.geometry("500x240")

        self.create_widgets()

    def create_widgets(self):

        tk.Label(self.root, text="Post URL or Text File Dir:").pack(anchor="w", padx=10)

        self.entry_url = tk.Entry(self.root, width=60)
        self.entry_url.pack(padx=10)

        tk.Button(self.root, text="Browse", command=self.browse_text).pack(anchor="e", padx=10)

        tk.Label(self.root, text="PDF file name:").pack(anchor="w", padx=10)

        self.entry_pdf_name = tk.Entry(self.root, width=60)
        self.entry_pdf_name.pack(padx=10)

        tk.Label(self.root, text="PDF File Dir:").pack(anchor="w", padx=10)

        self.entry_pdf_dir = tk.Entry(self.root, width=60)
        self.entry_pdf_dir.pack(padx=10)

        tk.Button(self.root, text="Browse", command=self.browse_dir).pack(anchor="e", padx=10)

        tk.Button(self.root, text="Run", command=self.start_process, width=15).pack(pady=10)

        self.status_label = tk.Label(self.root, text="Idle", fg="blue")
        self.status_label.pack(anchor="w", padx=10)

    def update_status(self, text):
        self.status_label.config(text=text)
        self.root.update()

    def browse_text(self):
        path = filedialog.askopenfilename(filetypes=[("Text file", "*.txt")])
        self.entry_url.delete(0, tk.END)
        self.entry_url.insert(0, path)

    def browse_dir(self):
        path = filedialog.askdirectory()
        self.entry_pdf_dir.delete(0, tk.END)
        self.entry_pdf_dir.insert(0, path)

    def start_process(self):

        input_path = self.entry_url.get().strip()
        pdf_name = self.entry_pdf_name.get().strip()
        pdf_dir = ensure_directory(self.entry_pdf_dir.get().strip())

        if not input_path:
            messagebox.showerror("Error", "Provide link or text file")
            return

        driver = create_driver()

        try:
            if input_path.startswith("http"):
                pdf_name_fixed = ensure_pdf_name(pdf_name)
                pdf_path = os.path.join(pdf_dir, pdf_name_fixed)
                img_dir = os.path.join(pdf_dir, "temp_imgs")

                success = run_scraper(
                    driver,
                    input_path,
                    img_dir,
                    pdf_path,
                    status_callback=self.update_status
                )

                if success:
                    notify()
                    messagebox.showinfo("Completed", f"Saved:\n{pdf_path}")

            else:
                if not os.path.exists(input_path):
                    messagebox.showerror("Error", "Text file not found")
                    return

                with open(input_path, "r", encoding="utf-8") as f:
                    lines = f.readlines()

                total = len([l for l in lines if l.strip()])
                count = 0

                for line in lines:
                    if not line.strip():
                        continue

                    count += 1
                    parts = shlex.split(line.strip())

                    url = parts[0]

                    if len(parts) > 1:
                        name = ensure_pdf_name(parts[1])
                    else:
                        name = timestamp_name()

                    pdf_path = os.path.join(pdf_dir, name)
                    img_dir = os.path.join(pdf_dir, "temp_imgs")

                    self.update_status(f"Processing {count}/{total}")

                    run_scraper(
                        driver,
                        url,
                        img_dir,
                        pdf_path,
                        status_callback=self.update_status
                    )

                notify()
                messagebox.showinfo("Completed", "All files processed successfully!")
                logging.info("Batch processing completed")

        finally:
            driver.quit()
