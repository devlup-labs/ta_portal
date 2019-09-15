<template lang="pug">
    v-row(justify="center")
        HeaderToolbar
        ProfileCard
</template>

<script>
import HeaderToolbar from "../components/HeaderToolbar.vue";
import ProfileCard from "../components/ProfileCard.vue";
export default {
  name: "profile",
  components: {
    HeaderToolbar,
    ProfileCard
  }
};
</script>

<style></style>
