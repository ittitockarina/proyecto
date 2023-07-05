<template>
    <div>
      <!-- Formulario de ingreso de tipousers -->
      <Panel :value="newTipouser" class="custom-panel">
        <template #header>
          <div class="header-wrapper">
            <span class="header-text">Crear Tipo de Usuario</span>
          </div>
        </template>
  
        <!-- Campos para ingresar los datos del nuevo tipouser -->
        <br>
        <span class="p-float-label custom-textarea">
          <Textarea v-model="newTipouser.tipo_usuario" rows="1" cols="30" />
          <label>Tipo de usuario</label>
        </span>
        <br>

        <Button type="button"  icon="pi pi-save" :loading="loading" @click="guardarnewTipouser" />
      </Panel>
      <br>
      <br>
      <br>
      <!-- Tabla de tipousers -->
      <DataTable :value="tipouser" :editable="true" paginator :rows="5" :rowsPerPageOptions="[5, 10, 20, 50]" tableStyle="min-width: 50rem">
        <!-- Columnas -->
        <Column field="tipo_usuario" header="Tipo de usuario" sortable :editable="true"></Column>
        <!-- Boton Acciones -->
        <Column header="Acciones">
          <template #body="rowData">
            <Button  icon="pi pi-pencil" @click="openPosition('top', rowData)" severity="warning" ></Button>
            <Button icon="pi pi-trash" severity="info" @click="deleteRow(rowData)"></Button>
          </template>
        </Column>
        
      </DataTable>
  
      <Dialog v-model:visible="visible" header="Actualizar Tipo de Usuario" :style="{ width: '30vw' }" :position="position" :modal="true" :draggable="false">
        <label>Tipo de Usuario</label>
        <br>
        <span class="p-float-label custom-textarea">
        <Textarea v-model="newTipouser.tipo_usuariop" autoResize rows="1" cols="30" />
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
        tipouser: [],
        newTipouser: {},
        postURL: 'http://127.0.0.1:5000',
        position: 'center',
        visible: false,
      };
    },
    created() {
      axios
        .post(this.postURL + '/tipousers')
        .then((res) => {
          console.log(res);
          this.tipouser = res.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    methods: {
        editRow() {
  if (this.newTipouser && this.newTipouser.tipo_usuariop) {
    // Deshabilitar la edición en todas las filas
    this.tipouser.forEach((course) => {
      course.editable = false;
    });
    console.log("carne humana");
    console.log(this.newTipouser.id_tipo_usuario);
    console.log(this.newTipouser.tipo_usuariop);
    console.log("más carne");
    // Realizar la solicitud PATCH al backend
    const payload = {
        id_tipo_usuario: this.newTipouser.id_tipo_usuario, // Obtén el id_tipo_usuario de alguna manera (por ejemplo, de la fila seleccionada)
        tipo_usuario: this.newTipouser.tipo_usuariop
    };

    axios
      .patch(`${this.postURL}/tipouser`, payload)
      .then((res) => {
        console.log(res.data);

        // Cerrar el Dialog
        this.visible = false;

        // Actualizar los datos de la tabla
        this.cargartipousers();
      })
      .catch((error) => {
        console.log(error);
      });
  }
},
  
      cargartipousers() {
        axios
          .post(this.postURL + '/tipousers')
          .then((res) => {
            console.log(res);
            this.tipouser = res.data;
          })
          .catch((error) => {
            console.log(error);
          });
      },
      deleteRow(rowData) {
        if (rowData) {
          const id_tipo_usuario = rowData.data.id_tipo_usuario;
          const confirmation = confirm('¿Estás seguro de que deseas eliminar esta fila?');
          if (confirmation) {
            axios
              .delete(`${this.postURL}/tipouser`, { data: { id_tipo_usuario } })
              .then((res) => {
                console.log(res);
                this.tipouser = this.tipouser.filter((course) => course.id_tipo_usuario !== id_tipo_usuario);
              })
              .catch((error) => {
                console.log(error);
              });
          }
        }
      },
      guardarnewTipouser() {
        // Validar los datos del nuevo tipouser antes de guardarlo
        if (this.validarDatostipouser(this.newTipouser)) {
          console.log("una noche más");
          console.log(this.newTipouser.nombre_tipouser);
          console.log("copas más");

  
          // Realizar la llamada a la API para guardar el nuevo tipouser y la imagen
          axios
            .put(`${this.postURL}/tipouser`, { tipo_usuario: this.newTipouser.tipo_usuario })
            .then((res) => {
                console.log(res);
                this.tipouser.push(this.newTipouser); // Agregar el nuevo tipouser al arreglo
                this.newTipouser = {}; // Limpiar los campos del nuevo tipouser
            })
            .catch((error) => {
                console.log(error);
            });
        }
      },
  
      validarDatostipouser(tipouser) {
        console.log("costumbre");
        console.log(tipouser);
        console.log("de costumbre");
        // Implementa la lógica de validación de los datos del tipouser
        // Puedes agregar validaciones adicionales según tus requisitos
        if (!tipouser.tipo_usuario) {
          console.log("maldita costumbre");
          console.log(tipouser.nombre_tipouser);
          console.log("asco de costumbre");
          alert('Por favor, complete todos los campos');
          return false;
        }
        return true;
      },
      openPosition(position, rowData) {
  this.position = position;
  this.visible = true;

  // Asignar los valores de rowData a newTipouser
  this.newTipouser = {
    id_tipo_usuario: rowData.data.id_tipo_usuario,
    tipo_usuariop: rowData.data.tipo_usuario
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
  