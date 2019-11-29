window.onload = function (e) {
    liff.init(function (data) {
        initializeApp(data);
    });
    $("#sendAJAX").click(function () {
        var user = "lole";
        var name = $("#outputName").val();
        var email = $("#outputEmail").val();
        var facebook = $("#outputFacebook").val();
        var selfIntro = $("#outputSelfIntro").val();
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
            url: "/signup",
            dataType: "json",
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