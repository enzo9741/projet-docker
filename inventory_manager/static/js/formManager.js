const SELECTOR = document.querySelector('#selector');
const AMOVIBLE_FORM = document.getElementById('amovible-form');
const CABLE_FORM = document.getElementById('cable-form');
const CPU_FORM = document.getElementById('cpu-form');
const HDD_FORM = document.getElementById('hdd-form');
const RAM_FORM = document.getElementById('ram-form');
const SSD_FORM = document.getElementById('ssd-form');
const DRIVE_FORM = document.getElementById('drive-form');

var currentSelected = SELECTOR.value.toLowerCase();
displayForm();

SELECTOR.addEventListener('change', (event) => {
  currentSelected = event.target.value.toLowerCase();
  displayForm();
});

function displayForm() {
    hideEveryElement();
    switch (currentSelected){
        case 'amovible':
            showElement(AMOVIBLE_FORM);
            break;
        case 'cable':
            showElement(CABLE_FORM);
            break;
        case 'cpu':
            showElement(CPU_FORM);
            break;
        case 'ram':
            showElement(RAM_FORM);
            break;
        case 'hdd':
            showElement(DRIVE_FORM);
            showElement(HDD_FORM);
            break;
        case 'ssd':
            showElement(DRIVE_FORM);
            //showElement(SSD_FORM);
            break;
        default:
            console.log(`Unknow ${currentSelected}`);
    }
}

function submitForms() {
    let data;
    switch (currentSelected){
        case 'amovible':
            data = $('#selector-form,#object-form, #amovible-form').serialize();
            break;
        case 'cable':
            data = $('#selector-form,#object-form, #cable-form').serialize();
            break;
        case 'cpu':
            data = $('#selector-form,#object-form, #cpu-form').serialize();
            break;
        case 'ram':
            data = $('#selector-form,#object-form, #ram-form').serialize();
            break;
        case 'hdd':
            data = $('#selector-form,#object-form, #drive-form, #hdd-form').serialize();
            break;
        case 'ssd':
            data = $('#selector-form,#object-form, #drive-form').serialize();
            break;
        default:
            console.log(`Unknow ${currentSelected}`);
            break;
    }
    $.ajax({
        url  : './add',
        type : 'POST',
        data : data,
        success : function() {
            window.location.replace('./add');
        }
    });
}

function hideElement(elem) {
    elem.classList.add("d-none");
}

function showElement(elem) {
    elem.classList.remove("d-none");
}

function hideEveryElement() {
    hideElement(AMOVIBLE_FORM);
    hideElement(CABLE_FORM);
    hideElement(CPU_FORM);
    hideElement(HDD_FORM);
    hideElement(RAM_FORM);
    hideElement(SSD_FORM);
    hideElement(DRIVE_FORM);
}

