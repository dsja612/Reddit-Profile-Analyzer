<template>
    <div id="chart">
        <apexchart type="line" :options="chartOptions" :series="seriesToBeSent" :xAxisText=xAxisText :yAxisText=yAxisText 
        :height=height :titleText=titleText :keys=keys :yAxisMin=yAxisMin :yAxisMax=yAxisMax :style="{'width': '1050px'}" 
        :colors=colors></apexchart>
    </div>
</template>

<script>
    import VueApexCharts from "vue3-apexcharts"
    import { store } from "../../main.js"
    export default {
        name: "ApexLineChart",
        props: {
            height: Number,
            titleText: String,
            xAxisText: String,
            yAxisText: String,
            yAxisMin: Number,
            yAxisMax: Number,
            keys: Object,
            seriesToBeSent: Object,
            colors: Array,
        },
        components: {
            apexchart: VueApexCharts,
        },
        data() {
            return { 
                store,
                series: this.seriesToBeSent,
                chartOptions: {
                    chart: {
                        height: this.height,
                        type: 'line',
                        dropShadow: {
                            enabled: true,
                            color: '#000',
                            top: 18,
                            left: 7,
                            blur: 10,
                            opacity: 0.2
                        },
                        toolbar: {
                            show: false
                        }
                    },
                    colors: this.colors,
                    dataLabels: {
                        enabled: true,
                    },
                    stroke: {
                        curve: 'smooth'
                    },
                    title: {
                        text: this.titleText,
                        align: 'left'
                    },
                    grid: {
                        borderColor: '#e7e7e7',
                        row: {
                            colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
                            opacity: 0.5
                        },
                    },
                    markers: {
                        size: 1
                    },
                    xaxis: {
                        categories: this.keys,
                        title: {
                            text: this.xAxisText
                        }
                    },
                    yaxis: {
                        title: {
                            text: this.yAxisText
                        },
                        min: this.yAxisMin,
                        max: this.yAxisMax
                    },
                    legend: {
                        position: 'top',
                        horizontalAlign: 'right',
                        floating: true,
                        offsetY: -25,
                        offsetX: -5
                    }
                },
            }
        },
    }
</script>

<style scoped>

</style>