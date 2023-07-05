<template>
    <div>
      <!-- Formulario de ingreso de grupos -->
      <Panel :value="newGrupo" class="custom-panel">
        <template #header>
          <div class="header-wrapper">
            <span class="header-text">Crear grupo</span>
          </div>
        </template>
  
        <!-- Campos para ingresar los datos del nuevo grupo -->
        <br>
        <span class="p-float-label custom-textarea">
          <Textarea v-model="newGrupo.id_curso" rows="1" cols="30" />
          <label>ID Curso</label>
        </span>
        <br>
        <span class="p-float-label custom-textarea">
          <Textarea v-model="newGrupo.nombre_grupo" rows="1" cols="30" />
          <label>Nombre grupo</label>
        </span>
        <br>
        <span class="p-float-label custom-textarea">
          <Textarea v-model="newGrupo.aula" rows="1" cols="30" />
          <label>Aula</label>
        </span>
        <br>

        <Button type="button" icon="pi pi-save" :loading="loading" @click="guardarnewGrupo" />
      </Panel>
      <br>
      <br>
      <br>
      <!-- Tabla de grupos -->
      <DataTable :value="grupo" :editable="true" paginator :rows="5" :rowsPerPageOptions="[5, 10, 20, 50]" tableStyle="min-width: 50rem">
        <!-- Columnas -->
        <Column field="id_curso" header="ID Curso" sortable :editable="true"></Column>
        <Column field="nombre_grupo" header="Nombre" sortable :editable="true"></Column>
        <Column field="aula" header="Aula" sortable :editable="true"></Column>
        <!-- Boton acciones -->
        <Column header="Acciones">
          <template #body="rowData">
            <Button  icon="pi pi-pencil" @click="openPosition('top', rowData)" severity="warning" ></Button>
            <Button  icon="pi pi-trash" severity="info" @click="deleteRow(rowData)"></Button>
          </template>
        </Column>
       
      </DataTable>
  
      <Dialog v-model:visible="visible" header="Actualizar grupo" :style="{ width: '30vw' }" :position="position" :modal="true" :draggable="false">
        <label>ID de curso</label>
        <br>
        <span class="p-float-label custom-textarea">
        <Textarea v-model="newGrupo.id_cursop" autoResize rows="1" cols="30" />
        </span>
        <br>
        <label>Nombre de grupo</label>
        <br>
        <span class="p-float-label custom-textarea">
        <Textarea v-model="newGrupo.nombre_gruposp" autoResize rows="1" cols="30" />
        </span>
        <br>
        <label>Nombre de aula</label>
        <br>
        <span class="p-float-label custom-textarea">
        <Textarea v-model="newGrupo.aulap" autoResize rows="1" cols="30" />
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
        grupo: [],
        newGrupo: {},
        postURL: 'http://127.0.0.1:5000',
        position: 'center',
        visible: false,
      };
    },
    created() {
      axios
        .post(this.postURL + '/grupos')
        .then((res) => {
          console.log(res);
          this.grupo = res.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    methods: {
        editRow() {
  if (this.newGrupo && this.newGrupo.id_cursop && this.newGrupo.nombre_gruposp && this.newGrupo.aulap) {
    // Deshabilitar la edición en todas las filas
    this.grupo.forEach((course) => {
      course.editable = false;
    });
    console.log("carne humana");
    console.log(this.newGrupo.id_grupo);
    console.log(this.newGrupo.nombre_gruposp);
    console.log("más carne");
    // Realizar la solicitud PATCH al backend
    const payload = {
      id_grupo: this.newGrupo.id_grupo, // Obtén el id_grupo de alguna manera (por ejemplo, de la fila seleccionada)
      id_curso: this.newGrupo.id_cursop,
      nombre_grupo: this.newGrupo.nombre_gruposp,
      aula: this.newGrupo.aulap
    };

    axios
      .patch(`${this.postURL}/grupo`, payload)
      .then((res) => {
        console.log(res.data);

        // Cerrar el Dialog
        this.visible = false;

        // Actualizar los datos de la tabla
        this.cargargrupos();
      })
      .catch((error) => {
        console.log(error);
      });
  }
},
  
      cargargrupos() {
        axios
          .post(this.postURL + '/grupos')
          .then((res) => {
            console.log(res);
            this.grupo = res.data;
          })
          .catch((error) => {
            console.log(error);
          });
      },
      deleteRow(rowData) {
        if (rowData) {
          const id_grupo = rowData.data.id_grupo;
          const confirmation = confirm('¿Estás seguro de que deseas eliminar esta fila?');
          if (confirmation) {
            axios
              .delete(`${this.postURL}/grupo`, { data: { id_grupo } })
              .then((res) => {
                console.log(res);
                this.grupo = this.grupo.filter((course) => course.id_grupo !== id_grupo);
              })
              .catch((error) => {
                console.log(error);
              });
          }
        }
      },
      guardarnewGrupo() {
        // Validar los datos del nuevo grupo antes de guardarlo
        if (this.validarDatosgrupo(this.newGrupo)) {
          console.log("una noche más");
          console.log(this.newGrupo.nombre_grupo);
          console.log("copas más");

  
          // Realizar la llamada a la API para guardar el nuevo grupo y la imagen
          axios
            .put(`${this.postURL}/grupo`, { id_curso: this.newGrupo.id_curso,
                                            nombre_grupo: this.newGrupo.nombre_grupo,
                                            aula: this.newGrupo.aula})
            .then((res) => {
                console.log(res);
                this.grupo.push(this.newGrupo); // Agregar el nuevo grupo al arreglo
                this.newGrupo = {}; // Limpiar los campos del nuevo grupo
            })
            .catch((error) => {
                console.log(error);
            });
        }
      },
  
      validarDatosgrupo(grupo) {
        console.log("costumbre");
        console.log(grupo);
        console.log("de costumbre");
        // Implementa la lógica de validación de los datos del grupo
        // Puedes agregar validaciones adicionales según tus requisitos
        if (!grupo.nombre_grupo) {
          console.log("maldita costumbre");
          console.log(grupo.nombre_grupo);
          console.log("asco de costumbre");
          alert('Por favor, complete todos los campos');
          return false;
        }
        return true;
      },
      openPosition(position, rowData) {
        this.position = position;
        this.visible = true;

  // Asignar los valores de rowData a newGrupo
        this.newGrupo = {
        id_grupo: rowData.data.id_grupo,
        id_cursop: rowData.data.id_curso,
        nombre_gruposp: rowData.data.nombre_grupo,
        aulap: rowData.data.aula
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
  