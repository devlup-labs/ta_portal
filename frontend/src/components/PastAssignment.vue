<template lang="pug">
  v-data-table(
    :headers="headers"
    :items="pastAssignments"
    :sort-by="['date', 'fat']"
    :sort-desc="[false, true]"
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
        {
          text: "Date",
          align: "left",
          sortable: false,
          value: "date_submitted"
        },
        { text: "Course Code", value: "course_code" },
        { text: "Course Name", value: "course_name" },
        { text: "TA Supervisor", value: "ta_supervisor" },
        { text: "Status", value: "status" }
      ],
      items: [
        {
          date: "Sept",
          coursecode: "EE213",
          tasupervisor: "Faculty Name",
          status: "approved/pending",
          coursename: "Signals and System"
        }
      ]
    };
  },
  computed: {
    ...mapGetters("pastAssignments", ["pastAssignments"]),

  },
    methods:{
        ...mapActions("pastAssignments", ["fetchPastAssignments"])
    },
    mounted() {
        this.fetchPastAssignments();
    }
};
</script>

<style scoped></style>
