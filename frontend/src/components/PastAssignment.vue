<template lang="pug">
    div
        h4.pa-5 SEP 2019 SEMESTER I, AY 2019-2020
        v-data-table.elevation-1(
            :headers='headers'
            :items='pastAssignments'
            sort-by='date_submitted')
            template(v-slot:top='')
                v-spacer
                v-dialog(v-model='dialog', max-width='1000px')
                    v-card.rounded-card
                        v-container.pa-2
                            v-card-title
                                v-row
                                    h4 {{DialogBoxItem.course_code}}, {{DialogBoxItem.course_name}}
                                    v-col.text-right
                                        v-chip.ma-2(color="#FCF9EB" align="right" v-if="DialogBoxItem.status === 'Pending Approval'")  Submitted on {{DialogBoxItem.date_submitted}}
                                        v-chip.ma-2(color="#E4F5F5" align="right" v-else-if="DialogBoxItem.status === 'Approved'")  Approved on {{DialogBoxItem.date_approved}}
                                        v-chip.ma-2(color="#E5CCD4" align="right" v-else-if="DialogBoxItem.status === 'Not Approved'")  Declined on {{DialogBoxItem.date_approved}}
                            div
                                div
                                    v-card-text
                                        h3 Completed TA Duties
                                        v-row
                                            v-textarea(
                                                name="input-7-1"
                                                filled
                                                background-color="white"
                                                label=""
                                                auto-grow
                                                rounded
                                                :value="DialogBoxItem.duties_completed"
                                                outlined
                                                readonly )
                                        h3(v-if="DialogBoxItem.comment") Supervisor's Comment
                                        v-row(v-if="DialogBoxItem.comment")
                                            v-textarea(
                                                name="input-7-1"
                                                filled
                                                background-color="white"
                                                label=""
                                                auto-grow
                                                rounded
                                                :value="DialogBoxItem.comment"
                                                outlined
                                                readonly)
                                div(align="right")
                                    v-btn.ma-2(width=200 rounded outlined color="blue" right @click="close") Close
            template(v-slot:item.status='{ item }')
                v-icon.mr-2(small='', @click='editItem(item)') {{item.status}} (View Form)
</template>

<script>
import { mapGetters, mapActions } from "vuex";
export default {
  data: () => ({
    dialog: false,
    headers: [
      { text: "Date", value: "date_submitted" },
      { text: "Course Code", value: "course_code" },
      { text: "Course Name", value: "course_name" },
      { text: "TA Supervisor", value: "ta_supervisor" },
      { text: "Status", value: "status" }
    ],
    DialogBoxIndex: -1,
    DialogBoxItem: {
      course_code: "",
      course_name: "",
      duties_completed: "",
      comment: "",
      date_approved: "",
      status: ""
    },
    defaultItem: {
      course_code: "",
      course_name: "",
      duties_completed: "",
      comment: "",
      date_approved: "",
      status: ""
    }
  }),
  methods: {
    ...mapActions("pastAssignments", ["fetchPastAssignments"]),
    editItem(item) {
      this.DialogBoxIndex = this.pastAssignments.indexOf(item);
      this.DialogBoxItem = Object.assign({}, item);
      this.dialog = true;
    },
    close() {
      this.dialog = false;
      setTimeout(() => {
        this.DialogBoxItem = Object.assign({}, this.defaultItem);
        this.DialogBoxIndex = -1;
      }, 300);
    }
  },
  computed: {
    ...mapGetters("pastAssignments", ["pastAssignments"])
  },
  beforeMount() {
    this.fetchPastAssignments();
  }
};
</script>
