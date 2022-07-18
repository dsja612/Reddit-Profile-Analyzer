<template>
  <h4>Subreddits</h4>
  <vue3-slider refs="sliderBar" v-model="modelValue" width="60%" :min=min :max=max :tooltip=tooltip 
    :tooltipText=tooltipText :color=color :trackColor=trackColor :disabled=disabled></vue3-slider>
  
  <Transition name="bounce">
    <p v-if="showSubLimitWarning">
      <p>Reached the max number </p>
      <p>of different subreddits</p>
    </p>
  </Transition>

</template>

<script>
  import slider from "vue3-slider"
  import { store } from '../main.js'

  export default {
    name: "SliderBar",

    data() {
      return {
        store,
        showSubLimitWarning: false,
      }
    },

    props: {
      height: {
        type: Number,
        default: 6,
      },
      color: {
        type: String,
        default: "#000000",
      },
      trackColor: {
        type: String,
        default: "#FFFFFF",
      },
      max: {
        type: Number,
        default: 50,
      },
      min: {
        type: Number,
        default: 1,
      },
      step: {
        type: Number,
        default: 1,
      },
      tooltip: {
        type: Boolean,
        default: false,
      },
      tooltipText: {
        type: String,
      },
      tooltipColor: {
        type: String,
        default: "#FFFFFF",
      },
      tooltipTextColor: {
        type: String,
        default: "#000000",
      },
      alwaysShowTooltip: {
        type: Boolean,
        default: false,
      },
      orientation: {
        type: String,
        default: "horizontal",
      },
      modelValue: {
        type: Number,
        default: 10,
      },
      repeat: {
        type: Boolean,
        default: false,
      },
      sticky: {
        type: Boolean,
        default: false,
      },
      flip: {
        type: Boolean,
        default: false,
      },
      disabled: {
        type: Boolean,
        default: false,
      },
    },

    components: {
      "vue3-slider": slider,
    },

    methods: {

      mvMoreThanLimit() {

        if (this.modelValue > Object.keys(store.topSubreddits).length) {

          return true
        }
        return false
      }
    },

    watch: {
      modelValue(value) {
        store.numSubsToShow = value
        if (this.mvMoreThanLimit()) {

          //console.log("more than limit")
          this.showSubLimitWarning = true

          setTimeout(() => {
                this.showSubLimitWarning = false
            }, 5000)

          store.numSubsToShow = Object.keys(store.topSubreddits).length
        }
      }
    },

    mounted() {
      if (Object.keys(store.topSubreddits).length == 0) {
        store.numSubsToShow = 0
      }
      else {
        store.numSubsToShow = Object.keys(store.topSubreddits).length
      }
      
    },
  }
</script>

<style scoped>
  h4 {
    margin-top: 10px;
    margin-bottom: -20px;
  }

  .v-enter-active,
  .v-leave-active {
    transition: opacity 0.5s ease;
  }

  .v-enter-from,
  .v-leave-to {
    opacity: 0;
  }

  .bounce-enter-active {
    animation: bounce-in 0.5s;
  }
  .bounce-leave-active {
    animation: bounce-in 0.5s reverse;
  }
  @keyframes bounce-in {
    0% {
      transform: scale(0);
    }
    50% {
      transform: scale(1.25);
    }
    100% {
      transform: scale(1);
    }
  }
</style>