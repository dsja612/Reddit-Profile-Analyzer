<template>
    <!-- icon -->
    <!-- title -->
    <!-- info -->
    <!-- search bar -->

    <header>
        <i class="fa-brands fa-reddit fa-2x"></i>
        <h2>{{title}}</h2>
        <h2>{{info}}</h2>
        <SearchBar prefix="/u/" username="baorui"/>
    </header>
    
</template>

<script>
import SearchBar from "./SearchBar"

export default {

    name: 'Header',
    props: {

        title: String,
        info: String
    },
    components: {
        SearchBar
    }
}
</script>

<style scoped>

</style>