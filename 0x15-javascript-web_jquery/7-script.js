// fetches the character name from
// this URL: https://swapi-api.alx-tools.com/api/people/5/?format=json
// .getJSON() - to make an AJAX request to fetch JSON data from a server
// 2nd arg; callback finc to handle response
$.getJSON('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(data) {
    $('#character').text(data.name);
});
