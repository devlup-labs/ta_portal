<template lang="pug">
    div
        v-row
            v-col(md="2")
                v-select(:items="months" label="Month"
                    item-text="label"
                    item-value="value"
                    single-line v-model="selectedMonth")
            v-col(md="1")
                v-select(:items="years" label="Year"
                    single-line v-model="selectedYear")
        v-data-table.elevation-1(
            v-if = "selectedYear && selectedMonth"
            :headers='headers'
            item-key='programme'
            :items='feedbackCount'
            sort-by='programme')
            template(v-slot:item.reports='{ item }')
                a(:href= " '//' + `${item.link}`" target="_blank") View
</template>

<script>
import { mapGetters, mapActions } from "vuex";
export default {
  data: () => ({
    dialog: false,
    headers: [
      { text: "Programme", value: "programme" },
      { text: "Submitted", value: "submitted" },
      { text: "Approved", value: "approved" },
      { text: "Rejected", value: "rejected" },
      { text: "Pending", value: "pending" },
      { text: "Reports", value: "reports" }
    ],
    selectedMonth: "",
    selectedYear: ""
  }),
  methods: {
    ...mapActions("taReleases", ["fetchFeedbackCount"])
  },
  computed: {
    ...mapGetters("taReleases", ["feedbackCount"]),
    years() {
      const year = new Date().getFullYear() + 1;
      return Array.from(
        { length: year - 2018 },
        (value, index) => year - index
      );
    },
    months() {
      return [
        { label: "January", value: "1" },
        { label: "February", value: "2" },
        { label: "March", value: "3" },
        { label: "April", value: "4" },
        { label: "May", value: "5" },
        { label: "June", value: "6" },
        { label: "July", value: "7" },
        { label: "August", value: "8" },
        { label: "September", value: "9" },
        { label: "October", value: "10" },
        { label: "November", value: "11" },
        { label: "December", value: "12" }
      ];
    }
  },
  watch: {
    selectedMonth: function(val) {
      const month = val;
      const year = this.selectedYear;
      if (month && year) {
        this.fetchFeedbackCount({ month, year });
      }
    },
    selectedYear: function(val) {
      const month = this.selectedMonth;
      const year = val;
      if (month && year) {
        this.fetchFeedbackCount({ month, year });
      }
    }
  }
};
</script>

<style scoped></style>
