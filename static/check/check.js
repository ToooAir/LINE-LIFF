window.onload = function (e) {
    liff.init(function (data) {
        initializeApp(data);
    });
};

function initializeApp(data) {
    var user = data.context.userId;
    $.ajax({
        type: "POST",
        cache: false,
        data: {
            user: user,
        },
        url: "/getNumber",
        dataType: "json",
        success: function (response) {
            alert(response);
            $("#number").text(response);
            console.log(response);
        },
        error: function (jqXHR) {
            alert("error: " + jqXHR.responseText);
            console.log(jqXHR);
        }
    })
}