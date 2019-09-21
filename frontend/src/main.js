import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
import { default as httpClientPlugin, httpClient } from "./plugins/httpClient";

Vue.use(httpClientPlugin);

Vue.config.productionTip = false;

const checkLogin = store => {
  httpClient
    .get("/api/auth-check/")
    .then(() => {
      store.dispatch("auth/login");
    })
    .catch(() => {});
};

new Vue({
  router,
  store,
  vuetify,
  created() {
    checkLogin(store);
  },
  render: h => h(App)
}).$mount("#app");
