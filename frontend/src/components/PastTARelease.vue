<template lang="pug">
  div
    v-row
        v-col(md="3")
            v-select(:items="years" label="Year"
                     single-line)
        v-col(md="3")
            v-select(:items="semester" label="Semester"
                single-line)
    v-data-table.elevation-1(
        :headers='headers'
        item-key='course_code'
        :items='currentReleases'
        sort-by='Month')
</template>

<script>
export default {
  data: () => ({
    dialog: false,
    headers: [
      { text: "Month", value: "Month" },
      { text: "Programme", value: "Programme" },
      { text: "Submitted", value: "Submitted" },
      { text: "Approved", value: "Approved" },
      { text: "Rejected", value: "Rejected" },
      { text: "Pending", value: "Pending" },
      { text: "Reports", value: "Report" }
    ],
    defaultItem: {
      Programme: "",
      Submitted: "",
      Approved: "",
      Rejected: "",
      Pending: "",
      Reports: ""
    },
    years: ["AY 2017-2018", "AY 2018-2019", "AY 2019-2020"],
    semester: [
      "SEMESTER 1",
      "SEMESTER 2",
      "SEMESTER 3",
      "SEMESTER 4",
      "SEMESTER 5",
      "SEMESTER 6",
      "SEMESTER 7",
      "SEMESTER 8"
    ],
    currentReleases: []
  })
};
</script>

<style scoped></style>
