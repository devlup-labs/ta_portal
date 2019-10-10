<template lang="pug">
  v-data-table(
    :headers="headers"
    :items="pastta"
    :sort-by="['calories', 'fat']"
    :sort-desc="[false, true]"
    multi-sort
    class="elevation-1")
</template>

<script>
export default {
  name: "PastAssignment",
  data() {
    return {
      headers: [
        {
          text: "Month",
          align: "left",
          sortable: false,
          value: "month"
        },
        { text: "Course Code", value: "coursecode" },
        { text: "Course Name", value: "coursename" },
        { text: "TA Supervisor", value: "tasupervisor" },
        { text: "Status", value: "status" }
      ],
      pastta: [
        {
          month: "Sept",
          coursecode: "EE213",
          tasupervisor: "Faculty Name",
          status: "approved/pending",
          coursename: "Signals and System"
        }
      ]
    };
  }
};
</script>

<style scoped></style>
