let hamburger = document.querySelector(".hamburger");
let profile_drop = document.querySelector(".profile-drop");
let close_ham = document.querySelector(".close-hamburger");
let login = document.querySelector("#login");
let signUp = document.querySelector("#signUp");
let profile = document.querySelector("#profile");
let logout = document.querySelector("#logout");
let login_page = document.querySelector(".login-page");
let close_login = document.querySelector(".close-login-page");
let username, email, password;
let signUp_page = document.querySelector(".sign-up-page");
let close_signUp = document.querySelector(".close-sign-up-page");
let become_host = document.querySelector(".become-host");
let become_host_page = document.querySelector(".become-host-page");
let close_host = document.querySelector(".close-become-host-page");
let create_account = document.querySelector(".create-account");
let error_login_mail = document.querySelector(".error-mail");
let error_login_password = document.querySelector(".error-password");
let error_sign_name = document.querySelector(".sign-error-name");
let error_sign_mail = document.querySelector(".sign-error-mail");
let error_sign_password = document.querySelector(".sign-error-password");

logout.addEventListener("click", () => {
  localStorage.removeItem("token");
  localStorage.removeItem("user_id");
  localStorage.removeItem("user_type");
  hamburger.style.display = "none";
  login.style.display = "flex";
  signUp.style.display = "flex";
  become_host.style.display = "flex";
  document.querySelector(".create-listings").style.display = "none";
  document.querySelector(".places-to-stay").style.display = "flex";
});

create_account.addEventListener("click", () => {
  login_page.style.display = "none";
  become_host_page.style.display = "none";
  signUp_page.style.display = "flex";
});
become_host.addEventListener("click", () => {
  become_host_page.style.display = "flex";
  hamburger.style.display = "none";
  login_page.style.display = "none";
  signUp_page.style.display = "none";
  document.querySelector("#hostUsername").value = "";
  document.querySelector("#hostMail").value = "";
  document.querySelector("#hostPassword").value = "";
});

close_host.addEventListener("click", () => {
  become_host_page.style.display = "none";
  document.querySelector("#hostUsername").value = "";
  document.querySelector("#hostMail").value = "";
  document.querySelector("#hostPassword").value = "";
});
profile_drop.addEventListener("click", () => {
  if (!localStorage.getItem("token")) {
    hamburger.style.display = "flex";
    login_page.style.display = "none";
    signUp_page.style.display = "none";
    become_host_page.style.display = "none";
    logout.style.display = "none";
    profile.style.display = "none";
    document.querySelector("#mail").value = "";
    document.querySelector("#password").value = "";
    document.querySelector("#username").value = "";
    document.querySelector("#signMail").value = "";
    document.querySelector("#signPassword").value = "";
    document.querySelector("#hostUsername").value = "";
    document.querySelector("#hostMail").value = "";
    document.querySelector("#hostPassword").value = "";
  } else {
    hamburger.style.display = "flex";
    login_page.style.display = "none";
    signUp_page.style.display = "none";
    become_host_page.style.display = "none";
    signUp.style.display = "none";
    login.style.display = "none";
    profile.style.display = "flex";
    logout.style.display = "flex";
  }
});
close_ham.addEventListener("click", () => {
  hamburger.style.display = "none";
});
login.addEventListener("click", () => {
  login_page.style.display = "flex";
  hamburger.style.display = "none";
});

signUp.addEventListener("click", () => {
  signUp_page.style.display = "flex";
  hamburger.style.display = "none";
});
close_login.addEventListener("click", () => {
  login_page.style.display = "none";
  error_login_mail.innerHTML = "";
  error_login_password.innerHTML = "";
});

close_signUp.addEventListener("click", () => {
  signUp_page.style.display = "none";
  error_sign_name.innerHTML = "";
  error_sign_mail.innerHTML = "";
  error_sign_password.innerHTML = "";
});
async function user_login(email, password) {
  const response = await fetch("http://0.0.0.0:5500/API/V1/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email: email, password: password }),
  });
  if (response.ok) {
    const data = await response.json();
    console.log(data);
    if (data.status === "invalid email") {
      error_login_mail.innerHTML = data.status;
      error_login_mail.style.display = "flex";
      error_login_password.innerHTML = "";
    } else if (data.status === "incorrect password") {
      error_login_password.innerHTML = data.status;
      error_login_password.style.display = "flex";
      error_login_mail.innerHTML = "";
    }
    if (data.token) {
      localStorage.setItem("token", data.token);
    }
    if (localStorage.getItem("token")) {
      profile.style.display = "flex";
      signUp.style.display = "none";
      login_page.style.display = "none";
      get_details(data.token);
    }
  } else {
    const data = await response.json();
    console.log(data);
  }
}

async function register(username, email, password, usertype) {
  const response = await fetch("http://0.0.0.0:5500/API/V1/register", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      username: username,
      email: email,
      password: password,
      user_type: usertype,
    }),
  });
  if (response.ok) {
    const data = await response.json();
    console.log(data);
    if (data.username || data.email || data.password) {
      error_sign_name.innerHTML = data.username;
      error_sign_name.style.display = "flex";
      error_sign_mail.innerHTML = data.email;
      error_sign_mail.style.display = "flex";
      error_sign_password.innerHTML = data.password;
      error_sign_password.style.display = "flex";
    }
    if (data.token) {
      localStorage.setItem("token", data.token);
    }
    if (localStorage.getItem("token")) {
      profile.style.display = "flex";
      signUp.style.display = "none";
      signUp_page.style.display = "none";
      get_details(data.token);
    }
  } else {
    const data = await response.json();
    console.log(data);
  }
}
async function get_details(token) {
  const response = await fetch(
    `http://0.0.0.0:5500//API/V1/get-details?token=${token}`,
    {
      method: "GET",
    }
  );
  if (response.ok) {
    console.log(response);
    const data = await response.json();
    console.log(data);
    localStorage.setItem("user_id", data.user_id);
    localStorage.setItem("user_type", data.user_type);
    if (localStorage.getItem("user_type") === "Host") {
      become_host.style.display = "none";
      document.querySelector(".create-listings").style.display = "flex";
      document.querySelector(".places-to-stay").style.display = "none";
    }
  } else {
    const data = await response.json();
    console.log(data);
  }
}

function submit_login() {
  email = document.querySelector("#mail").value;
  password = document.querySelector("#password").value;
  user_login(email, password);
  document.querySelector("#mail").value = "";
  document.querySelector("#password").value = "";
}
function submit_signUp() {
  username = document.querySelector("#username").value;
  email = document.querySelector("#signMail").value;
  password = document.querySelector("#signPassword").value;
  let usertype = "Guest";
  register(username, email, password, usertype);
  document.querySelector("#username").value = "";
  document.querySelector("#signMail").value = "";
  document.querySelector("#signPassword").value = "";
}
function submit_host() {
  username = document.querySelector("#hostUsername").value;
  email = document.querySelector("#hostMail").value;
  password = document.querySelector("#hostPassword").value;
  let usertype = "Host";
  register(username, email, password, usertype);
  become_host_page.style.display = "none";
  document.querySelector("#hostUsername").value = "";
  document.querySelector("#hostMail").value = "";
  document.querySelector("#hostPassword").value = "";
}

document.addEventListener("DOMContentLoaded",() => {
  if (localStorage.getItem("user_type") === "Host") {
    become_host.style.display = "none";
    document.querySelector(".create-listings").style.display = "flex";
    document.querySelector(".places-to-stay").style.display = "none";
  }
})