<template>
    <h2>Top Subreddits</h2>
    <div class="subredditsContainer">
        <template v-for="i in store.numSubsToShow">
            <SubredditContainer :subredditName=Object.keys(store.topSubreddits)[i-1] 
                :subredditPosts=Object.values(store.topSubreddits)[i-1]>
            </SubredditContainer>
        </template>
    </div>
    <SliderBar subject="subreddits" ending="commented or posted on!" :subjectLength=Object.keys(store.topSubreddits).length></SliderBar>
</template>

<script scoped>
    import SubredditContainer from "./SubredditContainer"
    import SliderBar from "../Interactive/SliderBar"
    import { store } from '../../main.js'

    export default {
        name: "UserTopSubreddits",
        components: {
            SubredditContainer,
            SliderBar,
        },
        data() {
            return {
                store,
            }
        },
    }
</script>

<style scoped>
    h2 {
        margin-top: -10px;
        margin-bottom: 15px;
    }
    .subredditsContainer {
        display: flex;
        width: 80%;
        flex-direction: row;
        flex-wrap: wrap;
        justify-content: center;
        align-items: center;
        gap: 10px;
    }
</style>