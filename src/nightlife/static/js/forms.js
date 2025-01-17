document.addEventListener('DOMContentLoaded', function() {
    var inputs = document.querySelectorAll(['input[type=text]', 'input[type=password]', 'input[type=email]', 'input[type=file]', 'input[type=url]', 'input[type=number]', 'textarea']);
    inputs.forEach(function (input) {
        input.classList.add("form-control");
    })

    var labels = document.querySelectorAll('label');
    labels.forEach(function (input) {
        input.classList.add("form-label");
    })

    var checkboxes = document.querySelectorAll('input[type=checkbox]');
    checkboxes.forEach(function (input) {
        input.classList.add("form-check-input");
    })

    document.getElementById('id_starts').type = 'datetime-local';
    document.getElementById('id_ends').type = 'datetime-local';

});