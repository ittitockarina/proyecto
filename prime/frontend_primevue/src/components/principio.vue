<template>
    <div >
      <h1>Login</h1>
      <template v-if="!loggedIn">
        <form @submit.prevent="login" class="login-form">
            <label for="dni">DNI:</label>
            <input type="text" id="dni" v-model="dni" required>
            <br>
            <label for="passw">Contraseña:</label>
            <input type="password" id="passw" v-model="passw" required>
            <br>
            <Button type="submit">Iniciar sesión</Button>
        </form>
      </template>
      <div v-else>
        <p>Bienvenido, {{ tipoUsuario }}</p>
        <Button @click="logout">Cerrar sesión</Button>
        <template v-if="tipoUsuario === 'admin'">
          <!-- elementos para el administrador -->
          <vistaComp />
        </template>
        <template v-else-if="tipoUsuario === 'docente'">
          <!-- elementos para el docente -->
          <DocenteLogin />
        </template>
        <template v-else-if="tipoUsuario === 'alumno'">
          <!-- elementos para el alumno -->
          <AlumnoLogin />
        </template>
        <template v-else>
          <!-- elementos para otros tipos de usuario -->
          <p>Tipo de usuario no válido</p>
        </template>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import vistaComp from './vistaComp.vue';
  import AlumnoLogin from './AlumnoLogin.vue';
  import DocenteLogin from './DocenteLogin.vue';
  
  export default {
    name: 'principio',
    components: {
      vistaComp,
      AlumnoLogin,
      DocenteLogin
    },
    data() {
      return {
        responseStatus: null,
        tipoUsuario: null,
        dni: '',
        passw: '',
        loggedIn: false
      };
    },
    methods: {
      login() {
        axios
          .post('http://localhost:5000/login', {
            dni: this.dni,
            passw: this.passw
          })
          .then(response => {
            console.log('Respuesta del backend:', response.data);
            this.responseStatus = response.status;
            this.tipoUsuario = response.data.tipo_usuario?.toLowerCase();
            localStorage.setItem('tipoUsuario', this.tipoUsuario);
            this.loggedIn = true;
          })
          .catch(error => {
            console.error(error);
            this.responseStatus = null;
            this.tipoUsuario = null;
            localStorage.removeItem('tipoUsuario');
          });
      },
      logout() {
        this.tipoUsuario = null;
        this.loggedIn = false;
        this.dni = '';
        this.passw = '';
        localStorage.removeItem('tipoUsuario');
      }
    },
    mounted() {
      this.tipoUsuario = localStorage.getItem('tipoUsuario');
      if (this.tipoUsuario) {
        this.loggedIn = true;
      }
    }
  };
  </script>
  
  <style scoped>
  
h1 {
  margin-bottom: 20px;
  text-align: center;
}

.login-form {
  background: rgba(255, 255, 255, 0.4);
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 20px;
}

.login-form label {
  margin-bottom: 10px;
}

.login-form input {
  margin-bottom: 10px;
  padding: 5px;
}

.logout-button {
  padding: 5px 10px;
  background-color: #e74c3c;
  color: #fff;
  border: none;
  border-radius: 3px;
  cursor: pointer;
}

.logout-button:hover {
  background-color: #c0392b;
}
</style>
  