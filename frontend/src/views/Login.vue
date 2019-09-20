<template lang="pug">
    v-row(align="center" justify="center")
        v-col(cols="12" xs="12" sm="8" md="10" lg="8")
            LoginCard
</template>

<script>
import LoginCard from "../components/LoginCard.vue";
export default {
  name: "Login",
  components: {
    LoginCard
  }
};
</script>

<style></style>
