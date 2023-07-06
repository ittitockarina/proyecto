<template>
  <div class="card">
    <TabMenu v-model:activeIndex="active" :model="items" />
    <router-view></router-view>
  </div>
</template>

<script setup>
import { ref } from "vue";


const active = ref(3);
const items = ref([
  {
    label: 'Home',
    url: '/',
    icon: 'pi pi-fw pi-home'
  },
  {
    label: 'tipoUsuario',
    url: '/tipo-usuario',
    icon: 'pi pi-fw pi-users'
  },
  {
    label: 'usuario',
    url: '/usuario',
    icon: 'pi pi-fw pi-user'
  },
  {
    label: 'Horario',
    url: '/horario',
    icon: 'pi pi-fw pi-calendar-times'
  },
  {
    label: 'Justificacion',
    url: '/justificacion',
    icon: 'pi pi-fw pi-pencil'
  },
  {
    label: 'Cursos',
    url: '/cursos',
    icon: 'pi pi-fw pi-book',
    
  },
  {
    label: 'Grupos',
    url: '/grupo',
    icon: 'pi pi-fw pi-users'
  },
  {
    label: 'Docente',
    url: '/docente',
    icon: 'pi pi-fw pi-user'
  },
  {
    label: 'Matricula',
    url: '/matricula',
    icon: 'pi pi-fw pi-file'
  },
  {
    label: 'Participaciones',
    url: '/participacion',
    icon: 'pi pi-fw pi-copy'
  },
  {
    label: 'alumnos',
    url: '/alumno',
    icon: 'pi pi-fw pi-user'
  },
  {
    label: 'asistencia',
    url: '/asistencia',
    icon: 'pi pi-fw pi-copy'
  }
]);
</script>

<style>
.card {
  background-color: #f0f0f0;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.p-tabmenu {
  margin-top: 20px;
}

.p-tabmenu .p-tabmenu-nav {
  background-color: #f0f0f0;
  border: none;
}

.p-tabmenu .p-tabmenu-nav .p-tabmenuitem {
  border: none;
}

.p-tabmenu .p-tabmenu-nav .p-tabmenuitem .p-menuitem-link {
  padding: 10px 20px;
  color: #333;
  font-weight: bold;
  text-decoration: none;
}

.p-tabmenu .p-tabmenu-nav .p-tabmenuitem .p-menuitem-link:hover {
  background-color: #ebebeb;
}
</style>
