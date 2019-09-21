import api from "../../api";

const state = {
  isAuthenticated: false,
  authenticating: false,
  error: null,
  thumbnailUrl: null
};

const getters = {
  isAuthenticated: state => state.isAuthenticated,
  authenticating: state => state.authenticating,
  error: state => state.error,
  thumbnailUrl: state => state.thumbnailUrl
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
  }
};

const actions = {
  login({ commit }, { email, password }) {
    commit("LOGIN_BEGIN");
    return api
      .login(email, password)
      .then(() => commit("LOGIN_SUCCESS"))
      .catch(err => commit("LOGIN_FAILURE", err.response.data.message));
  },
  logout({ commit }) {
    return api
      .logout()
      .then(() => {
        commit("LOGOUT");
      });
  },
  checkAuthentication({ commit }) {
    return api.authCheck().then(() => commit("LOGIN_SUCCESS"));
  }
};

export { state, mutations, actions, getters };
