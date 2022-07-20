<template>
    <div class="wordWrapper">
        <div class="wordContainer">
            <h2>{{word}}</h2>
            <h2>{{wordOccurrences}} times</h2>
        </div>
    </div>
</template>

<script>
    export default {
        name: "WordContainer",
        props: {
            subredditName: String,
            word: String,
            wordOccurrences: Number,
        }
    }
</script>

<style scoped>

    .wordWrapper {
        padding: 1rem;
        position: relative;
        background: linear-gradient(to right, #8A307F, #6883BC);
        padding: 3px;
    }
    .wordContainer {
        display: flex;
        background: #edddda;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding-left: 15px;
        padding-right: 15px;
        padding-top: 5px;
        padding-bottom: 5px;
    }
</style>