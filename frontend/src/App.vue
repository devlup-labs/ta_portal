<template lang="pug">
    v-if()
     v-app
        v-app-bar(app clipped-left color="primary" height="100")
            v-app-bar-nav-icon(@click="drawer = !drawer")
            v-col
                v-row TA MANAGEMENT PORTAL
                v-row Department of Electrical Engineering,IIT JODHPUR
                    v-avatar(color=" ")
                        v-icon(mdi-account-circle)
            v-col
                v-row(col="2" offset-md="4") Name
                v-row(col="2") Teaching Assistant
        v-navigation-drawer(v-model="drawer" app clipped color="grey lighten-4")
            v-list(dense class="grey lighten-4")
                template(v-for="(item, i) in items")
                    v-row(v-if="item.heading" :key="i" align="center")
                        v-col(cols="6")
                            v-subheader(v-if="item.heading") {{ item.heading }}
                    v-divider(v-else-if="item.divider" :key="i" dark class="my-4")
                    v-list-item(v-else :key="i" @click="")
                        v-list-item-action
                            v-icon {{ item.icon }}
                        v-list-item-content
                            v-list-item-title(class="grey--text") {{ item.text }}
        v-content
            router-view
</template>

<script>
    export default {
        name: "App",
        data: () => ({
            drawer: null,
            items: [
                { heading: "TA Assignments" },
                { icon: "mdi-notebook", text: "Current" },
                { icon: "mdi-reload", text: "Past" },
                { divider: true },
                { heading: "Academics" },
                { icon: "mdi-calendar", text: "Calendar" },
                { icon: "mdi-calendar-clock", text: "Time Table" }
            ]
        })
    };
</script>