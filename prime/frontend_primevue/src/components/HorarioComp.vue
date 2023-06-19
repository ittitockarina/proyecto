<template>
    <div>
      <!-- Formulario de ingreso de horarios -->
      <Panel :value="newHorario" class="custom-panel">
        <template #header>
          <div class="header-wrapper">
            <span class="header-text">Crear Horario</span>
          </div>
        </template>
  
        <!-- Campos para ingresar los datos del nuevo horario -->
        <br>
        <span class="p-float-label custom-textarea">
          <Textarea v-model="newHorario.id_grupo" rows="1" cols="30" />
          <label>ID Grupo</label>
        </span>
        <br>
        <span class="p-float-label custom-textarea">
          <Calendar id="calendar-timeonly" v-model="newHorario.hora_inicio" timeOnly class="custom-calendar" />
          <label>Hora de inicio</label>
        </span>
        <br>
        <span class="p-float-label custom-textarea">
          <Calendar id="calendar-timeonly" v-model="newHorario.hora_fin" timeOnly class="custom-calendar" />
          <label>Hora de fin</label>
        </span>
        <br>
        <span class="p-float-label custom-textarea">
          <Textarea v-model="newHorario.dia" rows="1" cols="30" />
          <label>Dia</label>
        </span>
        <br>

        <Button type="button" label="Guardar" icon="pi pi-check" :loading="loading" @click="guardarnewHorario" />
      </Panel>
      <br>
      <br>
      <br>
      <!-- Tabla de horarios -->
      <DataTable :value="horario" :editable="true" paginator :rows="5" :rowsPerPageOptions="[5, 10, 20, 50]" tableStyle="min-width: 50rem">
        <!-- Columnas -->
        <Column field="id_grupo" header="ID Grupo" sortable :editable="true"></Column>
        <Column field="hora_inicio" header="Hora de inicio" sortable :editable="true"></Column>
        <Column field="hora_fin" header="Hora de fin" sortable :editable="true"></Column>
        <Column field="dia" header="Día" sortable :editable="true"></Column>
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
  
      <Dialog v-model:visible="visible" header="Actualizar Horario" :style="{ width: '30vw' }" :position="position" :modal="true" :draggable="false">
        <label>ID de Grupo</label>
        <br>
        <span class="p-float-label custom-textarea">
        <Textarea v-model="newHorario.id_grupop" autoResize rows="1" cols="30" />
        </span>
        <br>
        <label>Hora de inicio</label>
        <br>
        <span class="p-float-label custom-textarea ">
        <Calendar id="calendar-timeonly" v-model="newHorario.hora_iniciop" timeOnly class="custom-calendar"/>
        </span>
        <br>
        <label>Hora de fin</label>
        <br>
        <span class="p-float-label custom-textarea">
        <Calendar id="calendar-timeonly" v-model="newHorario.hora_iniciop" timeOnly class="custom-calendar"/>
        </span>
        <label>Dia</label>
        <br>
        <span class="p-float-label custom-textarea">
        <Textarea v-model="newHorario.diap" rows="1" cols="30" />
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
        horario: [],
        newHorario: {},
        postURL: 'http://127.0.0.1:5000',
        position: 'center',
        visible: false,
      };
    },
    created() {
      axios
        .post(this.postURL + '/horarios')
        .then((res) => {
          console.log(res);
          this.horario = res.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    methods: {
        editRow() {
            console.log("carne humana");
            console.log(this.newHorario.id_usuariop);
            console.log(this.newHorario.horario_yearp);
            console.log(this.newHorario.horario_regularp);
            console.log("más carne");
            if (this.newHorario && this.newHorario.id_grupop && this.newHorario.hora_iniciop && this.newHorario.hora_finp && this.newHorario.diap) {
    // Deshabilitar la edición en todas las filas
                console.log("carne humanas");
                console.log(this.newHorario.id_usuariop);
                console.log(this.newHorario.horario_yearp);
                console.log(this.newHorario.horario_regularp);
                console.log("más carnes");
                this.horario.forEach((course) => {
                course.editable = false;
                });
    
    // Realizar la solicitud PATCH al backend
                const payload = {
                    id_horario: this.newHorario.id_horario, // Obtén el id_horario de alguna manera (por ejemplo, de la fila seleccionada)
                    id_grupo: this.newHorario.id_grupop,
                    hora_inicio: this.newHorario.hora_iniciop,
                    hora_fin: this.newHorario.hora_finp,
                    dia: this.newHorario.diap,
                };

                axios
                    .patch(`${this.postURL}/horario`, payload)
                    .then((res) => {
                        console.log(res.data);

        // Cerrar el Dialog
                        this.visible = false;

        // Actualizar los datos de la tabla
                        this.cargarhorarios();
                    })
                    .catch((error) => {
                        console.log(error);
                    });
            }
        },
  
      cargarhorarios() {
        axios
          .post(this.postURL + '/horarios')
          .then((res) => {
            console.log(res);
            this.horario = res.data;
          })
          .catch((error) => {
            console.log(error);
          });
      },
      deleteRow(rowData) {
        if (rowData) {
          const id_horario = rowData.data.id_horario;
          const confirmation = confirm('¿Estás seguro de que deseas eliminar esta fila?');
          if (confirmation) {
            axios
              .delete(`${this.postURL}/horario`, { data: { id_horario } })
              .then((res) => {
                console.log(res);
                this.horario = this.horario.filter((course) => course.id_horario !== id_horario);
              })
              .catch((error) => {
                console.log(error);
              });
          }
        }
      },
      guardarnewHorario() {
        // Validar los datos del nuevo horario antes de guardarlo
        if (this.validarDatoshorario(this.newHorario)) {
          console.log("una noche más");
          console.log(this.newHorario.nombre_horario);
          console.log("copas más");

  
          // Realizar la llamada a la API para guardar el nuevo horario y la imagen
          axios
            .put(`${this.postURL}/horario`, { id_grupo: this.newHorario.id_grupo,
                                              hora_inicio: this.newHorario.hora_inicio,
                                              hora_fin: this.newHorario.hora_fin,
                                              dia: this.newHorario.dia})
            .then((res) => {
                console.log(res);
                this.horario.push(this.newHorario); // Agregar el nuevo horario al arreglo
                this.newHorario = {}; // Limpiar los campos del nuevo horario
            })
            .catch((error) => {
                console.log(error);
            });
        }
      },
  
      validarDatoshorario(horario) {
        console.log("costumbre");
        console.log(horario);
        console.log("de costumbre");
        // Implementa la lógica de validación de los datos del horario
        // Puedes agregar validaciones adicionales según tus requisitos
        if (!horario.id_grupo) {
          console.log("maldita costumbre");
          console.log(horario.nombre_horario);
          console.log("asco de costumbre");
          alert('Por favor, complete todos los campos');
          return false;
        }
        return true;
      },
      openPosition(position, rowData) {
        this.position = position;
        this.visible = true;

  // Asignar los valores de rowData a newHorario
        this.newHorario = {
        id_horario: rowData.data.id_horario,
        id_grupop: rowData.data.id_grupo,
        hora_iniciop: rowData.data.hora_inicio,
        hora_finp: rowData.data.hora_fin,
        diap: rowData.data.dia
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
  
