<template>
    <div class="subredditWrapper">
        <a style="text-decoration: none" 
            :href="'https://www.reddit.com/r/' + subredditName" 
            target="_blank">
            <div class="subredditContainer">
                <h3>/r/{{subredditName}}</h3>
                <h4>{{formatText(subredditPosts)}}</h4>
            </div>
        </a>
    </div>
</template>

<script>
export default {
    name: "SubredditContainer",
    props: {
        subredditName: String,
        subredditPosts: Number,
    },
    methods: {
        formatText(value) {
            return value === 1 ? `${value} post` : `${value} posts`
        }
    }
}
</script>

<style scoped>
div {
    border-radius: 15px;
}
div:hover {
    background-color: #FCA311;
}
.subredditWrapper {
    padding: 1rem;
    position: relative;
    /* background: linear-gradient(to right, red, purple); */
    background: #14213D;
    padding: 3px;
}
.subredditContainer {
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