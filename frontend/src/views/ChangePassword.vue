<template lang="pug">
  v-row
    v-col(cols="12")
      h4.headline.ml-4 Change Password
    v-col(cols="12" lg="6" xl="6")
      v-card.elevation-3.ma-4
        v-container
          v-row.ma-4
            v-col(cols="12" sm="6" md="6")
              v-text-field(outlined
                v-model="oldPassword"
                :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                :rules="[rules.required, rules.min]"
                :type="show1 ? 'text' : 'password'"
                name= "Old Password" 
                label="Old Password"
                @click:append="show1 = !show1")
              v-text-field(outlined
                v-model="newPassword"
                :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
                :rules="[rules.required, rules.min]"
                :type="show2 ? 'text' : 'password'"
                name= "New Password" 
                label="New Password"
                @click:append="show2 = !show2")
              v-text-field(outlined
              v-model="confirmPassword"
                :append-icon="show3 ? 'mdi-eye' : 'mdi-eye-off'"
                :rules="[rules.required, rules.min]"
                :type="show3 ? 'text' : 'password'"
                name= "Retype New Password" 
                label="Retype New Password"
                @click:append="show3 = !show3")
        v-divider.mx-8
        v-card-actions
          v-col.px-6
              v-btn(color="primary" @click="changePassword" rounded max-width="1" large) Save
</template>

<script>
export default {
  name: "ChangePassword",
  data() {
    return {
      show1: false,
      show2: false,
      show3: false,
      rules: {
        required: value => !!value || "Required.",
        min: v => v.length >= 8 || "Min 8 characters"
      },
      oldPassword: "",
      newPassword: "",
      confirmPassword: ""
    };
  },
  methods: {
    changePassword() {
      if (this.newPassword !== this.confirmPassword) {
        this.$store.dispatch(
          "messages/showMessage",
          { message: "Passwords do not match", color: "error" },
          { root: true }
        );
      } else {
        this.$httpClient
          .patch("/api/accounts/change-password/", {
            old_password: this.oldPassword,
            new_password: this.newPassword
          })
          .then(() => {
            this.$store.dispatch(
              "messages/showMessage",
              { message: "Password Updated Successfully", color: "success" },
              { root: true }
            );
            this.oldPassword = this.newPassword = this.confirmPassword = "";
          })
          .catch(err => {
            this.$store.dispatch(
              "messages/showMessage",
              { message: err.response.data.message, color: "error" },
              { root: true }
            );
          });
      }
    }
  }
};
</script>
