<template lang="pug">
    div
        v-data-table.elevation-1(
            v-if="code"
            v-model="selected"
            :headers="headers"
            :items="tas(selected_program)"
            :single-select="singleSelect"
            :search="search"
            item-key="roll_no"
            show-select)
            template(v-slot:item.assigned_hours="{ item }")
                v-text-field(:value="item.assigned_hours" @input="changeHours(item.id, $event)")
            template(v-slot:top)
                v-toolbar(color="accent" :prominent="false")
                    v-row
                        v-col(cols="6")
                            v-tabs(background-color="transparent" v-model="selected_program")
                                v-tab(v-for="(program, i) in programs" :key="i")
                                    | {{ program }}
                        v-col(cols="6" align-self="center")
                            v-row.px-3
                                span
                                    strong SELECTED:&nbsp;
                                    | {{selected.length}} TAs
                                v-spacer
                                v-btn(color="primary" small rounded @click="makeTaAssignment") Save
                v-row
                    v-col
                        v-text-field.mx-4(append-icon="mdi-mic" flat hide-details label="Search"
                            prepend-icon="mdi-magnify" outlined v-model="search")

</template>

<script>
import { mapGetters, mapActions } from "vuex";
export default {
  name: "DutyAssigner",
  props: {
    code: String
  },
  data: () => ({
    singleSelect: false,
    search: "",
    selected_program: 0,
    selected: [],
    programs: ["PhD", "MTech"],
    headers: [
      { text: "Name", value: "name" },
      { text: "Roll No", value: "roll_no" },
      { text: "Availability", value: "availability" },
      { text: "Hours", value: "assigned_hours" }
    ]
  }),
  methods: {
    ...mapActions("assignTa", ["fetchAllTas", "updateHours"]),
    changeHours(taId, hours) {
      this.updateHours({ taId, hours });
    },
    makeTaAssignment() {
      console.log(this.selected);
    }
  },
  computed: {
    ...mapGetters("assignTa", ["tas", "assignedTas"])
  },
  watch: {
    code: function(course_code) {
      if (course_code) {
        this.fetchAllTas(course_code);
      }
    },
    assignedTas: function(newVal) {
      this.selected = newVal;
    }
  }
};
</script>

<style scoped></style>
