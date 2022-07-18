<template>
  <Slider v-model="value" :min="1" :max="10"></Slider>
</template>

<script>
  import Slider from '@vueform/slider'

  export default {
    components: {
      Slider,
    },
    data() {
      return {
        value: 20,
      }
    }
  }
</script>

<style src="@vueform/slider/themes/default.css"></style>