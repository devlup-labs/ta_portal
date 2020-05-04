import api from "../../api";
import { httpClient } from "../../plugins/httpClient";

const state = {
  isAuthenticated: false,
  authenticating: false,
  error: null,
  thumbnailUrl: null,
  profileType: ""
};

const getters = {
  isAuthenticated: state => state.isAuthenticated,
  authenticating: state => state.authenticating,
  error: state => state.error,
  thumbnailUrl: state => state.thumbnailUrl,
  profileType: state => state.profileType
};

const mutations = {
  LOGIN_BEGIN(state) {
    state.authenticating = true;
    state.error = null;
  },
  LOGIN_FAILURE(state, error) {
    state.authenticating = false;
    state.error = error;
  },
  LOGIN_SUCCESS(state) {
    state.authenticating = false;
    state.error = null;
    state.isAuthenticated = true;
  },
  LOGOUT(state) {
    state.isAuthenticated = false;
  },
  SET_THUMBNAIL_URL(state, URL) {
    state.thumbnailUrl = URL;
  },
  SET_PROFILE_TYPE(state, profileType) {
    state.profileType = profileType;
  }
};

const actions = {
  login({ commit, dispatch }, { email, password }) {
    commit("LOGIN_BEGIN");
    return api
      .login(email, password)
      .then(() => commit("LOGIN_SUCCESS"))
      .catch(err => {
        commit("LOGIN_FAILURE", err.response.data.message);
        dispatch(
          "messages/showMessage",
          { message: "Enter Email or Password Correctly", color: "error" },
          { root: true }
        );
      });
  },
  logout({ commit }) {
    return api.logout().then(() => {
      commit("LOGOUT");
    });
  },
  checkAuthentication({ commit }) {
    return api.authCheck().then(() => commit("LOGIN_SUCCESS"));
  },
  fetchProfileType({ commit }) {
    httpClient.get("/api/accounts/users/profile/").then(response => {
      commit("SET_PROFILE_TYPE", response.data.type);
    });
  }
};

export { state, mutations, actions, getters };
