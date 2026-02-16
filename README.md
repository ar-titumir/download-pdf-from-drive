
# Google Drive PDF Downloader (GUI Version)

This repository provides a **Beautiful GUI application** to download preview images from a **Google Drive file** and automatically convert them into a PDF.

Built using:
- Python
- Tkinter (GUI)
- Selenium (Chrome Automation)
- Pillow
- FPDF
- WebDriver Manager

No command line arguments required — everything is controlled from the GUI.

---

## ✅ Features

- 🖥️ Simple GUI interface
- 🔗 Single Google Drive link download
- 📂 Batch mode using `.txt` file
- 📁 Custom PDF save directory
- 📄 Auto PDF name generation (timestamp support)
- 🔔 Sound notification after completion
- 🚀 Automatic ChromeDriver management

---

## 🎥 Demo Video
[![Watch the Demo](https://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg)](https://www.youtube.com/watch?v=YOUTUBE_VIDEO_ID_HERE)

---

## 🖼️ GUI Preview

> ✏️ Replace image links below with your uploaded screenshot links

### 🔹 Main Window

![Main GUI Screenshot](YOUR_SCREENSHOT_LINK_HERE)

---

### 🔹 Running Process

![Processing Screenshot](YOUR_SCREENSHOT_LINK_HERE)

---

### 🔹 Batch Mode Example

![Batch Mode Screenshot](YOUR_SCREENSHOT_LINK_HERE)

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
* fpdf
* webdriver-manager

---

### 4️⃣ Run the Application

```sh
python app2.py
```

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
* Internet connection required
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
└── temp_imgs/   (auto-created)
```

---

## 📌 Author

Created by **ar_titumir**
[https://github.com/ar-titumir](https://github.com/ar-titumir)

If this project helps you, please give it a ⭐ on GitHub.

If you want, I can now make a **more professional GitHub-style version with badges and cleaner formatting**.
