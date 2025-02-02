<template>
    <div class="dashboard">
        <h5>Dashboard</h5>
        <p>Welcome to the dashboard!</p>
        <nav> Correlation List 
            <ul>
                <li>
                    <router-link to="/correlations">Correlations</router-link>
                </li>
            </ul>
            <!-- <ul>
                <li v-for="correlation in correlations" :key="correlation.id">
                    <router-link :to="{ name: 'Correlation', params: { id: correlation.id } }">
                        {{ correlation.name }}
                    </router-link>
                </li>
            </ul> -->
        </nav>
    </div>
</template>