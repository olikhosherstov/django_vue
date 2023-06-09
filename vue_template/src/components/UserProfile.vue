<template>
  <div class="card">
    <h1>Профіль користувача</h1>
    <img src="img.jpg" alt="Test user" style="width: 100%" />
    <h1>{{ userProfile.first_name }} {{ userProfile.last_name }}</h1>

    <p class="title">E-mail: {{ userProfile.username }}</p>
    <p>Телефон: +38{{ userProfile.phone }}</p>
    <p>Місто: {{ userProfile.city }}</p>
    <!-- <p><button>Зберегти</button></p> -->
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      userProfile: "",
    };
  },
  methods: {
    updateProfile() {
      // Here you can implement the logic to update the user profile
      console.log("Updating profile:", this.user);
    },
  },
  async beforeMount() {
    let username = this.$store.state.userdata;
    let url =
      "http://tennisvyshneve.pythonanywhere.com/api/profile/" + username + "/";
    const config = {
      headers: {
        Authorization: "JWT " + this.$store.state.access,
      },
    };
    let response = await axios.get(url, config);
    this.userProfile = response.data;
    this.$store.commit("userProfile", response.data);
  },
};
</script>

<style scoped>
@import "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css";
.card {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  max-width: 450px;
  margin: auto;
  text-align: center;
}

.title {
  color: grey;
  font-size: 18px;
}

button {
  border: none;
  outline: 0;
  display: inline-block;
  padding: 8px;
  color: white;
  background-color: #2e39fe;
  text-align: center;
  cursor: pointer;
  width: 100%;
  font-size: 18px;
}

a {
  text-decoration: none;
  font-size: 22px;
  color: rgb(88, 99, 240);
}

button:hover,
a:hover {
  opacity: 0.7;
}
</style>
