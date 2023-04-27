const dayOfWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
const monthOfYear = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];

const today = new Date();
const year = today.getFullYear();

document.write(`<br>${dayOfWeek[today.getDay()]}, ${monthOfYear[today.getMonth()]} ${today.getDate()}, ${year}`);