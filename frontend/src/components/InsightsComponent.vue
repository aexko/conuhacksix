<template>
    <div class="insights">
        <div class="">
            <div class="">
                <div class="card">
                    <div class="card-content">
                        <div class="media">
                            <div class="media-left">
                                <span class="icon is-large">
                                    <i class="fas fa-chart-line fa-2x"></i>
                                </span>
                            </div>
                            <div class="media-content">
                                <p class="title is-4">{{ datasheet1 }} in correlation with {{ datasheet2}}</p>
                            </div>
                        </div>
                        <div class="content">
                            <div class="field">
                                <span class="icon">
                                    <i class="fas fa-database"></i>
                                </span>
                                <span>{{ datasheet1 }}</span>
                            </div>
                            <div class="field">
                                <span class="icon">
                                    <i class="fas fa-database"></i>
                                </span>
                                <span>{{ datasheet2 }}</span>
                            </div>
                            <div class="field">
                                {{ reason }}
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
    // data() {
    //     return {
    //         insights: []
    //     };
    // },
    props: {
        reason: String,
        datasheet1: String,
        datasheet2: String,
    },
    // mounted() {
    //     this.fetchInsights();
    // }
};
</script>

<style scoped>
@import '@fortawesome/fontawesome-free/css/all.css';

/* .insights {
    padding: 20px;
} */

.card {
    margin-bottom: 20px;
}

/* .field {
    margin-bottom: 10px;
} */

.icon {
    margin-right: 5px;
}
</style>