document.addEventListener('DOMContentLoaded', function() {
    var inputs = document.querySelectorAll(['input[type=text]', 'input[type=file]', 'input[type=url]', 'textarea']);
    inputs.forEach(function (input) {
        input.classList.add("form-control");
    })

    var labels = document.querySelectorAll('label');
    labels.forEach(function (input) {
        input.classList.add("form-label");
    })

});