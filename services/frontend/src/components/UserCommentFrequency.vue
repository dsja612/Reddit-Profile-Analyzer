<template>
    <h2>Comment Frequency</h2>
    <ApexLineChart :height=350 titleText="Comment Frequency (last 100 comments)" xAxisText="Day" yAxisText="Frequency" :yAxisMin=0 
    :yAxisMax=Math.max(...store.commentFreqDays.values)
    :keys=store.commentFreqDays.keys 
    :seriesToBeSent=seriesToBeSent></ApexLineChart>
</template>

<script>
    import { store } from "../main.js"
    import ApexLineChart from "./ApexLineChart"
    export default {
        name: "UserCommentFrequency",
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
            }
        }
    }
</script>

<style scoped>

</style>