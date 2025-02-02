<script setup>
import GraphLine from '@/components/GraphLine.vue';
import InsightsComponent from '@/components/InsightsComponent.vue';
</script>

<template>
    <div class="dashboard">
        <h1>Dashboard</h1>
        <GraphLine />
        <InsightsComponent />
    </div>
</template>

<style scoped>
.dashboard {
    padding: 20px;
}

h1 {
    color: #333;
}
</style>