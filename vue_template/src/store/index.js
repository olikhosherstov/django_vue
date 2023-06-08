import { createStore } from "vuex";

export default createStore({
  state: {
    connectionTo: false,
    userdata: "",
    userProfile: {},
    access: "",
    refresh: "",
  },
  getters: {},
  mutations: {
    connectionTo(state, jwtData) {
      state.connectionTo = true;
      state.access = jwtData.access;
      state.refresh = jwtData.refresh;
    },
    saveUserdata(state, userdata) {
      console.log("Save userdata in state:", userdata);
      state.userdata = userdata;
    },
    username(state, username) {
      state.userdata = username;
    },
    userProfile(state, userProfile) {
      state.userProfile = userProfile;
    },
  },
  actions: {},
  modules: {},
});
