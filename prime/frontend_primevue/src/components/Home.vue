<template>
  <div v-if="isUserLoggedIn">
    <div class="card flex justify-content-center">

      
    </div>
    <UsuarioComp v-if="isUserLoggedIn" />
  </div>
  <div v-else class="card flex justify-content-center">
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
  </div>
</template>

<script>
import UsuarioComp from './UsuarioComp.vue';
import axios from 'axios';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const menu = ref(null);

export default {
  name: 'Home',
  components: {
    UsuarioComp,
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
            if (response.data.length) {
              localStorage.setItem('user', JSON.stringify(response.data[0]));
              this.isUserLoggedIn = true;

              const tipoUsuario = response.data[0].tipo_usuario;
              const router = useRouter();
              if (tipoUsuario === 'alumno') {
                router.push({ name: 'Alumnos' });
              } else if (tipoUsuario === 'admin') {
                router.push({ name: 'Admin' });
              } else if (tipoUsuario === 'docente') {
                router.push({ name: 'Docente' });
              } else {
                // Otros casos según los tipos de usuario
              }
            } else {
              this.errorMessage = 'Credenciales incorrectas';
            }
          })
          .catch((error) => {
            console.log(error);
            this.errorMessage = 'Error al iniciar sesión';
          });
      }
    },
  },
};
</script>

<style>
body {
  font-family: var(--font-family);
  font-weight: normal;
  background: var(--surface-ground);
  color: var(--text-color);
  padding: 1rem;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>