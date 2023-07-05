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
      <br>
      <span class="p-float-label custom-textarea">
        <Textarea v-model="newUser.nombre" rows="1" cols="30" />
        <label>Nombre</label>
      </span>
      <br>
      <br>
      <span class="p-float-label custom-textarea">
        <Textarea v-model="newUser.apellido" rows="1" cols="30" />
        <label>Apellido</label>
      </span>
      <br>
      <br>
      <span class="p-float-label custom-textarea">
        <Textarea v-model="newUser.email" rows="1" cols="30" />
        <label>Email</label>
      </span>
      <br>
      <br>
      <span class="p-float-label custom-textarea">
        <Textarea v-model="newUser.dni" rows="1" cols="30" />
        <label>DNI</label>
      </span>
      <br>
      <br>
      <span class="p-float-label custom-textarea">
        <Textarea v-model="newUser.id_tipo_usuario" rows="1" cols="30" />
        <label>ID Tipo de usuario</label>
      </span>
      <br>
      <br>
      <span class="p-float-label custom-password">
        <Password v-model="newUser.passw" inputId="password" toggleMask />
        <label for="password">Password</label>
      </span>
      <br>
      <br>
      <Button type="button" icon="pi pi-save" :loading="loading" @click="guardarnewUser" />
    </Panel>
    <br>
    <br>
    <br>
    <!-- Tabla de usuarios -->
    <DataTable :value="usuario" :editable="true" paginator :rows="5" :rowsPerPageOptions="[5, 10, 20, 50]" tableStyle="min-width: 50rem">
      <!-- Columnas -->
      <Column field="id_tipo_usuario" header="ID Tipo de usuario" :editable="true"></Column>
      <Column field="dni" header="DNI" :editable="true"></Column>
      <Column field="nombre" sortable header="Nombre" :editable="true"></Column>
      <Column field="apellido" sortable header="Apellido" :editable="true"></Column>
      <Column field="email" header="Correo" :editable="true"></Column>
      <!-- Boton Acciones -->
      <Column header="Acciones">
        <template #body="rowData">
          <Button icon="pi pi-pencil" @click="openPosition('top', rowData)" severity="warning" ></Button>
          <Button icon="pi pi-trash" severity="info" @click="deleteRow(rowData)"></Button>
        </template>
      </Column>
      
    </DataTable>

    <Dialog v-model:visible="visible" header="Actualizar Usuario" :style="{ width: '30vw' }" :position="position" :modal="true" :draggable="false">
      <label>Nombre</label>
      <br>
      <span class="p-float-label custom-textarea">
      <Textarea v-model="newUser.nombrep" autoResize rows="1" cols="30" />
      </span>
      <br>
      <span class="p-float-label custom-textarea">
      <label>Apellido</label>
      </span>
      <br>
      <span class="p-float-label custom-textarea">
      <Textarea v-model="newUser.apellidop" autoResize rows="1" cols="30" />
      </span>
      <br>
      <span class="p-float-label custom-textarea">
      <label>Email</label>
      </span>
      <br>
      <span class="p-float-label custom-textarea">
      <Textarea v-model="newUser.emailp" autoResize rows="1" cols="30" />
      </span>
      <br>
      <label>DNI</label>
      <br>
      <span class="p-float-label custom-textarea">
      <Textarea v-model="newUser.dnip" autoResize rows="1" cols="30" />
      </span>
      <br>
      <label>ID Tipo de usuario</label>
      <br>
      <span class="p-float-label custom-textarea">
      <Textarea v-model="newUser.id_tipo_usuariop" autoResize rows="1" cols="30" />
      </span>
      <br>
      <label>Password</label>
      <br>
      <span class="p-float-label custom-password">
        <Password v-model="newUser.passwp" toggleMask />
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
      usuario: [],
      newUser: {},
      postURL: 'http://127.0.0.1:5000',
      position: 'center',
      visible: false,
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
    editRow() {
      if (this.newUser && this.newUser.dnip && this.newUser.nombrep && this.newUser.apellidop && this.newUser.emailp && this.newUser.id_tipo_usuariop) {
        // Deshabilitar la edición en todas las filas
        this.usuario.forEach((user) => {
          user.editable = false;
        });

        // Realizar la solicitud PATCH al backend
        console.log("wars");
        console.log(this.newUser.id_usuario);
        console.log(this.newUser.id_tipo_usuariop);
        console.log(this.newUser.dnip);
        console.log(this.newUser.passwp);
        console.log(this.newUser.nombrep);
        console.log(this.newUser.apellidop);
        console.log(this.newUser.emailp);
        console.log("peaces");
        const formData = new FormData();
        formData.append('id_usuario', JSON.stringify(this.newUser.id_usuario));
        formData.append('id_tipo_usuario', JSON.stringify(this.newUser.id_tipo_usuariop));
        formData.append('dni', JSON.stringify(this.newUser.dnip));
        formData.append('passw', JSON.stringify(this.newUser.passwp));
        formData.append('nombre', JSON.stringify(this.newUser.nombrep));
        formData.append('apellido', JSON.stringify(this.newUser.apellidop));
        formData.append('email', JSON.stringify(this.newUser.emailp));

        axios
          .patch(`${this.postURL}/usuario`, formData)
          .then((res) => {
            console.log(res.data);

            // Cerrar el Dialog
            this.visible = false;

            // Actualizar los datos de la tabla
            this.cargarUsuarios();
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },

    cargarUsuarios() {
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
    deleteRow(rowData) {
      if (rowData) {
        const id_usuario = rowData.data.id_usuario;
        const confirmation = confirm('¿Estás seguro de que deseas eliminar esta fila?');
        if (confirmation) {
          axios
            .delete(`${this.postURL}/usuario`, { data: { id_usuario } })
            .then((res) => {
              console.log(res);
              this.usuario = this.usuario.filter((user) => user.id_usuario !== id_usuario);
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
        formData.append('id_tipo_usuario', JSON.stringify(this.newUser.id_tipo_usuario));
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
      if (!usuario.nombre || !usuario.apellido || !usuario.email || !usuario.dni || !usuario.passw || !usuario.id_tipo_usuario) {
        alert('Por favor, complete todos los campos');
        return false;
      }
      return true;
    },
    openPosition(position, rowData) {
      this.position = position;
      this.visible = true;

      // Asignar los valores de rowData a newUser
      this.newUser.id_usuario = rowData.data.id_usuario;
      this.newUser.id_tipo_usuariop = rowData.data.id_tipo_usuario;
      this.newUser.nombrep = rowData.data.nombre;
      this.newUser.apellidop = rowData.data.apellido;
      this.newUser.emailp = rowData.data.email;
      this.newUser.dnip = rowData.data.dni;
      this.newUser.passwp = rowData.data.passw;
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