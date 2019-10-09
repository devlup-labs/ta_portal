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
import CurrentAssignment from "../components/CurrentAssignment";
import PastAssignment from "../components/PastAssignment";
import ApprovalRequests from "../components/ApprovalRequests";
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
      path: "/about",
      name: "about",
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () =>
        import(/* webpackChunkName: "about" */ "../views/About.vue")
    },
    {
      path: "/ta-assignments",
      name: "ta-assignments",
      component: TaAssignment,
      meta: { taCoordinatorOnly: true }
    },
    {
      path: "/current",
      name: "current",
      component: CurrentAssignment,
      meta: { taOnly: true }
    },
    {
      path: "/past",
      name: "past",
      component: PastAssignment,
      meta: { taOnly: true }
    },
    {
      path: "/approval-requests",
      name: "approval-requests",
      component: ApprovalRequests,
      meta: { taSupervisorOnly: true }
    }
  ]
});

router.beforeEach(AuthGuard);
router.beforeEach(TaOnly);
router.beforeEach(TaSupervisorOnly);
router.beforeEach(TaCoordinatorOnly);

export default router;
