<template>
    <div class="insights">
        <div class="columns is-multiline">
            <div class="column is-one-third" v-for="insight in insights" :key="insight.id">
                <div class="card">
                    <div class="card-content">
                        <div class="media">
                            <div class="media-left">
                                <span class="icon is-large">
                                    <i :class="insight.icon"></i>
                                </span>
                            </div>
                            <div class="media-content">
                                <p class="title is-4">{{ insight.title }}</p>
                            </div>
                        </div>
                        <div class="content">
                            <div class="field">
                                <span class="icon">
                                    <i class="fas fa-database"></i>
                                </span>
                                <span>{{ insight.datasheet1 }}</span>
                            </div>
                            <div class="field">
                                <span class="icon">
                                    <i class="fas fa-database"></i>
                                </span>
                                <span>{{ insight.datasheet2 }}</span>
                            </div>
                            <div class="field">
                                {{ insight.description }}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'InsightsComponent',
    data() {
        return {
            insights: []
        };
    },
    mounted() {
        this.fetchInsights();
    },
    methods: {
        async fetchInsights() {
            try {
                const response = await axios.get('http://localhost:8000/gemini');
                this.insights = response.data.map((item, index) => ({
                    id: index + 1,
                    icon: 'fas fa-chart-line fa-2x', // You can customize the icon based on the data
                    title: item.title || `Insight ${index + 1}`,
                    datasheet1: item.datasheet1 || 'Dataset 1 not available',
                    datasheet2: item.datasheet2 || 'Dataset 2 not available',
                    description: item.reason || 'No description available.'
                }));
            } catch (error) {
                console.error('Error fetching insights:', error);
            }
        }
    }
};
</script>

<style scoped>
@import '@fortawesome/fontawesome-free/css/all.css';

.insights {
    padding: 20px;
}

.card {
    margin-bottom: 20px;
}

.field {
    margin-bottom: 10px;
}

.icon {
    margin-right: 5px;
}
</style>