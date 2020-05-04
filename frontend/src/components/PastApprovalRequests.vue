<template lang="pug">
    div
        v-col(md="1")
            v-select(:items="years" label="Year"
                single-line)

</template>

<script>
export default {
  data: () => ({}),
  computed: {
    years() {
      const year = new Date().getFullYear() + 1;
      return Array.from(
        { length: year - 2018 },
        (value, index) => year - index
      );
    }
  }
};
</script>

<style scoped></style>
