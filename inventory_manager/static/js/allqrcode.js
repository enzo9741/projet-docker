const UUID = djangoArrayToJsArray(document.getElementById("uuid").value);
const BRAND =  djangoArrayToJsArray(document.getElementById("brand").value);
const REFERENCE =  djangoArrayToJsArray(document.getElementById("reference").value);
const SERIAL_NUMBER =  djangoArrayToJsArray(document.getElementById("serial").value);
const DISPLAY = document.getElementById('display');
const BASE_URL = "./qrcode/";

for(let i = 0; i < BRAND.length; i++) {
    mainDiv = document.createElement("div");
    mainDiv.setAttribute("style","margin-top: 32px");

    imageDiv = document.createElement("div");
    imageDiv.setAttribute("id", i.toString() + "-image");

    textDiv = document.createElement("div");
    textDiv.setAttribute("id", i.toString() + "-text");
    textDiv.setAttribute("style", "margin-top: 16px;");
    textDiv.innerText = BRAND[i] + " " + REFERENCE[i] + "\n" + SERIAL_NUMBER[i];

    mainDiv.appendChild(imageDiv);
    mainDiv.appendChild(textDiv);
    DISPLAY.appendChild(mainDiv);

    generateQrcode(UUID[i], i.toString() + "-image");
}

function djangoArrayToJsArray(djangoArray) {
    let array = [];
    let temp = "";
    for (const element of djangoArray) {
        let value = element.toString();
        if (value === ',' || value === ']') {
            array.push(temp);
            temp = ""
        } else if ((value == '\'') || (value == '[') || (value == ' ')) {

        } else {
            temp += value
        }
    }
    return array;
}

function generateQrcode(uuid, id) {
    let url = BASE_URL + uuid;
    console.log(url);
    const QRCODE = new QRCode(document.getElementById(id), {
        text: url,
        width: 128,
        height: 128,
        colorDark : '#000',
        colorLight : '#fff',
        correctLevel : QRCode.CorrectLevel.H
    });
}

function printAllQrcode() {
    const PRINTABLE = DISPLAY.outerHTML;
    console.log(PRINTABLE);
    const WIDTH = DISPLAY.offsetWidth * 1.25;
    const HEIGHT = DISPLAY.offsetHeight *1.5;
    const MY_WINDOW = window.open('', '', 'height=' + HEIGHT + ', width=' + WIDTH);

    MY_WINDOW.document.write('<html>');
    MY_WINDOW.document.write('<style>section {margin-left: 32px; margin-right: 32px; display: grid; grid-template-columns: repeat(4, 1fr); grid-gap: 10px; </style>');
    MY_WINDOW.document.write(PRINTABLE);
    MY_WINDOW.document.write('</body></html>');

    MY_WINDOW.print();
    MY_WINDOW.close();
}