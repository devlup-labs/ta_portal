<template lang="pug">
  div
    v-toolbar(primary)
      v-toolbar-title.blue--text
        p.headline.mb-0  Login

    v-card
      v-card-text(pt-4)
        div
          v-form(v-model="valid" ref="form")
            v-text-field(
              outline
              prepend-icon="mdi-email"
              label="Email"
              v-model="email"
              :rules="emailRules"
              required
            )

            v-text-field(
              outline
              prepend-icon="mdi-lock"
              :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
              @click:append="() => (showPassword = !showPassword)"
              :rules="passwordRules"
              :type="showPassword ? 'password' : 'text'"
              label="Password"
              min="8"
              required
              v-model="password"
            )
            v-layout(justify-center)
              v-btn(color="primary") Login

            v-layout(justify-center)
              h4 OR

            v-layout(justify-center)
              a
                img(
                  :src="googleSignInBtn"
                  class="gsign-responsive"
                  alt="sign in google"
                )

</template>

<script>
import googleSignInBtn from "../assets/btn_google_light_normal.svg";
import HeaderToolbar from "./HeaderToolbar";
export default {
  name: "LoginCard",
  components: { HeaderToolbar },
    data() {
    return {
      valid: false,
      showPassword: false,
      password: "",
      passwordRules: [v => !!v || "Password is required"],
      email: "",
      emailRules: [v => !!v || "E-mail is required"],
      googleSignInBtn
    };
  }
};
</script>

<style scoped>
.gsign-responsive {
  width: 100%;
  height: auto;
}
</style>
