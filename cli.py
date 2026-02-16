import argparse
import os
import shlex
import logging

from scraper import create_driver, run_scraper
from utils import ensure_pdf_name, timestamp_name, ensure_directory, setup_logging, notify


def main():
    parser = argparse.ArgumentParser(
        description="Google Drive PDF Downloader (CLI)"
    )

    parser.add_argument(
        "input",
        help="Drive URL OR path to .txt batch file"
    )

    parser.add_argument(
        "-o", "--output",
        help="Output PDF name (single mode only)",
        default=""
    )

    parser.add_argument(
        "-d", "--dir",
        help="Output directory",
        default="."
    )

    parser.add_argument(
        "--no-sound",
        action="store_true",
        help="Disable completion sound"
    )

    args = parser.parse_args()

    setup_logging()
    logging.info("CLI started")

    input_path = args.input
    output_dir = ensure_directory(args.dir)

    driver = create_driver()

    try:
        # -------- SINGLE LINK MODE --------
        if input_path.startswith("http"):

            pdf_name = ensure_pdf_name(args.output)
            pdf_path = os.path.join(output_dir, pdf_name)
            img_dir = os.path.join(output_dir, "temp_imgs")

            run_scraper(driver, input_path, img_dir, pdf_path)

            if not args.no_sound:
                notify()

            print(f"\nSaved → {pdf_path}")

        # -------- BATCH MODE --------
        else:
            if not os.path.exists(input_path):
                print("Text file not found")
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

                pdf_path = os.path.join(output_dir, name)
                img_dir = os.path.join(output_dir, "temp_imgs")

                print(f"[{count}/{total}] Processing...")

                run_scraper(driver, url, img_dir, pdf_path)

            if not args.no_sound:
                notify()

            print("\nAll files completed")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
