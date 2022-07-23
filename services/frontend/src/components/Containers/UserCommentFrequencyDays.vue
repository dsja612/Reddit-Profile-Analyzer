<template>
    <h2>Comment Frequency</h2>
    <ApexLineChart :height=350 titleText="Comment Frequency (Days)" xAxisText="Day" yAxisText="Frequency" :yAxisMin=0 
    :yAxisMax=Math.max(...store.commentFreqDays.values)
    :keys=store.commentFreqDays.keys 
    :seriesToBeSent=seriesToBeSent 
    :colors=colorsToBeSent></ApexLineChart>
</template>

<script>
    import { store } from "../../main.js"
    import ApexLineChart from "../Interactive/ApexLineChart"
    export default {
        name: "UserCommentFrequencyDays",
        components: {
            ApexLineChart,
        },
        data() {
            return { 
                store,
                seriesToBeSent: [
                    {
                        name: "Frequency",
                        data: store.commentFreqDays.values
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