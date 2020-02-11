<template lang="pug">
  v-card.elevation-3
    v-card-text
      v-container
        v-row
          v-col(cols="12" sm="6" md="6")
            v-row
              v-col(cols="12" sm="6" md="6")
                v-text-field(outlined :value="user.first_name" @input="setFirstName"
                  name= "first_name" :rules="[rules.required]" label="First Name")
              v-col(cols="12" sm="6" md="6")
                v-text-field(outlined :value="user.last_name" @input="setLastName"
                  name= "last_name" :rules="[rules.required]" label="Last Name")
              v-col(cols="12" sm="6" md="6")
                v-text-field(outlined :value="taProfile.roll_no"
                  :rules= "[rules.required]" label="Roll no." disabled)
              v-col(cols="12" sm="6" md="6")
                v-select(outlined :value="taProfile.program"
                  :items ="programItems"
                  item-text="label"
                  item-value="value"
                  label="Programme" disabled)
              v-col(cols="12")
                v-text-field(outlined :value="user.email"
                  :rules= "[rules.required]" label="Email" disabled)
              v-col(cols="12")
                v-text-field(outlined :value="taProfile.phone" @input="setPhone"
                  name="phone" :rules="[rules.phone]" label="Contact no.")
              v-col(cols="12")
                v-text-field(outlined :value= "taProfile.alternate_phone" @input="setAlternatePhone"
                  name="alternate_phone" :rules="[rules.phone]" label="Alternate Contact no.")
          v-col(cols="12" sm="6" md="6")
            v-row
              v-col(cols="12")
                h4.pb-2 Research Area
                v-textarea(
                  outlined
                  no-resize
                  counter
                  name="research_area"
                  :value="taProfile.research_area"
                  @input="setResearchArea"
                  :rules= "[rules.required, rules.length(256)]"
                  placeholder="Current Area of Research")
                h4.pb-2 Educational Background
              v-col(cols="12")
                v-combobox(
                  outlined
                  counter
                  label="BTech Specialisation"
                  name="btech_specialization"
                  :items="bTechSpecializationItems"
                  :value="taProfile.btech_specialization"
                  @input="setBtechSpecialization"
                  :rules= "[rules.required, rules.length(64)]"
                  hint="Enter Specialisation like Electrical Engineering")
              v-col(cols="12")
                v-text-field(outlined :value="taProfile.mtech_specialization" @input="setMtechSpecialization"
                  name = "mtech_specialization" :rules= "[rules.required]"
                  label="MTech Specialisation"
                  hint="Enter Specialisation like Image Processing")
    v-divider.mx-8
    v-card-actions
      v-col.px-6
        v-btn(color="primary" @click="saveTaProfile" rounded max-width="1" large) Save
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import { phoneRegex } from "./utils";

export default {
  name: "Profile",
  data() {
    return {
      rules: {
        required: value => !!value || "Required.",
        phone: value => phoneRegex.test(value) || "Invalid phone number.",
        length: limit => value =>
          value.length <= limit || "Character limit exceeded"
      }
    };
  },
  computed: {
    ...mapGetters("taProfile", ["taProfile", "user", "errors"]),
    programItems() {
      return [
        { label: "M.Tech", value: "1" },
        { label: "Ph.D MHRD", value: "2" },
        { label: "Ph.D VSS", value: "3" }
      ];
    },
    bTechSpecializationItems() {
      return [
        "Electrical Engineering or equivalent",
        "Electronics and Communication or equivalent"
      ];
    }
  },
  methods: {
    ...mapActions("taProfile", [
      "fetchTaProfile",
      "saveTaProfile",
      "setFirstName",
      "setLastName",
      "setPhone",
      "setAlternatePhone",
      "setResearchArea",
      "setBtechSpecialization",
      "setMtechSpecialization"
    ])
  },
  mounted() {
    this.fetchTaProfile();
  }
};
</script>

<style scoped></style>
