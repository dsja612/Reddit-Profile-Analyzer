<template>
    <h2>Top Subreddits</h2>
    <div class="subredditsContainer">
        <SubredditContainer subredditName="bao" subredditPosts="50"></SubredditContainer>
        <SubredditContainer subredditName="ahloi" subredditPosts="800"></SubredditContainer>
        <SubredditContainer subredditName="roi" subredditPosts="800"></SubredditContainer>
        <SubredditContainer subredditName="maang" subredditPosts="800"></SubredditContainer>
        <SubredditContainer subredditName="miserycat" subredditPosts="800"></SubredditContainer>
        <SubredditContainer subredditName="yash" subredditPosts="800"></SubredditContainer>
    </div>
</template>

<script>
    import SubredditContainer from "./SubredditContainer"
    export default {
        name: "UserTopSubreddits",
        components: {
            SubredditContainer,
        }
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