<template>
    <div class="searchBarContainer">
        <label id="searchBarPrefix" for="username"><h3>{{prefix}}</h3></label>
        <input id="searchBarUsername" type="text" name="username" placeholder="Baorui" size="50">
        <Button id="searchBarButton" text="Search"></Button>
    </div>
</template>

<script>
import Button from "./Button"

export default {
    name: "SearchBar",
    props: {
        prefix: String,
        username: String,
    },
    components: {
        Button
    }
    
}
</script>

<style scoped>

    .searchBarContainer {

        display: flex;
        justify-content: center;
        vertical-align: baseline;
        gap: 2px;
    }

    .searchBarContainer > * {

        display: flex;
        border-radius: 5px;
        align-items: center;
        justify-content: center;
    }

    #searchBarPrefix {

        background-color: #EF9273;
        width: 50px;
        height: 40px;
    }

    #searchBarButton {

        width: 60px;
    }

    input {

        text-indent: 10px;
    }

</style>