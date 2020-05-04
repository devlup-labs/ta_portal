<template lang="pug">
    div
        h4.pa-5 SEP 2019 SEMESTER I, AY 2019-2020
        v-data-table.elevation-1(
            v-model="selected"
            :headers='headers'
            :items='currentApprovals',
            show-select
            sort-by='date_submitted')
            template(v-slot:top='')
                v-toolbar(flat='', color='white')
                    v-toolbar-title
                        v-tabs(v-model="current_course")
                            v-tab(v-for ="course in courses" :key = "course.id" ) {{ course.code }}
                    v-spacer
                    v-dialog(v-model='dialog', max-width='1000px')
                        v-card.rounded-card
                            v-container.pa-2
                                v-card-title
                                    v-row
                                        h4 Submission Details
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
                                            h3 Add Comments
                                            v-row
                                                v-textarea(
                                                    name="input-7-1"
                                                    filled
                                                    background-color="white"
                                                    label=""
                                                    auto-grow
                                                    rounded
                                                    v-model="DialogBoxItem.comment"
                                                    outlined
                                                    )
                                    div(align="right")
                                        v-btn.ma-2(width=200 rounded outlined color="blue" right @click="close") Close
                                        v-btn.ma-2(width=200 rounded color="#00948E" right @click="save") Save
            template(v-slot:item.action='{ item }')
                v-icon.mr-2(small='', @click='editItem(item)')  View Form
        div.pa-2 By clicking Approve,you are certifying that the above student(s) have successfully performed the ta duty equivalent to 8 hours per week.
        v-btn.ma-2(width=200 rounded color="#00948E" class="white--text" right @click.stop="approveDialog = true") Approve TA Release
        v-btn.ma-2(width=200 rounded outlined color="red" right @click.stop="approveDialog = true; disapproveDialog = true") Not Approved
        v-dialog(v-model = "approveDialog", max-width="290")
            v-card.align-center
                v-card-title(class="headline" v-if = "!disapproveDialog") Submit TA Approval?
                v-card-title(class="headline" v-else) Decline TA Approval?
                v-card-text This action cannot be undone
                v-card-actions
                    v-spacer
                    div
                        v-btn.ma-2(width=100 rounded outlined color="blue" right @click ="approveDialog = false; disapproveDialog = false") Close
                        v-btn.ma-2(width=100 rounded color="#00948E" class="white--text" right @click="submitApproval('2')" v-if = "!disapproveDialog") Submit
                        v-btn.ma-2(width=100 rounded color="red" class="white--text" right @click="submitApproval('3')" v-else) Submit

</template>

<script>
import { mapGetters, mapActions } from "vuex";
export default {
  data: () => ({
    dialog: false,
    approveDialog: false,
    disapproveDialog: false,
    current_course: 0,
    selected: [],
    headers: [
      { text: "Student Name", value: "name" },
      { text: "Roll no.", value: "roll_no" },
      { text: "Date of submission", value: "date_submitted" },
      { text: "Comments", value: "action" }
    ],
    DialogBoxIndex: -1,
    DialogBoxItem: {
      id: "",
      duties_completed: "",
      comment: ""
    },
    defaultItem: {
      id: "",
      duties_completed: "",
      comment: ""
    }
  }),
  methods: {
    ...mapActions("currentApprovalRequests", [
      "setCurrentCourse",
      "fetchCourses",
      "fetchCurrentApprovals",
      "addComment",
      "changeStatus"
    ]),
    editItem(item) {
      this.DialogBoxIndex = this.currentApprovals.indexOf(item);
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
    save() {
      if (this.DialogBoxIndex > -1) {
        this.addComment({
          id: this.DialogBoxItem.id,
          comment: this.DialogBoxItem.comment
        });
      }
      this.close();
    },
    submitApproval(status) {
      this.changeStatus({
        currentApprovals: this.selected,
        status: status
      });
      this.selected = [];
      this.approveDialog = false;
      this.disapproveDialog = false;
      this.fetchCurrentApprovals();
    }
  },
  computed: {
    ...mapGetters("currentApprovalRequests", ["courses", "currentApprovals"])
  },
  watch: {
    current_course: function(newVal) {
      this.selected = [];
      this.setCurrentCourse(this.courses[newVal].code);
    }
  },
  beforeMount() {
    this.setCurrentCourse(this.courses[this.current_course].code);
    this.fetchCourses();
    this.fetchCurrentApprovals();
  }
};
</script>
