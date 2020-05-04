import { httpClient } from "../../plugins/httpClient";

const state = {
  taProfile: {
    id: "",
    roll_no: "",
    program: "",
    phone: "",
    alternate_phone: "",
    research_area: "",
    btech_specialization: "",
    mtech_specialization: "",
    user: ""
  },
  user: {
    first_name: "",
    last_name: "",
    email: ""
  },
  errors: []
};
const getters = {
  taProfile: state => state.taProfile,
  user: state => state.user,
  errors: state => state.errors
};

const mutations = {
  SET_TA_PROFILE(state, taProfile) {
    state.taProfile = taProfile;
  },
  SET_USER(state, user) {
    state.user = user;
  },
  SET_ERROR(state, error) {
    state.errors.push(error);
  },
  RESET_ERRORS(state) {
    state.errors = [];
  },
  SET_FIRST_NAME(state, firstName) {
    state.user.first_name = firstName;
  },
  SET_LAST_NAME(state, lastName) {
    state.user.last_name = lastName;
  },
  SET_PROGRAM(state, program) {
    state.taProfile.program = program;
  },
  SET_PHONE(state, phone) {
    state.taProfile.phone = phone;
  },
  SET_ALTERNATE_PHONE(state, alternatePhone) {
    state.taProfile.alternate_phone = alternatePhone;
  },
  SET_RESEARCH_AREA(state, researchArea) {
    state.taProfile.research_area = researchArea;
  },
  SET_BTECH_SPECIALIZATION(state, btechSpecialization) {
    state.taProfile.btech_specialization = btechSpecialization;
  },
  SET_MTECH_SPECIALIZATION(state, mtechSpecialization) {
    state.taProfile.mtech_specialization = mtechSpecialization;
  }
};

const actions = {
  fetchTaProfile({ commit }) {
    httpClient
      .get("/api/accounts/ta-profiles/current/")
      .then(response => {
        commit("SET_TA_PROFILE", response.data);
        httpClient
          .get(`/api/accounts/users/${response.data.user}/`)
          .then(response => {
            commit("SET_USER", response.data);
          })
          .catch(err => commit("SET_ERROR", err));
      })
      .catch(err => commit("SET_ERROR", err));
  },
  saveTaProfile({ commit, state, dispatch }) {
    httpClient
      .patch(`/api/accounts/users/${state.taProfile.user}/`, {
        first_name: state.user.first_name,
        last_name: state.user.last_name
      })
      .then(response => {
        commit("SET_USER", response.data);
        httpClient
          .patch(`/api/accounts/ta-profiles/${state.taProfile.id}/`, {
            phone: state.taProfile.phone,
            alternate_phone: state.taProfile.alternate_phone,
            research_area: state.taProfile.research_area,
            btech_specialization: state.taProfile.btech_specialization,
            mtech_specialization: state.taProfile.mtech_specialization
          })
          .then(response => {
            commit("SET_TA_PROFILE", response.data);
            dispatch(
              "messages/showMessage",
              { message: "Profile updated successfully", color: "success" },
              { root: true }
            );
          })
          .catch(err =>
            dispatch(
              "messages/showMessage",
              { message: err.response.data.message, color: "error" },
              { root: true }
            )
          );
      })
      .catch(err =>
        dispatch(
          "messages/showMessage",
          { message: err.response.data.message, color: "error" },
          { root: true }
        )
      );
  },

  setFirstName: ({ commit }, firstName) => commit("SET_FIRST_NAME", firstName),
  setLastName: ({ commit }, lastName) => commit("SET_LAST_NAME", lastName),
  setPhone: ({ commit }, phone) => commit("SET_PHONE", phone),
  setAlternatePhone: ({ commit }, alternatePhone) =>
    commit("SET_ALTERNATE_PHONE", alternatePhone),
  setResearchArea: ({ commit }, researchArea) =>
    commit("SET_RESEARCH_AREA", researchArea),
  setBtechSpecialization: ({ commit }, btechSpecialization) =>
    commit("SET_BTECH_SPECIALIZATION", btechSpecialization),
  setMtechSpecialization: ({ commit }, mtechSpecialization) =>
    commit("SET_MTECH_SPECIALIZATION", mtechSpecialization)
};

export { state, getters, mutations, actions };
