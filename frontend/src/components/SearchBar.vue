<template>
    <div class="searchBarContainer">
        <label id="searchBarPrefix" for="username">{{prefix}}</label>
        <input id="searchBarUsername" type="text" name="username" placeholder="Baorui" size="35">
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

    .searchBarContainer{

        display: flex;
        justify-content: center;
        vertical-align: baseline;
        gap: 2px;
    }

    .searchBarContainer > * {

        display: flex;
        border-radius: 5px;
    }

    #searchBarPrefix{

        background-color: #EF9273;
    }

</style>