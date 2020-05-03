<template lang="pug">
    div
        v-row
            v-col(cols="6")
                TACoordinator(@change = "selected")
            v-col(cols="6")
                AssignTA(:course ="course")
</template>

<script>
import TACoordinator from "../components/TACoordinator";
import AssignTA from "../components/AssignTA";
export default {
  name: "TACoordi",
  components: {
    TACoordinator,
    AssignTA
  },
  data: () => ({
    course: {}
  }),
  methods: {
    selected(course) {
      this.course = course;
    }
  }
};
</script>
