import { httpClient } from "../../plugins/httpClient";

const state = {
  pastAssignments: [
    {
      id: "",
      course_code: "",
      course_name: "",
      ta_supervisor: "",
      duties_completed: "",
      comment: "",
      status: "",
      date_submitted: "",
      date_approved: ""
    }
  ]
};

const getters = {
  pastAssignments: state => state.pastAssignments
};

const mutations = {
  SET_PAST_ASSIGNMENTS(state, pastAssignments) {
    state.pastAssignments = pastAssignments;
  }
};

const actions = {
  fetchPastAssignments({ commit }) {
    httpClient.get("api/core/feedbacks/past/").then(response => {
      commit("SET_PAST_ASSIGNMENTS", response.data);
    });
  }
};

export { state, getters, mutations, actions };
