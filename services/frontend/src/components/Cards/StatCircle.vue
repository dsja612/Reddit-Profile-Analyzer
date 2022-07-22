<template>
    <div class="wrapper">
        <div class="circle" :style="{'background-color': colour, border: '1px solid'}">
            <h2>{{value}}</h2>
        </div>
        <h3>{{subject}}</h3>
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