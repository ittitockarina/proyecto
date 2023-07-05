<template>
    <div>
      <!-- Formulario de ingreso de docentes -->
      <Panel :value="newDocente" class="custom-panel">
        <template #header>
          <div class="header-wrapper">
            <span class="header-text">Crear Docente</span>
          </div>
        </template>
  
        <!-- Campos para ingresar los datos del nuevo docente -->
        <br>
        <span class="p-float-label custom-textarea">
          <Textarea v-model="newDocente.id_usuario" rows="1" cols="30" />
          <label>ID Usuario</label>
        </span>
        <br>
        <span class="p-float-label custom-textarea">
          <Textarea v-model="newDocente.tipo_docente" rows="1" cols="30" />
          <label>Tipo de docente</label>
        </span>
        <br>

        <Button type="button"  icon="pi pi-save" :loading="loading" @click="guardarnewDocente" />
      </Panel>
      <br>
      <br>
      <br>
      <!-- Tabla de docentes -->
      <DataTable :value="docente" :editable="true" paginator :rows="5" :rowsPerPageOptions="[5, 10, 20, 50]" tableStyle="min-width: 50rem">
        <!-- Columnas -->
        <Column field="id_usuario" header="ID Usuario" sortable :editable="true"></Column>
        <Column field="tipo_docente" header="Tipo de docente" sortable :editable="true"></Column>
        <!-- Boton Editar -->
        <Column header="Acciones">
          <template #body="rowData">
            <Button  icon="pi pi-pencil" @click="openPosition('top', rowData)" severity="warning" ></Button>
            <Button icon="pi pi-trash" severity="info" @click="deleteRow(rowData)"></Button>
           </template>
        </Column>
        <!-- Boton Eliminar -->
       <!--  <Column header="Eliminar">
         <template #body="rowData">
            <Button label="Eliminar" severity="info" @click="deleteRow(rowData)"></Button>
          </template>
        </Column> -->
      </DataTable>
  
      <Dialog v-model:visible="visible" header="Actualizar Docente" :style="{ width: '30vw' }" :position="position" :modal="true" :draggable="false">
        <label>ID de Usuario</label>
        <br>
        <span class="p-float-label custom-textarea">
        <Textarea v-model="newDocente.id_usuariop" autoResize rows="1" cols="30" />
        </span>
        <br>
        <label>Tipo de docente</label>
        <br>
        <span class="p-float-label custom-textarea">
        <Textarea v-model="newDocente.tipo_docentep" autoResize rows="1" cols="30" />
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
        docente: [],
        newDocente: {},
        postURL: 'http://127.0.0.1:5000',
        position: 'center',
        visible: false,
      };
    },
    created() {
      axios
        .post(this.postURL + '/docentes')
        .then((res) => {
          console.log(res);
          this.docente = res.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    methods: {
        editRow() {
  if (this.newDocente && this.newDocente.tipo_docentep && this.newDocente.id_usuariop) {
    // Deshabilitar la edición en todas las filas
    this.docente.forEach((course) => {
      course.editable = false;
    });
    console.log("carne humana");
    console.log(this.newDocente.id_docente);
    console.log(this.newDocente.nombre_docentesp);
    console.log("más carne");
    // Realizar la solicitud PATCH al backend
    const payload = {
      id_docente: this.newDocente.id_docente, // Obtén el id_docente de alguna manera (por ejemplo, de la fila seleccionada)
      tipo_docente: this.newDocente.tipo_docentep,
      id_usuario: this.newDocente.id_usuariop
    };

    axios
      .patch(`${this.postURL}/docente`, payload)
      .then((res) => {
        console.log(res.data);

        // Cerrar el Dialog
        this.visible = false;

        // Actualizar los datos de la tabla
        this.cargardocentes();
      })
      .catch((error) => {
        console.log(error);
      });
  }
},
  
      cargardocentes() {
        axios
          .post(this.postURL + '/docentes')
          .then((res) => {
            console.log(res);
            this.docente = res.data;
          })
          .catch((error) => {
            console.log(error);
          });
      },
      deleteRow(rowData) {
        if (rowData) {
          const id_docente = rowData.data.id_docente;
          const confirmation = confirm('¿Estás seguro de que deseas eliminar esta fila?');
          if (confirmation) {
            axios
              .delete(`${this.postURL}/docente`, { data: { id_docente } })
              .then((res) => {
                console.log(res);
                this.docente = this.docente.filter((course) => course.id_docente !== id_docente);
              })
              .catch((error) => {
                console.log(error);
              });
          }
        }
      },
      guardarnewDocente() {
        // Validar los datos del nuevo docente antes de guardarlo
        if (this.validarDatosdocente(this.newDocente)) {
          console.log("una noche más");
          console.log(this.newDocente.nombre_docente);
          console.log("copas más");

  
          // Realizar la llamada a la API para guardar el nuevo docente y la imagen
          axios
            .put(`${this.postURL}/docente`, { tipo_docente: this.newDocente.tipo_docente,
                                              id_usuario: this.newDocente.id_usuario})
            .then((res) => {
                console.log(res);
                this.docente.push(this.newDocente); // Agregar el nuevo docente al arreglo
                this.newDocente = {}; // Limpiar los campos del nuevo docente
            })
            .catch((error) => {
                console.log(error);
            });
        }
      },
  
      validarDatosdocente(docente) {
        console.log("costumbre");
        console.log(docente);
        console.log("de costumbre");
        // Implementa la lógica de validación de los datos del docente
        // Puedes agregar validaciones adicionales según tus requisitos
        if (!docente.id_usuario) {
          console.log("maldita costumbre");
          console.log(docente.nombre_docente);
          console.log("asco de costumbre");
          alert('Por favor, complete todos los campos');
          return false;
        }
        return true;
      },
      openPosition(position, rowData) {
        this.position = position;
        this.visible = true;

  // Asignar los valores de rowData a newDocente
        this.newDocente = {
        id_docente: rowData.data.id_docente,
        tipo_docentep: rowData.data.tipo_docente,
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
    width: 338px; /* Ajusta el ancho según tus necesidades */
  }
  
  .custom-textarea textarea {
    width: 356px; /* Ajusta el ancho según tus necesidades */
  }
  </style>
  