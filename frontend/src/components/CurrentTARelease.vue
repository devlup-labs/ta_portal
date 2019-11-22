<template lang="pug">
    div
        h4.pa-5 SEP 2019 SEMESTER I, AY 2019-2020
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
    ...mapActions("currentTaReleases", ["fetchFeedbackCount"])
  },
  computed: {
    ...mapGetters("currentTaReleases", ["feedbackCount"])
  },
  beforeMount() {
    this.fetchFeedbackCount();
  }
};
</script>

<style scoped></style>
