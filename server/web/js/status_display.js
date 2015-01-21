

$(function() {
    console.log("asdf");
    var template = $('#stats_template').html()
    Mustache.parse(template);
    var rendered = Mustache.render(template, {"statistics": [
        {"display_name": "foo", "value":"bar"},
        {"display_name": "what", "value": "lol"}]})
    $('#stats_target').html(rendered);
});