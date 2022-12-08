//Following code handles the navigation elements and adds the events needed to change page, login and logout.
//general functions located in utility.

const startPage = select("#startPage");
const loginPage = select("#loginPage");
const authorPage = select("#authorPage");
const locationPage = select("#locationPage");

const startBtn = select("#startBtn");
const loginBtn = select("#loginBtn");
const authorBtn = select("#authorBtn");
const locationBtn = select("#locationBtn");
const logoutBtn = select("#logoutBtn");

const dynamicParagraph = select("#dynamic-paragraph"); //dynamic element embedded in text

startPage.style.display = 'flex'; //All pages are hidden as default - this displays startpage.

bindBtnPage(loginBtn, loginPage);
bindBtnPage(startBtn, startPage);
bindBtnPage(authorBtn, authorPage);
bindBtnPage(locationBtn, locationPage);
bindBtnFunc(loginBtn, signIn);
bindBtnFunc(locationBtn, refreshMap);
bindBtnFunc(logoutBtn, signOut); //creates event listeners

function loginMode() {
    loginBtn.style.display = "none";
    locationBtn.style.display = "flex";
    logoutBtn.style.display = "flex";
    select("#testModeBtn").style.display = "none"; //removes the excess functionality elements, and adds new functionality elements

    dynamicParagraph.innerHTML = `<a id="location-link">Go to location to find the home of your IP!</a>`;
    let textBtn = select("#location-link");
    bindBtnPage(textBtn, locationPage);
    bindBtnFunc(textBtn, refreshMap);   //Edits dynamic content and functionality
} 

function defaultMode() {
    loginBtn.style.display = "flex";
    locationBtn.style.display = "none";
    logoutBtn.style.display = "none";
    select("#testModeBtn").style.display = "flex"; //removes the excess functionality elements, and adds new functionality elements

    dynamicParagraph.innerHTML = `<a id="login-link">Login to find the home of your IP!</a>`
    var textBtn = select("#login-link");
    bindBtnPage(textBtn, loginPage);
    bindBtnFunc(textBtn, signIn); //Edits dynamic content and functionality
}