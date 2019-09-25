import Vue from "vue";
import Router from "vue-router";
import Login from "./views/Login";
import Profile from "./views/Profile";
import FeedbackTextBox from "./components/FeedbackTextBox";
Vue.use(Router);

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/login",
      name: "login",
      component: Login
    },
    {
      path: "/ftest",
      name: "ftest",
      component: FeedbackTextBox
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
    }
  ]
});
