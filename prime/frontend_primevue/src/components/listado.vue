<template>
    <div>
      <!-- Tabla de listado -->
      <DataTable :value="curso" :editable="true" paginator :rows="5" :rowsPerPageOptions="[1, 5, 10, 50]" tableStyle="min-width: 50rem">
        <!-- Columnas -->
        <Column field="hora_inicio" header="Hora Inicio"></Column>
        <Column field="hora_fin" header="Hora Fin"></Column>
        <Column field="nombre_grupo" header="Nombre Grupo"></Column>
        <Column field="nombre_curso" header="Nombre Curso"></Column>
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
      const curso = ref([]);
  
      const cargarCursos = () => {
        axios
          .get('http://localhost:5000/listado')
          .then((res) => {
            console.log(res);
            curso.value = res.data;
          })
          .catch((error) => {
            console.log(error);
          });
      };
  
      onMounted(cargarCursos);
  
      return {
        curso
      };
    }
  };
  </script>
  
  <style scoped>
  .custom-panel {
    width: 400px; /* Ajusta el ancho según tus necesidades */
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
    width: 356px; /* Ajusta el ancho según tus necesidades */
  }
  
  .custom-textarea {
    display: inline-block;
    width: 338px; /* Ajusta el ancho según tus necesidades */
  }
  
  .custom-textarea textarea {
    width: 356px; /* Ajusta el ancho según tus necesidades */
  }
  </style>
  