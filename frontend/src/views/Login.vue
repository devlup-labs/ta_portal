<template lang="pug">
    v-container(fluid fill-height)
        v-layout(flex align-center offset-md5 fill-height justify-center)
            v-flex( xs10 sm8 lg6)
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
