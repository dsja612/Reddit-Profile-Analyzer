<template>
    <div class="wrapper">
        <div class="circle" :style="{'background-color': colour}">
            <h2>{{value}}</h2>
        </div>
        <div>{{subject}}</div>
    </div>
    
</template>

<script>
    export default {
        name: "StatCircle",
        props: {
            value: Number,
            subject: String,
            colour: String,
        }
    }
</script>

<style scoped>
    .wrapper {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
</style>