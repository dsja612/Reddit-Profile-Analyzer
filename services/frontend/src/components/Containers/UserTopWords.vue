<template>
    <h2>Top Words</h2>
    <SliderBar subject="words" ending="commented by user!" :subjectLength=Object.keys(store.topWords).length></SliderBar>
    <div class="wordsContainer">
        <template v-for="i in store.numWordsToShow">
            <WordContainer :word=Object.keys(store.topWords)[i-1] 
                :wordOccurrences=Object.values(store.topWords)[i-1]>
            </WordContainer>
        </template>
    </div>

</template>

<script scoped>
    import { store } from "../../main.js"
    import SliderBar from "../Interactive/SliderBar"
    import WordContainer from "./WordContainer"
    export default {
        name: "UserTopWords",
        components: {
            WordContainer,
            SliderBar,
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
        margin-top: -10px;
        margin-bottom: 15px;
    }
    .wordsContainer {
        display: flex;
        width: 80%;
        flex-direction: row;
        flex-wrap: wrap;
        justify-content: center;
        align-items: center;
        gap: 10px;
    }
</style>