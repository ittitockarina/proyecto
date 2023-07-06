<template>
    <div>
      <!-- Tabla de listado -->
      <DataTable :value="datos" :editable="true" paginator :rows="5" :rowsPerPageOptions="[1, 5, 10, 50]" tableStyle="min-width: 50rem">
        <!-- Columnas -->
        <Column field="nombre_curso" header="Nombre Curso"></Column>
        <Column field="nombre_grupo" header="Nombre Grupo"></Column>
        <Column field="aula" header="Aula"></Column>
      </DataTable>
    </div>
  </template>
  
  <script>
  import { ref, onMounted } from 'vue';
  import axios from 'axios';
  import DataTable from 'primevue/datatable';
  import Column from 'primevue/column';
  
  export default {
    components: {
      DataTable,
      Column
    },
    setup() {
      const datos = ref([]);
  
      const obtenerDatos = () => {
        axios
          .get('http://localhost:5000/aula')
          .then((res) => {
            console.log(res);
            datos.value = res.data;
          })
          .catch((error) => {
            console.log(error);
          });
      };
  
      onMounted(obtenerDatos);
  
      return {
        datos
      };
    }
  };
  </script>
  
  <style scoped>
  .custom-panel {
    width: 400px; 
    margin: auto;
  }
  
  .header-wrapper {
    text-align: center;
  }
  
  .header-text {
    font-size: 1.5rem;
    font-weight: bold;
  }
  
  .custom-password input {
    width: 356px; 
  }
  
  .custom-textarea {
    display: inline-block;
    width: 338px; 
  }
  
  .custom-textarea textarea {
    width: 356px; 
  }
  </style>
  