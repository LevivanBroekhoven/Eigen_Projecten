let Wachtwoord = "Test";                                                                       
let Username =  "User";
let Toelaten = false;

const Usernameinput = document.getElementById("Username");
const WWinput = document.getElementById("WW");


Usernameinput.addEventListener("input", function() {
    const inputValue2 = Usernameinput.value;
    console.log(inputValue2);


WWinput.addEventListener("input", function() {
    const inputValue = WWinput.value;
    console.log(inputValue);
  
    if (inputValue === Wachtwoord  && inputValue2 === Username) {
        Toelaten = true;
    } else {
        Toelaten = false;
    }
    

    if (Toelaten === true){
        window.location.href = "Achterhetww.html";
    }

})
});
