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
    label: 'Alumnos',
    url: '/vistaParticipa',
    icon: 'pi pi-fw pi-users'
  },
  {
    label: 'Horario',
    url: '/horario',
    icon: 'pi pi-fw pi-calendar-times'
  },
  {
    label: 'Justificacion',
    url: '/justiDocente',
    icon: 'pi pi-fw pi-pencil'
  },
 
  {
    label: 'ver materias',
    url: '/listadoDocente',
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
