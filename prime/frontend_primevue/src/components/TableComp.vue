<template>
  <div>
    <!-- Formulario de ingreso de usuarios -->
    <Panel :value="newUser" class="custom-panel">
      <template #header>
        <div class="header-wrapper">
          <span class="header-text">Crear usuario</span>
        </div>
      </template>

      <!-- Campos para ingresar los datos del nuevo usuario -->
      <div>
        <label>Foto: </label>
        <input type="file" id="foto" ref="fileInput" accept="image/*" required>
      </div>
      <br>
      <span class="p-float-label">
        <Textarea v-model="newUser.nombre" rows="1" cols="30" />
        <label>Nombre</label>
      </span>
      <br>
      <span class="p-float-label">
        <Textarea v-model="newUser.apellido" rows="1" cols="30" />
        <label>Apellido</label>
      </span>
      <br>
      <span class="p-float-label">
        <Textarea v-model="newUser.email" rows="1" cols="30" />
        <label>Email</label>
      </span>
      <br>
      <span class="p-float-label">
        <Textarea v-model="newUser.dni" rows="1" cols="30" />
        <label>DNI</label>
      </span>
      <br>
      <span class="p-float-label custom-password">
        <Password v-model="newUser.passw" inputId="password" toggleMask />
        <label for="password">Password</label>
      </span>
      <br>
      <Button type="button" label="Guardar" icon="pi pi-check" :loading="loading" @click="guardarnewUser" />
    </Panel>
    <br>
    <br>
    <br>
    <!-- Tabla de usuarios -->
    <DataTable :value="usuario" :editable="true" paginator :rows="5" :rowsPerPageOptions="[5, 10, 20, 50]" tableStyle="min-width: 50rem">
      <!-- Columnas -->
      <Column field="dni" header="DNI" :editable="true"></Column>
      <Column field="nombre" sortable header="Nombre" :editable="true"></Column>
      <Column field="apellido" sortable header="Apellido" :editable="true"></Column>
      <Column field="email" header="Correo" :editable="true"></Column>
      <!-- Boton Editar -->
      <Column header="Editar">
        <div class="flex flex-wrap justify-content-center gap-2 mb-2">
          <Button label="Editar" severity="info" @click="editRow(rowData)"></Button>
<!--           <Button label="Editar" icon="pi pi-arrow-down" @click="editRow(rowData)" @click="openPosition('top')" severity="warning" style="min-width: 10rem"></Button>
 -->        </div>
      </Column>
      <!-- Boton Eliminar -->
      <Column header="Eliminar">
        <template #body="rowData">
          <Button label="Eliminar" severity="info" @click="deleteRow(rowData)"></Button>
        </template>
      </Column>
    </DataTable>

    <Dialog v-model:visible="visible" header="Header" :style="{ width: '50vw' }" :position="position" :modal="true" :draggable="false">
    <p class="m-0">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
        Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
    </p>
    <template #footer>
        <Button label="No" icon="pi pi-times" @click="visible = false" text />
        <Button label="Yes" icon="pi pi-check" @click="visible = false" autofocus />
    </template>
    </Dialog>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      usuario: [],
      newUser: {},
      postURL: 'http://127.0.0.1:5000',
    };
  },
  created() {
    axios
      .post(this.postURL + '/usuarios')
      .then((res) => {
        console.log(res);
        this.usuario = res.data;
      })
      .catch((error) => {
        console.log(error);
      });
  },
  methods: {
    editRow(rowData) {
      if (rowData && rowData.data && rowData.data.dni && rowData.data.nombre && rowData.data.apellido && rowData.data.email) {
        // Deshabilitar la edición en todas las filas
        this.usuario.forEach((user) => {
          user.editable = false;
        });
        // Habilitar la edición solo en la fila seleccionada
        rowData.data.editable = true;
      }
    },
    deleteRow(rowData) {
      if (rowData) {
        const dni = rowData.data.dni;
        const confirmation = confirm('¿Estás seguro de que deseas eliminar esta fila?');
        if (confirmation) {
          axios
            .delete(`${this.postURL}/usuarios`, { data: { dni } })
            .then((res) => {
              console.log(res);
              this.usuario = this.usuario.filter((user) => user.dni !== dni);
            })
            .catch((error) => {
              console.log(error);
            });
        }
      }
    },
    guardarnewUser() {
      // Validar los datos del nuevo usuario antes de guardarlo
      if (this.validarDatosUsuario(this.newUser)) {
        const formData = new FormData();
        formData.append('dni', JSON.stringify(this.newUser.dni));
        formData.append('passw', JSON.stringify(this.newUser.passw));
        formData.append('nombre', JSON.stringify(this.newUser.nombre));
        formData.append('apellido', JSON.stringify(this.newUser.apellido));
        formData.append('email', JSON.stringify(this.newUser.email));
        formData.append('file', this.$refs.fileInput.files[0]);

        // Realizar la llamada a la API para guardar el nuevo usuario y la imagen
        axios
          .put(`${this.postURL}/usuario`, formData)
          .then((res) => {
            console.log(res);
            this.usuario.push(this.newUser); // Agregar el nuevo usuario al arreglo
            this.newUser = {}; // Limpiar los campos del nuevo usuario
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },

    validarDatosUsuario(usuario) {
      // Implementa la lógica de validación de los datos del usuario
      // Puedes agregar validaciones adicionales según tus requisitos
      if (!usuario.nombre || !usuario.apellido || !usuario.email || !usuario.dni || !usuario.passw) {
        alert('Por favor, complete todos los campos');
        return false;
      }
      return true;
    }
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
</style>
