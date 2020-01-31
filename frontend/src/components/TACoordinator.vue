<template lang="pug">
    v-data-table.elevation-1(
        v-model="selected"
        :headers="headers"
        :items="courseList"
        :single-select="singleSelect"
        item-key="code"
        show-select)
</template>

<script>
import { mapGetters, mapActions } from "vuex";
export default {
  name: "TaAssignmentCard",
  data: () => ({
    singleSelect: true,
    courseSelected: false,
    selected: [],
    headers: [
      { text: "Course Code", value: "code" },
      { text: "Course Name", value: "name" },
      { text: "Ta Supervisor", value: "supervisor_name" },
      { text: "Required TA", value: "tas_required" },
      { text: "Assigned TA", value: "assigned_ta" }
    ]
  }),
  methods: {
    ...mapActions("taCoordinator", ["fetchCourseList"])
  },
  computed: {
    ...mapGetters("taCoordinator", ["courseList"])
  },
  watch: {
    selected: function(newSelected, oldSelected) {
      if (newSelected[0]) {
        this.$emit("change", newSelected[0]);
      } else {
        this.$emit("change", "");
      }
    }
  },
  beforeMount() {
    this.fetchCourseList();
  }
};
</script>

<style>
thead.v-data-table-header tr {
  background-color: #ebfdfd;
}
</style>
