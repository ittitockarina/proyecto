<template>
    <div>
     
      <br>
      <br>
      <br>
      <!-- Tabla de justificacions -->
      <DataTable :value="justificacion" :editable="true" paginator :rows="5" :rowsPerPageOptions="[5, 10, 20, 50]" tableStyle="min-width: 50rem">
        <!-- Columnas -->
        <Column field="fecha" header="Fecha de justificacion" sortable :editable="true"></Column>
        <Column field="descrip" header="Descripcion" sortable :editable="true"></Column>
        <Column field="id_asist" header="ID Asistencia" sortable :editable="true"></Column>
        
         
       
      </DataTable>
  
      <Dialog v-model:visible="visible" header="Actualizar Justificacion" :style="{ width: '30vw' }" :position="position" :modal="true" :draggable="false">
        <label>ID de Asistencia</label>
        <br>
        <span class="p-float-label custom-textarea">
        <Textarea v-model="newJustificacion.id_asistp" autoResize rows="1" cols="30" />
        </span>
        <br>
        <label>Descripcion</label>
        <br>
        <span class="p-float-label custom-textarea">
        <Textarea v-model="newJustificacion.descripp" autoResize rows="1" cols="30" />
        </span>
        <br>
        <label>Fecha de justificacion</label>
        <br>
        <span class="p-float-label custom-textarea ">
        <Calendar v-model="newJustificacion.fechap" dateFormat="dd/mm/yy" class="custom-calendar" />
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
        justificacion: [],
        newJustificacion: {},
        postURL: 'http://127.0.0.1:5000',
        position: 'center',
        visible: false,
      };
    },
    created() {
      axios
        .post(this.postURL + '/justificaciones')
        .then((res) => {
          console.log(res);
          this.justificacion = res.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    methods: {
        editRow() {
            console.log("carne humana");
            console.log(this.newJustificacion.id_usuariop);
            console.log(this.newJustificacion.justificacion_yearp);
            console.log(this.newJustificacion.justificacion_regularp);
            console.log("más carne");
            if (this.newJustificacion && this.newJustificacion.id_asistp && this.newJustificacion.fechap && this.newJustificacion.descripp ) {
    // Deshabilitar la edición en todas las filas
                console.log("carne humanas");
                console.log(this.newJustificacion.id_usuariop);
                console.log(this.newJustificacion.justificacion_yearp);
                console.log(this.newJustificacion.justificacion_regularp);
                console.log("más carnes");
                this.justificacion.forEach((course) => {
                course.editable = false;
                });
    
    // Realizar la solicitud PATCH al backend
                const payload = {
                    id_justif: this.newJustificacion.id_justif, // Obtén el id_justif de alguna manera (por ejemplo, de la fila seleccionada)
                    id_asist: this.newJustificacion.id_asistp,
                    fecha: this.newJustificacion.fechap,
                    descrip: this.newJustificacion.descripp
                };

                axios
                    .patch(`${this.postURL}/justificacion`, payload)
                    .then((res) => {
                        console.log(res.data);

        // Cerrar el Dialog
                        this.visible = false;

        // Actualizar los datos de la tabla
                        this.cargarjustificacions();
                    })
                    .catch((error) => {
                        console.log(error);
                    });
            }
        },
  
      cargarjustificacions() {
        axios
          .post(this.postURL + '/justificaciones')
          .then((res) => {
            console.log(res);
            this.justificacion = res.data;
          })
          .catch((error) => {
            console.log(error);
          });
      },
      deleteRow(rowData) {
        if (rowData) {
          const id_justif = rowData.data.id_justif;
          const confirmation = confirm('¿Estás seguro de que deseas eliminar esta fila?');
          if (confirmation) {
            axios
              .delete(`${this.postURL}/justificacion`, { data: { id_justif } })
              .then((res) => {
                console.log(res);
                this.justificacion = this.justificacion.filter((course) => course.id_justif !== id_justif);
              })
              .catch((error) => {
                console.log(error);
              });
          }
        }
      },
      guardarnewJustificacion() {
        // Validar los datos del nuevo justificacion antes de guardarlo
        if (this.validarDatosjustificacion(this.newJustificacion)) {
          console.log("una noche más");
          console.log(this.newJustificacion.nombre_justificacion);
          console.log("copas más");

  
          // Realizar la llamada a la API para guardar el nuevo justificacion y la imagen
          axios
            .put(`${this.postURL}/justificacion`, { id_asist: this.newJustificacion.id_asist,
                fecha: this.newJustificacion.fecha,
                descrip: this.newJustificacion.descrip})
            .then((res) => {
                console.log(res);
                this.justificacion.push(this.newJustificacion); // Agregar el nuevo justificacion al arreglo
                this.newJustificacion = {}; // Limpiar los campos del nuevo justificacion
            })
            .catch((error) => {
                console.log(error);
            });
        }
      },
  
      validarDatosjustificacion(justificacion) {
        console.log("costumbre");
        console.log(justificacion);
        console.log("de costumbre");
        // Implementa la lógica de validación de los datos del justificacion
        // Puedes agregar validaciones adicionales según tus requisitos
        if (!justificacion.id_asist) {
          console.log("maldita costumbre");
          console.log(justificacion.nombre_justificacion);
          console.log("asco de costumbre");
          alert('Por favor, complete todos los campos');
          return false;
        }
        return true;
      },
      openPosition(position, rowData) {
        this.position = position;
        this.visible = true;

  // Asignar los valores de rowData a newJustificacion
        this.newJustificacion = {
        id_justif: rowData.data.id_justif,
        id_asistp: rowData.data.id_asist,
        fechap: rowData.data.fecha,
        descripp: rowData.data.descrip
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
  
