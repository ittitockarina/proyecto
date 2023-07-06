<template>
  <div>
    <principio /> 
    <h1>Bienvenido a la plataforma </h1>
    
  </div>
</template>

<script>

import principio from './components/principio.vue';

export default {
  name: 'App',
  components: {
    principio
}
}
</script>

<style>
h1{
  color:aqua;
}
.image {
  height: 20rem;
  margin: 1px;
  user-select: none;
  border-radius: 200rem;
}
#app {
  background: url("./assets/background.jpg");
  background-size: cover;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
  
  image-rendering: crisp-edges;
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
}


</style>