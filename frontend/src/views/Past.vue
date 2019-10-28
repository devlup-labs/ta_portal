<template lang="pug">
    v-container( fluid )
        PastAssignment
</template>

<script>
import PastAssignment from "../components/PastAssignment";
import FeedbackTextBox from "../components/FeedbackTextBox";
export default {
  name: "Past",
  components: {
    PastAssignment,
    FeedbackTextBox
  }
};
</script>

<style scoped></style>
