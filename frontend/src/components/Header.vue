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
                        img(src="../assets/account_box-24px.svg")
            v-list
                v-list-item(
                    v-for="(item, i) in menuItems"
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
  data() {
    return {
      menu: [
        { title: "View Profile", to: { name: "profile" }, profileType: "ta" },
        { title: "Change Password", to: { name: "change-password" } },
        { title: "Logout", to: { name: "logout" } }
      ]
    };
  },
  computed: {
    ...mapGetters("auth", ["isAuthenticated"]),
    menuItems() {
      return this.menu.filter(
        e =>
          e.profileType === this.$store.getters["auth/profileType"] ||
          e.profileType == null
      );
    }
  }
};
</script>

<style scoped></style>
