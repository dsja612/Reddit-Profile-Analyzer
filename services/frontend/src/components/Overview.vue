<template>
    <div class="overviewContainer">
        <div class="userInfoContainer">
            <!-- username probably from GET request (?) -->
            <UserBasicInfo username="ahbao" userDateJoined="maang date"></UserBasicInfo>
        </div>

        <br><hr>

        <div class="userStatisticsContainer">
            <div class="userBasicStatisticsContainer">
                <StatCircle value="1000" subject="comments" colour="#4affe6"></StatCircle>
                <StatCircle value="15000" subject="submissions"></StatCircle>
                <StatCircle value="4650" subject="comment karma"></StatCircle>
                <StatCircle value="310203" subject="post karma"></StatCircle>
            </div>

            <br><hr>

            <div class="userTopSubredditsContainer">

                <!-- add data from request -->
                <UserTopSubreddits></UserTopSubreddits>
            
            </div>

            <br><hr>
        </div>

        
    </div>
</template>

<script>
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
    }
}
</script>

<style scoped>

    .overviewContainer {
        /* probably set display to show only when button is clicked and user exists */
        /* display: none; */
        max-width: 1200px;
        margin: auto;
        margin-bottom: 50px;
        overflow: auto;
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

