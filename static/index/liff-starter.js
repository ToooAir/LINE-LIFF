document.getElementById('sendAJAX').addEventListener('click', function () {
    user = liff.getProfile().userId
    var name = $('#outputName').val();
    var email = $('#outputEmail').val();
    var facebook = $('#outputFacebook').val();
    window.alert(user);
    $.ajax({
        type: "POST",
        cache: false,
        data: {
            user: profile.userId,
            name: name,
            email: email,
            Facebook: facebook
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