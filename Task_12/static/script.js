// Simple form validation and enhancement
document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector(".prediction-form");
  const inputs = document.querySelectorAll("input");

  // Add input validation
  inputs.forEach((input) => {
    input.addEventListener("input", function () {
      validateInput(this);
    });

    input.addEventListener("blur", function () {
      validateInput(this);
    });
  });

  function validateInput(input) {
    const value = input.value;
    const name = input.name;

    // Remove previous error styling
    input.classList.remove("error");

    // Basic validation rules
    if (value === "") return; // Allow empty for now, required will handle

    switch (name) {
      case "pregnancies":
        if (value < 0 || value > 20) {
          input.classList.add("error");
        }
        break;
      case "glucose":
        if (value < 0 || value > 200) {
          input.classList.add("error");
        }
        break;
      case "blood_pressure":
        if (value < 0 || value > 200) {
          input.classList.add("error");
        }
        break;
      case "skin_thickness":
        if (value < 0 || value > 100) {
          input.classList.add("error");
        }
        break;
      case "insulin":
        if (value < 0 || value > 1000) {
          input.classList.add("error");
        }
        break;
      case "bmi":
        if (value < 0 || value > 70) {
          input.classList.add("error");
        }
        break;
      case "diabetes_pedigree":
        if (value < 0 || value > 3) {
          input.classList.add("error");
        }
        break;
      case "age":
        if (value < 0 || value > 120) {
          input.classList.add("error");
        }
        break;
    }
  }

  // Form submission enhancement
  form.addEventListener("submit", function (e) {
    let hasErrors = false;
    inputs.forEach((input) => {
      if (
        input.classList.contains("error") ||
        (input.hasAttribute("required") && input.value === "")
      ) {
        hasErrors = true;
      }
    });

    if (hasErrors) {
      e.preventDefault();
      alert(
        "Please correct the highlighted fields and fill in all required information."
      );
    }
  });
});
