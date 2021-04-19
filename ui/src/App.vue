<template>
  <div id="app">
    <SimulationDashboard/>
  </div>
</template>

<script>
import SimulationDashboard from './components/SimulationDashboard.vue'

export default {
  name: 'App',
  components: {
    SimulationDashboard
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 15px;
}
</style>
