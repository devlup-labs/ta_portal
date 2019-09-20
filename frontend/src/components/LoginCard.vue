<template lang="pug">
  v-card
    v-row
      v-col.hidden-sm-and-down(md="5" offset-md="1" align-self="center")
        h2.display-1 TA Management
        p.heading.mb-0 Department of Electrical Engineering
        | IIT Jodhpur
      v-col.py-12(xs="12" md="6")
        v-toolbar(flat)
          v-toolbar-title
            span.primary--text Sign in to TA Portal
        v-card-text
          v-form(v-model="valid" ref="form")
            v-text-field(
              label="Email"
              name="email"
              outlined
              v-model="email"
              prepend-icon="mdi-email"
              :rules="emailRules"
              required
            )
          v-text-field(
            label="Password"
            name="password"
            outlined
            prepend-icon="mdi-lock"
            :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
            @click:append="() => (showPassword = !showPassword)"
            :rules="passwordRules"
            :type="showPassword ? 'text' : 'password'"
            min="8"
            required
            v-model="password"
          )
          v-row
            v-col.ml-auto.py-0(cols="auto")
              span.info--text Forgot Password?
          v-row(justify="center")
            v-btn(rounded color="primary" dark extra large) Log in

          v-row.py-3(justify="center")
            h4 OR

          v-row(justify="center")
            a
              img(
                :src="googleSignInBtn"
                class="gsign-responsive"
                alt="sign in google"
              )
</template>

<script>
import googleSignInBtn from "../assets/btn_google_light_normal.svg";

export default {
  name: "LoginCard",
  data() {
    return {
      valid: false,
      showPassword: false,
      password: "",
      passwordRules: [
        v => !!v || "Password is required",
        v => v.length > 7 || "Password must be greater than 8 characters"
      ],
      email: "",
      emailRules: [
        v => !!v || "E-mail is required",
        v => /.+@.+\..+/.test(v) || "E-mail must be valid"
      ],
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
