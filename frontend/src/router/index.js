import Vue from "vue";
import Router from "vue-router";
import Login from "../views/Login";
import Profile from "../views/Profile";
import TaAssignment from "../views/TaAssignment";
import {
  AuthGuard,
  TaOnly,
  TaSupervisorOnly,
  TaCoordinatorOnly
} from "./auth-middleware";
import Logout from "../views/Logout";
import Current from "../views/Current";
import Past from "../views/Past";
import ApproveCurrent from "../views/ApproveCurrent";
Vue.use(Router);

const router = new Router({
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
      path: "/current",
      name: "current",
      component: Current,
      meta: { taOnly: true }
    },
    {
      path: "/past",
      name: "past",
      component: Past,
      meta: { taOnly: true }
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
    },

  ]
});

router.beforeEach(AuthGuard);
router.beforeEach(TaOnly);
router.beforeEach(TaSupervisorOnly);
router.beforeEach(TaCoordinatorOnly);

export default router;
