<template>
  <v-card>
      <h4>October 1</h4>
  <v-data-table
    :headers="headers"
    :items="data"
    :sort-by="['calories', 'fat']"
    :sort-desc="[false, true]"
    multi-sort
    class="elevation-1"
  ></v-data-table>
  </v-card>
</template>

<script>
export default {
  name: "CurrentAssignment",
  data () {
      return {
        headers: [
          {
            text: 'Course Code ',
            align: 'left',
            sortable: false,
            value: 'name',
          },
          { text: 'Course name', value: 'coursename' },
          { text: 'TA Supervisor', value: 'supervisor' },
          { text: 'Status', value: 'status' },
          { text: 'Due By', value: 'duedate' },
          
        ],
        data: [
          {
            name: 'EE213',
            coursename: 'Signals and System',
            supervisor: 'TA name',
            status: 'submit/due',
            duedate: '1 oct',
          },
          {
            name: 'EE213',
            coursename: 'Basic Electronics',
            supervisor: 'TA name',
            status: 'submit/due',
            duedate: '--',
          },
          {
            name: 'EE213',
            coursename: 'Electronics Lab',
            supervisor: 'TA name',
            status: 'submit/due',
            duedate: '--',
          },
          
        ],
      }
    },
  };

</script>

<style scoped></style>