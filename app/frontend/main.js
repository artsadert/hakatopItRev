async function postData(url = "", data = {}) {
  const response = await fetch(url, {
    method: "POST",
    mode: "cors",
    cache: "no-cache",
    credentials: "same-origin",
    headers: {
      "Content-Type": "application/json",
    },
    redirect: "follow",
    referrerPolicy: "no-referrer",
    body: JSON.stringify(data),
  });
  return response.json();
}

const iphoneNumber = document.getElementById("iphone-number");
const email = document.getElementById("email");
const dataVerification = {
  number: iphoneNumber.value,
  email: email.value,
};
postData('http://localhost/auth', dataVerification);
