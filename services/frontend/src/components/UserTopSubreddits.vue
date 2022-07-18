<template>
    <h2>Top Subreddits</h2>
    <div class="subredditsContainer">
        <template v-for="i in store.numSubsToShow">
            <SubredditContainer :subredditName=Object.keys(store.topSubreddits)[i-1] 
                :subredditPosts=Object.values(store.topSubreddits)[i-1]>
            </SubredditContainer>
        </template>

        <!-- <SubredditContainer v-for="(posts, name) in store.topSubreddits" :key="name"
            :subredditName="name" :subredditPosts="posts">
        </SubredditContainer> -->
    </div>
    <SliderBar></SliderBar>
</template>

<script>
    import SubredditContainer from "./SubredditContainer"
    import SliderBar from "./SliderBar"
    import { store } from '../main.js'

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
    .subredditsContainer {
        display: flex;
        width: 70%;
        flex-direction: row;
        flex-wrap: wrap;
        justify-content: center;
        align-items: center;
        gap: 10px;
    }
</style>