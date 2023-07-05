<template>
    <div>
      <!-- Formulario de ingreso de asistencias -->
      <Panel :value="newAsistencia" class="custom-panel">
        <template #header>
          <div class="header-wrapper">
            <span class="header-text">Crear Asistencia</span>
          </div>
        </template>
  
        <!-- Campos para ingresar los datos del nuevo asistencia -->
        <br>
        <span class="p-float-label custom-textarea">
          <Textarea v-model="newAsistencia.id_horario" rows="1" cols="30" />
          <label>ID Horario</label>
        </span>
        <br>
        <span class="p-float-label custom-textarea">
          <Textarea v-model="newAsistencia.id_alumno" rows="1" cols="30" />
          <label>ID Alumno</label>
        </span>
        <br>
        <span class="p-float-label custom-textarea">
          <Calendar v-model="newAsistencia.fecha" dateFormat="dd/mm/yy" class="custom-calendar"/>
          <label>Fecha</label>
        </span>
        <br>
        <span class="p-float-label custom-textarea">
          <InputSwitch v-model="newAsistencia.presente" />
          <label>Presente</label>
        </span>
        <br>

        <Button type="button" icon="pi pi-save" :loading="loading" @click="guardarnewAsistencia" />
      </Panel>
      <br>
      <br>
      <br>
      <!-- Tabla de asistencias -->
      <DataTable :value="asistencia" :editable="true" paginator :rows="5" :rowsPerPageOptions="[5, 10, 20, 50]" tableStyle="min-width: 50rem">
        <!-- Columnas -->
        <Column field="id_horario" header="ID Horario" sortable :editable="true"></Column>
        <Column field="id_alumno" header="ID Alumno" sortable :editable="true"></Column>
        <Column field="fecha" header="Fecha" sortable :editable="true"></Column>
        <Column field="presente" header="Presente" sortable :editable="true"></Column>
        <!-- Boton Editar -->
        <Column header="Acciones">
          <template #body="rowData">
            <Button icon="pi pi-pencil" @click="openPosition('top', rowData)" severity="warning" ></Button>
            <Button icon="pi pi-trash" severity="info" @click="deleteRow(rowData)"></Button>
          </template>
        </Column>
        <!-- Boton Eliminar -->
        <!-- <Column header="Eliminar">
         <template #body="rowData">
            <Button label="Eliminar" severity="info" @click="deleteRow(rowData)"></Button>
          </template>
        </Column> -->
      </DataTable>
  
      <Dialog v-model:visible="visible" header="Actualizar Asistencia" :style="{ width: '30vw' }" :position="position" :modal="true" :draggable="false">
        <label>ID de Horario</label>
        <br>
        <span class="p-float-label custom-textarea">
        <Textarea v-model="newAsistencia.id_horariop" autoResize rows="1" cols="30" />
        </span>
        <br>
        <label>ID de Alumno</label>
        <br>
        <span class="p-float-label custom-textarea">
        <Textarea v-model="newAsistencia.id_alumnop" autoResize rows="1" cols="30" />
        </span>
        <br>
        <label>Fecha</label>
        <br>
        <span class="p-float-label custom-textarea ">
        <Calendar v-model="newAsistencia.fechap" dateFormat="dd/mm/yy" class="custom-calendar" />
        </span>
        <br>
        <label>Presente</label>
        <br>
        <span class="p-float-label custom-textarea">
        <InputSwitch v-model="newAsistencia.presentep" />
        </span>
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
        asistencia: [],
        newAsistencia: {},
        postURL: 'http://127.0.0.1:5000',
        position: 'center',
        visible: false,
      };
    },
    created() {
      axios
        .post(this.postURL + '/asistencias')
        .then((res) => {
          console.log(res);
          this.asistencia = res.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    methods: {
        editRow() {
            console.log("carne humana");
            console.log(this.newAsistencia.id_usuariop);
            console.log(this.newAsistencia.asistencia_yearp);
            console.log(this.newAsistencia.asistencia_regularp);
            console.log("más carne");
            if (this.newAsistencia && this.newAsistencia.fechap && this.newAsistencia.id_horariop && this.newAsistencia.id_alumnop) {
    // Deshabilitar la edición en todas las filas
                console.log("carne humanas");
                console.log(this.newAsistencia.id_usuariop);
                console.log(this.newAsistencia.asistencia_yearp);
                console.log(this.newAsistencia.asistencia_regularp);
                console.log("más carnes");
                this.asistencia.forEach((course) => {
                course.editable = false;
                });
    
    // Realizar la solicitud PATCH al backend
                const payload = {
                    id_asist: this.newAsistencia.id_asist, // Obtén el id_asist de alguna manera (por ejemplo, de la fila seleccionada)
                    fecha: this.newAsistencia.fechap,
                    id_horario: this.newAsistencia.id_horariop,
                    id_alumno: this.newAsistencia.id_alumnop,
                    presente: this.newAsistencia.presentep
                };

                axios
                    .patch(`${this.postURL}/asistencia`, payload)
                    .then((res) => {
                        console.log(res.data);

        // Cerrar el Dialog
                        this.visible = false;

        // Actualizar los datos de la tabla
                        this.cargarasistencias();
                    })
                    .catch((error) => {
                        console.log(error);
                    });
            }
        },
  
      cargarasistencias() {
        axios
          .post(this.postURL + '/asistencias')
          .then((res) => {
            console.log(res);
            this.asistencia = res.data;
          })
          .catch((error) => {
            console.log(error);
          });
      },
      deleteRow(rowData) {
        if (rowData) {
          const id_asist = rowData.data.id_asist;
          const confirmation = confirm('¿Estás seguro de que deseas eliminar esta fila?');
          if (confirmation) {
            axios
              .delete(`${this.postURL}/asistencia`, { data: { id_asist } })
              .then((res) => {
                console.log(res);
                this.asistencia = this.asistencia.filter((course) => course.id_asist !== id_asist);
              })
              .catch((error) => {
                console.log(error);
              });
          }
        }
      },
      guardarnewAsistencia() {
        // Validar los datos del nuevo asistencia antes de guardarlo
        if (this.validarDatosasistencia(this.newAsistencia)) {
          console.log("una noche más");
          console.log(this.newAsistencia.nombre_asistencia);
          console.log("copas más");

  
          // Realizar la llamada a la API para guardar el nuevo asistencia y la imagen
          axios
            .put(`${this.postURL}/asistencia`, { fecha: this.newAsistencia.fecha,
                id_horario: this.newAsistencia.id_horario,
                id_alumno: this.newAsistencia.id_alumno,
                presente: this.newAsistencia.presente})
            .then((res) => {
                console.log(res);
                this.asistencia.push(this.newAsistencia); // Agregar el nuevo asistencia al arreglo
                this.newAsistencia = {}; // Limpiar los campos del nuevo asistencia
            })
            .catch((error) => {
                console.log(error);
            });
        }
      },
  
      validarDatosasistencia(asistencia) {
        console.log("costumbre");
        console.log(asistencia);
        console.log("de costumbre");
        // Implementa la lógica de validación de los datos del asistencia
        // Puedes agregar validaciones adicionales según tus requisitos
        if (!asistencia.id_alumno) {
          console.log("maldita costumbre");
          console.log(asistencia.nombre_asistencia);
          console.log("asco de costumbre");
          alert('Por favor, complete todos los campos');
          return false;
        }
        return true;
      },
      openPosition(position, rowData) {
        this.position = position;
        this.visible = true;

  // Asignar los valores de rowData a newAsistencia
        this.newAsistencia = {
        id_asist: rowData.data.id_asist,
        fechap: rowData.data.fecha,
        id_horariop: rowData.data.id_horario,
        id_alumnop: rowData.data.id_alumno,
        presentep: rowData.data.presente
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
  
