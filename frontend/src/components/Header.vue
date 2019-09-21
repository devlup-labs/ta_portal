<template lang="pug">
    v-app-bar(app clipped-left color="primary")
        v-app-bar-nav-icon.white--text(v-if="navIcon" @click="$emit('toggleDrawer')")
        v-toolbar-title.white--text
            span.title.ml-3.mr-5 TA Portal&nbsp;
            span.font-weight-light Department of Electrical Engineering, IIT Jodhpur
        v-spacer
        v-menu(v-if="profile" bottom left)
            template(v-slot:activator="{ on }")
                v-btn(dark icon v-on="on")
                    v-avatar(size="38px")
                        img(src="https://cdn.vuetifyjs.com/images/logos/logo.svg")
            v-list
                v-list-item(
                    v-for="(item, i) in menu"
                    :key="i"
                    @click="")
                    v-list-item-title {{ item.title }}
        v-btn.white--text(v-else outlined :to="{name: 'login'}") Login
</template>

<script>
export default {
  name: "Header",
  props: {
    profile: Object,
    navIcon: Boolean
  },
  data() {
    return {
      menu: [{ title: "View Profile" }, { title: "Logout" }]
    };
  }
};
</script>

<style scoped></style>
