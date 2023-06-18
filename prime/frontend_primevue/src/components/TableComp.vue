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
      <span class="p-float-label custom-textarea">
        <Textarea v-model="newUser.nombre" rows="1" cols="30" />
        <label>Nombre</label>
      </span>
      <br>
      <span class="p-float-label custom-textarea">
        <Textarea v-model="newUser.apellido" rows="1" cols="30" />
        <label>Apellido</label>
      </span>
      <br>
      <span class="p-float-label custom-textarea">
        <Textarea v-model="newUser.email" rows="1" cols="30" />
        <label>Email</label>
      </span>
      <br>
      <span class="p-float-label custom-textarea">
        <Textarea v-model="newUser.dni" rows="1" cols="30" />
        <label>DNI</label>
      </span>
      <br>
      <span class="p-float-label">
        <Textarea v-model="newUser.email" rows="1" cols="30" />
        <!-- <input v-model="newUser.id_tipo_usuario" type="text"> -->
        <label>Tipo Usuario</label>
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
    <br><template>
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
      <span class="p-float-label">
        <Textarea v-model="newUser.id_tipo_usuario" rows="1" cols="30" />
        <!-- <input v-model="newUser.id_tipo_usuario" type="text"> -->
        <label>Tipo Usuario</label>
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
      <Column field="tipo_usuario" header="Tipo usuario" :editable="true"></Column>
     
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

    <!-- Formulario de toma de asistencia -->
    <Panel :value="asistencia" class="custom-panel">
      <template #header>
        <div class="header-wrapper">
          <span class="header-text">Tomar asistencia</span>
        </div>
      </template>

      <!-- Campos para ingresar los datos de la asistencia -->
      <div>
        <label>Foto: </label>
        <input type="file" id="fotoAsistencia" ref="fileInputAsistencia" accept="image/*" required>
      </div>
      <br>
      <span class="p-float-label">
        <Textarea v-model="asistencia.dni" rows="1" cols="30" />
        <label>DNI</label>
      </span>
      <br>
      <Button type="button" label="Tomar asistencia" icon="pi pi-check" :loading="loadingAsistencia" @click="tomarAsistencia" />
    </Panel>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      usuario: [],
      newUser: {},
      asistencia: {},
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
    deleteRow(rowData) {
      if (rowData) {
        const dni = rowData.data.dni;
        const confirmation = confirm('¿Estás seguro de que deseas eliminar esta fila?');
        if (confirmation) {
          axios
            .delete(`${this.postURL}/delete_usuario`, { data: { dni: dni } }) // Pasar el parámetro dni correctamente
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
        formData.append('id_tipo_usuario', this.newUser.id_tipo_usuario); // Agrega el campo id_tipo_usuario
        formData.append('file', this.$refs.fileInput.files[0]);

        // Realizar la llamada a la API para guardar el nuevo usuario y la imagen
        axios
          .post(`${this.postURL}/add_usuario`, formData)
          .then((res) => {
            console.log(res);
            // Agregar el nuevo usuario a la lista actualizada
            this.usuario.push(res.data);
            // Limpiar los campos del formulario
            this.newUser = {};
            this.$refs.fileInput.value = '';
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
    tomarAsistencia() {
      const formData = new FormData();
      formData.append('dni', JSON.stringify(this.asistencia.dni));
      formData.append('file', this.$refs.fileInputAsistencia.files[0]);

      // Realizar la llamada a la API para tomar la asistencia y guardar la imagen
      axios
        .post(`${this.postURL}/tomar_asistencia`, formData)
        .then((res) => {
          console.log(res);
          // Limpiar los campos del formulario
          this.asistencia = {};
          this.$refs.fileInputAsistencia.value = '';
        })
        .catch((error) => {
          console.log(error);
        });
    },
    validarDatosUsuario(user) {
      // Realizar validaciones de los campos del usuario
      if (!user.nombre || !user.apellido || !user.email || !user.dni || !user.passw || !user.id_tipo_usuario) {
        alert('Por favor, completa todos los campos');
        return false;
      }

      // Otras validaciones si es necesario

      return true;
    },
  },
};
</script>

<style scoped>
.custom-panel {
  margin-bottom: 1rem;
}
.header-wrapper {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.header-text {
  font-size: 1.5rem;
  font-weight: bold;
}
.custom-password {
  margin-bottom: 1rem;
}
</style>
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
      if (this.newUser && this.newUser.dnip && this.newUser.nombrep && this.newUser.apellidop && this.newUser.emailp) {
        // Deshabilitar la edición en todas las filas
        this.usuario.forEach((user) => {
          user.editable = false;
        });

        // Realizar la solicitud PATCH al backend
        const formData = new FormData();
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
    },
    openPosition(position, rowData) {
      this.position = position;
      this.visible = true;

      // Asignar los valores de rowData a newUser
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