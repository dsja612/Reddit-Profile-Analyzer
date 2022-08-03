<template>
    <div class="usernameDiv">
        <h1 id="usernamePrefix">Overview for </h1>
        <h1 id="usernameSuffix"> 
            <a style="text-decoration: none" 
            :href="'https://www.reddit.com/user/' + username" 
            target="_blank">
                /u/{{username}} 
            </a>
        </h1>
    </div>
    <div class="usernameDiv">
        <h3 id="userDateJoinedPrefix"> Joined Reddit </h3>
        <h3 id="userDateJoinedSuffix">{{getAge(userDateJoined)}} years ago</h3>
        <h3> on </h3>
        <h3 id="userDateJoinedSuffix">{{formatDateString(userDateJoined)}}.</h3>
    </div>
    <div class="subTextDiv" style="color: #575757;">
        <h4>*Overview includes deleted comments & submissions; activity and comment analysis is based on 200 most recent comments</h4>
    </div>
    
</template>

<script>
export default {
    name: "UserBasicInfo",
    props: {
        username: String,
        userDateJoined: Date,
    },
    methods: {
        formatDateString(date) {
            var options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' }
            return date.toLocaleDateString("en-US", options)
        },
        getAge(date) {
            var ageDate = new Date(Date.now() - date)
            return Math.abs(ageDate.getUTCFullYear() - 1970)
        }
    }
}
</script>

<style>
.usernameDiv > * {
    display: inline-block;
    margin: 0 3px 20px;
}

#usernameSuffix {
    color: #FCA311;
}

#usernameSuffix:hover {
    background-color: #E5E5E5;
}

#userDateJoinedSuffix {
    color: #FCA311;
}
a {
    color: #FCA311;
}
</style>
