<template>
    <div>
  <v-app id="inspire">
    <v-container id="dropdown-example">
      <v-row>
        <v-col cols="12" sm="3">
          <v-overflow-btn
            class="my-2"
            :items="dropdown_item"
            label="Course Name"
            target="#dropdown-example"
          ></v-overflow-btn>
        </v-col>
      </v-row>
    </v-container>
  <v-data-table
    v-model="selected"
    :headers="headers"
    :items="ta"
    :single-select="singleSelect"
    item-key="name"
    show-select
    class="elevation-1"
  >
    </v-data-table>
  <div>By clicking Approve,you are certifying that the above student(s) have succesfully performed the ta duty equivaent to * hours per week.</div>
  <div class="text-center">
 <v-row>
   <v-col cols="12" sm="2">
   <v-btn>Approve</v-btn>
   </v-col>
   <v-col cols="12" sm="2">
   <v-btn>Not Approved</v-btn>
   </v-col>
   </v-row>
  </div>
  </v-app>
</div>
</template>

<script>
export default {
  name: "ApprovalRequests",
  data: () => ({
    dropdown_item: ['EE212', 'EE121', 'EE213', 'EE415'],
    headers: [
          {
            text: 'Student Name',
            align: 'left',
            sortable: false,
            value: 'name',
          },
          { text: 'Roll no.', value: 'rollno' },
          { text: 'Date of submission', value: 'date' },
          { text: 'Comments', value: 'comments'},
        ],
        ta: [
          {
            name: 'Student1',
            rollno: 'M18ECE001',
            date: 'Oct 1,2019',
            comments: 'View/Edit',
          },
          {
            name: 'Student2',
            rollno: 'M18ECE004',
            date: 'Oct 1,2019',
            comments: 'View/Edit',
          },
          {
            name: 'Student3',
            rollno: 'M18ECE007',
            date: 'Oct 1,2019',
            comments: 'View/Edit',
          },
        ],
    }),
};
</script>

<style scoped></style>