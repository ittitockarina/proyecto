<template>
  <div class="card flex justify-content-center">
    <Menu :model="items">
      <template #start>
        <button @click="profileClick" class="w-full p-link flex align-items-center p-2 pl-3 text-color hover:surface-200 border-noround">
          <Avatar :image="user.image" class="mr-2" shape="circle" />
          <div class="flex flex-column align">
            <span class="font-bold">{{ user.name }}</span>
            <span class="text-sm">{{ user.email }}</span>
          </div>
        </button>
      </template>
      <template #end>
        <button @click="logoutClick" class="w-full p-link flex align-items-center p-2 pl-4 text-color hover:surface-200 border-noround">
          <i class="pi pi-sign-out" />
          <span class="ml-2">Log Out</span>
        </button>
      </template>
    </Menu>
    <Toast />
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useToast } from "primevue/usetoast";

const items = ref([
  { separator: true },
  { label: 'Inicio', icon: 'pi pi-fw ' },
  { label: 'Estudiantes', icon: 'pi pi-fw ' },
  { label: 'Docentes', icon: 'pi pi-fw ' },
  { label: 'Asistencia', icon: 'pi pi-fw ' },
  { label: 'Usuarios', icon: 'pi pi-fw ' },//pi-cog
  { label: 'Cursos inscritos', icon: 'pi pi-fw ' },
  { separator: true }
]);

const toast = useToast();

// Datos del usuario
const user = ref({
  name: "USUARIO"
});

const profileClick = () => {
  toast.add({ severity: 'info', summary: 'Info', detail: 'Item Selected', life: 3000 });
}

const logoutClick = () => {
  // Lógica para cerrar sesión
}
</script>
