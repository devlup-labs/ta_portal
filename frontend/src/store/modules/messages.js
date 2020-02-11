const state = {
  snackbar: false,
  message: "Test message",
  color: "info",
  timeout: 3000,
  mode: ""
};

const getters = {
  snackbar: state => state.snackbar,
  message: state => state.message,
  color: state => state.color,
  timeout: state => state.timeout,
  mode: state => state.mode
};

const mutations = {
  RESET_MESSAGE(state, { message, color, timeout, mode }) {
    state.message = message;
    state.color = color || "info";
    state.timeout = timeout || 5000;
    state.mode = mode || "";
    state.snackbar = true;
  },
  SET_SNACKBAR(state, value) {
    state.snackbar = value;
  }
};

const actions = {
  showMessage({ commit }, { message, color, timeout, mode }) {
    if (message != null) {
      commit("RESET_MESSAGE", { message, color, timeout, mode });
    } else {
      console.log("Nothing to show in snackbar!");
    }
  }
};

export { state, getters, mutations, actions };
