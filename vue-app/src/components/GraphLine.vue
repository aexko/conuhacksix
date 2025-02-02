<template>
    <div ref="plotlyChart" style="width: 100%; height: 100%;"></div>
</template>

<script>
import Plotly from 'plotly.js-dist';

export default {
    name: 'GraphLine',
    mounted() {
        this.drawChart();
    },
    methods: {
        drawChart() {
            const trace1 = {
                x: [1, 2, 3, 4, 5],
                y: [10, 15, 13, 17, 21],
                type: 'scatter'
            };

            const data = [trace1];

            const layout = {
                title: 'Line Graph',
                xaxis: {
                    title: 'X Axis'
                },
                yaxis: {
                    title: 'Y Axis'
                }
            };

            Plotly.newPlot(this.$refs.plotlyChart, data, layout);
        }
    }
};
</script>

<style scoped>
/* Add any styles you need for your chart */
</style>