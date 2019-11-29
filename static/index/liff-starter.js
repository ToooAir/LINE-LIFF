window.onload = function (e) {
    liff.init(function (data) {
        initializeApp(data);
    });
};

function initializeApp(data) {
    // todo line is logged in or not
    var user = data.context.userId;
    getStatus(user);
    singUp(user);
}

function getStatus(user){
    $.ajax({
        type: "POST",
        cache: false,
        data: {
            user: user,
        },
        url: "/getStatus",
        dataType: "json",
        success: function (response) {
            $("#outputName").val(response["name"]);
            $("#outputEmail").val(response["email"]);
            $("#outputFacebook").val(response["facebook"]);
            $("#outputSelfIntro").val(response["intro"]);
            $("#status").text(response["status"]);
            console.log(response);
        },
        error: function (jqXHR) {
            alert("error: " + jqXHR.responseText);
            console.log(jqXHR);
        }
    })
}

function singUp(user){
    $("#sendAJAX").click(function () {
        data = new FormData($("#myform")[0]);
        data.append("user",user);
        window.alert(user);
        $.ajax({
            type: "POST",
            cache: false,
            data: data,
            url: "/signup",
            dataType: "formData",
            processData: false,
            contentType: false,
            success: function (data) {
                alert(data);
                console.log(data);
            },
            error: function (jqXHR) {
                alert("error: " + jqXHR.responseText);
                console.log(jqXHR);
            }
        })
    });
}