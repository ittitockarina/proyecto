<template>
    <div>
  
      <!-- Formulario de toma de asistencia -->
      <Panel :value="asistencia" class="custom-panel">
        <template #header>
          <div class="header-wrapper">
            <span class="header-text">Tomar asistencia</span>
          </div>
        </template>
  
        <!-- Campos para ingresar los datos de la asistencia -->
        <div>
          <label>Foto: </label>
          <input type="file" id="fotoAsistencia" ref="fileInputAsistencia" accept="image/*" required>
        </div>
        <br>
        <span class="p-float-label">
          <Textarea v-model="asistencia.dni" rows="1" cols="30" />
          <label>DNI</label>
        </span>
        <br>
        <Button type="button" label="Tomar asistencia" icon="pi pi-check" :loading="loadingAsistencia" @click="tomarAsistencia" />
      </Panel>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        asistencia: {},
        postURL: 'http://127.0.0.1:5000',
      };
    },
    methods: {
      tomarAsistencia() {
        const formData = new FormData();
        formData.append('dni', JSON.stringify(this.asistencia.dni));
        formData.append('file', this.$refs.fileInputAsistencia.files[0]);
  
        // Realizar la llamada a la API para tomar la asistencia y guardar la imagen
        axios
          .post(`${this.postURL}/tomar_asistencia`, formData)
          .then((res) => {
            console.log(res);
            // Limpiar los campos del formulario
            this.asistencia = {};
            this.$refs.fileInputAsistencia.value = '';
          })
          .catch((error) => {
            console.log(error);
          });
      
  
        return true;
      },
    },
  };
  </script>
  
  <style scoped>
  .custom-panel {
    margin-bottom: 1rem;
  }
  .header-wrapper {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .header-text {
    font-size: 1.5rem;
    font-weight: bold;
  }
  .custom-password {
    margin-bottom: 1rem;
  }
  </style>
  