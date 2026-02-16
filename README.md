# 🔥 Google Drive PDF Downloader – Download Preview Files Without Print or Download Permission (GUI Tool)

A powerful **Python GUI application** that allows you to download Google Drive preview files and convert them into a high-quality PDF — even when **Print and Download options are disabled**.

This tool extracts preview images directly from the browser and compiles them into a complete PDF automatically.

🚀 Perfect for:
- View-only Google Drive files
- Disabled print/download documents

---

## 📌 Why This Tool?

Many Google Drive files disable:
- ❌ Download option
- ❌ Print option
- ❌ Save as PDF

This application works by extracting preview images directly from the browser session and rebuilding the full PDF locally.

⚠️ **Important:** Use responsibly and only for content you have permission to access.

---

## 🛠 Built With

- Python
- Tkinter (GUI)
- Selenium (Chrome Automation)
- Pillow
- FPDF
- WebDriver Manager

No command-line arguments required — everything is controlled from a clean desktop interface.

---

## ✅ Features

- 🖥️ Clean and Simple GUI
- 🔓 Works even if Print/Download is disabled
- 🔗 Single Google Drive link mode
- 📂 Batch mode using `.txt` file
- 📁 Custom PDF save directory
- 📄 Auto PDF naming (timestamp support)
- 🔔 Sound notification after completion
- 🚀 Automatic ChromeDriver installation
- 🔄 Opens browser only once for batch processing

---

## 🎥 Demo Video
[![Watch the Demo](https://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg)](https://www.youtube.com/watch?v=YOUTUBE_VIDEO_ID_HERE)

---

## 🖼️ GUI Preview

> ✏️ Replace image links below with your uploaded screenshot links

### 🔹 Main Window

![Main GUI Screenshot](https://github.com/user-attachments/assets/48b72900-2104-4ba4-9fda-0a20761d0bc9)

---

### 🔹 Running Process

![Processing Screenshot](https://github.com/user-attachments/assets/d2aeb849-464e-4b5d-9815-abd866706bba)

---

### 🔹 Batch Mode Example

![Batch Mode Screenshot](https://github.com/user-attachments/assets/6aa7c5b2-e637-489f-b0a5-00d7c3915372)

---

## 🚀 How to Run

Make sure you have Python installed.

### 1️⃣ Clone this repository

```sh
git clone https://github.com/ar-titumir/download-pdf-from-drive.git
cd download-pdf-from-drive
````

---

### 2️⃣ Create Virtual Environment (Recommended)

```sh
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```sh
pip install -r requirements.txt
```

Required libraries:

* selenium
* Pillow
* fpdf2
* webdriver-manager

---

### 4️⃣ Run the Application

```sh
python app2.py
```
### Alternative
Just *double click* the `run_app2.bat` file to run the GUI!

The GUI window will open.

---

## 🖥️ How to Use the GUI

### 🔹 Single File Mode

1. Paste Google Drive preview URL
2. Enter PDF name (optional)
3. Select PDF save directory
4. Click **Run**

If no PDF name is provided → timestamp name will be used.

---

### 🔹 Batch Mode

1. Create a `.txt` file like this:

```
https://drive.google.com/file/abc123/view "Physics Full Book"
https://drive.google.com/file/xyz456/view "Math Notes"
```

2. Select the text file using **Browse**
3. Choose output directory
4. Click **Run**

Each line supports quoted PDF names.

---

## ⚙️ How It Works

* Selenium opens Google Drive preview
* Scrolls through all preview pages
* Extracts blob images using JavaScript canvas
* Saves images locally
* Converts all images into a single PDF
* Closes browser after completion

ChromeDriver is automatically handled by `webdriver-manager`.

---

## ⚠️ Notes

* Keep Google Chrome updated
* Works only for previewable Drive files
* Browser window must remain open during processing
* Windows only (uses `winsound`)

---

## 📂 Project Structure

```
download-pdf-from-drive/
├── app2.py
├── requirements.txt
├── README.md
```

---

## 📌 Author

Created by **ar_titumir**
[https://github.com/ar-titumir](https://github.com/ar-titumir)

If this project helps you, please give it a ⭐ on GitHub.

If you want, I can now make a **more professional GitHub-style version with badges and cleaner formatting**.
