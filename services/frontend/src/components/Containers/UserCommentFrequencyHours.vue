<template>
    <h2>Comment Frequency</h2>
    <ApexLineChart :height=350 titleText="Comment Frequency (last 100 comments)" xAxisText="Hour" yAxisText="Frequency" :yAxisMin=0 
    :yAxisMax=Math.max(...store.commentFreqHrs.values)
    :keys=store.commentFreqHrs.keys 
    :seriesToBeSent=seriesToBeSent></ApexLineChart>
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
            }
        }
    }
</script>

<style scoped>

</style>