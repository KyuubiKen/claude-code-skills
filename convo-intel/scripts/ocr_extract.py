#!/usr/bin/env python3
"""Extract text from all screenshots in a folder using Apple Vision. Saves raw OCR to a file."""

import sys
from pathlib import Path

import Quartz
import Vision
from Foundation import NSURL

IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".heic", ".webp"}


def ocr_image(image_path: Path) -> str:
    try:
        url = NSURL.fileURLWithPath_(str(image_path))
        input_image = Quartz.CIImage.imageWithContentsOfURL_(url)
        if input_image is None:
            return "[IMAGE LOAD FAILED]"

        handler = Vision.VNImageRequestHandler.alloc().initWithCIImage_options_(input_image, {})
        request = Vision.VNRecognizeTextRequest.alloc().init()
        request.setRecognitionLevel_(Vision.VNRequestTextRecognitionLevelAccurate)
        request.setUsesLanguageCorrection_(True)
        handler.performRequests_error_([request], None)

        results = request.results()
        if not results:
            return "[NO TEXT DETECTED]"

        lines = []
        for observation in results:
            candidates = observation.topCandidates_(1)
            if candidates:
                lines.append(str(candidates[0].string()))
        return "\n".join(lines)
    except Exception as e:
        return f"[OCR ERROR: {e}]"


folder = Path(sys.argv[1])
files = sorted([f for f in folder.iterdir() if f.suffix.lower() in IMAGE_EXTENSIONS], key=lambda x: x.name)

output = []
for f in files:
    print(f"  OCR: {f.name}")
    text = ocr_image(f)
    output.append(f"=== {f.name} ===\n{text}\n")

out_path = Path.home() / "Desktop" / "SCREENSHOTS_ocr_raw.txt"
out_path.write_text("\n".join(output), encoding="utf-8")
print(f"\nSaved → {out_path}")
