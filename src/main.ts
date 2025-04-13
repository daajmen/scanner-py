import { BrowserMultiFormatReader } from '@zxing/browser';

const video = document.getElementById('video') as HTMLVideoElement;
const reader = new BrowserMultiFormatReader();

reader.decodeFromVideoDevice(undefined, video, (result, err) => {
  if (result) {
    console.log(result.getText());
    alert('Barcode: ' + result.getText());
    reader.reset();
  }
});
