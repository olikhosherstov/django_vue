<template>
  <div v-if="LoginFormAppear">
    <LoginForm />
    <a href="#" @click="toRegistration" class="styled-link">Реєстрація</a>
  </div>
  <div
    v-else
    style="
      max-width: 500px;
      margin-left: auto;
      margin-right: auto;
      padding: 15px;
    "
  >
    <h1>Форма реєстрації на сервісі</h1>

    <form @submit="submitFormRegistration">
      <div class="text-field">
        <label class="text-field__label" for="firstname">Ім'я*</label>
        <input
          class="text-field__input"
          type="text"
          name="firstname"
          id="firstname"
          v-model="firstname"
          required
        />
        <div class="text-field__message"></div>
      </div>
      <div class="text-field">
        <label class="text-field__label" for="lastname">Прізвище*</label>
        <input
          class="text-field__input"
          type="text"
          name="lastname"
          id="lastname"
          v-model="lastname"
          required
        />
        <div class="text-field__message"></div>
      </div>
      <div class="text-field">
        <label class="text-field__label" for="email">Email*</label>
        <input
          class="text-field__input"
          type="email"
          name="email"
          id="email"
          v-model="email"
          required
        />
        <div class="text-field__message"></div>
      </div>
      <div class="radio-button__group">
        <input
          id="radio-1"
          name="gender"
          type="radio"
          value="Чоловік"
          checked
        />
        <label for="radio-1" class="radio-label">Чоловіки</label>
        <input id="radio-2" name="gender" type="radio" value="Жінка" />
        <label for="radio-2" class="radio-label">Жінки</label>
      </div>
      <div class="text-field">
        <label class="text-field__label" for="city">Місто</label>
        <input
          class="text-field__input"
          type="text"
          name="city"
          id="city"
          v-model="city"
          required
        />
        <div class="text-field__message"></div>
      </div>
      <div class="text-field">
        <label class="text-field__label" for="number"
          >Номер телефону, цифри після +38</label
        >
        <input
          class="text-field__input"
          type="text"
          name="phone"
          id="tenDigitsInput"
          maxlength="10"
          @input="validateTenDigits()"
          v-model="phone"
          required
        />
        <div class="text-field__message"></div>
      </div>
      <div class="text-field">
        <label class="text-field__label" for="photo">Завантаження фото</label>
        <input
          class="text-field__input"
          type="file"
          ref="fileInput"
          @change="handleFileChange"
          name="photo"
          id="photo"
          required
        />
        <div class="text-field__message"></div>
      </div>
      <div class="text-field">
        <label class="text-field__label" for="password">Пароль</label>
        <input
          class="text-field__input"
          type="password"
          name="pwd"
          id="pwd"
          v-model="password"
          required
        />
        <div class="text-field__message"></div>
      </div>
      <button @click="registrationEvent">Зареєструватись</button>
    </form>
    <br />
    <a href="#" @click="toLogin" class="styled-link">Увійти</a>
  </div>
</template>

<script>
import LoginForm from "@/components/LoginForm.vue";
import { mapMutations } from "vuex";
import axios from "axios";

export default {
  name: "RegistrationView",
  components: { LoginForm },
  data() {
    return {
      LoginFormAppear: true,
      firstname: "",
      lastname: "",
      email: "",
      city: "",
      phone: "",
      file: null,
      password: "",
    };
  },
  methods: {
    ...mapMutations(["saveUserdata"]),
    displayRadioValue() {
      var element = document.getElementsByName("gender");
      var resultValue;
      for (var i = 0; i < element.length; i++) {
        if (element[i].checked) {
          resultValue = element[i].value;
        }
      }
      return resultValue;
    },
    submitFormRegistration(event) {
      event.preventDefault();
      if (event.target.checkValidity() && this.isValidFile()) {
        console.log("Form submitted");
        const formData = new FormData();
        formData.append("first_name", this.firstname);
        formData.append("last_name", this.lastname);
        formData.append("username", this.email);
        formData.append("city", this.city);
        formData.append("gender", this.displayRadioValue());
        formData.append("phone", this.phone);
        formData.append("photo", this.file);
        formData.append("password", this.password);
        //Send form data to api endpoint
        axios
          .post("http://tennisvyshneve.pythonanywhere.com/api/register/", formData)
          .then((response) => {
            console.log("Form submitted successfully", response.data);
            this.LoginFormAppear = true;
            // Handle response
          })
          .catch((error) => {
            console.error("Error submitting form", error);
            // Handle error
          });
        //Mock object to save userdata
        // var userdata = {
        //   firstname: this.firstname,
        //   lastname: this.lastname,
        //   email: this.email,
        //   city: this.city,
        //   gender: this.displayRadioValue(),
        //   phone: this.phone,
        //   password: this.password,
        // };
        // this.saveUserdata(userdata);
        // this.LoginFormAppear = true;
      } else {
        alert("Перевірте правильність вводу даних");
        console.log("Form validation failed");
      }
    },
    handleFileChange(event) {
      this.file = event.target.files[0];
    },
    isValidFile() {
      if (this.file) {
        const allowedExtensions = ["jpg", "jpeg", "png"]; // Допустимі розширення файлів
        const fileExtension = this.file.name.split(".").pop().toLowerCase();
        return allowedExtensions.includes(fileExtension);
      }
      return false;
    },
    toRegistration() {
      this.LoginFormAppear = false;
    },
    toLogin() {
      this.LoginFormAppear = true;
    },
    validateTenDigits() {
      const inputsDigits = document.getElementById("tenDigitsInput");
      if (inputsDigits) {
        const value = inputsDigits.value.replace(/\D/g, ""); // Remove non-digit characters
        inputsDigits.value = value.slice(0, 10); // Limit the input to 9 digits
      }
    },
  },
};
</script>

