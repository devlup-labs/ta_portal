<template lang="pug">
    h3 &nbsp VIEW/UPDATE PROFILE
     v-container.elevation-5.pa-lg-8
        v-card(flat)
            v-card-title(justify="center")

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
                                :rules= "[rules.required]" label="Roll no." readonly)
                        v-col(cols="12" sm="6" md="6")
                            v-select(outlined :value="taProfile.program"
                                :items ="programItems"
                                item-text="label"
                                item-value="value"
                                label="Programme" readonly)
                        v-col(cols="12")
                            v-text-field(outlined :value="taProfile.phone" @input="setPhone"
                                name="phone" :rules="[rules.phone]" label="Contact no.")
                        v-col(cols="12")
                            v-text-field(outlined :value= "taProfile.alternate_phone" @input="setAlternatePhone"
                                name="alternate_phone" :rules="[rules.phone]" label="Alternate Contact no.")
                    v-col(cols="12" sm="6" md="6")
                        v-col(cols="12")
                            v-text-field(outlined :value="user.email"
                             :rules= "[rules.required]" label="Email" readonly)
                            h3 Educational Background
                            v-row
                                v-col(cols="12")
                                    v-text-field(outlined :value="taProfile.research_area" @input="setResearchArea"
                                        name="research_area" :rules= "[rules.required]" label="Research Area" height=10 placeholder="Current area of Research")
                                v-col(cols="12" sm="6" md="6")
                                    v-text-field(outlined :value="taProfile.btech_specialization" @input="setBtechSpecialization"
                                        name = "btech_specialization" :rules= "[rules.required]"
                                        label="BTech Specialisation"
                                        hint="Enter Specialisation like Electrical Engineering")
                                v-col(cols="12" sm="6" md="6")
                                    v-text-field(outlined :value="taProfile.mtech_specialization" @input="setMtechSpecialization"
                                        name = "mtech_specialization" :rules= "[rules.required]"
                                        label="MTech Specialisation"
                                        hint="Enter Specialisation like Image Processing")
            v-divider
            v-card-actions
                v-btn(color="primary" @click="saveTaProfile" rounded max-width="1" large) Save
</template>

<style scoped></style>

<script>
import { mapGetters, mapActions } from "vuex";
export default {
  name: "Profile",
  data() {
    return {
      rules: {
        required: value => !!value || "Required.",
        phone: value =>
          /\(?\+[0-9]{1,3}\)? ?-?[0-9]{1,3} ?-?[0-9]{3,5} ?-?[0-9]{4}( ?-?[0-9]{3})? ?(\w{1,10}\s?\d{1,6})?|([6-9][0-9]{9})/.test(
            value
          ) || "Invalid phone number."
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
