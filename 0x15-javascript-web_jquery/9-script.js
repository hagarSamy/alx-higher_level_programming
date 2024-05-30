// The translation of “hello” must be displayed in the HTML tag DIV#hello
// ensure - the code is executed only after the DOM has been fully loaded and parsed
$(document).ready(function () {
    $.getJSON('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
      $('DIV#hello').text(data.hello);
    });
});
