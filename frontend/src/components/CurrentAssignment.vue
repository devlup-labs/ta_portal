<template lang="pug">
    v-data-table.elevation-1(
        :headers='headers'
        :items='data'
        sort-by='calories')
        template(v-slot:top='')
            v-toolbar(flat='', color='white')
                v-toolbar-title SEP 2019
                v-divider.mx-4(inset='', vertical='')
                v-spacer
                v-dialog(v-model='dialog', max-width='500px')
                    v-card.rounded-card
                        v-container.pa-2
                            v-card-title
                                v-row
                                    h4 EE213,Signals and Systems
                                    v-col.text-right
                                        v-chip.ma-2(color="#e3cceb" align="right" )  Submitted on 20th September,2019
                            h3 Completed TA Duties
                                div(class="text-center")
                                    v-card-text
                                        v-row
                                            v-textarea(
                                                name="input-7-1"
                                                filled
                                                background-color="white"
                                                label=""
                                                auto-grow
                                                rounded
                                                value="Tutorial and attendance of EE batch(Tuesday and Thursday)"
                                                outlined)
                                        v-row
                                            v-textarea(
                                                name="input-7-1"
                                                filled
                                                background-color="white"
                                                label=""
                                                auto-grow
                                                rounded
                                                value="Tutorial and attendance of EE batch(Tuesday and Thursday)"
                                                outlined)
                                div(align="right")
                                    v-btn.ma-2(width=200 rounded outlined color="blue" right) Close
        template(v-slot:item.action='{ item }')
            v-icon.mr-2(small='', @click='editItem(item)')
                | edit
            v-icon(small='', @click='deleteItem(item)')
                | delete
        template(v-slot:no-data='')
            v-btn(color='primary', @click='initialize') Reset
</template>

<script>
export default {
  data: () => ({
    dialog: false,
    headers: [
      {
        text: "Course Code ",
        align: "left",
        sortable: false,
        value: "name"
      },
      { text: "Course name", value: "coursename" },
      { text: "TA Supervisor", value: "supervisor" },
      { text: "Due By", value: "duedate" },
      { text: "Status", value: "action", sortable: false }
    ],
    data: [
      {
        name: "EE213",
        coursename: "Signals and System",
        supervisor: "Faculty name",
        duedate: "1 oct"
      },
      {
        name: "EE213",
        coursename: "Basic Electronics",
        supervisor: "Faculty name",
        duedate: "--"
      },
      {
        name: "EE213",
        coursename: "Electronics Lab",
        supervisor: "Faculty name",
        duedate: "--"
      }
    ]
  }),

  created() {
    this.initialize();
  },

  methods: {
    initialize() {
      this.desserts = [];
    },

    editItem(item) {
      this.editedIndex = this.desserts.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem(item) {
      const index = this.desserts.indexOf(item);
      confirm("Are you sure you want to delete this item?") &&
        this.desserts.splice(index, 1);
    },

    close() {
      this.dialog = false;
      setTimeout(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      }, 300);
    },

    save() {
      if (this.editedIndex > -1) {
        Object.assign(this.desserts[this.editedIndex], this.editedItem);
      } else {
        this.desserts.push(this.editedItem);
      }
      this.close();
    }
  }
};
</script>
