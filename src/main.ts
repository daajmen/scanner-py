import { BrowserMultiFormatReader } from '@zxing/browser';

const video = document.createElement('video');
video.setAttribute('autoplay', 'true');
video.setAttribute('width', '300');
video.setAttribute('height', '200');
document.body.appendChild(video);

const reader = new BrowserMultiFormatReader();

reader.decodeFromVideoDevice(undefined, video, (result, err) => {
  if (result) {
    alert('Barcode: ' + result.getText());
    reader.reset(); // Stop scanning efter första träffen
  }
});
