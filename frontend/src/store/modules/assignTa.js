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
  ],
  assignedTas: [
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
  },
  assignedTas: state => state.assignedTas
};

const mutations = {
  SET_TAS(state, tas) {
    state.tas = tas;
  },
  SET_ASSIGNED_TAS(state, assignedTas) {
    state.assignedTas = assignedTas;
  },
  UPDATE_ASSIGNED_HOURS(state, { taId, hours }) {
    const index = state.tas.findIndex(ta => ta.id === taId);
    state.tas[index].assigned_hours = hours;
  }
};

const actions = {
  fetchAllTas({ commit }, course_code) {
    httpClient.get(`/api/core/course-tas/${course_code}/`).then(response => {
      commit("SET_TAS", response.data);
    });
    httpClient
      .get(`/api/core/course-assigned-tas/${course_code}/`)
      .then(response => {
        commit("SET_ASSIGNED_TAS", response.data);
      });
  },
  updateHours({ commit }, { taId, hours }) {
    commit("UPDATE_ASSIGNED_HOURS", { taId, hours });
  },
  updateTas({ dispatch }, { courseId, selectedTas }) {
    selectedTas.forEach(selectedTa => {
      httpClient
        .post("/api/core/assignments/", {
          course: courseId,
          teaching_assistant: selectedTa.id,
          assigned_hours: selectedTa.assigned_hours
        })
        .then();
    });
    dispatch(
      "messages/showMessage",
      { message: "Successfully assigned TAs", color: "success" },
      { root: true }
    );
  }
};

export { state, getters, mutations, actions };
