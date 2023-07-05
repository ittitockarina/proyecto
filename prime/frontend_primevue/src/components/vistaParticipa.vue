<template>
  <div>
    <br>
    <DataTable :value="alumnos" :paginator="true" :rows="5" :rowsPerPageOptions="[5, 10, 20, 50]" tableStyle="min-width: 50rem">
      <Column field="id_alumno" header="ID Alumno"></Column>
      <Column field="nombre" header="Nombre"></Column>
      <Column field="apellido" header="Apellido"></Column>
      <Column field="nombre_curso" header="Nombre del Curso"></Column>
      <Column field="cantidad_participaciones" header="puntaje"></Column>
      <Column header="Puntos">
        <template #body="rowData">
          <div>
            <Button icon="pi pi-pencil" @click="puntos('top', rowData)" severity="warning" style="min-width: 5rem"></Button>
          </div>
        </template>
      </Column>
    </DataTable>

    <Dialog v-model:visible="visible" header="cantidad" :style="{ width: '20vw' }" :position="position" :modal="true" :draggable="false">
     
    
      <span class="p-float-label custom-textarea">
        <!-- <Textarea v-model="newAlumnos.cantidad" autoResize rows="1" cols="1" /> -->
        <input   v-model="newAlumnos.cantidad" type="number" min="0" max="5" >

      </span>
      <br>
      <template #footer>
        <Button  icon="pi pi-plus" @click="sumar(); visible = false " autofocus style="min-width: 5rem"/>
        <Button  icon="pi pi-minus" @click="restar(); visible = false" autofocus style="min-width: 5rem"/>
      </template>
    </Dialog>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import axios from 'axios';

export default {
  data() {
    return {
      alumnos: [],
      newAlumnos: {},
      postURL: 'http://localhost:5000',
      position: 'center',
      visible: false,
    };
  },
  methods: {
    cargarAlumnos() {
      axios
        .post(this.postURL + '/todos')
        .then((res) => {
          console.log(res);
          this.alumnos = res.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    sumar() {
      axios
        .patch(this.postURL + '/agregar', this.newAlumnos)
        .then((res) => {
          console.log(res);
          this.cargarAlumnos();
        })
        .catch((error) => {
          console.log(error);
        });
    },
    restar() {
      axios
        .patch(this.postURL + '/quitar', this.newAlumnos)
        .then((res) => {
          console.log(res);
          this.cargarAlumnos();
        })
        .catch((error) => {
          console.log(error);
        });
    },
    puntos(position, rowData) {
      this.position = position;
      this.visible = true;
      console.log("fd");
      this.newAlumnos = {
        id_alumno: rowData.data.id_alumno,
        
      };
    },
    
  },
  created() {
    this.cargarAlumnos();
  },
};
</script>


<style>
  
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
  