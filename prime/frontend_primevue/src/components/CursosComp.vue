<template>
    <div>
      <!-- Formulario de ingreso de cursos -->
      <Panel :value="newCurso" class="custom-panel">
        <template #header>
          <div class="header-wrapper">
            <span class="header-text">Crear curso</span>
          </div>
        </template>
  
        <!-- Campos para ingresar los datos del nuevo curso -->
        <br>
        <span class="p-float-label custom-textarea">
          <Textarea v-model="newCurso.nombre_curso" rows="1" cols="30" />
          <label>Nombre curso</label>
        </span>
        <br>

        <Button type="button"  icon="pi pi-save" :loading="loading" @click="guardarnewCurso" />
      </Panel>
      <br>
      <br>
      <br>
      <!-- Tabla de cursos -->
      <DataTable :value="curso" :editable="true" paginator :rows="5" :rowsPerPageOptions="[1, 5, 10, 50]" tableStyle="min-width: 50rem">
        <!-- Columnas -->
        <Column field="nombre_curso" header="Nombre" sortable :editable="true"></Column>
        <!-- Boton Editar -->
        <Column header="Acciones">
          <template #body="rowData">
            <Button  icon="pi pi-pencil" @click="openPosition('top', rowData)" severity="warning" ></Button>
            <Button  icon="pi pi-trash"  severity="info" @click="deleteRow(rowData)"></Button>
          </template>
        </Column>
        <!-- Boton Eliminar -->
      <!--   <Column header="Eliminar">
         <template #body="rowData">
            <Button  icon="pi pi-trash"  severity="info" @click="deleteRow(rowData)"></Button>
          </template>
        </Column> -->
      </DataTable>
  
      <Dialog v-model:visible="visible" header="Actualizar curso" :style="{ width: '30vw' }" :position="position" :modal="true" :draggable="false">
        <label>Nombre de curso</label>
        <br>
        <span class="p-float-label custom-textarea">
        <Textarea v-model="newCurso.nombre_cursosp" autoResize rows="1" cols="30" />
        </span>
        <br>
        <template #footer>
          <Button label="Aceptar" icon="pi pi-check" @click="editRow(); visible = false" autofocus />
          <Button label="Cancelar" icon="pi pi-times" @click="visible = false" text />
        </template>
      </Dialog>
    </div>
  </template>
  
  <script>
  import { ref } from 'vue';
  import axios from 'axios';
  
  export default {
    data() {
      return {
        curso: [],
        newCurso: {},
        postURL: 'http://127.0.0.1:5000',
        position: 'center',
        visible: false,
      };
    },
    created() {
      axios
        .post(this.postURL + '/cursos')
        .then((res) => {
          console.log(res);
          this.curso = res.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    methods: {
        editRow() {
  if (this.newCurso && this.newCurso.nombre_cursosp) {
    // Deshabilitar la edición en todas las filas
    this.curso.forEach((course) => {
      course.editable = false;
    });
    console.log("carne humana");
    console.log(this.newCurso.id_curso);
    console.log(this.newCurso.nombre_cursosp);
    console.log("más carne");
    // Realizar la solicitud PATCH al backend
    const payload = {
      id_curso: this.newCurso.id_curso, // Obtén el id_curso de alguna manera (por ejemplo, de la fila seleccionada)
      nombre_curso: this.newCurso.nombre_cursosp
    };

    axios
      .patch(`${this.postURL}/curso`, payload)
      .then((res) => {
        console.log(res.data);

        // Cerrar el Dialog
        this.visible = false;

        // Actualizar los datos de la tabla
        this.cargarcursos();
      })
      .catch((error) => {
        console.log(error);
      });
  }
},
  
      cargarcursos() {
        axios
          .post(this.postURL + '/cursos')
          .then((res) => {
            console.log(res);
            this.curso = res.data;
          })
          .catch((error) => {
            console.log(error);
          });
      },
      deleteRow(rowData) {
        if (rowData) {
          const id_curso = rowData.data.id_curso;
          const confirmation = confirm('¿Estás seguro de que deseas eliminar esta fila?');
          if (confirmation) {
            axios
              .delete(`${this.postURL}/curso`, { data: { id_curso } })
              .then((res) => {
                console.log(res);
                this.curso = this.curso.filter((course) => course.id_curso !== id_curso);
              })
              .catch((error) => {
                console.log(error);
              });
          }
        }
      },
      guardarnewCurso() {
        // Validar los datos del nuevo curso antes de guardarlo
        if (this.validarDatoscurso(this.newCurso)) {
          console.log("una noche más");
          console.log(this.newCurso.nombre_curso);
          console.log("copas más");

  
          // Realizar la llamada a la API para guardar el nuevo curso y la imagen
          axios
            .put(`${this.postURL}/curso`, { nombre_curso: this.newCurso.nombre_curso })
            .then((res) => {
                console.log(res);
                this.curso.push(this.newCurso); // Agregar el nuevo curso al arreglo
                this.newCurso = {}; // Limpiar los campos del nuevo curso
            })
            .catch((error) => {
                console.log(error);
            });
        }
      },
  
      validarDatoscurso(curso) {
        console.log("costumbre");
        console.log(curso);
        console.log("de costumbre");
        // Implementa la lógica de validación de los datos del curso
        // Puedes agregar validaciones adicionales según tus requisitos
        if (!curso.nombre_curso) {
          console.log("maldita costumbre");
          console.log(curso.nombre_curso);
          console.log("asco de costumbre");
          alert('Por favor, complete todos los campos');
          return false;
        }
        return true;
      },
      openPosition(position, rowData) {
        this.position = position;
        this.visible = true;

  // Asignar los valores de rowData a newCurso
  this.newCurso = {
    id_curso: rowData.data.id_curso,
    nombre_cursosp: rowData.data.nombre_curso
  };
},

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
  