<template lang="pug">
  v-app(style="background-color: white")
    Header(v-if="showAppBar" :navIcon="showSidenav" @toggleDrawer="drawer = !drawer")
    Sidenav(v-if="showSidenav" :drawer="drawer")
    v-content
      v-container(fluid :fill-height="$route.meta.fillHeight")
        router-view
    v-snackbar(
      v-model="snackbar"
      :color="color"
      :multi-line="mode === 'multi-line'"
      :timeout="timeout"
      :vertical="mode === 'vertical'") {{ message }}
      v-btn(text @click="snackbar = false") Close
</template>

<script>
import Header from "./components/Header";
import Sidenav from "./components/Sidenav";
import { httpClient } from "./plugins/httpClient";
import { mapGetters } from "vuex";

export default {
  name: "App",
  components: { Header, Sidenav },
  data: () => ({
    drawer: true,
    showAppBar: true,
    showSidenav: true
  }),
  computed: {
    ...mapGetters("messages", ["message", "color", "timeout", "mode"]),
    snackbar: {
      get() {
        return this.$store.getters['messages/snackbar']
      },
      set(value) {
        this.$store.commit('messages/SET_SNACKBAR', value)
      }
    }
  },
  methods: {
    isPropHidden(propName) {
      const routeMeta = this.$route.meta;
      return (
        routeMeta.hasOwnProperty("hide") && routeMeta.hide.includes(propName)
      );
    },
    updateVisibility() {
      this.showAppBar = !this.isPropHidden("app-bar");
      this.showSidenav = !this.isPropHidden("sidenav");
    }
  },
  watch: {
    $route() {
      this.updateVisibility();
    }
  },
  created() {
    this.updateVisibility();
    httpClient.get("api/csrf-token/").then(response => {
      const token = response.data.csrftoken;
      document.cookie = `csrftoken = ${token}`;
    });
  }
};
</script>
