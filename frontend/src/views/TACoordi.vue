<template lang="pug">
    div
        v-row
            v-col(cols="6")
                TACoordinator(@change = "selected")
            v-col(cols="6")
                AssignTA(:show ="show")
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
    code: "",
    show: false
  }),
  methods: {
    selected(course) {
      this.show = !!course.code;
    }
  }
};
</script>
