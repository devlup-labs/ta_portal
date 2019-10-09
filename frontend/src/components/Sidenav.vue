<template lang="pug">
    v-navigation-drawer(:value="drawer" app clipped color="grey lighten-4")
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
import { mapGetters } from "vuex";
export default {
  name: "Sidenav",
  props: {
    drawer: Boolean
  },
  data() {
    return {};
  },
  computed: {
    ...mapGetters("sidenav", ["items"])
  }
};
</script>

<style scoped></style>
