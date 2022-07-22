<template>
    <h2>Comment Sentiment</h2>
    <div class="commentPolarityContainer">
        <ApexPieChart></ApexPieChart>
    </div>
</template>

<script scoped>
    import { store } from '../../main.js'
    import ApexPieChart from '../Interactive/ApexPieChart'

    export default {
        name: "UserCommentPolarity",
        components: {
            ApexPieChart,
        },
        data() {
            return {
                store,
            }
        }
    }
</script>

<style scoped>
    h2 {
        margin-top: 15px;
        margin-bottom: 15px;
    }
    .commentPolarityContainer {
        display: flex;
        margin-left: 160px;
        margin-right: auto;
        width: 80%;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        gap: 10px;
    }
</style>