<template>
  <h3>{{ capitaliseFirst(subject) }}</h3>
  <vue3-slider v-model="modelValue" width="60%" :min=min :max=max
    :color=color :trackColor="trackColor" :height=height sticky="true"></vue3-slider>

  <Popper placement="right" :show="showPopper">
    <template #content>
      <div id="innerPopperPadding">
        <h5>Data shown is reflected</h5>
        <h5>by the last 200 posts and</h5>
        <h5>comments made by the user</h5>
      </div>
    </template>

    <Transition name="bounce">
      <div v-if="showLimitWarning" @mouseover="showPopper = true" @mouseleave="showPopper = false">
        <p style="text-shadow:1px 1px 10px #c9fffa, 1px 1px 10px #c9fffa, 1px 1px 10px #c9fffa, 1px 1px 10px #c9fffa;">Reached the max number of </p>
        <p style="text-shadow:1px 1px 10px #c9fffa, 1px 1px 10px #c9fffa, 1px 1px 10px #c9fffa, 1px 1px 10px #c9fffa;">{{ subject }} ({{ subjectLength }}) {{ ending }}</p>
      </div>
    </Transition> 
  </Popper>

  <Transition name="bounce">
    <p v-if="showNoSubWarning">
      <p>The user has not posted</p>
      <p>or commented on any subreddits!</p>
    </p>
  </Transition>
</template>

<script>
import slider from "vue3-slider"
import { store } from '../../main.js'
import Popper from 'vue3-popper'

export default {
  name: "SliderBar",

  data() {
    return {
      store,
      showLimitWarning: false,
      showNoSubWarning: false,
      showPopper: false,
    }
  },

  props: {
    subject: {
      type: String,
    },
    storeLength: {
      type: Number,
    },
    ending: {
      type: String,
    },
    subjectLength: {
      type: Number,
    },

    height: {
      type: Number,
      default: 15,
    },
    color: {
      type: String,
      default: "#14213D",
    },
    trackColor: {
      type: String,
      default: "#E5E5E5",
    },
    max: {
      type: Number,
      default: 50,
    },
    min: {
      type: Number,
      default: 1,
    },
    orientation: {
      type: String,
      default: "horizontal",
    },
    modelValue: {
      type: Number,
      default: 10,
    },
  },

  components: {
    "vue3-slider": slider,
    Popper,
  },

  methods: {
    mvMoreThanLimit() {
      if (this.modelValue > this.getSubjectLength(this.subject)) {
        return true
      }
      return false
    },

    userHasNoSubs() {
      if (this.getSubjectLength(this.subject) == 0) {
        return true
      }
      return false
    },

    capitaliseFirst(string) {
      return string.charAt(0).toUpperCase() + string.slice(1);
    },

    // method in sliderbar to modify subs/words to show 
    // arguments: string, either sub or word

    setSubjectToShow(string, value) {

      if (string == "subreddits") {
        store.numSubsToShow = value
      }

      else if (string == "words") {
        store.numWordsToShow = value
      }
    },

    getCurrentSubjectToShow() {

      if (this.subject == "subreddits") {
        return store.numSubsToShow
      }
      
      else if (this.subject == "words") {
        return store.numWordsToShow
      }
    },

    getSubjectLength(string) {

      if (string == "subreddits") {
        return Object.keys(store.topSubreddits).length
      }

      else if (string == "words") {
        return Object.keys(store.topWords).length
      }
    },

    goto(subject) {
      if (subject == "subreddits") {
        var top = this.$parent.$parent.$refs["subBreak"].getBoundingClientRect().top
      }
      else if (subject == "words") {
        var top = this.$parent.$parent.$refs["wordBreak"].getBoundingClientRect().top
      }

      window.scrollBy({
        top: top,
        behavior: "smooth"
      })
    }
  },

  watch: {
    modelValue(value) {
      this.showNoSubWarning = false
      this.setSubjectToShow(this.subject, value)

      if (this.userHasNoSubs()) {
        this.showLimitWarning = false
        this.showNoSubWarning = true
        this.setSubjectToShow(this.subject, 0)
      }
      else {
        if (this.mvMoreThanLimit()) {

          //console.log("more than limit")
          this.showLimitWarning = true
          this.setSubjectToShow(this.subject, this.getSubjectLength(this.subject))
        }
        else{
          this.showLimitWarning = false
        }
      }

      this.goto(this.subject)
    }
  },

  mounted() {
    if (this.userHasNoSubs()) {
      this.setSubjectToShow(this.subject, 0)
      this.showLimitWarning = false
      this.showNoSubWarning = true
    }
    else {
      if (this.subject == "subreddits"){
        this.setSubjectToShow(this.subject, Math.ceil(this.getSubjectLength(this.subject) * 20/100))
      }
      else if (this.subject == "words"){
        this.setSubjectToShow(this.subject, Math.ceil(this.getSubjectLength(this.subject) * 1/100))
      }
    }   
  },
}
</script>

<style scoped>
  h3 {
    margin-top: 15px;
    margin-bottom: -20px;
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

<!-- style for Popper (tooltip popup) -->
<style>
  :root {
      --popper-theme-background-color: #14213D;
      --popper-theme-border-width: 2px;
      --popper-theme-border-style: solid;
      --popper-theme-border-radius: 5px;
    }

    #innerPopperPadding {
      padding: 5px;
      color: white;
    }
</style>