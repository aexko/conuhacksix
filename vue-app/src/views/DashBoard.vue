<template>
    <div class="dashboard">
        <h1 class="title">Dashboard</h1>
        <div class="columns">
            <div class="column">
                <div class="box" v-for="(correlation, index) in correlations" :key="index">
                    {{ correlation[0] }} - {{ correlation[1] }}
                </div>
            </div>
            <div class="column">
                <p>Second container content</p>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const insights = ref([])
const correlations = ref([])
const fetchInsights = async () => {
    const response = await fetch('http://localhost:8000/gemini')
    const data = await response.json()

    for (const result of data) {
        insights.value.push(result)
        correlations.value.push([result.datasheet1, result.datasheet2])
    }


    console.log(insights.value)
    console.log(correlations.value)
}

onMounted(() => {
    fetchInsights()
})
</script>