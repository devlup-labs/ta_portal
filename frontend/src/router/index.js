import Vue from "vue";
import Router from "vue-router";
import Login from "../views/Login";
import Profile from "../views/Profile";
import { guards } from "./auth-middleware";
import Logout from "../views/Logout";
import Past from "../views/Past";
import Current from "../views/Current";
import ApproveCurrent from "../views/ApproveCurrent";
import ApprovePast from "../views/ApprovePast";
import PastRelease from "../views/PastRelease";
import CurrentRelease from "../views/CurrentRelease";
import TACoordi from "../views/TACoordi";
import ChangePassword from "../views/ChangePassword";
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
      path: "/change-password",
      name: "change-password",
      component: ChangePassword,
      meta: { requiresAuth: true }
    },
    {
      path: "/currenttarelease",
      name: "currenttarelease",
      component: CurrentRelease,
      meta: { requiresAuth: true, officeOnly: true }
    },
    {
      path: "/pasttarelease",
      name: "pasttarelease",
      component: PastRelease,
      meta: { requiresAuth: true, officeOnly: true }
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
      meta: { requiresAuth: true, taSupervisorOnly: true }
    },
    {
      path: "/approve-past",
      name: "approve-past",
      component: ApprovePast,
      meta: { requiresAuth: true, taSupervisorOnly: true }
    },
    {
      path: "/assign",
      name: "assign",
      component: TACoordi,
      meta: { requiresAuth: true, taCoordinatorOnly: true }
    },
    {
      path: "*",
      redirect: "/login"
    }
  ]
});

guards.forEach(guard => router.beforeEach(guard));

export default router;
