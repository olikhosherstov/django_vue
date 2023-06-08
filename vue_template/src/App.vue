<template>
  <nav>
    <router-link to="/">Головна |</router-link>
    <router-link v-if="connectionTo" to="/profile"> Профіль |</router-link>
    <router-link v-if="!connectionTo" to="/registration"> Увійти |</router-link>
    <router-link to="/greencort"> Зелений корт |</router-link>
    <router-link to="/redcort"> Червоний корт</router-link>
  </nav>
  <router-view />
</template>
<script>
import { mapState } from "vuex";

export default {
  computed: {
    ...mapState(["connectionTo"]),
  },
};
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
