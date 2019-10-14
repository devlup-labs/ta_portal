<template lang="pug">
  v-container
    v-row
      v-col(cols='12', sm='3')
        v-overflow-btn.my-2(:items='dropdown_item', label='Course Name', target='')
    v-data-table.elevation-1(v-model='selected', :headers='headers', :items='ta', :single-select='singleSelect', item-key='name', show-select='')
    div
      | By clicking Approve,you are certifying that the above student(s) have successfully performed the ta duty equivalent to * hours per week.
    .text-center
      v-row
        v-col(cols='12', sm='2')
          v-btn Approve
        v-col(cols='12', sm='2')
          v-btn Not Approved
</template>

<script>
export default {
  name: "ApprovalRequests",
  data: () => ({
    dropdown_item: ["EE212", "EE121", "EE213", "EE415"],
    headers: [
      {
        text: "Student Name",
        align: "left",
        sortable: false,
        value: "name"
      },
      { text: "Roll no.", value: "rollno" },
      { text: "Date of submission", value: "date" },
      { text: "Comments", value: "comments" }
    ],
    ta: [
      {
        name: "Student1",
        rollno: "M18ECE001",
        date: "Oct 1,2019",
        comments: "View/Edit"
      },
      {
        name: "Student2",
        rollno: "M18ECE004",
        date: "Oct 1,2019",
        comments: "View/Edit"
      },
      {
        name: "Student3",
        rollno: "M18ECE007",
        date: "Oct 1,2019",
        comments: "View/Edit"
      }
    ]
  })
};
</script>

<style scoped></style>
