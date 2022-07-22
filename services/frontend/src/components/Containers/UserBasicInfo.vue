<template>
    <div class="usernameDiv">
        <h1 id="usernamePrefix">Overview for </h1>
        <h1 id="usernameSuffix">/u/{{username}}</h1>
    </div>
    <div class="usernameDiv">
        <h3 id="userDateJoinedPrefix"> Joined Reddit </h3>
        <!-- <h3 id="userDateJoinedSuffix">{{getAge(userDateJoined)}} years ago on {{formatDateString(userDateJoined)}}.</h3> -->
        <h3 id="userDateJoinedSuffix">{{getAge(userDateJoined)}} years ago</h3>
        <h3> on </h3>
        <h3 id="userDateJoinedSuffix">{{formatDateString(userDateJoined)}}.</h3>
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
    display: inline;
}

#usernameSuffix {
    color: #FCA311;
}

#userDateJoinedSuffix {
    color: #FCA311;
}
</style>
