<template lang="pug">

        v-card(class="rounded-card")
            div(class="movement")
                v-card-title
                     v-row
                        h4 EE213,Signals and Systems
                        v-col(class="rightside")
                            v-chip(  class="ma-2 " color="#e3cceb" align="right" )  Submitted on 20th September,2019
                h3 Completed TA Duties

                    div(class="text-center")
                        v-card-text
                            v-row
                                v-textarea(
                                        class="tarea1"
                                        name="input-7-1"
                                        filled
                                        background-color="white"
                                        label=""
                                        auto-grow
                                        rounded
                                        value="Tutorial and attendance of EE batch(Tuesday and Thursday)"
                                )
                            v-row
                                v-textarea(
                                    class="tarea2"
                                    name="input-7-1"
                                    filled
                                    background-color="white"
                                    label=""
                                    auto-grow
                                    rounded
                                    value="Tutorial and attendance of EE batch(Tuesday and Thursday)"
                                )
                    div(align="right")
                        v-btn(class="ma-2 fbtn" rounded outlined color="blue" right) Close
</template>

<script>
export default {
    name: "FeedbackTextBox",
};
</script>

<style scoped>
    .movement{
        padding:2%;
    }
    .tarea1{
        border:lightgrey 0.5px solid;
    }
    .tarea2{
        border:lightgrey 0.5px solid;
        margin-top: 2%;
    }
    .fbtn{
        width: 200px;
    }
    .rightside{
        text-align: right;
    }
</style>
