<template lang="pug">
    v-navigation-drawer(v-model="drawer" app clipped color="grey lighten-4")
        v-list(dense class="grey lighten-4")
            template(v-for="(item, i) in items")
                v-row(v-if="item.heading" :key="i" align="center")
                    v-col(cols="6")
                        v-subheader(v-if="item.heading") {{ item.heading }}
                v-divider(v-else-if="item.divider" :key="i" dark class="my-4")
                v-list-item(v-else :key="i" @click="" :to="{name:item.name}")
                    v-list-item-action
                        v-icon {{ item.icon }}
                    v-list-item-content
                        v-list-item-title(class="grey--text") {{ item.text }}
</template>



<script>
//import routes from '../router.js';
export default {
  name: "Sidenav",
  props: ["drawer"],
  data() {
    return {
      items: [
        { heading: "TA Assignments" },
        { icon: "mdi-notebook", text: "Current", name:"current" },
        { icon: "mdi-reload", text: "Past", name:"past" },
        { divider: true },
        { heading: "Academics" },
        { icon: "mdi-calendar", text: "Calendar", },
        { icon: "mdi-calendar-clock", text: "Time Table",  }
      ]
    };
  }
};
</script>

<style scoped></style>
