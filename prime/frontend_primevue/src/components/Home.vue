<template>
  <div>
    <h1>Iniciar sesión</h1>
    <form @submit.prevent="submitForm">
      <div>
        <label for="DNI">DNI:</label>
        <input type="text" v-model="DNI" name="DNI" required>
      </div>
      <div>
        <label for="password">Contraseña:</label>
        <input type="password" v-model="password" name="password" required>
      </div>
      <button type="submit">Iniciar sesión</button>
      <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      DNI: '',
      password: '',
      postURL: 'http://127.0.0.1:5000',
      errorMessage: ''
    };
  },
  methods: {
    submitForm() {
      if (!this.DNI || !this.password) {
        this.errorMessage = 'Por favor, ingresa tu DNI y contraseña.';
        return;
      }

      axios.post(this.postURL + '/login', {
        DNI: this.DNI,
        password: this.password
      })
      .then(response => {
        const usuario = response.data;
        if (usuario.tipo_usuario === 'admin') {
          this.$router.push('/usuario');
        } else if (usuario.tipo_usuario === 'docente') {
          this.$router.push('/docente');
        } else if (usuario.tipo_usuario === 'alumno') {
          this.$router.push('/alumno');
        }
      })
      .catch(error => {
        console.error(error);
        this.errorMessage = 'Credenciales incorrectas. Por favor, verifica tu DNI y contraseña.';
      });
    }
  }
};
</script>

<style>
.error-message {
  color: red;
}
</style>
