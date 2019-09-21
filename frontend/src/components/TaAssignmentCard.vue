<template lang="pug">
    v-data-table(
        v-model="selected"
        :headers="headers"
        :items="courses"
        :single-select="singleSelect"
        item-key="name"
        show-select
        class="elevation-1")

</template>

<script>
export default {
  name: "TaAssignmentCard",
  data() {
    return {
      singleSelect: false,
      selected: [],
      headers: [
        {
          text: "COURSE",
          align: "left",
          sortable: false,
          value: "name"
        },
        { text: "TA SUPERVISOR", value: "supervisor" },
        { text: "REQUIRED", value: "required" },
        { text: "ASSIGNED TA", value: "assigned" }
      ],
      courses: [
        {
          name: "EE121 Course Name[L-T-P]",
          supervisor: "Faculty Name",
          required: 5,
          assigned: 0
        },
        {
          name: "EE221 Course Name[L-T-P]",
          supervisor: "Faculty Name",
          required: 7,
          assigned: 2
        },
        {
          name: "EE122 Course Name[L-T-P]",
          supervisor: "Faculty Name",
          required: 3,
          assigned: 2
        },
        {
          name: "EE321 Course Name[L-T-P]",
          supervisor: "Faculty Name",
          required: 7,
          assigned: 4
        },
        {
          name: "EE241 Course Name[L-T-P]",
          supervisor: "Faculty Name",
          required: 2,
          assigned: 1
        },
        {
          name: "EE241 Course Name[L-T-P]",
          supervisor: "Faculty Name",
          required: 2,
          assigned: 1
        },
        {
          name: "EE241 Course Name[L-T-P]",
          supervisor: "Faculty Name",
          required: 2,
          assigned: 1
        },
        {
          name: "EE241 Course Name[L-T-P]",
          supervisor: "Faculty Name",
          required: 2,
          assigned: 1
        },
        {
          name: "EE241 Course Name[L-T-P]",
          supervisor: "Faculty Name",
          required: 2,
          assigned: 1
        },
        {
          name: "EE241 Course Name[L-T-P]",
          supervisor: "Faculty Name",
          required: 2,
          assigned: 1
        },
        {
          name: "EE241 Course Name[L-T-P]",
          supervisor: "Faculty Name",
          required: 2,
          assigned: 1
        },
        {
          name: "EE241 Course Name[L-T-P]",
          supervisor: "Faculty Name",
          required: 2,
          assigned: 1
        },
        {
          name: "EE241 Course Name[L-T-P]",
          supervisor: "Faculty Name",
          required: 2,
          assigned: 1
        },
        {
          name: "EE241 Course Name[L-T-P]",
          supervisor: "Faculty Name",
          required: 2,
          assigned: 1
        },
        {
          name: "EE241 Course Name[L-T-P]",
          supervisor: "Faculty Name",
          required: 2,
          assigned: 1
        },
        {
          name: "EE241 Course Name[L-T-P]",
          supervisor: "Faculty Name",
          required: 2,
          assigned: 1
        },
        {
          name: "EE241 Course Name[L-T-P]",
          supervisor: "Faculty Name",
          required: 2,
          assigned: 1
        },
          {
              name: "EE241 Course Name[L-T-P]",
              supervisor: "Faculty Name",
              required: 2,
              assigned: 1
          },
          {
              name: "EE241 Course Name[L-T-P]",
              supervisor: "Faculty Name",
              required: 2,
              assigned: 1
          },
          {
              name: "EE241 Course Name[L-T-P]",
              supervisor: "Faculty Name",
              required: 2,
              assigned: 1
          },
          {
              name: "EE241 Course Name[L-T-P]",
              supervisor: "Faculty Name",
              required: 2,
              assigned: 1
          },
          {
              name: "EE241 Course Name[L-T-P]",
              supervisor: "Faculty Name",
              required: 2,
              assigned: 1
          },
          {
              name: "EE241 Course Name[L-T-P]",
              supervisor: "Faculty Name",
              required: 2,
              assigned: 1
          },
          {
              name: "EE241 Course Name[L-T-P]",
              supervisor: "Faculty Name",
              required: 2,
              assigned: 1
          },
          {
              name: "EE241 Course Name[L-T-P]",
              supervisor: "Faculty Name",
              required: 2,
              assigned: 1
          }
      ]
    };
  }
};
</script>

<style>
thead.v-data-table-header tr {
  background-color: #ebfdfd;
}
</style>
