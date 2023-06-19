
<template>
    <div class="card flex flex-column align-items-center">
        <div class="mb-3">
            <Button type="button" icon="pi pi-plus" label="Ver Mas" @click="expandAll" class="mr-2" />
            <Button type="button" icon="pi pi-minus" label="Ver Menos" @click="collapseAll" />
        </div>
        <PanelMenu v-model:expandedKeys="expandedKeys" :model="items" class="w-full md:w-25rem"  />
    </div>
</template>

<script setup>
import { ref } from "vue";
import axios from 'axios';

const expandedKeys = ref({});
const items = ref([
    {
        key: '0',
        label: 'Usuario',
        icon: 'pi pi-fw pi-user',
        items: [
            {
                label: 'Cargar Usuarios',
                command: cargarUsuarios
            },
        
        ]
    },
    {
        key: '1',
        label: 'Edit',
        icon: 'pi pi-fw pi-pencil',
        items: [
            {
                key: '1_0',
                label: 'Left',
                icon: 'pi pi-fw pi-align-left'
            },
            {
                key: '1_1',
                label: 'Right',
                icon: 'pi pi-fw pi-align-right'
            },
            {
                key: '1_2',
                label: 'Center',
                icon: 'pi pi-fw pi-align-center'
            },
            {
                key: '1_3',
                label: 'Justify',
                icon: 'pi pi-fw pi-align-justify'
            }
        ]
    },
    {
        key: '2',
        label: 'Users',
        icon: 'pi pi-fw pi-user',
        items: [
            {
                key: '2_0',
                label: 'New',
                icon: 'pi pi-fw pi-user-plus'
            },
            {
                key: '2_1',
                label: 'Delete',
                icon: 'pi pi-fw pi-user-minus'
            },
            {
                key: '2_2',
                label: 'Search',
                icon: 'pi pi-fw pi-users',
                items: [
                    {
                        key: '2_2_0',
                        label: 'Filter',
                        icon: 'pi pi-fw pi-filter',
                        items: [
                            {
                                key: '2_2_0_0',
                                label: 'Print',
                                icon: 'pi pi-fw pi-print'
                            }
                        ]
                    },
                    {
                        key: '2_2_1',
                        icon: 'pi pi-fw pi-bars',
                        label: 'List'
                    }
                ]
            }
        ]
    },
    {
        key: '3',
        label: 'Events',
        icon: 'pi pi-fw pi-calendar',
        items: [
            {
                key: '3_0',
                label: 'Edit',
                icon: 'pi pi-fw pi-pencil',
                items: [
                    {
                        key: '3_0_0',
                        label: 'Save',
                        icon: 'pi pi-fw pi-calendar-plus'
                    },
                    {
                        key: '3_0_0',
                        label: 'Delete',
                        icon: 'pi pi-fw pi-calendar-minus'
                    }
                ]
            },
            {
                key: '3_1',
                label: 'Archieve',
                icon: 'pi pi-fw pi-calendar-times',
                items: [
                    {
                        key: '3_1_0',
                        label: 'Remove',
                        icon: 'pi pi-fw pi-calendar-minus'
                    }
                ]
            }
        ]
    }
]);


const expandAll = () => {
    for (let node of items.value) {
        expandNode(node);
    }

    expandedKeys.value = {...expandedKeys.value};
};

const collapseAll = () => {
    expandedKeys.value = {};
};

const expandNode = (node) => {
    if (node.items && node.items.length) {
        expandedKeys.value[node.key] = true;

        for (let child of node.items) {
            expandNode(child);
        }
    }
};



const usuario = ref([]);
//const newUser = ref({});

function cargarUsuarios() {
  const postURL = 'http://127.0.0.1:5000';

  axios.post(postURL + '/usuarios')
    .then((response) => {
      console.log(response);
      usuario.value = response.data;
    })
    .catch((error) => {
      console.log(error);
    });
}

</script>