import Vue from "vue";
import Router from "vue-router";
import Login from "./views/Login";
import Profile from "./views/Profile";
import CurrentAssignment from "./components/CurrentAssignment";
import PastAssignment from "./components/PastAssignment";

Vue.use(Router);

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/login",
      name: "login",
      component: Login,
      meta: { hide: ["sidenav"] }
    },
    {
      path: "/profile",
      name: "profile",
      component: Profile
    },
    {
      path: "/about",
      name: "about",
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () =>
        import(/* webpackChunkName: "about" */ "./views/About.vue")
    },
    {
      path: "/current",
      name: "current",
      component: CurrentAssignment
    },
    {
      path: "/past",
      name: "past",
      component: PastAssignment
    },
  ]
});
