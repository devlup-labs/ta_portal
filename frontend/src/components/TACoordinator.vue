<template lang="pug">
    div
        h4 SEMESTER I, AY 2019-2020
        v-data-table.elevation-1(
            :headers='headers'
            :itmes='Course'
            sort-by='Course'
            show-select)
        v-row
            v-col(cols="8")
                v-btn Save Assignment
                v-btn Reset
</template>

<script>
export default {
  data: () => ({
    dialog: false,
    headers: [
      { text: "Course", value: "Course" },
      { text: "TA Supervisor", value: "TASupervisor" },
      { text: "Required", value: "Required" },
      { text: "Assigned", value: "Assigned" }
    ],
    defaultItem: {
      Course: "",
      TASupervisor: "",
      Required: "",
      Assigned: ""
    }
  })
};
</script>

<style scoped></style>
