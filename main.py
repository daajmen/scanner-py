import subprocess
from pyzbar.pyzbar import decode
from PIL import Image
import io
import time

print("Startar barcode-scanning... (Ctrl+C för att avsluta)")
while True:
    result = subprocess.run(
        ["libcamera-jpeg", "-n", "-o", "-"],
        stdout=subprocess.PIPE
    )

    try:
        img = Image.open(io.BytesIO(result.stdout))
        for barcode in decode(img):
            print("Avläst:", barcode.data.decode("utf-8"))
    except Exception as e:
        print("Fel vid bildavläsning:", e)

    time.sleep(5)
