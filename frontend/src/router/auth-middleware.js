import store from "../store";

export default (to, from, next) => {
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
};
