<template>
  <div v-if="isUserLoggedIn">
    <div class="card flex justify-content-center">
      <Button type="button" label="abrir menu" @click="toggle" aria-haspopup="true" aria-controls="overlay_menu" />
      <Menu ref="menu" id="overlay_menu" :model="items" :popup="true" />
    </div>
    <TableComp v-if="isUserLoggedIn" />
  </div>
  <div v-else class="card flex justify-content-center">
    <form @submit="onSubmit" class="cart flex flex-column align-items-center gap-3 p-fluid">
      <div class="field">
        <InputNumber :useGrouping="false" placeholder="Introduce tu DNI" id="DNI" v-model="DNIInput" />
      </div>
      <div class="field">
        <Password placeholder="Introduce tu password" id="password" v-model="passwordInput" />
      </div>
      <small class="p-error" id="text-error">{{ errorMessage || '&nbsp;' }}</small>
      <Button type="submit" label="Submit" />
    </form>
  </div>
</template>

<script>
import TableComp from './TableComp.vue';
import axios from 'axios';
import { ref } from 'vue';
import { Toast } from 'primevue/toast';

const menu = ref(null);



function getUser() {
  return localStorage.getItem('user');
}

export default {
  name: 'Home',
  components: {
    TableComp,
    Toast,
  },
  data() {
    return {
      isUserLoggedIn: getUser(),
      DNIInput: '',
      passwordInput: '',
      postURL: 'http://127.0.0.1:5000',
    };
  },
  methods: {
    toggle(e) {
      menu.value.toggle(e);
    },
    onSubmit(e) {
      e.preventDefault();
      if (!this.DNIInput || !this.passwordInput) {
        alert('Datos inválidos');
      } else {
        axios
          .post(this.postURL + '/login', {
            DNI: this.DNIInput,
            password: this.passwordInput,
          })
          .then((res) => {
            if (res.data.length) {
              localStorage.setItem('user', JSON.stringify(res.data[0]));
              this.isUserLoggedIn = true;
            } else {
              alert('Credenciales incorrectas');
            }
          })
          .catch((error) => {
            alert(error);
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
