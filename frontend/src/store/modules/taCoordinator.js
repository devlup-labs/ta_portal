import { httpClient } from "../../plugins/httpClient";

const state = {
  courseList: [
    {
      id: "",
      supervisor_name: "",
      assigned_ta: 0,
      name: "",
      code: "",
      tas_required: 0
    }
  ]
};

const getters = {
  courseList: state => state.courseList
};

const mutations = {
  SET_COURSE_LIST(state, courseList) {
    state.courseList = courseList;
  }
};

const actions = {
  fetchCourseList({ commit }) {
    httpClient.get("/api/core/courses/").then(response => {
      commit("SET_COURSE_LIST", response.data);
    });
  }
};

export { state, getters, mutations, actions };
