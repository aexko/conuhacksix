<template>
    <nav class="navbar" role="navigation" aria-label="main navigation">
        <div class="navbar-brand">

            <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false"
                data-target="navbarBasicExample" @click="toggleNavbar">
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
            </a>
        </div>

        <div id="navbarBasicExample" class="navbar-menu" :class="{ 'is-active': isActive }">
            <div class="navbar-start">
                <router-link class="navbar-item" to="/dashboard">Dashboard</router-link>
                <router-link class="navbar-item" to="/csv-reader">Datasets</router-link>
            </div>
        </div>
    </nav>
</template>

<script>
import { ref } from 'vue';

export default {
    name: 'Navbar',
    setup() {
        const isActive = ref(false);

        const toggleNavbar = () => {
            isActive.value = !isActive.value;
        };

        return {
            isActive,
            toggleNavbar
        };
    }
};
</script>

<style scoped>
.navbar {
    background-color: #333;
    color: white;
    padding-left: 10%;
}

.navbar-item {
    color: white;
    font-size: larger;
}

.navbar-item:hover {
    background-color: #555;
}

.button.is-primary {
    background-color: #00d1b2;
    border-color: transparent;
}

.button.is-light {
    background-color: #fff;
    color: #333;
}
</style>