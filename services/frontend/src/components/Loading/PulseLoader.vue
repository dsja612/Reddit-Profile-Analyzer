<!-- modified version of PulseLoader from vue-spinner -->
<!-- https://github.com/greyby/vue-spinner -->

<template>
<div class="v-spinner" v-show="loading">
    <div class="v-pulse v-pulse1" v-bind:style="[spinnerStyle,spinnerDelay1]"></div>
    <div class="v-pulse v-pulse2" v-bind:style="[spinnerStyle,spinnerDelay2]"></div>
    <div class="v-pulse v-pulse3" v-bind:style="[spinnerStyle,spinnerDelay3]"></div>
    <div class="v-pulse v-pulse4" v-bind:style="[spinnerStyle,spinnerDelay4]"></div>
    <div class="v-pulse v-pulse5" v-bind:style="[spinnerStyle,spinnerDelay5]"></div>
</div>
</template>

<script>
export default {
  
  name: 'PulseLoader',

  props: {
    loading: {
      type: Boolean,
      default: true
    },
    size: {
      type: String,
      default: '15px'
    },
    margin: {
      type: String,
      default: '4px'
    },
    radius: {
      type: String,
      default: '100%'
    }
  },
  data () {
    return {
      spinnerStyle: {
      	backgroundColor: this.color,
      	width: this.size,
        height: this.size,
      	margin: this.margin,
      	borderRadius: this.radius,
        display: 'inline-block',
        animationName: 'v-pulseStretchDelay',
        animationDuration: '1s',
        animationIterationCount: 'infinite',
        animationTimingFunction: 'cubic-bezier(.2,.68,.18,1.08)',
        animationFillMode: 'both'
      },
      spinnerDelay1: {
        backgroundColor: "#E2D1F9",
        animationDelay: '0.1s'
      },
      spinnerDelay2: {
        backgroundColor: "#317773",
        animationDelay: '0.2s'
      },
      spinnerDelay3: {
        backgroundColor: "#FF69B4",
        animationDelay: '0.3s'
      },
      spinnerDelay4: {
        backgroundColor: "#00FFFF",
        animationDelay: '0.4s'
      },
      spinnerDelay5: {
        backgroundColor: "#E3B448",
        animationDelay: '0.5s'
      }
    }
  }

}
</script>

<style>
/*.v-spinner
{
    margin: 100px auto;
    text-align: center;
}
*/

@-webkit-keyframes v-pulseStretchDelay
{
    0%,
    80%
    {
        -webkit-transform: scale(1);
                transform: scale(1);
        -webkit-opacity: 1;             
                opacity: 1;
    }
    45%
    {
        -webkit-transform: scale(0.1);
                transform: scale(0.1);
        -webkit-opacity: 0.7;             
                opacity: 0.7;
    }
}

@keyframes v-pulseStretchDelay
{
    0%,
    80%
    {
        -webkit-transform: scale(1);
                transform: scale(1);
        -webkit-opacity: 1;             
                opacity: 1;
    }
    45%
    {
        -webkit-transform: scale(0.1);
                transform: scale(0.1);
        -webkit-opacity: 0.7;             
                opacity: 0.7;
    }
}
</style>