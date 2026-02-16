import os
import time
import base64
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
from fpdf import FPDF
import logging


logging.basicConfig(level=logging.INFO)

def create_driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    return webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

def run_scraper(driver, url, img_dir, pdf_path, status_callback=None):

    def update_status(msg):
        if status_callback:
            status_callback(msg)
        logging.info(msg)

    logging.info(f"Opening URL: {url}")
    update_status(f"Loading: {url}")

    driver.delete_all_cookies()
    driver.get(url)
    time.sleep(5)

    update_status("Finding pages...")
    divs = driver.find_elements(By.XPATH, "//div[starts-with(@style, 'padding-bottom:')]")

    os.makedirs(img_dir, exist_ok=True)
    saved_count = 0

    for idx, div in enumerate(divs, start=1):
        driver.execute_script("arguments[0].scrollIntoView();", div)
        time.sleep(0.4)

        update_status(f"Downloading page {idx} image...")

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
                    img_path = os.path.join(img_dir, f"{idx:03d}.png")

                    with open(img_path, "wb") as f:
                        f.write(data)

                    saved_count += 1

        except Exception as e:
            logging.error(f"Error on page {idx}: {e}")

    if saved_count == 0:
        update_status("No images found")
        logging.warning("No images were extracted.")
        return False

    update_status("Converting to PDF...")
    logging.info("Starting PDF conversion")

    pdf = FPDF(unit="pt")

    for i in range(1, saved_count + 1):
        img_path = os.path.join(img_dir, f"{i:03d}.png")
        if os.path.exists(img_path):
            image = Image.open(img_path)
            w, h = image.size
            pdf.add_page(format=(w, h))
            pdf.image(img_path, 0, 0, w, h)

    pdf.output(pdf_path)

    update_status(f"Saved: {os.path.basename(pdf_path)}")
    logging.info(f"PDF saved successfully at {pdf_path}")

    return True
