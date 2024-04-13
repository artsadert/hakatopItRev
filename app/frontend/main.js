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

const iphoneNumber = document.getElementById("phoneNumber");
const email = document.getElementById("email");
const dataVerification = {
  number: iphoneNumber.value,
  email: email.value,
};

const buttonVerf = document.getElementById("verf");
buttonVerf.addEventListener("click", async () => {
  try {
    await postData("http://localhost/auth", dataVerification);
    document.cookie = `${iphoneNumber.value}=${email.value}`;
  } catch (e) {
    console.log(e);
  } finally {
    window.location.pathname = "./action.html";
  }
});

const photo = document.getElementById("photo");
const shopName = document.getElementById("shopName");
const dataAction = {
  photo: photo.value,
  shopName: shopName.value,
};

const buttonAction = document.getElementById("action");
buttonAction.addEventListener(
  "click",
  async () => await postData("http://localhost/special-shop-price", dataAction)
);
