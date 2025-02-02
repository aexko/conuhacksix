<template>
    <p class="has-text-centered is-size-7">Traced Graph</p>
    <div ref="plotlyChart" style="width: 100%; height: 100%;"></div>
</template>

<script>
import Plotly from 'plotly.js-dist';

export default {
    name: 'GraphLine',
    mounted() {
        this.fetchDatasets();
        this.drawChart();
    },
    props: {
        datasheet1: String,
        datasheet2: String,
    },
    data() {
        return {
            datasets: [],
            filename1: [],
            filename2: [],
            dataset1: [],
            dataset2: [],

        };
    },
    methods: {
        async fetchDatasets() {
            try {
                const response = await fetch('http://localhost:8000/getcorrelations')
                const data = await response.json();
                console.log('line',data);
                this.datasets = data;

                for (let i = 0; i < this.datasets.length; i++) {
                    if (this.datasets[i].title === this.datasheet1) {
                        this.filename1 = this.datasets[i].filename;
                        const response = await fetch('http://localhost:8000/getcsvdata?filename=' + this.filename1)
                        const data = await response.json();
                        this.dataset1 = data;
                    }
                    if (this.datasets[i].title === this.datasheet2) {
                        this.filename2 = this.datasets[i].filename;
                        const response = await fetch('http://localhost:8000/getcsvdata?filename=' + this.filename2)
                        const data = await response.json();
                        this.dataset2 = data;
                    }
                }
                console.log(this.dataset1);
                console.log(this.dataset2);
                this.drawChart();
            } catch (error) {
                console.error('There was a problem with the fetch operation:', error)
            }
        },
        drawChart() {
            const trace1 = {
                x: this.dataset1.x,
                y: this.dataset1.y,
                type: 'scatter'
            };

            const data = [trace1];

            const layout = {
                title: 'Line Graph',
                autosize: true,
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