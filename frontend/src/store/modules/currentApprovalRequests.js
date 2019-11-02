import { httpClient } from "../../plugins/httpClient";

const state = {
  currentApprovals: [
    {
      id: "",
      course_code: "",
      name: "",
      roll_no: "",
      duties_completed: "",
      comment: "",
      date_submitted: ""
    }
  ],
  courses: [
    {
      id: "",
      name: "",
      code: "",
      supervisor: ""
    }
  ],
  currentCourse: ""
};

const getters = {
  currentApprovals(state) {
    return state.currentApprovals.filter(
      currentApproval => currentApproval.course_code === state.currentCourse
    );
  },
  courses: state => state.courses
};

const mutations = {
  SET_CURRENT_APPROVALS(state, currentApprovals) {
    state.currentApprovals = currentApprovals;
  },
  SET_COURSES(state, courses) {
    state.courses = courses;
  },
  SET_CURRENT_COURSE(state, currentCourse) {
    state.currentCourse = currentCourse;
  }
};

const actions = {
  fetchCurrentApprovals({ commit }) {
    httpClient.get("api/core/feedbacks/approval_current/").then(response => {
      commit("SET_CURRENT_APPROVALS", response.data);
    });
  },
  fetchCourses({ commit }) {
    httpClient.get("api/core/courses/current/").then(response => {
      commit("SET_COURSES", response.data);
    });
  },
  setCurrentCourse({ commit }, currentCourse) {
    commit("SET_CURRENT_COURSE", currentCourse);
  },
  addComment({ dispatch }, { id, comment }) {
    httpClient
      .patch(`api/core/feedbacks/${id}/`, {
        comment: comment
      })
      .then(() => {
        dispatch("fetchCurrentApprovals");
      });
  },
  changeStatus({ dispatch }, { currentApprovals, status }) {
    currentApprovals.forEach(currentApproval => {
      httpClient
        .patch(`api/core/feedbacks/${currentApproval.id}/`, {
          status: status
        })
        .then();
    });
    dispatch("fetchCurrentApprovals");
  }
};

export { state, getters, mutations, actions };
