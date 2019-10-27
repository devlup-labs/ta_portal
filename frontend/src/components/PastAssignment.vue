<template lang="pug">
  v-data-table(
    :headers="headers"
    :items="pastAssignments"
    :sort-by="['date' ]"
    :sort-desc="[false ]"
    multi-sort
    class="elevation-1")
</template>

<script>
import { mapGetters, mapActions } from "vuex";
export default {
  name: "PastAssignment",
  data() {
    return {
      headers: [
        { text: "Date", value: "date_submitted" },
        { text: "Course Code", value: "course_code" },
        { text: "Course Name", value: "course_name" },
        { text: "TA Supervisor", value: "ta_supervisor" },
        { text: "Status", value: "status" }
      ]
    };
  },
  computed: {
    ...mapGetters("pastAssignments", ["pastAssignments"])
  },
  methods: {
    ...mapActions("pastAssignments", ["fetchPastAssignments"])
  },
  mounted() {
    this.fetchPastAssignments();
  }
};
</script>

<style scoped></style>
