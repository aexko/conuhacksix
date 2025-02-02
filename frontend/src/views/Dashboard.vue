<script setup>
import GraphLine from '@/components/GraphLine.vue';
import InsightsComponent from '@/components/InsightsComponent.vue';

import { ref, onMounted} from 'vue';

const correlations = ref([]);
const index = ref(null);

const setIndex = (i) => {
    index.value = i;
};
console.log(correlations.value);
const fetchResults = async () => {
    const response = await fetch('http://localhost:8000/gemini');
    const data = await response.json();
    correlations.value = data;  
    console.log(correlations.value);
};

onMounted(() => {
    fetchResults();
});
</script>

<template>
    <div class="dashboard">
        <div class="columns">
            <div class="column" style="max-width: 30%;">
                <h1 class="title text">Dashboard</h1><br>
                <h2 class="subtitle text">Dataset pairs generated</h2>
                <div v-for="(correlation, index) in correlations" :key="index">
                    <div @click="setIndex(index)" class="box" style="margin-bottom: 7px;">{{ correlation.datasheet1 }} with {{ correlation.datasheet2 }}</div>
                </div>
                <p v-if="correlations.length === 0" class="has-text-centered is-size-3">Loading...</p>
            </div>
            <div class="column">
                <div v-if="index != null">
                    <GraphLine :datasheet1="correlations[index].datasheet1" :datasheet2="correlations[index].datasheet2"/>
                </div>
                
            </div>
        </div>
            
        <InsightsComponent v-if="index != null" :reason="correlations[index].reason" :datasheet1="correlations[index].datasheet1" :datasheet2="correlations[index].datasheet2"/>
        <!-- <h1>Dashboard</h1> -->
        <p v-if="index == null" class="has-text-centered is-size-3">Click a pair for a detailed report</p>
        
    </div>
</template>

<style scoped>
/* .dashboard {
    padding: 20px;
} */

h1 {
    color: #333;
}

.text {
    padding-left: 10px;
}
</style>