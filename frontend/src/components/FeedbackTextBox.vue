<template lang="pug">
    v-card.rounded-card
        v-container.pa-2
            v-card-title
                 v-row
                    h4 EE213,Signals and Systems
                    v-col.text-right
                        v-chip.ma-2(color="#e3cceb" align="right" )  Submitted on 20th September,2019
            h3 Completed TA Duties

                div(class="text-center")
                    v-card-text
                        v-row
                            v-textarea(

                                    name="input-7-1"
                                    filled
                                    background-color="white"
                                    label=""
                                    auto-grow
                                    rounded
                                    value="Tutorial and attendance of EE batch(Tuesday and Thursday)"
                                    outlined
                            )
                        v-row
                            v-textarea(

                                name="input-7-1"
                                filled
                                background-color="white"
                                label=""
                                auto-grow
                                rounded
                                value="Tutorial and attendance of EE batch(Tuesday and Thursday)"
                                outlined
                            )
                div(align="right")
                    v-btn.ma-2(width=200 rounded outlined color="blue" right) Close
</template>

<script>
export default {
  name: "FeedbackTextBox"
};
</script>

<style scoped></style>
