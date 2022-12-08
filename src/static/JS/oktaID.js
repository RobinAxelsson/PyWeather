//The following adds the Okta Identification feature to the web-app but the 
//general functions located in utility.

const loginAddress = select("#loginAddress"); //the element in the navbar that displays your address at login

oktaSignIn = new OktaSignIn({   //the oktaSignIn-object contains all the functionality needed for the identification service
    baseUrl: 'https://dev-34426554.okta.com/',
    clientId: '0oa7d2j7dMdzbChTQ5d6',
    redirectUri: 'http://127.0.0.1:8080',
    authParams: {
        issuer: 'https://dev-34426554.okta.com/oauth2/default',
        responseType: ['token', 'id_token'],
        display: 'page'
    },
    features: {
        registration: true
    }
}); 

oktaSignIn.session.get(function (res) {      //Checks the login status at every page load and adjusts mode accordingly.
    if (res.status === 'ACTIVE') {
        loginAddress.innerHTML = res.login;
        window.location.hash = '';
        loginMode();
    } else {
        defaultMode();
    }
});

function signIn() {
        oktaSignIn.renderEl({      //renders the login form at loginBtn press
                    el: '#okta-login-container'
                },
                function success(res) {
                    console.log(res);
                },
                function error(err) {
                    console.error(err);
                }
            );
}

function signOut() {
    oktaSignIn.signOut();
    oktaSignIn.session.close();
    loginAddress.innerHTML = "";
    jumpToPage(startPage);
    defaultMode();
}