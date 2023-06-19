<template>
    <div>
      <!-- Formulario de ingreso de participacions -->
      <Panel :value="newParticipacion" class="custom-panel">
        <template #header>
          <div class="header-wrapper">
            <span class="header-text">Crear participacion</span>
          </div>
        </template>
  
        <!-- Campos para ingresar los datos del nuevo participacion -->
        <br>
        <span class="p-float-label custom-textarea">
          <Textarea v-model="newParticipacion.part_fecha" rows="1" cols="30" />
          <label>Participacion Fecha</label>
        </span>
        <br>
        <span class="p-float-label custom-textarea">
          <Textarea v-model="newParticipacion.id_horario" rows="1" cols="30" />
          <label>ID Horario</label>
        </span>
        <br>
        <span class="p-float-label custom-textarea">
          <Textarea v-model="newParticipacion.id_alumno" rows="1" cols="30" />
          <label>ID Alumno</label>
        </span>
        <br>
        <span class="p-float-label custom-textarea">
          <Textarea v-model="newParticipacion.cantidad" rows="1" cols="30" />
          <label>Cantidad</label>
        </span>
        <br>

        <Button type="button" label="Guardar" icon="pi pi-check" :loading="loading" @click="guardarnewParticipacion" />
      </Panel>
      <br>
      <br>
      <br>
      <!-- Tabla de participacions -->
      <DataTable :value="participacion" :editable="true" paginator :rows="5" :rowsPerPageOptions="[5, 10, 20, 50]" tableStyle="min-width: 50rem">
        <!-- Columnas -->
        <Column field="part_fecha" header="Participacion Fecha" sortable :editable="true"></Column>
        <Column field="id_horario" header="ID Horario" sortable :editable="true"></Column>
        <Column field="id_alumno" header="ID Alumno" sortable :editable="true"></Column>
        <Column field="cantidad" header="Cantidad" sortable :editable="true"></Column>
        <!-- Boton Editar -->
        <Column header="Editar">
          <template #body="rowData">
            <Button label="Actualizar" icon="pi pi-arrow-down" @click="openPosition('top', rowData)" severity="warning" style="min-width: 10rem"></Button>
          </template>
        </Column>
        <!-- Boton Eliminar -->
        <Column header="Eliminar">
         <template #body="rowData">
            <Button label="Eliminar" severity="info" @click="deleteRow(rowData)"></Button>
          </template>
        </Column>
      </DataTable>
  
      <Dialog v-model:visible="visible" header="Actualizar participacion" :style="{ width: '30vw' }" :position="position" :modal="true" :draggable="false">
        <label>Participacion Fecha</label>
        <br>
        <span class="p-float-label custom-textarea">
        <Textarea v-model="newParticipacion.part_fechap" autoResize rows="1" cols="30" />
        </span>
        <br>
        <label>ID Horario</label>
        <br>
        <span class="p-float-label custom-textarea">
        <Textarea v-model="newParticipacion.id_horariop" autoResize rows="1" cols="30" />
        </span>
        <br>
        <label>ID Alumno</label>
        <br>
        <span class="p-float-label custom-textarea">
        <Textarea v-model="newParticipacion.id_alumnop" autoResize rows="1" cols="30" />
        </span>
        <br>
        <label>Cantidad</label>
        <br>
        <span class="p-float-label custom-textarea">
        <Textarea v-model="newParticipacion.cantidadp" autoResize rows="1" cols="30" />
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
        participacion: [],
        newParticipacion: {},
        postURL: 'http://127.0.0.1:5000',
        position: 'center',
        visible: false,
      };
    },
    created() {
      axios
        .post(this.postURL + '/participaciones')
        .then((res) => {
          console.log(res);
          this.participacion = res.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    methods: {
        editRow() {
  if (this.newParticipacion && this.newParticipacion.part_fechap && this.newParticipacion.id_horariop && this.newParticipacion.id_alumnop && this.newParticipacion.cantidadp) {
    // Deshabilitar la edición en todas las filas
    this.participacion.forEach((course) => {
      course.editable = false;
    });
    console.log("carne humana");
    console.log(this.newParticipacion.id_participacion);
    console.log(this.newParticipacion.id_horariop);
    console.log("más carne");
    // Realizar la solicitud PATCH al backend
    const payload = {
      part_id: this.newParticipacion.part_id,
      part_fecha: this.newParticipacion.part_fechap, // Obtén el id_participacion de alguna manera (por ejemplo, de la fila seleccionada)
      id_horario: this.newParticipacion.id_horariop,
      id_alumno: this.newParticipacion.id_alumnop,
      cantidad: this.newParticipacion.cantidadp
    };

    axios
      .patch(`${this.postURL}/participacion`, payload)
      .then((res) => {
        console.log(res.data);

        // Cerrar el Dialog
        this.visible = false;

        // Actualizar los datos de la tabla
        this.cargarparticipacions();
      })
      .catch((error) => {
        console.log(error);
      });
  }
},
  
      cargarparticipacions() {
        axios
          .post(this.postURL + '/participaciones')
          .then((res) => {
            console.log(res);
            this.participacion = res.data;
          })
          .catch((error) => {
            console.log(error);
          });
      },
      deleteRow(rowData) {
        if (rowData) {
          const part_id = rowData.data.part_id;
          const confirmation = confirm('¿Estás seguro de que deseas eliminar esta fila?');
          if (confirmation) {
            axios
              .delete(`${this.postURL}/participacion`, { data: { part_id } })
              .then((res) => {
                console.log(res);
                this.participacion = this.participacion.filter((course) => course.part_id !== part_id);
              })
              .catch((error) => {
                console.log(error);
              });
          }
        }
      },
      guardarnewParticipacion() {
        // Validar los datos del nuevo participacion antes de guardarlo
        if (this.validarDatosparticipacion(this.newParticipacion)) {
          console.log("una noche más");
          console.log(this.newParticipacion.nombre_participacion);
          console.log("copas más");

  
          // Realizar la llamada a la API para guardar el nuevo participacion y la imagen
          axios
            .put(`${this.postURL}/participacion`, { part_fecha: this.newParticipacion.part_fecha,
                                            id_horario: this.newParticipacion.id_horario,
                                            id_alumno: this.newParticipacion.id_alumno,
                                            cantidad: this.newParticipacion.cantidad})
            .then((res) => {
                console.log(res);
                this.participacion.push(this.newParticipacion); // Agregar el nuevo participacion al arreglo
                this.newParticipacion = {}; // Limpiar los campos del nuevo participacion
            })
            .catch((error) => {
                console.log(error);
            });
        }
      },
  
      validarDatosparticipacion(participacion) {
        console.log("costumbre");
        console.log(participacion);
        console.log("de costumbre");
        // Implementa la lógica de validación de los datos del participacion
        // Puedes agregar validaciones adicionales según tus requisitos
        if (!participacion.part_fecha) {
          console.log("maldita costumbre");
          console.log(participacion.part_fecha);
          console.log("asco de costumbre");
          alert('Por favor, complete todos los campos');
          return false;
        }
        return true;
      },
      openPosition(position, rowData) {
        this.position = position;
        this.visible = true;

  // Asignar los valores de rowData a newParticipacion
        this.newParticipacion = {
        part_id: rowData.data.part_id,
        part_fechap: rowData.data.part_fecha,
        id_horariop: rowData.data.id_horario,
        id_alumnop: rowData.data.id_alumno,
        cantidadp: rowData.data.cantidad
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
  