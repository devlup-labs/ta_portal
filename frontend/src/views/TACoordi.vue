<template lang="pug">
    div
        v-row
            v-col(cols="6")
                TACoordinator
            v-col(cols="6")
                AssignTA
</template>

<script>
import TACoordinator from "../components/TACoordinator";
import AssignTA from "../components/AssignTA";
export default {
  name: "TACoordi",
  components: {
    TACoordinator,
    AssignTA
  }
};
</script>
