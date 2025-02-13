document.addEventListener('DOMContentLoaded', function() {
    var inputs = document.querySelectorAll(['input[type=text]', 'input[type=password]', 'input[type=email]', 'input[type=file]', 'input[type=url]', 'input[type=number]', 'textarea']);
    inputs.forEach(function (input) {
        input.classList.add("form-control");
    });

    var labels = document.querySelectorAll('label');
    labels.forEach(function (input) {
        input.classList.add("form-label");
    });

    var checkboxes = document.querySelectorAll('input[type=checkbox]');
    checkboxes.forEach(function (input) {
        input.classList.add("form-check-input");
    });

    var selects = document.querySelectorAll('select');
    selects.forEach(function (input) {
        input.classList.add("form-select");
    });

    var startInput = document.getElementById('id_starts');
    if (startInput) {
        startInput.type = 'datetime-local';
    } else {
        console.error("Element with ID 'id_starts' not found.");
    }

    var endInput = document.getElementById('id_ends');
    if (endInput) {
        endInput.type = 'datetime-local';
    } else {
        console.error("Element with ID 'id_ends' not found.");
    }
});