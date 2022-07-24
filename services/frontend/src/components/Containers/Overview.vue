<template>
    <div class="overviewContainer">
        <div class="userInfoContainer">
            <UserBasicInfo :username=store.username :userDateJoined=store.userDateJoined></UserBasicInfo>
        </div>

        <div class="userStatisticsContainer">
            <div class="userBasicStatisticsContainer">
                <StatCard :value=store.numComments subject="comments" icon="pi-comment"></StatCard>
                <StatCard :value=store.numSubmissions subject="submissions" icon="pi-upload"></StatCard>
                <StatCard :value=store.commentKarma subject="comment karma" icon="pi-arrow-up"></StatCard>
                <StatCard :value=store.submissionKarma subject="post karma" icon="pi-arrow-circle-up"></StatCard>
            </div>

        <div v-if="Object.values(store.commentSentiment).length !== 0">
            
            <br ref="subBreak"><hr>

            <div class="userTopSubredditsContainer">
                <UserTopSubreddits></UserTopSubreddits>
            </div>

            <br ref="wordBreak"><hr>

            <div class="userTopWordsContainer">
                <UserTopWords></UserTopWords>
            </div>

            <br><hr>

            <div class="userCommentPolarityContainer">
                <UserCommentPolarity></UserCommentPolarity>
            </div>

            <div class="userSentimentContainer">
                <CommentTable></CommentTable>
            </div>

            <br><hr>

            <div class="userCommentFrequencyContainer">
                <UserCommentFrequencyDays></UserCommentFrequencyDays>
                <UserCommentFrequencyHours></UserCommentFrequencyHours>
            </div>
        </div>
        <div class="errorMessageContainer" v-else>
            <br ref="subBreak"><hr>
            <h3>There are no comments to analyse (excluding deleted comments).</h3>
        </div>
        </div>
    </div>
</template>

<script>
import { store } from '../../main.js'
import UserBasicInfo from "./UserBasicInfo"
import StatCard from "../Cards/StatCard"
import UserTopSubreddits from"./UserTopSubreddits"
import UserTopWords from "./UserTopWords"
import UserCommentPolarity from "./UserCommentPolarity"
import CommentTable from "../Interactive/CommentTable"
import UserCommentFrequencyDays from "./UserCommentFrequencyDays"
import UserCommentFrequencyHours from "./UserCommentFrequencyHours"

export default {
    name: "Overview",
    props: {

    },
    components: {
        UserBasicInfo,
        StatCard,
        UserTopSubreddits,
        UserTopWords,
        UserCommentPolarity,
        CommentTable,
        UserCommentFrequencyDays,
        UserCommentFrequencyHours,
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
    border-radius: 25px;
    text-align: center;
    background-color: white;
}

.userBasicStatisticsContainer, .userTopSubredditsContainer, .userTopWordsContainer, .userSentimentContainer, 
.userCommentFrequencyContainer, .errorMessageContainer
{
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 30px;
}   
.userBasicStatisticsContainer {
    gap: 50px;
}

.userTopSubredditsContainer, .userTopWordsContainer, .userCommentFrequencyContainer {
    flex-direction: column;
    gap: 20px;
}

.userInfoContainer {
    margin: 10px;
}

</style>

