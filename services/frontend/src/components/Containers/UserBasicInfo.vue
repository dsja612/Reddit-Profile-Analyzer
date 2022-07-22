<template>
    <div class="usernameDiv">
        <h1 id="usernamePrefix">Overview for </h1>
        <h1 id="usernameSuffix">/u/{{username}}</h1>
    </div>
    <div class="usernameDiv">
        <h3 id="userDateJoinedPrefix">Joined Reddit on </h3>
        <h3 id="userDateJoinedSuffix">{{userDateJoined}}</h3>
    </div>
    
</template>

<script>
export default {
    name: "UserBasicInfo",
    props: {
        username: String,
        userDateJoined: Date,
    }
}
</script>

<style>
    .usernameDiv > * {
        display: inline;
    }

    #usernameSuffix {
        color: teal;
    }

    #userDateJoinedSuffix {
        color: purple;
    }

</style>
