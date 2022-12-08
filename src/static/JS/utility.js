//Following code abstracts away some of the logic and is used in the other javascript files.
//The functions are aimed to shorten code and adding a layer of error checking.

function select(element) {
    if (document.querySelector(element) !== null) {
        return document.querySelector(element);
    } else {
        console.error('select(element): ' + element + ' is not found!');
        return null;
    }
}

function isPage(page) {
    if (page.classList.contains("page"))
        return true;
    else {
        console.error("Following element is not a page");
        console.log(page);
        return false;
    }
}

function hideAllPages() {
    document.querySelectorAll(".page").forEach(page => {
        page.style.display = "none";
    });
}

function bindBtnPage(btn, page) {
    if (isPage(page) && btn !== null) {
        btn.addEventListener("click", event => {
            event.preventDefault;
            hideAllPages();
            page.style.display = "flex";
        });
    }
    else
        console.error("error page-binding")
}

function bindBtnFunc(btn, func) {
    if (btn !== null && func !== null) {
        btn.addEventListener("click", event => {
            event.preventDefault;
            func();
        });
    }
    else
        console.error("Btn element or func is null");
}

function jumpToPage(page) {
    if(isPage(page)){
        hideAllPages();
        page.style.display = "flex";
    }
}