<template>
    <div class="subredditWrapper">
        <div class="subredditContainer">
            <h2>/r/{{subredditName}}</h2>
            <h2>{{subredditPosts}} posts</h2>
        </div>
    </div>
</template>

<script>
    export default {
        name: "SubredditContainer",
        props: {
            subredditName: String,
            subredditPosts: Number,
        }
    }
</script>

<style scoped>

    .subredditWrapper {
        padding: 1rem;
        position: relative;
        background: linear-gradient(to right, red, purple);
        padding: 3px;
    }
    .subredditContainer {
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