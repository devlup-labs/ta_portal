import router from "../../router";
import axios from "axios";

const state = {
  isLoggedIn: false,
  thumbnailUrl: null
};

const getters = {
  isLoggedIn: state => state.isLoggedIn,
  thumbnailUrl: state => state.thumbnailUrl
};

const mutations = {
  LOGIN(state) {
    state.isLoggedIn = true;
  },
  LOGOUT(state) {
    state.isLoggedIn = false;
  },
  SET_THUMBNAIL_URL(state, URL) {
    state.thumbnailUrl = URL;
  }
};

const actions = {
  login({ commit }) {
    commit("LOGIN");
  },
  logout({ commit }) {
    axios
      .get("/logout/")
      .then(() => {
        commit("LOGOUT");
        router.push({ name: "login" });
      })
      .catch(err => console.log(err));
  }
};

export { state, mutations, actions, getters };
