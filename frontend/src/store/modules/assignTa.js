import { httpClient } from "../../plugins/httpClient";

const state = {
  tas: [
    {
      id: "",
      roll_no: "",
      availability: 0,
      name: "",
      program: "",
      hours: ""
    }
  ]
};

const getters = {
  tas: state => state.tas
};

const mutations = {
  SET_TAS(state, tas) {
    state.tas = tas;
  }
};

const actions = {
  fetchTas({ commit }) {
    httpClient.get("/api/core/assignments/assign/").then(response => {
      commit("SET_TAS", response.data);
    });
  }
};

export { state, getters, mutations, actions };
