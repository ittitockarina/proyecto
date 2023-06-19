import { createApp } from 'vue';

import App from './App.vue';
///////////////////////////
import { createRouter, createWebHistory } from 'vue-router';
///////////////////////////////

// Importar PrimeVue y los estilos necesarios
import PrimeVue from 'primevue/config';
import 'primevue/resources/themes/saga-blue/theme.css';
import 'primevue/resources/primevue.min.css';
import 'primeicons/primeicons.css';
import "primevue/resources/themes/lara-light-indigo/theme.css"; 

// Importar los componentes específicos de PrimeVue que necesites
import Button from 'primevue/button';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import Panel from 'primevue/panel';
import ColumnGroup from 'primevue/columngroup';
import Row from 'primevue/row';
import Textarea from 'primevue/textarea';
import FileUpload from 'primevue/fileupload';
import Menu from 'primevue/menu';
import Password from 'primevue/password';
import ToastService from 'primevue/toastservice'; // Importar el servicio Toast
import PanelMenu from 'primevue/panelmenu';
import TieredMenu from 'primevue/tieredmenu';
import Dock from 'primevue/dock';
import TabMenu from 'primevue/tabmenu';
import Dialog from 'primevue/dialog';
import Calendar from 'primevue/calendar';
import InputSwitch from 'primevue/inputswitch';

///////////////////////////////////////77
import AsistenciaComp from './components/AsistenciaComp.vue';
import DocenteComp from './components/DocenteComp.vue';
import AlumnoComp from './components/AlumnoComp.vue';

/////////////////////////////////////////



const app = createApp(App);
////////////////////////////////////
const router = createRouter({
    history: createWebHistory(),
    routes: [
      { path: '/admin', name: 'Admin', component: AsistenciaComp },
      { path: '/docente', name: 'Docente', component: DocenteComp },
      { path: '/estudiante', name: 'Alumnos', component: AlumnoComp },
    ],
  });
///////////////////////////////////

// Usar PrimeVue y el servicio Toast en la aplicación
app.use(ToastService);
app.use(PrimeVue);

// Registrar los componentes específicos de PrimeVue que necesites
app.component('Button', Button);
app.component('DataTable', DataTable);
app.component('Column', Column);
app.component('Panel', Panel);
app.component('ColumnGroup', ColumnGroup);
app.component('Row', Row);
app.component('Textarea', Textarea);
app.component('FileUpload', FileUpload);
app.component('Menu', Menu);
app.component('Password', Password);
app.component('PanelMenu', PanelMenu);
app.component('TieredMenu', TieredMenu);
app.component('Dock', Dock);
app.component('TabMenu', TabMenu);
app.component('Dialog',Dialog)
app.component('Calendar',Calendar);
app.component('InputSwitch',InputSwitch);

app.mount('#app');
