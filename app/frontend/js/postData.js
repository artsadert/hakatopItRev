async function postData(url = "", data = {}) {
    const response = await fetch(url, {
      method: "POST",
      mode: "no-cors",
      body: JSON.stringify(data),
    });
    
    return response.json;
  }

export { postData };