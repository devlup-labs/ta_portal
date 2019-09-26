<template lang="pug">
  v-card.elevation-10
    v-row
      v-col.hidden-sm-and-down(md="5" offset-md="1" align-self="center" )
        v-img(src="../assets/iitjlogo.jpg" aspect-ratio=1 height="100" contain=true position="left-top" )
        h2.display-1 TA Management
        p.heading.mb-0 Department of Electrical Engineering
        | IIT Jodhpur
      v-col(xs="12" md="6")
        v-stepper.elevation-0(v-model="forgetPasswordStep")
          v-stepper-items
            v-stepper-content(step="1")
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
                    v-model="password"
                    :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                    @click:append="() => (showPassword = !showPassword)"
                    :rules="passwordRules"
                    :type="showPassword ? 'text' : 'password'"
                    min="8"
                    required
                  )
                  v-row
                    v-col.ml-auto.pt-0(cols="9")
                      v-btn(color="info" text rounded @click="forgetPasswordStep = 2") Forgot Password?
                  v-row(justify="center")
                    v-btn(color="primary" :disabled="!valid" @click="login" large rounded) Login

                v-row.py-3(justify="center")
                  h4 OR

                v-row(justify="center")
                  a
                    img(
                      :src="googleSignInBtn"
                      class="gsign-responsive"
                      alt="sign in google"
                    )
            v-stepper-content.py-12(step="2")
              v-toolbar(flat)
                v-toolbar-title
                  span.primary--text Forgot Password?
              v-card-text
                v-text-field.pb-0(
                  label="Roll Number"
                  name="roll_no"
                  outlined
                  v-model="rollNumber"
                  prepend-icon="mdi-account-card-details"
                  :rules="rollNumberRules"
                  required
                )
                v-row
                  v-col.ml-auto.pt-0(cols="auto")
                    v-btn.mr-3(color="info" text rounded @click="forgetPasswordStep = 1") Discard
                    v-btn(color="primary" rounded @click="resetPassword" :loading="resettingPassword") Reset Password
                v-card(color="accent" flat)
                  v-card-text
                    span A new password will be sent to the Email ID associated with the roll number.
            v-stepper-content.py-12(step="3")
              v-toolbar(flat)
                v-toolbar-title
                  span.primary--text Password Reset
              v-card.mb-5(color="accent" flat)
                v-card-text
                  span A new password has been sent to your registered Email ID. Please check your inbox and login with the new password.
              v-row.my-3(justify="center")
                v-btn(color="primary" large rounded @click="forgetPasswordStep = 1") Back to Login
</template>

<script>
import googleSignInBtn from "../assets/btn_google_light_normal.svg";

export default {
  name: "LoginCard",
  data() {
    return {
      valid: false,
      showPassword: false,
      forgetPasswordStep: 0,
      resettingPassword: false,
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
      rollNumber: "",
      rollNumberRules: [v => !!v || "Roll number is required"],
      googleSignInBtn
    };
  },
  methods: {
    login() {
      this.$store
        .dispatch("auth/login", {
          email: this.email,
          password: this.password
        })
        .then(() => {
          if (this.$route.query.next) this.$router.push(this.$route.query.next);
          else this.$router.push({ name: "profile" });
        });
    },
    resetPassword() {
      this.resettingPassword = true;
      setTimeout(() => {
        this.resettingPassword = false;
        this.forgetPasswordStep = 3;
      }, 3000);
    }
  }
};
</script>

<style scoped>
.gsign-responsive {
  width: 100%;
  height: auto;
}
</style>
