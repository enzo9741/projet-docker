const MODAL_TITLE = document.getElementById('modalTitle');
const QRCODE_IMAGE = document.getElementById('qrcode');
const QRCODE_TEXT = document.getElementById('qrcodeText');

URL = "";
if(window.location.hostname == "127.0.0.1"){
    URL = "http://192.168.1.25:7000/qrcode/";
}
else {
    URL = window.location.origin + "/qrcode/";
}
const BASE_URL = URL;

function showModal(uuid,brand,reference, serial) {
    $("#myModal").modal('show');
    MODAL_TITLE.innerHTML = brand + " " + reference;
    QRCODE_TEXT.innerText = brand + " " + reference + "\n" + serial;
    QRCODE_IMAGE.innerHTML = "";

    generateQrcode(BASE_URL + uuid);
}

function generateQrcode(url) {
    const QRCODE = new QRCode(document.getElementById('qrcode'), {
        text: url,
        width: 128,
        height: 128,
        colorDark : '#000',
        colorLight : '#fff',
        correctLevel : QRCode.CorrectLevel.H
    });
}

function printQrcode() {
    const PRINTABLE = document.getElementById('printable').innerHTML;
    const WIDTH = document.getElementById('printable').offsetWidth + 20;
    const HEIGHT = document.getElementById('printable').offsetHeight + 40;
    const MY_WINDOW = window.open('', '', 'height=' + HEIGHT + ', width=' + WIDTH);

    MY_WINDOW.document.write('<html>');
    MY_WINDOW.document.write(PRINTABLE);
    MY_WINDOW.document.write('</body></html>');

    MY_WINDOW.print();
    MY_WINDOW.close();
}
