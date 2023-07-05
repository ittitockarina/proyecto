<template>
    <div v-if="isUserLoggedIn" class="main" :style="mainStyle">
      <Principal v-if="isUserLoggedIn" />
    </div>
    <div v-else class="main" :style="mainStyle">
      <h1>Portal Academico Docente<br/> La Salle <br/> Universidad</h1>
      <form @submit="onSubmit" class="cart flex flex-column align-items-center gap-3 p-fluid">
        <div class="field">
          <input type="number" class="form-control" placeholder="Introduce tu DNI" id="DNI" v-model="DNIInput" />
        </div>
        <div class="field">
          <input type="password" class="form-control" placeholder="Introduce tu password" id="password" v-model="passwordInput" />
        </div>
        <small class="text-danger" id="text-error">{{ errorMessage || '&nbsp;' }}</small>
        <button type="submit" class="btn btn-primary">Submit</button> 
      </form>
      <a>¿Olvido su contraseña?</a><br/>
      <img src="../assets/google.svg" alt="Login using Google" />
      <img src="../assets/facebook.svg" alt="Login using Facebook" />
    </div>
  </template>
  
  <script>
  import Principal from './Principal.vue';
  import DocenteComp from './DocenteComp.vue';
  import AlumnoComp from './AlumnoComp.vue';
  import axios from 'axios';
  import { ref } from 'vue';
  import { useRouter } from 'vue-router';
  
  const menu = ref(null);
  
  export default {
    name: 'Home',
    components: {
      Principal,
      DocenteComp,
      AlumnoComp
    },
    data() {
      return {
        isUserLoggedIn: localStorage.getItem('user'),
        DNIInput: '',
        passwordInput: '',
        postURL: 'http://127.0.0.1:5000',
        errorMessage: '',
      };
    },
    methods: {
      toggle() {
        menu.value.classList.toggle('show');
      },
      onSubmit(event) {
        event.preventDefault();
        if (!this.DNIInput || !this.passwordInput) {
          this.errorMessage = 'Datos inválidos';
        } else {
          axios
            .post(`${this.postURL}/login`, {
              DNI: this.DNIInput,
              password: this.passwordInput,
            })
            .then((response) => {
              if (response.data.message === 'Error: Usuario no encontrado o contraseña incorrecta') {
                this.errorMessage = 'Credenciales incorrectas';
              } else {
                localStorage.setItem('user', JSON.stringify(response.data));
                this.isUserLoggedIn = true;
                this.redirectToUserComponent(response.data.tipo_usuario);
              }
            })
            .catch((error) => {
              console.log(error);
              this.errorMessage = 'Error al iniciar sesión';
            });
        }
      },
      redirectToUserComponent(tipoUsuario) {
        switch (tipoUsuario) {
          case 'usuario':
            this.$router.push('/usuario');
            break;
          case 'docente':
            this.$router.push('/docente');
            break;
          case 'alumno':
            this.$router.push('/alumno');
            break;
          default:
            this.$router.push('/');
            break;
        }
      },
    },
    props: {
      mainStyle: String,
      inputStyle: String,
    },
  };
  </script>
  
  <style>
  /* Import Poppins font: */
  @import url("https://fonts.googleapis.com/css2?family=Poppins&display=swap");
  
  .main {
    background: rgba(255, 255, 255, 0.4);
    position: absolute;
    top: 14%;
    left: 30%;
    width: 40%;
    text-align: center;
    padding: 5px;
    border-radius: 3rem;
    box-shadow: 0px 0px 8px -5px #000000;
    padding-top: 2%;
    padding-bottom: 1%;
    font-family: "Poppins", sans-serif;
  }
  
  h1 {
    cursor: default;
    user-select: none;
  }
  
  input {
    border-radius: 3rem;
    border: none;
    padding: 10px;
    text-align: center;
    outline: none;
    margin: 10px;
    width: 30%;
    box-sizing: border-box;
    font-family: "Poppins", sans-serif;
    font-weight: 400;
  }
  
  input:hover {
    box-shadow: 0px 0px 8px -5px #000000;
  }
  
  input:active {
    box-shadow: 0px 0px 8px -5px #000000;
  }
  
  #done {
    background: lightgreen;
  }
  
  .button {
    cursor: pointer;
    user-select: none;
  }
  
  img {
    height: 2.2rem;
    margin: 10px;
    user-select: none;
  }
  
  img:hover {
    box-shadow: 0px 0px 8px -5px #000000;
    cursor: pointer;
    border-radius: 200rem;
  }
  
  a {
    text-decoration: none;
    color: #000000;
  }
  </style>
  