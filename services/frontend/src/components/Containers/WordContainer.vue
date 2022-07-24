<template>
    <div class="wordWrapper">
        <a style="text-decoration: none" 
            :href="'https://www.dictionary.com/browse/' + word" 
            target="_blank">
            <div class="wordContainer">
                <h3>{{word}}</h3>
                <h5>{{formatText(wordOccurrences)}}</h5>
            </div>
        </a>
    </div>
</template>

<script>
export default {
    name: "WordContainer",
    props: {
        subredditName: String,
        word: String,
        wordOccurrences: Number,
    },
    methods: {
        formatText(value) {
            return value === 1 ? `${value} time` : `${value} times`
        }
    }
}
</script>

<style scoped>

/* .wordWrapper {
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
} */

div {
    border-radius: 15px;
    display: inline-block;
}
div:hover {
    background-color: #FCA311;
}
.wordWrapper {
    padding: 1rem;
    position: relative;
    /* background: linear-gradient(to right, red, purple); */
    background: #14213D;
    padding: 3px;
}
.wordContainer {
    display: flex;
    background: #17274b;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding-left: 15px;
    padding-right: 15px;
    padding-top: 5px;
    padding-bottom: 5px;
    color: white;
}
</style>