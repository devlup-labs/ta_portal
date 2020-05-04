import { httpClient } from "../../plugins/httpClient";

const state = {
  tas: [
    {
      id: "",
      roll_no: "",
      availability: 0,
      name: "",
      program: "",
      assigned_hours: 0
    }
  ],
  assignedTas: [
    {
      id: "",
      roll_no: "",
      availability: 0,
      name: "",
      program: "",
      assigned_hours: 0
    }
  ]
};

const getters = {
  tas: state => selectedProgram => {
    if (selectedProgram === 1) {
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
    const taIndex = state.tas.findIndex(ta => ta.id === taId);
    state.tas[taIndex].assigned_hours = hours;
    const assignedTaIndex = state.assignedTas.findIndex(ta => ta.id === taId);
    if (assignedTaIndex !== -1)
      state.assignedTas[assignedTaIndex].assigned_hours = hours;
  }
};

const actions = {
  fetchAllTas({ commit }, courseCode) {
    httpClient.get(`/api/core/course-tas/${courseCode}/`).then(response => {
      commit("SET_TAS", response.data);
    });
    httpClient
      .get(`/api/core/course-assigned-tas/${courseCode}/`)
      .then(response => {
        commit("SET_ASSIGNED_TAS", response.data);
      });
  },
  updateHours({ commit }, { taId, hours }) {
    commit("UPDATE_ASSIGNED_HOURS", { taId, hours });
  },
  updateTas({ dispatch }, { course, selectedTas }) {
    selectedTas.forEach(selectedTa => {
      httpClient
        .post("/api/core/assignments/", {
          course: course.id,
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
