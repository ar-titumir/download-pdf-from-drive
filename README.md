
# 🚀 Google Drive PDF Downloader (Professional Modular GUI Tool)

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Selenium](https://img.shields.io/badge/Selenium-Automation-green)
![GUI](https://img.shields.io/badge/Tkinter-GUI-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)
![Status](https://img.shields.io/badge/Status-Active-success)

A **professional modular Python desktop application** that downloads Google Drive preview pages and rebuilds them into a complete high-quality PDF — even when **Print and Download are disabled**.

This version is fully **refactored into modules**, includes **structured logging**, and follows a clean, maintainable architecture.

---

## 🎯 Why This Tool Exists

Many Google Drive files disable:

* ❌ Download
* ❌ Print
* ❌ Save as PDF

This tool reconstructs the document by extracting preview images from the browser and converting them back into a full PDF locally.

⚠️ **Use responsibly and only for content you are allowed to access.**

---

## 🎥 Demo Video

[![Watch the Demo](https://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg)](https://www.youtube.com/watch?v=YOUTUBE_VIDEO_ID_HERE)

---

## 🖼️ GUI Preview

### 🔹 Main Window

![Main GUI Screenshot](https://github.com/user-attachments/assets/48b72900-2104-4ba4-9fda-0a20761d0bc9)

### 🔹 Running Process

![Processing Screenshot](https://github.com/user-attachments/assets/d2aeb849-464e-4b5d-9815-abd866706bba)

### 🔹 Batch Mode Example

![Batch Mode Screenshot](https://github.com/user-attachments/assets/6aa7c5b2-e637-489f-b0a5-00d7c3915372)

---

## ✨ Core Features

* 🖥️ Clean desktop GUI
* 🔓 Works when download/print disabled
* 🔗 Single link mode
* 📂 Batch mode (.txt input)
* 📄 Auto PDF naming
* 📁 Custom output folder
* 🔔 Completion notification
* 🚀 ChromeDriver auto install
* 🔄 Browser reused for batch jobs
* 🧩 Modular architecture
* 🪵 Structured logging system
* 🛠 Production-style codebase

---

## 🧠 Architecture Overview

```
GUI (tkinter)
   │
   ├── gui.py → Handles UI + user actions
   │
   ├── scraper.py → Selenium + image extraction + PDF builder
   │
   ├── utils.py → logging, naming, helpers
   │
   └── app2.py → entry point
```

Flow:

```
User → GUI → Scraper → Images → PDF → Logs → Done
```

---

## 🪵 Logging System

A centralized logging system is implemented.

Logs are saved to:

```
logs/app.log
```

Logs include:

* GUI start
* URL processing
* Batch progress
* Errors
* PDF generation
* Completion status

Example:

```
2026-02-10 12:22:31 | INFO | GUI initialized
2026-02-10 12:22:35 | INFO | Opening URL
2026-02-10 12:22:52 | INFO | PDF saved successfully
```

Logging outputs to:

* console
* log file

---

## 📂 Project Structure

```
download-pdf-from-drive/
│
├── app2.py              # Entry point
├── gui.py               # GUI logic
├── scraper.py           # Selenium + PDF builder
├── utils.py             # logging + helpers
├── cli.py               # cli version 
│
├── logs/
│   └── app.log
│
├── requirements.txt
├── LICENSE
└── README.md
```

---

## ⚙️ Tech Stack

| Layer      | Technology        |
| ---------- | ----------------- |
| GUI        | Tkinter           |
| Automation | Selenium          |
| PDF        | FPDF2             |
| Images     | Pillow            |
| Driver     | webdriver-manager |
| Logging    | Python logging    |

---

## 🚀 Installation

### 1️⃣ Clone repo

```bash
git clone https://github.com/ar-titumir/download-pdf-from-drive.git
cd download-pdf-from-drive
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
python app2.py
```

Or double-click:

```
run_app2.bat
```

---

## 🖥️ How to Use

### 🔹 Single File Mode

1. Paste Drive preview URL
2. Enter PDF name (optional)
3. Select output directory
4. Click **Run**

If no name provided → timestamp auto used.

---

### 🔹 Batch Mode

Create `.txt`:

```
https://drive.google.com/file/abc/view "Physics Book"
https://drive.google.com/file/xyz/view "Math Notes"
```

Then:

* Select file
* Choose output dir
* Click Run

---

## ⚙️ How It Works Internally

1. Selenium opens preview
2. Scrolls through pages
3. Extracts canvas images
4. Saves PNG files
5. Combines into PDF
6. Logs everything
7. Notifies user

---

## 🧩 Modular Design Philosophy

This project is structured like a real software project:

| Module     | Purpose           |
| ---------- | ----------------- |
| app2.py    | App launcher      |
| gui.py     | UI + batch logic  |
| scraper.py | Automation engine |
| utils.py   | Logging + helpers |

Benefits:

* Easier debugging
* Easier expansion
* Cleaner code
* Production ready
* Scalable

---

## 🧪 Developer Mode

To debug issues:

```
logs/app.log
```

You can monitor:

* failed pages
* selenium errors
* batch progress

---


## 🖥 CLI Mode

You can run the tool without GUI.

### Single file
```
python cli.py "DRIVE_URL" -o output.pdf
```

### Batch
```
python cli.py links.txt -d output_folder
```

### Disable sound
```
python cli.py links.txt --no-sound
```

---


## 🛣 Roadmap

Future improvements:

* progress bar
* retry failed pages
* CLI version
* EXE build
* headless mode
* config file
* parallel downloads
* drag-drop links
* dark mode

---

## ⚠️ Important Notes

* Keep Chrome updated
* Browser must stay open
* Only works on previewable Drive files
* Respect copyright & permissions
* Windows fully supported
* Linux/mac supported

---

## 👨‍💻 Author

**ar_titumir**
GitHub: [https://github.com/ar-titumir](https://github.com/ar-titumir)

If this project helped you, give it a ⭐


## 📜 License

This project is licensed under the MIT License.

See the LICENSE file for details.

