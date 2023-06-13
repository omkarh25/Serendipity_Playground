// Import the functions you need from the Firebase SDKs
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getFirestore, collection, addDoc } from "firebase/firestore";

// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyD2heqi47uAbgFb1oGJKthXL565Y7NBoao",
  authDomain: "fir-674e7.firebaseapp.com",
  databaseURL: "https://fir-674e7-default-rtdb.firebaseio.com",
  projectId: "fir-674e7",
  storageBucket: "fir-674e7.appspot.com",
  messagingSenderId: "545483267403",
  appId: "1:545483267403:web:f3cbd18a060ba5bdc85cce",
  measurementId: "G-MZ8X4411MZ"
  // Your Firebase configuration details
};

firebaseConfig.initalizeApp(firebaseConfig);

// Reference messages collection
var messagesRef = firebase.database().ref('messages');
// listen for form submit
document.getElementById('contactForm').addEventListener('submit', submitForm);
//submit form
function submitForm(e){
    e.preventDefault();
    // get values
    var name = getInputVal('name');
    var company = getInputVal('company');
    var email = getInputVal('email');
    var phone = getInputVal('phone');
    var message = getInputVal('message');
    // save message
    saveMessage(name, company, email, phone, message);
    // show alert
    document.querySelector('.alert').style.display = 'block';
    // hide alert after 3 seconds
    setTimeout(function(){
        document.querySelector('.alert').style.display = 'none';
    }, 3000);
    // clear form
    document.getElementById('contactForm').reset();
}
// function to get get form values
function getInputVal(id){
    return document.getElementById(id).value;
}
// save message to firebase
function saveMessage(name, company, email, phone, message){
    var newMessageRef = messagesRef.push();
    newMessageRef.set({
        name: name,
        company: company,
        email: email,
        phone: phone,
        message: message
    });
}
