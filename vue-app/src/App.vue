<script setup>
import { RouterView } from 'vue-router'
import NavBar from './components/NavBar.vue'
</script>

<template>
  <header>
    <nav>
      <NavBar />
    </nav>
  </header>
  <main>
    <RouterView />
  </main>
</template>

<style scoped>
header {
  width: 100%;
  padding: 1rem;
}

nav {
  display: flex;
  justify-content: flex;
}

main {
  padding: 1rem;
}
</style>