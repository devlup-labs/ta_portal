<template lang="pug">
    v-card(flat)
        v-card-title(justify="center")
            h2(class="headline") User Profile
        v-card-text
            v-container
                v-row
                    v-col(cols="12")
                        v-text-field(solo-inverted label="Name" required)
                    v-col(cols="12" sm="6" md="6")
                        v-text-field(solo-inverted label="Roll no.")
                    v-col(cols="12" sm="6" md="6")
                        v-text-field(solo-inverted label="Programme" required)
                    v-col(cols="12")
                        v-text-field(solo-inverted label="Email" required)
                    v-col(cols="12")
                        v-text-field(solo-inverted label="Contact no." required)
                        h3 Educational Background
                v-row
                    v-col(cols="12" sm="6")
                        v-select(solo-inverted :items="['Electrical Engineering', 'Electronics and Comunication Engineering', ]"
                            label="B.Tech Specialisation"
                            required)
                    v-col(cols="12" sm="6")
                        v-select(solo-inverted :items="['Electrical Engineering', 'Electronics and Comunication Engineering', 'Any other option' ]"
                            label="M.Sc/M.Tech Specialisation"
                            multiple)
                    v-col(cols="12")
                        v-text-field(solo-inverted label="Area of Research" required)
        v-card-actions
            div(class="flex-grow-1")
            v-btn(color="blue darken-1" text @click="dialog = false") Close
            v-btn(color="blue darken-1" text @click="dialog = false") Save
</template>

<style scoped></style>

<script>
export default {
  name: "Profile",
  data() {
    return {};
  }
};
</script>
