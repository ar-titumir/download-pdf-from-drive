import os
import sys
import logging
from datetime import datetime
import os
import sys
import logging


def setup_logging():
    os.makedirs("logs", exist_ok=True)

    log_file = os.path.join("logs", "app.log")

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Remove existing handlers (important!)
    if logger.hasHandlers():
        logger.handlers.clear()

    # File handler
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setLevel(logging.INFO)

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logging.info("Logging system initialized")


# ---------------- FILE NAMING ----------------
def timestamp_name():
    return datetime.now().strftime("%Y%m%d_%H%M%S") + ".pdf"


def ensure_pdf_name(name):
    if not name:
        return timestamp_name()
    if not name.lower().endswith(".pdf"):
        name += ".pdf"
    return name


def ensure_directory(path):
    if not path:
        return os.getcwd()
    os.makedirs(path, exist_ok=True)
    return path


# # ---------------- LOGGING SETUP ----------------
# def setup_logging():
#     os.makedirs("logs", exist_ok=True)

#     logging.basicConfig(
#         level=logging.INFO,
#         format="%(asctime)s | %(levelname)s | %(message)s",
#         handlers=[
#             logging.FileHandler("logs/app.log", encoding="utf-8"),
#             logging.StreamHandler(sys.stdout),
#         ],
#     )

#     logging.info("Application started")


# ---------------- CROSS PLATFORM NOTIFICATION ----------------
def notify():
    """
    Cross-platform completion notification.
    """
    try:
        if sys.platform.startswith("win"):
            import winsound
            winsound.MessageBeep()

        elif sys.platform.startswith("darwin"):
            os.system("afplay /System/Library/Sounds/Glass.aiff")

        else:
            # Linux
            os.system('printf "\\a"')

    except Exception as e:
        logging.warning(f"Notification failed: {e}")
