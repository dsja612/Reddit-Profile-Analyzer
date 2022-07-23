<template>
    <ApexLineChart :height=350 titleText="Comment Frequency (Hours)" xAxisText="Hour" yAxisText="Frequency" :yAxisMin=0 
    :yAxisMax=Math.max(...store.commentFreqHrs.values)
    :keys=store.commentFreqHrs.keys 
    :seriesToBeSent=seriesToBeSent 
    :colors=colorsToBeSent></ApexLineChart>
</template>

<script>
    import { store } from "../../main.js"
    import ApexLineChart from "../Interactive/ApexLineChart"
    export default {
        name: "UserCommentFrequencyHours",
        components: {
            ApexLineChart,
        },
        data() {
            return { 
                store,
                seriesToBeSent: [
                    {
                        name: "Frequency",
                        data: store.commentFreqHrs.values
                    },
                ],
                colorsToBeSent: [
                    '#B1967C'
                ],
            }
        }
    }
</script>

<style scoped>

</style>