async function getData(url) {
    const response = await fetch(url, {
        mode: "no-cors",
    });
    return response.json;
}

export { getData };