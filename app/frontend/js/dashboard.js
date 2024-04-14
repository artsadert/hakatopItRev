import { getData } from "./getData.js";

export default () => {
    document.addEventListener("DOMContentLoaded", async () => {
        if (prompt("Введите пароль", "") !== "14231423") return;

        const pricesList = await getData("http://localhost:8000/admin");
        const divPricesList = document.getElementById("pricesList");

        for (let i = 0; i < pricesList.length; i++) {
          const currentPrice = JSON.parse(pricesList[i]);
          console.log(currentPrice);
          const address = currentPrice[0][0];
          const phone = currentPrice[0][1];
          const email = currentPrice[0][2];

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
}

  