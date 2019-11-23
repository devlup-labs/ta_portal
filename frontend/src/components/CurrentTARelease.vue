<template lang="pug">
  div 
     h4 SEP 2019 SEMESTER I, AY 2019-2020
     v-data-table.elevation-1(
            :headers='headers'
            item-key='course_code'
            :items='currentReleases'
            sort-by='Programme')
</template>

<script>
export default {
  data: () => ({
    dialog: false,
    headers: [
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
    }
  })
};
</script>

<style scoped></style>
