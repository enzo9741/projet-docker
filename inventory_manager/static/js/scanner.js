const HTML5_QRCODE = new Html5Qrcode("reader");
const CONFIG = {fps: 15, qrbox: {width: 250, height: 250}};


const qrCodeSuccessCallback = (decodedText, decodedResult) => {
    console.log(`Code matched = ${decodedText}`, decodedResult);
    HTML5_QRCODE.stop().then((ignore) => {
            window.location.href = decodedText;
    }).catch((err) => {
        console.log(err);
    });
};


HTML5_QRCODE.start({facingMode: "environment"}, CONFIG, qrCodeSuccessCallback);