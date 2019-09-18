<template lang="pug">
    v-app
        Header(v-if="showHeader" @toggleDrawer="drawer = !drawer")
        Sidenav(v-if="showHeader" :drawer="drawer")
        v-content
            router-view
</template>

<script>
import Header from "./components/Header";
import Sidenav from "./components/Sidenav";

export default {
  name: "App",
  components: { Header, Sidenav },
  data: () => ({
    drawer: true
  }),
  computed: {
    showHeader() {
      return this.$router.currentRoute.name === "profile";
    }
  }
};
</script>
