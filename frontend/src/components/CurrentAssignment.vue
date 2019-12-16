<template lang="pug">
    div
        h4.pa-5 SEP 2019 SEMESTER I, AY 2019-2020
        v-data-table.elevation-1(
            :headers='headers'
            item-key='course_code'
            :items='currentAssignments'
            sort-by='course_code')
            template(v-slot:top='')
                v-spacer
                v-dialog(v-model='dialog', max-width='1000px')
                    v-card.rounded-card
                        v-container.pa-2
                            v-card-title
                                v-row
                                    h4 {{DialogBoxItem.course_code}}, {{DialogBoxItem.course_name}}
                                    v-col.text-right
                                        v-chip.ma-2(color="#FCF9EB" align="right"
                                            v-if="DialogBoxItem.status === 'Pending Approval'")  Submitted on {{DialogBoxItem.date_submitted}}
                                        v-chip.ma-2(color="#E4F5F5" align="right"
                                            v-else-if="DialogBoxItem.status === 'Approved'")  Approved on {{DialogBoxItem.date_approved}}
                                        v-chip.ma-2(color="#E5CCD4" align="right"
                                            v-else-if="DialogBoxItem.status === 'Not Approved'")  Declined on {{DialogBoxItem.date_approved}}
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
                                                v-model="DialogBoxItem.duties_completed"
                                                outlined
                                                :readonly="isReadOnly")
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
                                    v-btn.ma-2(width=200 rounded outlined color="blue" right @click="update"
                                                v-if="DialogBoxItem.status === 'Not Approved'") Resubmit
                                    v-btn.ma-2(width=200 rounded color="#00948E" right @click="submit"
                                        v-if="DialogBoxItem.status === 'Submit TA Release Request'") Send
            template(v-slot:item.status='{ item }')
                v-icon.mr-2(small='', @click='editItem(item)') {{item.status}} (View Form)
</template>

<script>
import { mapGetters, mapActions } from "vuex";
export default {
  data: () => ({
    dialog: false,
    headers: [
      { text: "Course Code", value: "course_code" },
      { text: "Course Name", value: "course_name" },
      { text: "TA Supervisor", value: "ta_supervisor" },
      { text: "Status", value: "status" },
      { text: "Due By", value: "due_by" }
    ],
    DialogBoxIndex: -1,
    DialogBoxItem: {
      id: "",
      course_code: "",
      course_name: "",
      duties_completed: "",
      comment: "",
      date_approved: "",
      date_submitted: "",
      status: ""
    },
    defaultItem: {
      id: "",
      course_code: "",
      course_name: "",
      duties_completed: "",
      comment: "",
      date_approved: "",
      date_submitted: "",
      status: ""
    }
  }),
  methods: {
    ...mapActions("currentAssignments", [
      "fetchUnSubmittedAssignments",
      "fetchCurrentAssignments",
      "updateCurrentAssignment",
      "submitCurrentAssignment"
    ]),
    editItem(item) {
      this.DialogBoxIndex = this.currentAssignments.indexOf(item);
      this.DialogBoxItem = Object.assign({}, item);
      this.dialog = true;
    },
    close() {
      this.dialog = false;
      setTimeout(() => {
        this.DialogBoxItem = Object.assign({}, this.defaultItem);
        this.DialogBoxIndex = -1;
      }, 300);
    },
    update() {
      if (this.DialogBoxIndex > -1) {
        this.updateCurrentAssignment({
          current_id: this.DialogBoxItem.id,
          duties: this.DialogBoxItem.duties_completed
        });
      }
      this.close();
    },
    submit() {
      if (this.DialogBoxIndex > -1) {
        this.submitCurrentAssignment({
          duties_completed: this.DialogBoxItem.duties_completed,
          assignment: this.DialogBoxItem.id
        });
      }
      this.close();
    }
  },
  computed: {
    ...mapGetters("currentAssignments", ["currentAssignments"]),
    isReadOnly() {
      return (
        this.DialogBoxItem.status === "Pending Approval" ||
        this.DialogBoxItem.status === "Approved"
      );
    }
  },
  beforeMount() {
    this.fetchUnSubmittedAssignments();
  }
};
</script>
