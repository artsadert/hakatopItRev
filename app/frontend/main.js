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

async function getData(url) {
  const response = await fetch(url, {
    method: "GET",
    mode: "cors",
    cache: "no-cache",
    credentials: "same-origin",
    headers: {
      "Content-Type": "application/json",
    },
    redirect: "follow",
    referrerPolicy: "no-referrer",
  });
  return response.json();
}

const phoneNumber = document.getElementById("phoneNumber");
const email = document.getElementById("email");
const photo = document.getElementById("photo");
const address = document.getElementById("address");

const data = {
  address: address.value,
  number: phoneNumber.value,
  email: email.value,
  photo: photo.value,
};

const buttonAction = document.getElementById("action");
buttonAction.addEventListener(
  "click",
  async () => await postData("http://localhost/special_shop_price"),
  data
);

document.addEventListener("DOMContentLoaded", async () => {
  if (prompt("Введите пароль", "") !== "14231423") return;

  const pricesList = await getData("http://localhost/admin");
  const divPricesList = document.getElementById("pricesList");

  const currentPrice = JSON.parse(pricesList[i]);

  const address = currentPrice[0][0];
  const phone = currentPrice[0][1];
  const email = currentPrice[0][2];
  const photo = currentPrice[0][4].filename;

  for (let i = 0; i < pricesList.length; i++) {
    divPricesList.innerHTML += `
      <div class="flex flex-col items-center">
        <img src="${photo}" alt="">
        <h3 class="block text-black text-md font-bold mb-2">${address}</h3>
        <p class="block text-black text-sm mb-2">${email}</p>
        <p class="block text-black text-sm mb-2">${phone}</p>
      </div>
    `;
  }
});
