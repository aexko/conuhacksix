<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <nav>
      <RouterLink to="/csv-reader">CSV READER</RouterLink>
    </nav>
  </header>
  <RouterView />
</template>