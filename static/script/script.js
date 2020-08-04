

function goBack() {
  window.history.back();
}

function logout() {
  var r = confirm("Are you sure you want to logout");
  if (r == true) {
    window.location.replace("http://127.0.0.1:5000/gear");
  } else {
    window.location.replace("http://127.0.0.1:5000/");
  }
}
