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

const phoneNumber = document.getElementById("phoneNumber");
const email = document.getElementById("email");
const photo = document.getElementById("photo");
const shopName = document.getElementById("shopName");

const data = {
  shopName: shopName.value,
  number: phoneNumber.value,
  email: email.value,
  photo: photo.value
};

const buttonAction = document.getElementById("action");
buttonAction.addEventListener(
  "click",
  async () => await postData("http://localhost/special-shop-price", data)
);
