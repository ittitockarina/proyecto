<template>
  <div>
  
    <CursosComp /> 
    <GrupoComp/> 
    <ParticipacionComp/> 
    <AlumnoComp/> 
    <DocenteComp/> 
    <HorarioComp/> 
    <AsistenciaComp/> 
    <MatriculaComp/> 
    <JustificacionComp/> 
    <TipoUserComp/>
    <UsuarioComp /> 
 
    <vistaComp /> 
  </div>
</template>

<script>
import vistaComp from './components/vistaComp.vue';

 
import Home from './components/Home.vue';
import CursosComp from './components/CursosComp.vue';
import GrupoComp from './components/GrupoComp.vue';
import ParticipacionComp from './components/ParticipacionComp.vue';
import AlumnoComp from './components/AlumnoComp.vue';
import DocenteComp from './components/DocenteComp.vue';
import HorarioComp from './components/HorarioComp.vue';
import AsistenciaComp from './components/AsistenciaComp.vue';
import MatriculaComp from './components/MatriculaComp.vue';
import JustificacionComp from './components/JustificacionComp.vue';
import TipoUserComp from './components/TipoUserComp.vue';
export default {
  name: 'App',
  components: {
    vistaComp,
    CursosComp,
    GrupoComp,
 ParticipacionComp,
 AlumnoComp,
 DocenteComp,
  HorarioComp,
 AsistenciaComp,
 MatriculaComp,
 JustificacionComp,
 TipoUserComp
}
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
