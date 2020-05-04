import { httpClient } from "../../plugins/httpClient";

const state = {
  feedbackCount: [
    {
      programme: "",
      submitted: "",
      approved: "",
      rejected: "",
      pending: "",
      link: ""
    }
  ]
};

const getters = {
  feedbackCount: state => state.feedbackCount
};

const mutations = {
  SET_FEEDBACK_COUNT(state, feedbackCount) {
    state.feedbackCount = feedbackCount;
  }
};

const actions = {
  fetchFeedbackCount({ commit }, { month, year }) {
    httpClient
      .get(`/api/core/feedback-count/${month}/${year}/`)
      .then(response => {
        commit("SET_FEEDBACK_COUNT", response.data);
      });
  }
};

export { state, getters, mutations, actions };
