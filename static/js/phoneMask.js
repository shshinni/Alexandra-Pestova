window.addEventListener("DOMContentLoaded", function () {
    let phoneInput = document.getElementById("phone-input");
    phoneInput.value = null;

    let keyCode;


    }

    phoneInput.addEventListener("input", mask, false);
    phoneInput.addEventListener("focus", mask, false);
    phoneInput.addEventListener("blur", mask, false);
    phoneInput.addEventListener("keydown", mask, false);
});