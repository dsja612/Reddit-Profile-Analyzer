<template>
  <div class="container">
    <Header title="reddit app thing" info="just some info"></Header>
  </div>
  
</template>

<script>
import Header from "./components/Header"

export default {
  name: 'App',
  components: {
    Header
  }
}
</script>

<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400&display=swap');
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}
body {
  font-family: 'Poppins', sans-serif;
  background-color: #FEF9F8;
}
.container {
  max-width: 500px;
  margin: 15px auto;
  overflow: auto;
  min-height: 100px;
  /* border: 1px solid steelblue; */
  padding: 15px;
  border-radius: 5px;
  text-align: center;
  
}

h1, h2, h3, h4, h5 {

  color: #0d0d0d;
}
</style>

