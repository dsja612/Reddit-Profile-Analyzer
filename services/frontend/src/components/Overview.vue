<template>
    <div class="overviewContainer">
        <div class="userInfoContainer">
            <UserBasicInfo :username=store.username :userDateJoined=store.userDateJoined></UserBasicInfo>
        </div>

        <br><hr>

        <div class="userStatisticsContainer">
            <div class="userBasicStatisticsContainer">
                <StatCircle :value=store.numComments subject="comments" colour="#E3B448"></StatCircle>
                <StatCircle :value=store.numSubmissions subject="submissions" colour="#CBD18F"></StatCircle>
                <StatCircle :value=store.commentKarma subject="comment karma" colour="#FFBE7BFF"></StatCircle>
                <StatCircle :value=store.submissionKarma subject="post karma" colour="#EED971FF"></StatCircle>
            </div>

            <br><hr>

            <div class="userTopSubredditsContainer">
                <UserTopSubreddits></UserTopSubreddits>
            </div>

            <br><hr>
        </div>
    </div>
</template>

<script>
import { store } from '../main.js'
import UserBasicInfo from "./UserBasicInfo"
import StatCircle from "./StatCircle"
import UserTopSubreddits from"./UserTopSubreddits"
export default {
    name: "Overview",
    props: {

    },
    components: {
        UserBasicInfo,
        StatCircle,
        UserTopSubreddits,
    },
    data() {
        return {
            store,
        }
    }
}
</script>

<style scoped>

    .overviewContainer {
        max-width: 1200px;
        margin: auto;
        margin-bottom: 50px;
        min-height: 1000px;
        padding: 15px;
        border-radius: 5px;
        text-align: center;
        background-color: #edddda;
    }
    .userBasicStatisticsContainer {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 30px;
        gap: 50px;
    }

    .userTopSubredditsContainer {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        margin-top: 30px;
        gap: 20px;
    }
</style>

