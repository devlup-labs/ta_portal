import Vue from "vue";
import Router from "vue-router";
import Login from "../views/Login";
import Profile from "../views/Profile";
import TaAssignment from "../views/TaAssignment";
import { guards } from "./auth-middleware";
import Logout from "../views/Logout";
import Past from "../views/Past";
import Current from "../views/Current";
import ApproveCurrent from "../views/ApproveCurrent";
import CurrentRelease from "../views/CurrentRelease";
Vue.use(Router);

const router = new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/login",
      name: "login",
      component: Login,
      meta: { hide: ["sidenav"], fillHeight: true }
    },
    {
      path: "/logout",
      name: "logout",
      component: Logout,
      meta: { hide: ["sidenav", "app-bar"] }
    },
    {
      path: "/profile",
      name: "profile",
      component: Profile,
      meta: { requiresAuth: true }
    },
    {
      path: "/currenttarelease",
      name: "currenttarelease",
      component: CurrentRelease,
      meta: { OfficeOnly: true }
    },
    {
      path: "/current",
      name: "current",
      component: Current,
      meta: { requiresAuth: true, taOnly: true }
    },
    {
      path: "/past",
      name: "past",
      component: Past,
      meta: { requiresAuth: true, taOnly: true }
    },
    {
      path: "/approve-current",
      name: "approve-current",
      component: ApproveCurrent,
      meta: { taSupervisorOnly: true }
    },
    {
      path: "/ta-assignments",
      name: "ta-assignments",
      component: TaAssignment,
      meta: { taCoordinatorOnly: true }
    }
  ]
});

guards.forEach(guard => router.beforeEach(guard));

export default router;
