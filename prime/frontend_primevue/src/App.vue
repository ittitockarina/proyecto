<template>
  <div>
    <!-- <CursosComp /> 
    <tomarAsistencia /> 
    
    <GrupoComp/> 
    <ParticipacionComp/> 
    <AlumnoComp/> 
    <DocenteComp/> 
    <HorarioComp/> 
    <AsistenciaComp/> 
    <MatriculaComp/> 
    <JustificacionComp/> 
    <TipoUserComp/>
    <UsuarioComp />  -->
    <vistaComp /> 
    <h1>Bienvenido a la plataforma </h1>
    <!-- <img class="image" src="https://www.ulasalle.edu.pe/wp-content/uploads/2022/08/ulasalle_.jpg" />
     -->
  </div>
</template>

<script>


 
//import vistaComp from './components/vistaComp.vue';


import vistaComp from './components/vistaComp.vue';
/* import CursosComp from './components/CursosComp.vue';
import tomarAsistencia from './components/tomarAsistencia.vue';

import GrupoComp from './components/GrupoComp.vue';
import ParticipacionComp from './components/ParticipacionComp.vue';
import AlumnoComp from './components/AlumnoComp.vue';
import DocenteComp from './components/DocenteComp.vue';
import HorarioComp from './components/HorarioComp.vue';
import AsistenciaComp from './components/AsistenciaComp.vue';
import MatriculaComp from './components/MatriculaComp.vue';
import JustificacionComp from './components/JustificacionComp.vue';
import TipoUserComp from './components/TipoUserComp.vue';
import UsuarioComp from './components/UsuarioComp.vue'; */
export default {
  name: 'App',
  components: {
   /*  tomarAsistencia, */
    vistaComp/*  ,
    CursosComp,
    GrupoComp,
 ParticipacionComp,
 AlumnoComp,
 DocenteComp,
  HorarioComp,
 AsistenciaComp,
 MatriculaComp,
 JustificacionComp,
 TipoUserComp,
 UsuarioComp */

}
}
</script>

<style>
/* h1{
  color:antiquewhite;
} */
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