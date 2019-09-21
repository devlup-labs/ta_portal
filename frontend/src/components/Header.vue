<template lang="pug">
    v-app-bar(app clipped-left color="primary")
        v-app-bar-nav-icon.white--text(v-if="navIcon" @click="$emit('toggleDrawer')")
        v-toolbar-title.white--text
            span.title.ml-3.mr-5 TA Portal&nbsp;
            span.font-weight-light Department of Electrical Engineering, IIT Jodhpur
        v-spacer
        v-menu(v-if="isAuthenticated" bottom left)
            template(v-slot:activator="{ on }")
                v-btn(dark icon v-on="on")
                    v-avatar(size="38px")
                        img(src="https://cdn.vuetifyjs.com/images/logos/logo.svg")
            v-list
                v-list-item(
                    v-for="(item, i) in menu"
                    :key="i"
                    @click=""
                    :to="item.to")
                    v-list-item-title {{ item.title }}
        v-btn.white--text(v-else outlined :to="{name: 'login'}") Login
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "Header",
  props: {
    navIcon: Boolean
  },
  computed: {
    ...mapGetters("auth", ["isAuthenticated"])
  },
  data() {
    return {
      menu: [
        { title: "View Profile", to: { name: "profile" } },
        { title: "Logout", to: { name: "logout" } }
      ]
    };
  }
};
</script>

<style scoped></style>
