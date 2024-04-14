import action from "./action.js";
import dashboard from "./dashboard.js";

const pathName = window.location.pathname.split("/").at(-1);

if (pathName === "index.html") action();
else if (pathName === "dashboard.html") dashboard();

