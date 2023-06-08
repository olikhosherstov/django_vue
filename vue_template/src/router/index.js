import { createRouter, createWebHistory } from "vue-router";
import HomeView from "@/views/HomeView.vue";
import RegistrationViewVue from "@/views/RegistrationView.vue";
import ProfileView from "@/views/ProfileView.vue";
import GreenViewVue from "@/views/GreenView.vue";
import RedViewVue from "@/views/RedView.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/registration",
    name: "registration",
    component: RegistrationViewVue,
  },
  {
    path: "/profile",
    name: "profile",
    component: ProfileView,
  },
  {
    path: "/greencort",
    name: "greencort",
    component: GreenViewVue,
  },
  {
    path: "/redcort",
    name: "redcort",
    component: RedViewVue,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
