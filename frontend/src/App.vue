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
  methods: {
    isPropHidden(propName) {
      const routeMeta = this.$router.currentRoute.meta;
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
  }
};
</script>
