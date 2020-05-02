import { httpClient } from "../../plugins/httpClient";

const state = {
  tas: [
    {
      id: "",
      roll_no: "",
      availability: 0,
      name: "",
      program: "",
      assigned_hours: ""
    }
  ]
};

const getters = {
  tas: state => selected_program => {
    if (selected_program === 1) {
      return state.tas.filter(ta => ta.program === "1");
    } else {
      return state.tas.filter(ta => ta.program === "2" || ta.program === "3");
    }
  }
};

const mutations = {
  SET_TAS(state, tas) {
    state.tas = tas;
  },
  UPDATE_ASSIGNED_HOURS(state, { taId, hours }) {
    const index = state.tas.findIndex(ta => ta.id === taId);
    state.tas[index].assigned_hours = hours;
  }
};

const actions = {
  fetchTas({ commit }) {
    httpClient.get("/api/core/assignments/assign/").then(response => {
      commit("SET_TAS", response.data);
    });
  },
  updateHours({ commit }, { taId, hours }) {
    commit("UPDATE_ASSIGNED_HOURS", { taId, hours });
  }
};

export { state, getters, mutations, actions };
