<template>
    <nav class="nav">
        <li class="links">
    <RouterLink to="/csv-reader">Home</RouterLink>
        </li>
        <li class="links">
    <RouterLink to="/dashboard">Dashboard</RouterLink>
        </li>
  </nav>
</template>

<script>
export default {
    name: 'NavBar'
}
</script>

<style scoped>
.nav {
    position: fixed;
    left: 0;
    top: 0;
    height: 100%;
    width: 175px;
    background-color: #333;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding-top: 20px;
}

.nav .links{
    list-style-type: none;
    padding: 0;
}

.nav .links {
    margin: 20px 0;
}

.nav .links {
    color: white;
    text-decoration: none;
    font-size: 18px;
}

.nav .links:hover {
    color: #ddd;
}
</style>