<template lang="pug">
  div
    v-data-table(
        :headers="headers"
        :items="names"
        :single-select="singleSelect"
        item-key="name"
        show-select
        class="elevation-1")
        template(v-slot:item.hours="{ item }")
            v-text-field(type="number" v-model.number="item.hours")
        template(v-slot:top)
            v-toolbar(color="accent" :prominent="false")
                v-row
                    v-col(cols="6")
                        v-tabs(background-color="transparent")
                            v-tab(v-for="(item, i) in programs" :key="i")
                                | {{ item }}
                    v-col(cols="6" align-self="center")
                        v-row.px-3
                            span
                                strong SELECTED:&nbsp;
                                | 4 TAs
                            v-spacer
                            v-btn(color="primary" small rounded) Save
            v-row
                v-col
                    v-text-field.mx-4(append-icon="mdi-mic" flat hide-details label="Search"
                        prepend-icon="mdi-magnify" outlined)

</template>

<script>
export default {
  name: "DutyAssigner",
  data: () => ({
    singleSelect: false,
    selected: [],
    programs: ["PhD", "MTech"],
    headers: [
      { text: "Name", valuue: "name" },
      { text: "Roll No", value: "rollno" },
      { text: "Availability", value: "availability" },
      { text: "Hours", value: "hours" }
    ],
    defaultItem: {
      name: "",
      rollno: "",
      availability: "",
      hours: ""
    }
  })
};
</script>

<style scoped></style>