<style scoped>
*,
*::before,
*::after {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue",
    Arial, "Noto Sans", "Liberation Sans", sans-serif, "Apple Color Emoji",
    "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
  font-size: 1rem;
  font-weight: 400;
  line-height: 1.5;
  color: #212529;
  background-color: #fff;
  -webkit-text-size-adjust: 100%;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}

h1 {
  font-size: 1.25rem;
  font-weight: 500;
}

p {
  font-weight: 500;
}

/* text field */
.text-field {
  margin-bottom: 1rem;
}

.text-field__label {
  display: block;
  margin-bottom: 0.25rem;
}

.text-field__input {
  display: block;
  width: 100%;
  height: calc(2.25rem + 2px);
  padding: 0.375rem 0.75rem;
  font-family: inherit;
  font-size: 1rem;
  font-weight: 400;
  line-height: 1.5;
  color: #212529;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid #bdbdbd;
  border-radius: 0.25rem;
  transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
}

.text-field__input::placeholder {
  color: #212529;
  opacity: 0.4;
}

.text-field__input:focus {
  color: #212529;
  background-color: #fff;
  border-color: #bdbdbd;
  outline: 0;
  box-shadow: 0 0 0 0.2rem rgba(158, 158, 158, 0.25);
}

.text-field__input:disabled,
.text-field__input[readonly] {
  background-color: #f5f5f5;
  opacity: 1;
}

/* is invalid */
.text-field__input_invalid,
.text-field__input_valid {
  border-color: #dc3545;
  padding-right: 2.25rem;
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 12 12' width='12' height='12' fill='none' stroke='%23dc3545'%3e%3ccircle cx='6' cy='6' r='4.5'/%3e%3cpath stroke-linejoin='round' d='M5.8 3.6h.4L6 6.5z'/%3e%3ccircle cx='6' cy='8.2' r='.6' fill='%23dc3545' stroke='none'/%3e%3c/svg%3e");
  background-repeat: no-repeat;
  background-position: right 0.5625rem center;
  background-size: 1.125rem 1.125rem;
}

.text-field__input_valid {
  border-color: #198754;
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 8 8'%3e%3cpath fill='%23198754' d='M2.3 6.73L.6 4.53c-.4-1.04.46-1.4 1.1-.8l1.1 1.4 3.4-3.8c.6-.63 1.6-.27 1.2.7l-4 4.6c-.43.5-.8.4-1.1.1z'/%3e%3c/svg%3e");
}

.text-field__input_invalid:focus {
  border-color: #dc3545;
  box-shadow: 0 0 0 0.25rem rgba(220, 53, 69, 0.25);
}

.text-field__input_valid:focus {
  border-color: #198754;
  box-shadow: 0 0 0 0.25rem rgb(25 135 84 / 25%);
}

.text-field__message {
  display: none;
  width: 100%;
  margin-top: 0.25rem;
  font-size: 0.875rem;
  color: #dc3545;
}

.text-field__input_valid ~ .text-field__message {
  color: #198754;
}

.text-field__input_invalid ~ .text-field__message,
.text-field__input_valid ~ .text-field__message {
  display: block;
}

button {
  display: inline-block;
  font-weight: 400;
  line-height: 1.5;
  color: #fff;
  text-align: center;
  text-decoration: none;
  vertical-align: middle;
  cursor: pointer;
  -webkit-user-select: none;
  -moz-user-select: none;
  user-select: none;
  background-color: #0d6efd;
  border: 1px solid #0d6efd;
  padding: 0.375rem 0.75rem;
  font-size: 1rem;
  border-radius: 0.25rem;
  transition: background-color 0.15s ease-in-out;
}

button:hover {
  color: #fff;
  background-color: #0b5ed7;
  border-color: #0a58ca;
}

.styled-link {
  color: #0f7afc;
  text-decoration: none;
  border-bottom: 1px solid;
  border-bottom-color: rgba(15, 122, 252, 0.2);
  transition: border-color 0.3s ease-in-out;
}

.styled-link:hover {
  text-decoration: none;
  color: #cf0000;
  border-bottom-color: rgba(208, 64, 0, 0.2);
}

.styled-link:visited {
  text-decoration: none;
  color: #800080;
  border-bottom-color: rgba(128, 0, 128, 0.2);
}

.radio-button__group {
  padding: 3px;
  margin: 10px;
}
</style>
