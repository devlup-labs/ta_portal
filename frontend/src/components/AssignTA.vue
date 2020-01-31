<template lang="pug">
    div
        v-data-table.elevation-1(
            v-if="show"
            v-model="selected"
            :headers="headers"
            :items="tas"
            :single-select="singleSelect"
            item-key="roll_no"
            show-select)
            template(v-slot:item.hours="{ item }")
                v-text-field(
                    @input ="updateHours({id : item.id, roll_no : item.roll_no, availability : item.availability, name : item.name, program : item.program, hours : $event})")
            template(v-slot:top)
                v-toolbar(color="accent" :prominent="false")
                    v-row
                        v-col(cols="6")
                            v-tabs(background-color="transparent")
                                v-tab(v-for="(program, i) in programs" :key="i")
                                    | {{ program }}
                        v-col(cols="6" align-self="center")
                            v-row.px-3
                                span
                                    strong SELECTED:&nbsp;
                                    | {{selected.length}} TAs
                                v-spacer
                                v-btn(color="primary" small rounded) Save
                v-row
                    v-col
                        v-text-field.mx-4(append-icon="mdi-mic" flat hide-details label="Search"
                            prepend-icon="mdi-magnify" outlined)

</template>

<script>
import { mapGetters, mapActions } from "vuex";
export default {
  name: "DutyAssigner",
  props: {
    show: Boolean
  },
  data: () => ({
    singleSelect: false,
    selected: [],
    programs: ["PhD", "MTech"],
    headers: [
      { text: "Name", value: "name" },
      { text: "Roll No", value: "roll_no" },
      { text: "Availability", value: "availability" },
      { text: "Hours", value: "hours" }
    ]
  }),
  methods: {
    ...mapActions("assignTa", ["fetchTas"]),
    updateHours: function(value) {
      console.log(value);
    }
  },
  computed: {
    ...mapGetters("assignTa", ["tas"])
  },
  watch: {
    selected: function(newSelected, oldSelected) {
      console.log(newSelected);
    }
  },

  beforeMount() {
    this.fetchTas();
  }
};
</script>

<style scoped></style>
