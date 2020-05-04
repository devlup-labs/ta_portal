import store from "../store";

function AuthGuard(to, from, next) {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!store.getters["auth/isAuthenticated"]) {
      next({
        name: "login",
        query: { next: to.fullPath }
      });
    } else {
      next();
    }
  } else {
    next();
  }
}

function ProfileTypeGuardGenerator(profileType, metaOption) {
  return (to, from, next) => {
    if (to.matched.some(record => record.meta[metaOption])) {
      if (store.getters["auth/profileType"] !== profileType) {
        next({
          name: "profile",
          query: { next: to.fullPath }
        });
      } else {
        next();
      }
    } else {
      next();
    }
  };
}

const guards = [
  AuthGuard,
  ProfileTypeGuardGenerator("ta", "taOnly"),
  ProfileTypeGuardGenerator("ta-supervisor", "taSupervisorOnly"),
  ProfileTypeGuardGenerator("ta-coordinator", "taCoordinatorOnly"),
  ProfileTypeGuardGenerator("office", "officeOnly")
];

export { guards };
