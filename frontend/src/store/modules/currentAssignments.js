import { httpClient } from "../../plugins/httpClient";

const state = {
  currentAssignments: [
    {
      id: "",
      course_code: "",
      course_name: "",
      ta_supervisor: "",
      duties_completed: "",
      comment: "",
      status: "",
      date_submitted: "",
      date_approved: "",
      due_by: ""
    }
  ]
};

const getters = {
  currentAssignments: state => state.currentAssignments
};

const mutations = {
  SET_CURRENT_ASSIGNMENTS(state, currentAssignmentList) {
    state.currentAssignments = currentAssignmentList;
  },
  ADD_CURRENT_ASSIGNMENTS(state, currentAssignments) {
    state.currentAssignments.push(...currentAssignments);
  }
};

const actions = {
  fetchUnSubmittedAssignments({ commit, dispatch }) {
    httpClient.get("api/core/feedbacks/submit/").then(response => {
      commit("SET_CURRENT_ASSIGNMENTS", response.data);
      dispatch("fetchCurrentAssignments");
    });
  },
  fetchCurrentAssignments({ commit }) {
    httpClient.get("api/core/feedbacks/current/").then(response => {
      commit("ADD_CURRENT_ASSIGNMENTS", response.data);
    });
  },
  updateCurrentAssignment({ dispatch }, { current_id, duties }) {
    httpClient
      .patch(`api/core/feedbacks/${current_id}/`, {
        duties_completed: duties,
        status: "1"
      })
      .then(() => {
        dispatch("fetchUnSubmittedAssignments");
      });
  },
  submitCurrentAssignment({ dispatch }, currentAssignment) {
    httpClient.post("api/core/feedbacks/", currentAssignment).then(() => {
      dispatch("fetchUnSubmittedAssignments");
    });
  }
};

export { state, getters, mutations, actions };
