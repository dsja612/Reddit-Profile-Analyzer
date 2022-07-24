<template>
    <div id="chart">
        <apexchart type="pie" width="380" :options="chartOptions" :series="series"></apexchart>
    </div>
</template>

<script scoped>
    import VueApexCharts from "vue3-apexcharts"
    import { store } from "../../main.js"
    export default {
        name: "ApexPieChart",
        components: {
            apexchart: VueApexCharts,
        },
        data() {
            return {
                store,
                series: [Object.values(store.commentPolarity)[0], Object.values(store.commentPolarity)[1]], 
                chartOptions: {
                    chart: {
                        width: 380,
                        type: 'pie',
                    },
                    labels: ['Positive', 'Negative'],
                    legend: {
                        show: false,
                    },
                    colors: ['#50C878', '#E30B5C'],
                    responsive: [{
                        breakpoint: 480,
                        options: {
                            chart: {
                                width: 200
                            },
                            legend: {
                                position: 'bottom',
                            }
                        }
                    }]
                },
            }
        }
    };
</script>