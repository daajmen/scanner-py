import subprocess
from pyzbar.pyzbar import decode
from PIL import Image
import io
import time

print("Startar barcode-scanning... (Ctrl+C för att avsluta)")
while True:
    result = subprocess.run(
        ["libcamera-still", "-n", "--width", "640", "--height", "480", "--format", "jpeg", "--output", "-"],
        stdout=subprocess.PIPE
    )

    img = Image.open(io.BytesIO(result.stdout))
    barcodes = decode(img)

    if barcodes:
        for barcode in barcodes:
            print("Avläst:", barcode.data.decode("utf-8"))
    else:
        print("Ingen streckkod hittad.")

    time.sleep(5)
