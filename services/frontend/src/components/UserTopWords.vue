<template>
    <h2>Top Words</h2>
    <div class="wordsContainer">
        <template v-for="i in store.numWordsToShow">
            <WordContainer :word=Object.keys(store.topWords)[i-1] 
                :wordOccurrences=Object.values(store.topWords)[i-1]>
            </WordContainer>
        </template>
    </div>
    <SliderBar subject="words" ending="commented by user!" :storeLength=Object.keys(store.topWords).length></SliderBar>
</template>

<script scoped>
    import { store } from "../main.js"
    import SliderBar from "./SliderBar"
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