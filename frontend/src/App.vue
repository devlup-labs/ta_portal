<template lang="pug">
    v-app(style="background-color: white")
        Header(v-if="showAppBar" :navIcon="showSidenav" @toggleDrawer="drawer = !drawer")
        Sidenav(v-if="showSidenav" :drawer="drawer")
        v-content
            v-container(fluid fill-height)
                router-view
</template>

<script>
import Header from "./components/Header";
import Sidenav from "./components/Sidenav";
export default {
  name: "App",
  components: { Header, Sidenav },
  data: () => ({
    drawer: true,
    showAppBar: true,
    showSidenav: true
  }),
<<<<<<< HEAD
  computed: {
    showHeader() {
      return this.$router.currentRoute.name === "login" ;
=======
  methods: {
    isPropHidden(propName) {
      const routeMeta = this.$router.currentRoute.meta;
      return (
        routeMeta.hasOwnProperty("hide") && routeMeta.hide.includes(propName)
      );
    }
  },
  watch: {
    $route() {
      this.showAppBar = !this.isPropHidden("app-bar");
      this.showSidenav = !this.isPropHidden("sidenav");
>>>>>>> 2482f841f3a25aa017e13b8859b85802c52755a0
    }
  }
};
</script>
