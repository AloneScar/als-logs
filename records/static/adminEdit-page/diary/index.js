$(function () {
    $(".input").css("height", $(window).height() - $(".others").height() - 79)
    $(".markdown-body").css("height", $(window).height() - $(".others").height() - 79)
})

$(window).resize(function () {
    $(".input").css("height", $(window).height() - $(".others").height() - 79)
    $(".markdown-body").css("height", $(window).height() - $(".others").height() - 79)
})

$(".input").on("keyup blur", function () {
    $(".markdown-body").html(marked.parse($(".input").val()));
});

$(".input").on("scroll", function () {
    $(".markdown-body").scrollTop($(".input").scrollTop())
})

function commit() {
    let data = {}
    let attributes = []
    const inputs = $('input')
    // console.log(inputs);
    for (let index = 0; index < inputs.length; index++) {
        const input = $(inputs[index]);
        if (input.val().trim() === '') {
            swal('Please set your ' + input.attr('placeholder'))
            return
        }
        attributes.push(input.val())
    }
    if ($('.input').val().trim() === '') {
        swal('Please write your text')
        return
    }
    data.text = $('input').val()
    data.attributes = attributes
    console.log(JSON.stringify(data));
    $.post({
        url: '/admin/edit/diary',
        data: JSON.stringify(data),
        success: (data) => {
            console.log(data);
            if (data === 'true') swal('Committed successfully')
            else swal('Committed failed')
        }
    })
}