window.onload = function (e) {
    liff.init(function (data) {
        initializeApp(data);
    });
};

function initializeApp(data) {
    $("#sendAJAX").click(function () {
        var user = data.context.userId;
        var name = $("#outputName").val();
        var email = $("#outputEmail").val();
        var facebook = $("#outputFacebook").val();
        var selfIntro = $("#outputSelfIntro").val();
        window.alert(user);
        $.ajax({
            type: "POST",
            cache: false,
            data: {
                user: user,
                name: name,
                email: email,
                facebook: facebook,
                selfIntro: selfIntro
            },
            url: "/ajax",
            dataType: "json",
            success: function (data) {
                console.log(data);
            },
            error: function (jqXHR) {
                alert("error: " + jqXHR.status);
                console.log(jqXHR);
            }
        })
        window.alert("send success");
    });
}