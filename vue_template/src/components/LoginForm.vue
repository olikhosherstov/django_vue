<template>
  <div
    style="
      max-width: 500px;
      margin-left: auto;
      margin-right: auto;
      padding: 15px;
    "
  >
    <!-- <h1>Вхід</h1> -->
    <form @submit="submitForm">
      <div class="text-field">
        <label class="text-field__label" for="email">Email*</label>
        <input
          class="text-field__input"
          type="email"
          name="email"
          id="email"
          v-model="emaillogin"
          required
        />
        <div class="text-field__message"></div>
      </div>
      <div class="text-field">
        <label class="text-field__label" for="password">Пароль</label>
        <input
          class="text-field__input"
          type="password"
          name="password"
          id="password"
          minlength="4"
          maxlength="8"
          v-model="password"
          required
        />
        <div class="text-field__message"></div>
      </div>
      <button type="submit">Вхід</button>
    </form>
  </div>
</template>

<script>
import { mapState, mapMutations } from "vuex";
import axios from "axios";
export default {
  name: "LoginForm",
  data() {
    return {
      emaillogin: "",
      password: "",
    };
  },
  computed: {
    ...mapState(["userdata"]),
  },
  methods: {
    ...mapMutations(["connectionTo"]),
    submitForm(event) {
      event.preventDefault();
      if (event.target.checkValidity()) {
        var loginDetails = {
          username: this.emaillogin,
          password: this.password,
        };
        //Send form to api endpoint
        axios
          .post(
            "https://tennisvyshneve.pythonanywhere.com/api/token/",
            loginDetails
          )
          .then((response) => {
            console.log("Form submitted successfully", response.data);
            this.$store.commit("username", this.emaillogin);
            this.$store.commit("connectionTo", response.data);
            this.$router.push("profile");
            // Handle response
          })
          .catch((error) => {
            console.error("Error submitting form", error);
            alert("Логін або пароль неправильні.");
            // Handle error
          });
      } else {
        console.log("Form validation failed");
      }
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
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
</style>
