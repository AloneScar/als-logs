$(function () {
    $("#input").css("height", $(window).height() - 113)
})

$(window).resize(function () {
    $('#input').css("height", $(window).height() - 113)
})

$("#input").on("keyup blur", function (event) {
    $(".markdown-body").html(marked.parse(input.val()));
});