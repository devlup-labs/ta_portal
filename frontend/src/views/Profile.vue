<template lang="pug">
  v-row(justify="center")
    v-col(cols="12")
      h4.headline VIEW/UPDATE PROFILE
    v-col(cols="12")
      ProfileCard
</template>

<script>
import ProfileCard from "../components/ProfileCard.vue";

export default {
  name: "profile",
  components: {
    ProfileCard
  }
};
</script>

<style></style>
