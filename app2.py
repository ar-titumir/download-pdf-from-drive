import os
import time
import base64
import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime
import shlex
import winsound

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from PIL import Image
from fpdf import FPDF


# ---------------- UTIL ----------------
def timestamp_name():
    return datetime.now().strftime("%Y%m%d_%H%M%S") + ".pdf"


def ensure_pdf_name(name):
    if not name:
        return timestamp_name()
    if not name.lower().endswith(".pdf"):
        name += ".pdf"
    return name


def update_status(text):
    status_label.config(text=text)
    root.update()


# ---------------- DRIVER ----------------
def create_driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    return webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )


# ---------------- SCRAPER ----------------
def run_scraper(driver, URL, IMG_DIR, PDF_PATH):

    print(f"\nOpening: {URL}")
    update_status(f"Loading: {URL}")

    driver.delete_all_cookies()
    driver.get(URL)
    time.sleep(5)

    update_status("Finding pages...")
    print("Finding pages...")

    divs = driver.find_elements(By.XPATH, "//div[starts-with(@style, 'padding-bottom:')]")

    os.makedirs(IMG_DIR, exist_ok=True)
    saved_count = 0

    for idx, div in enumerate(divs, start=1):
        driver.execute_script("arguments[0].scrollIntoView();", div)
        time.sleep(0.4)

        update_status(f"Downloading page {idx} image...")
        print(f"Downloading page {idx} image...")

        try:
            img_tag = div.find_element(By.TAG_NAME, "img")
            src = img_tag.get_attribute("src")

            if src and src.startswith("blob:"):
                script = """
                const img = arguments[0];
                const canvas = document.createElement('canvas');
                canvas.width = img.naturalWidth;
                canvas.height = img.naturalHeight;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(img, 0, 0);
                return canvas.toDataURL('image/png');
                """
                img_base64 = driver.execute_script(script, img_tag)

                if img_base64.startswith("data:image"):
                    data = base64.b64decode(img_base64.split(",")[1])
                    img_path = os.path.join(IMG_DIR, f"{idx:03d}.png")
                    with open(img_path, "wb") as f:
                        f.write(data)
                    saved_count += 1

        except Exception as e:
            print(f"Error on page {idx}:", e)

    if saved_count == 0:
        update_status("No images found")
        print("No images found")
        return False

    # ---------- Convert to PDF ----------
    update_status("Converting to PDF...")
    print("Converting to PDF...")

    pdf = FPDF(unit="pt")

    for i in range(1, saved_count + 1):
        img_path = os.path.join(IMG_DIR, f"{i:03d}.png")
        if os.path.exists(img_path):
            image = Image.open(img_path)
            w, h = image.size
            pdf.add_page(format=(w, h))
            pdf.image(img_path, 0, 0, w, h)

    pdf.output(PDF_PATH)

    update_status(f"Saved: {os.path.basename(PDF_PATH)}")
    print(f"Saved: {os.path.basename(PDF_PATH)}")
    return True


# ---------------- GUI ----------------
def start_process():

    input_path = entry_url.get().strip()
    pdf_name = entry_pdf_name.get().strip()
    pdf_dir = entry_pdf_dir.get().strip()

    if not input_path:
        messagebox.showerror("Error", "Provide link or text file")
        return

    if not pdf_dir:
        pdf_dir = os.getcwd()

    os.makedirs(pdf_dir, exist_ok=True)

    driver = create_driver()   # 🔥 OPEN ONCE

    try:
        # ---------- SINGLE MODE ----------
        if input_path.startswith("http"):

            pdf_name_fixed = ensure_pdf_name(pdf_name)
            pdf_path = os.path.join(pdf_dir, pdf_name_fixed)
            img_dir = os.path.join(pdf_dir, "temp_imgs")

            success = run_scraper(driver, input_path, img_dir, pdf_path)

            if success:
                winsound.MessageBeep()
                messagebox.showinfo("Completed", f"Saved:\n{pdf_path}")

        # ---------- BATCH MODE ----------
        else:
            if not os.path.exists(input_path):
                messagebox.showerror("Error", "Text file not found")
                return

            update_status("Batch processing...")

            with open(input_path, "r", encoding="utf-8") as f:
                lines = f.readlines()

            total = len([l for l in lines if l.strip()])
            count = 0

            for line in lines:
                if not line.strip():
                    continue

                count += 1
                parts = shlex.split(line.strip())  # 🔥 Supports quoted names

                url = parts[0]

                if len(parts) > 1:
                    name = ensure_pdf_name(parts[1])
                else:
                    name = timestamp_name()

                pdf_path = os.path.join(pdf_dir, name)
                img_dir = os.path.join(pdf_dir, "temp_imgs")

                update_status(f"Processing file {count}/{total}")

                run_scraper(driver, url, img_dir, pdf_path)

            winsound.MessageBeep()
            update_status("All done!")
            messagebox.showinfo("Completed", "All files processed successfully!")

    finally:
        driver.quit()   # 🔥 CLOSE ONCE AFTER EVERYTHING


def browse_text():
    path = filedialog.askopenfilename(filetypes=[("Text file", "*.txt")])
    entry_url.delete(0, tk.END)
    entry_url.insert(0, path)


def browse_dir():
    path = filedialog.askdirectory()
    entry_pdf_dir.delete(0, tk.END)
    entry_pdf_dir.insert(0, path)


# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("PDF file maker from Google Drive link")
root.geometry("500x240")

tk.Label(root, text="Post URL or Text File Dir:").pack(anchor="w", padx=10)
entry_url = tk.Entry(root, width=60)
entry_url.pack(padx=10)
tk.Button(root, text="Browse", command=browse_text).pack(anchor="e", padx=10)

tk.Label(root, text="PDF file name:").pack(anchor="w", padx=10)
entry_pdf_name = tk.Entry(root, width=60)
entry_pdf_name.pack(padx=10)

tk.Label(root, text="PDF File Dir:").pack(anchor="w", padx=10)
entry_pdf_dir = tk.Entry(root, width=60)
entry_pdf_dir.pack(padx=10)
tk.Button(root, text="Browse", command=browse_dir).pack(anchor="e", padx=10)

tk.Button(root, text="Run", command=start_process, width=15).pack(pady=10)

status_label = tk.Label(root, text="Idle", fg="blue")
status_label.pack(anchor="w", padx=10)

root.mainloop()
