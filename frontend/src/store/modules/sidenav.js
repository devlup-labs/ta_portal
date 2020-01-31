const state = {
  items: [
    { heading: "TA Assignments" },
    {
      icon: "mdi-notebook",
      text: "Current",
      name: "current",
      profileType: "ta"
    },
    { icon: "mdi-notebook", text: "Past", name: "past", profileType: "ta" },
    {
      icon: "mdi-notebook",
      text: "Current Approvals",
      name: "approve-current",
      profileType: "ta-supervisor"
    },
    {
      icon: "mdi-notebook",
      text: "Past Approvals",
      name: "approve-past",
      profileType: "ta-supervisor"
    },
    {
      icon: "mdi-notebook",
      text: "Current Assignments",
      name: "assign",
      profileType: "ta-coordinator"
    },
    {
      icon: "mdi-notebook",
      text: "Past Assignments",
      name: "assign",
      profileType: "ta-coordinator"
    },
    {
      icon: "mdi-notebook",
      text: "Current TA Release",
      name: "currenttarelease",
      profileType: "office"
    },
    {
      icon: "mdi-notebook",
      text: "Past TA Release",
      name: "pasttarelease",
      profileType: "office"
    },
    { divider: true },
    { heading: "Academics" },
    { icon: "mdi-calendar", text: "Calendar" },
    { icon: "mdi-calendar-clock", text: "Time Table" }
  ]
};

const getters = {
  items(state, getters, rootState, rootGetters) {
    return state.items.filter(
      e =>
        e.profileType === rootGetters["auth/profileType"] ||
        e.profileType == null
    );
  }
};

const mutations = {};

const actions = {};

export { state, mutations, actions, getters };
