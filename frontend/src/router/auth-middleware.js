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

function TaOnly(to, from, next) {
  if (to.matched.some(record => record.meta.taOnly)) {
    if (store.getters["auth/profileType"] !== "ta") {
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

function TaSupervisorOnly(to, from, next) {
  if (to.matched.some(record => record.meta.taSupervisorOnly)) {
    if (store.getters["auth/profileType"] !== "ta-supervisor") {
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

function TaCoordinatorOnly(to, from, next) {
  if (to.matched.some(record => record.meta.taCoordinatorOnly)) {
    if (store.getters["auth/profileType"] !== "ta-coordinator") {
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

export { AuthGuard, TaOnly, TaSupervisorOnly, TaCoordinatorOnly };
