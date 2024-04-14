import { postData } from "./postData.js";

export default () => {
    const phoneNumber = document.getElementById("phoneNumber");
    const email = document.getElementById("email");
    const photo = document.getElementById("photo");
    const address = document.getElementById("address");
    
    const buttonAction = document.getElementById("action");
    buttonAction.addEventListener(
      "click",
      async () => {
        const formData = new FormData();
        formData.append(photo.value, photo.files[0]);

        const data = {
          "address": address.value,
          "phone": phoneNumber.value,
          "email": email.value,
        };

        console.log(data, formData);

        await fetch("http://localhost:8000/check_social_price/file", {
          method: "POST",
          body: formData,
          mode: "no-cors",
          headers: {
            "Content-Type": "multipart/form-data"
          }
        });
        await postData("http://localhost:8000/check_social_price", data)
      },
    );
    
}