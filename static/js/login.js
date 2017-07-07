function refreshCaptcha() {
  $.getJSON("/captcha/refresh/", {}, function(result) {
    $("input[name='captcha_0']").val(result.key);
    $("#captchaRefresh").attr("src", result.image_url);
  });
}

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
      }
    }
  }
  return cookieValue;
}

function loginFormSubmit() {
  var url = $("#loginForm").attr("action")
  var username = $("input[name='username'").val();
  var password = $("input[name='password'").val();
  var captcha_0 = $("input[name='captcha_0'").val();
  var captcha_1 = $("input[name='captcha_1'").val();
  var csrftoken = getCookie('csrftoken');
  $.ajax({
    type: "POST",
    url: url,
    contentType: "application/json",
    headers: {"X-CSRFToken": csrftoken},
    data: JSON.stringify({
      "username": username,
      "password": password,
      "captcha_0": captcha_0,
      "captcha_1": captcha_1
    }),
    success: function(result, status, xhr) {
      if (result.status == 302) {
        $(location).attr('href', result.location);
      }else {
        console.log(result)
        $("html").html(result)
//        window.location.reload()
      }
    }
  });
}


$(function() {
  $("#captchaRefresh").click(refreshCaptcha);
  $("#loginBtn").click(loginFormSubmit);
})
