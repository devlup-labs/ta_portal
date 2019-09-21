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
  },
  mounted() {
    this.$store.dispatch("auth/checkAuthentication").then(() => {
      if (this.$route.query.next) this.$router.push(this.$route.query.next);
      else this.$router.push({ name: "profile" });
    });
  }
};
</script>

<style></style>
