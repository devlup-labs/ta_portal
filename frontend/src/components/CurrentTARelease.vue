<template lang="pug">
    div
        h4.pa-5 {{ currentDate() }}
        v-data-table.elevation-1(
            :headers='headers'
            item-key='programme'
            :items='feedbackCount'
            sort-by='programme')
            template(v-slot:item.reports='{ item }')
                a(:href= " '//' + `${item.link}`" target="_blank") View

</template>

<script>
import { mapGetters, mapActions } from "vuex";
const monthNames = [
  "January",
  "February",
  "March",
  "April",
  "May",
  "June",
  "July",
  "August",
  "September",
  "October",
  "November",
  "December"
];
export default {
  data: () => ({
    headers: [
      { text: "Programme", value: "programme" },
      { text: "Submitted", value: "submitted" },
      { text: "Approved", value: "approved" },
      { text: "Rejected", value: "rejected" },
      { text: "Pending", value: "pending" },
      { text: "Reports", value: "reports" }
    ]
  }),
  methods: {
    ...mapActions("taReleases", ["fetchFeedbackCount"]),
    currentDate() {
      const today = new Date();
      return `${monthNames[today.getMonth()]} ${today.getFullYear()}`;
    }
  },
  computed: {
    ...mapGetters("taReleases", ["feedbackCount"])
  },
  beforeMount() {
    const today = new Date();
    let month = today.getMonth() + 1;
    let year = today.getFullYear();
    if (month > 12) {
      month = month - 12;
      year = year + 1;
    }
    this.fetchFeedbackCount({ month, year });
  }
};
</script>

<style scoped></style>
