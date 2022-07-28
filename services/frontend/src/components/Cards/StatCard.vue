<template>
    <!-- <div class="wrapper">
        <div class="circle" :style="{'background-color': colour, border: '1px solid'}">
            <h2>{{value}}</h2>
        </div>
        <h3>{{subject}}</h3>
    </div> -->

    <Card style="width: 25em">
        <template #header>
            <i :class="[{'pi': true}, icon ? 'pi ' + icon : '']" style="font-size: 2rem"></i>
        </template>
        <template #title>
            {{value}}
        </template>
        <template #content>
            {{subject}}
        </template>
    </Card>
    
</template>

<script>
import Card from 'primevue/card';

    export default {
        name: "StatCard",
        props: {
            value: Number,
            subject: String,
            icon: {
                type: String,
                required: false,
                default: ''
            }
        },
        components: {
            Card
        }
    }
</script>

<style scoped>
/* .wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
} */
</style>