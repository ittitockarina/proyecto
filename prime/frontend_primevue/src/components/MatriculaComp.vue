<template>
    <div>
      <!-- Formulario de ingreso de matriculas -->
      <Panel :value="newMatricula" class="custom-panel">
        <template #header>
          <div class="header-wrapper">
            <span class="header-text">Crear Matricula</span>
          </div>
        </template>
  
        <!-- Campos para ingresar los datos del nuevo matricula -->
        <br>
        <span class="p-float-label custom-textarea">
          <Textarea v-model="newMatricula.id_alumno" rows="1" cols="30" />
          <label>ID Alumno</label>
        </span>
        <br>
        <span class="p-float-label custom-textarea">
          <Textarea v-model="newMatricula.id_grupo" rows="1" cols="30" />
          <label>ID Grupo</label>
        </span>
        <br>
        <span class="p-float-label custom-textarea">
          <Textarea v-model="newMatricula.estado_matricula" rows="1" cols="30" />
          <label>Estado de matricula</label>
        </span>
        <br>
        <span class="p-float-label custom-textarea">
          <Calendar v-model="newMatricula.fecha_matricula" dateFormat="dd/mm/yy" class="custom-calendar"/>
          <label>Fecha de matricula</label>
        </span>
        <br>

        <Button type="button"  icon="pi pi-save" :loading="loading" @click="guardarnewMatricula" />
      </Panel>
      <br>
      <br>
      <br>
      <!-- Tabla de matriculas -->
      <DataTable :value="matricula" :editable="true" paginator :rows="5" :rowsPerPageOptions="[5, 10, 20, 50]" tableStyle="min-width: 50rem">
        <!-- Columnas -->
        <Column field="id_alumno" header="ID Alumno" sortable :editable="true"></Column>
        <Column field="id_grupo" header="ID Grupo" sortable :editable="true"></Column>
        <Column field="fecha_matricula" header="Fecha de matricula" sortable :editable="true"></Column>
        <Column field="estado_matricula" header="Estado de matricula" sortable :editable="true"></Column>
        <!-- Boton Acciones -->
        <Column header="Acciones">
          <template #body="rowData">
            <Button  icon="pi pi-pencil" @click="openPosition('top', rowData)" severity="warning" ></Button>
            <Button icon="pi pi-trash" severity="info" @click="deleteRow(rowData)"></Button>
          </template>
        </Column>
        
        
      </DataTable>
  
      <Dialog v-model:visible="visible" header="Actualizar Matricula" :style="{ width: '30vw' }" :position="position" :modal="true" :draggable="false">
        <label>ID de Alumno</label>
        <br>
        <span class="p-float-label custom-textarea">
        <Textarea v-model="newMatricula.id_alumnop" autoResize rows="1" cols="30" />
        </span>
        <br>
        <label>ID de Grupo</label>
        <br>
        <span class="p-float-label custom-textarea">
        <Textarea v-model="newMatricula.id_grupop" autoResize rows="1" cols="30" />
        </span>
        <br>
        <label>Estado de matricula</label>
        <br>
        <span class="p-float-label custom-textarea">
        <Textarea v-model="newMatricula.estado_matriculap" autoResize rows="1" cols="30" />
        </span>
        <br>
        <label>Fecha de matricula</label>
        <br>
        <span class="p-float-label custom-textarea ">
        <Calendar v-model="newMatricula.fecha_matriculap" dateFormat="dd/mm/yy" class="custom-calendar" />
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
        matricula: [],
        newMatricula: {},
        postURL: 'http://127.0.0.1:5000',
        position: 'center',
        visible: false,
      };
    },
    created() {
      axios
        .post(this.postURL + '/matriculas')
        .then((res) => {
          console.log(res);
          this.matricula = res.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    methods: {
        editRow() {
            console.log("carne humana");
            console.log(this.newMatricula.id_usuariop);
            console.log(this.newMatricula.matricula_yearp);
            console.log(this.newMatricula.matricula_regularp);
            console.log("más carne");
            if (this.newMatricula && this.newMatricula.id_alumnop && this.newMatricula.id_grupop && this.newMatricula.fecha_matriculap && this.newMatricula.estado_matriculap) {
    // Deshabilitar la edición en todas las filas
                console.log("carne humanas");
                console.log(this.newMatricula.id_usuariop);
                console.log(this.newMatricula.matricula_yearp);
                console.log(this.newMatricula.matricula_regularp);
                console.log("más carnes");
                this.matricula.forEach((course) => {
                course.editable = false;
                });
    
    // Realizar la solicitud PATCH al backend
                const payload = {
                    matricula_id: this.newMatricula.matricula_id, // Obtén el matricula_id de alguna manera (por ejemplo, de la fila seleccionada)
                    id_alumno: this.newMatricula.id_alumnop,
                    id_grupo: this.newMatricula.id_grupop,
                    fecha_matricula: this.newMatricula.fecha_matriculap,
                    estado_matricula: this.newMatricula.estado_matriculap
                };

                axios
                    .patch(`${this.postURL}/matricula`, payload)
                    .then((res) => {
                        console.log(res.data);

        // Cerrar el Dialog
                        this.visible = false;

        // Actualizar los datos de la tabla
                        this.cargarmatriculas();
                    })
                    .catch((error) => {
                        console.log(error);
                    });
            }
        },
  
      cargarmatriculas() {
        axios
          .post(this.postURL + '/matriculas')
          .then((res) => {
            console.log(res);
            this.matricula = res.data;
          })
          .catch((error) => {
            console.log(error);
          });
      },
      deleteRow(rowData) {
        if (rowData) {
          const matricula_id = rowData.data.matricula_id;
          const confirmation = confirm('¿Estás seguro de que deseas eliminar esta fila?');
          if (confirmation) {
            axios
              .delete(`${this.postURL}/matricula`, { data: { matricula_id } })
              .then((res) => {
                console.log(res);
                this.matricula = this.matricula.filter((course) => course.matricula_id !== matricula_id);
              })
              .catch((error) => {
                console.log(error);
              });
          }
        }
      },
      guardarnewMatricula() {
        // Validar los datos del nuevo matricula antes de guardarlo
        if (this.validarDatosmatricula(this.newMatricula)) {
          console.log("una noche más");
          console.log(this.newMatricula.nombre_matricula);
          console.log("copas más");

  
          // Realizar la llamada a la API para guardar el nuevo matricula y la imagen
          axios
            .put(`${this.postURL}/matricula`, { id_alumno: this.newMatricula.id_alumno,
                id_grupo: this.newMatricula.id_grupo,
                fecha_matricula: this.newMatricula.fecha_matricula,
                estado_matricula: this.newMatricula.estado_matricula})
            .then((res) => {
                console.log(res);
                this.matricula.push(this.newMatricula); // Agregar el nuevo matricula al arreglo
                this.newMatricula = {}; // Limpiar los campos del nuevo matricula
            })
            .catch((error) => {
                console.log(error);
            });
        }
      },
  
      validarDatosmatricula(matricula) {
        console.log("costumbre");
        console.log(matricula);
        console.log("de costumbre");
        // Implementa la lógica de validación de los datos del matricula
        // Puedes agregar validaciones adicionales según tus requisitos
        if (!matricula.id_alumno) {
          console.log("maldita costumbre");
          console.log(matricula.nombre_matricula);
          console.log("asco de costumbre");
          alert('Por favor, complete todos los campos');
          return false;
        }
        return true;
      },
      openPosition(position, rowData) {
        this.position = position;
        this.visible = true;

  // Asignar los valores de rowData a newMatricula
        this.newMatricula = {
        matricula_id: rowData.data.matricula_id,
        id_alumnop: rowData.data.id_alumno,
        id_grupop: rowData.data.id_grupo,
        fecha_matriculap: rowData.data.fecha_matricula,
        estado_matriculap: rowData.data.estado_matricula
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
    width: 356px; /* Ajusta el ancho según tus necesidades */
  }
  
  .custom-textarea textarea {
    width: 356px; /* Ajusta el ancho según tus necesidades */
  }

  .custom-calendar .p-inputtext {
    width: 800px; /* Ajusta el ancho según tus necesidades */
  }

  .custom-calendar {
  width: 750px; /* Ajusta el ancho según tus necesidades */
}
  </style>
  
