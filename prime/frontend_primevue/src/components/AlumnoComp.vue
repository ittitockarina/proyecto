<template>
    <div>
      <!-- Formulario de ingreso de alumnos -->
      <Panel :value="newAlumno" class="custom-panel">
        <template #header>
          <div class="header-wrapper">
            <span class="header-text">Crear alumno</span>
          </div>
        </template>
  
        <!-- Campos para ingresar los datos del nuevo alumno -->
        <br>
        <span class="p-float-label custom-textarea">
          <Textarea v-model="newAlumno.id_usuario" rows="1" cols="30" />
          <label>ID Usuario</label>
        </span>
        <br>
        <span class="p-float-label custom-textarea">
          <Calendar v-model="newAlumno.alumno_year" dateFormat="dd/mm/yy" class="custom-calendar"/>
          <label>Year de nacimiento</label>
        </span>
        <br>
        <span class="p-float-label custom-textarea">
          <InputSwitch v-model="newAlumno.alumno_regular" />
          <label>Activo</label>
        </span>
        <br>

        <Button type="button" label="Guardar" icon="pi pi-check" :loading="loading" @click="guardarnewAlumno" />
      </Panel>
      <br>
      <br>
      <br>
      <!-- Tabla de alumnos -->
      <DataTable :value="alumno" :editable="true" paginator :rows="5" :rowsPerPageOptions="[5, 10, 20, 50]" tableStyle="min-width: 50rem">
        <!-- Columnas -->
        <Column field="id_usuario" header="ID Usuario" sortable :editable="true"></Column>
        <Column field="alumno_year" header="Year de nacimiento" sortable :editable="true"></Column>
        <Column field="alumno_regular" header="Activo" sortable :editable="true"></Column>
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
  
      <Dialog v-model:visible="visible" header="Actualizar alumno" :style="{ width: '30vw' }" :position="position" :modal="true" :draggable="false">
        <label>ID de Usuario</label>
        <br>
        <span class="p-float-label custom-textarea">
        <Textarea v-model="newAlumno.id_usuariop" autoResize rows="1" cols="30" />
        </span>
        <br>
        <label>Year de nacimiento</label>
        <br>
        <span class="p-float-label custom-textarea ">
        <Calendar v-model="newAlumno.alumno_yearp" dateFormat="dd/mm/yy" class="custom-calendar" />
        </span>
        <br>
        <label>Activo</label>
        <br>
        <span class="p-float-label custom-textarea">
        <InputSwitch v-model="newAlumno.alumno_regularp" />
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
        alumno: [],
        newAlumno: {},
        postURL: 'http://127.0.0.1:5000',
        position: 'center',
        visible: false,
      };
    },
    created() {
      axios
        .post(this.postURL + '/alumnos')
        .then((res) => {
          console.log(res);
          this.alumno = res.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    methods: {
        editRow() {
            console.log("carne humana");
            console.log(this.newAlumno.id_usuariop);
            console.log(this.newAlumno.alumno_yearp);
            console.log(this.newAlumno.alumno_regularp);
            console.log("más carne");
            if (this.newAlumno && this.newAlumno.alumno_yearp && this.newAlumno.id_usuariop) {
    // Deshabilitar la edición en todas las filas
                console.log("carne humanas");
                console.log(this.newAlumno.id_usuariop);
                console.log(this.newAlumno.alumno_yearp);
                console.log(this.newAlumno.alumno_regularp);
                console.log("más carnes");
                this.alumno.forEach((course) => {
                course.editable = false;
                });
    
    // Realizar la solicitud PATCH al backend
                const payload = {
                    id_alumno: this.newAlumno.id_alumno, // Obtén el id_alumno de alguna manera (por ejemplo, de la fila seleccionada)
                    alumno_regular: this.newAlumno.alumno_regularp,
                    alumno_year: this.newAlumno.alumno_yearp,
                    id_usuario: this.newAlumno.id_usuariop
                };

                axios
                    .patch(`${this.postURL}/alumno`, payload)
                    .then((res) => {
                        console.log(res.data);

        // Cerrar el Dialog
                        this.visible = false;

        // Actualizar los datos de la tabla
                        this.cargaralumnos();
                    })
                    .catch((error) => {
                        console.log(error);
                    });
            }
        },
  
      cargaralumnos() {
        axios
          .post(this.postURL + '/alumnos')
          .then((res) => {
            console.log(res);
            this.alumno = res.data;
          })
          .catch((error) => {
            console.log(error);
          });
      },
      deleteRow(rowData) {
        if (rowData) {
          const id_alumno = rowData.data.id_alumno;
          const confirmation = confirm('¿Estás seguro de que deseas eliminar esta fila?');
          if (confirmation) {
            axios
              .delete(`${this.postURL}/alumno`, { data: { id_alumno } })
              .then((res) => {
                console.log(res);
                this.alumno = this.alumno.filter((course) => course.id_alumno !== id_alumno);
              })
              .catch((error) => {
                console.log(error);
              });
          }
        }
      },
      guardarnewAlumno() {
        // Validar los datos del nuevo alumno antes de guardarlo
        if (this.validarDatosalumno(this.newAlumno)) {
          console.log("una noche más");
          console.log(this.newAlumno.nombre_alumno);
          console.log("copas más");

  
          // Realizar la llamada a la API para guardar el nuevo alumno y la imagen
          axios
            .put(`${this.postURL}/alumno`, { alumno_regular: this.newAlumno.alumno_regular,
                                             alumno_year: this.newAlumno.alumno_year,
                                             id_usuario: this.newAlumno.id_usuario})
            .then((res) => {
                console.log(res);
                this.alumno.push(this.newAlumno); // Agregar el nuevo alumno al arreglo
                this.newAlumno = {}; // Limpiar los campos del nuevo alumno
            })
            .catch((error) => {
                console.log(error);
            });
        }
      },
  
      validarDatosalumno(alumno) {
        console.log("costumbre");
        console.log(alumno);
        console.log("de costumbre");
        // Implementa la lógica de validación de los datos del alumno
        // Puedes agregar validaciones adicionales según tus requisitos
        if (!alumno.id_usuario) {
          console.log("maldita costumbre");
          console.log(alumno.nombre_alumno);
          console.log("asco de costumbre");
          alert('Por favor, complete todos los campos');
          return false;
        }
        return true;
      },
      openPosition(position, rowData) {
        this.position = position;
        this.visible = true;

  // Asignar los valores de rowData a newAlumno
        this.newAlumno = {
        id_alumno: rowData.data.id_alumno,
        alumno_regularp: rowData.data.alumno_regular,
        alumno_yearp: rowData.data.alumno_year,
        id_usuariop: rowData.data.id_usuario
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
  
