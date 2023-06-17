import { createApp } from 'vue'
import App from './App.vue'

// import
import PrimeVue from 'primevue/config';

import 'primevue/resources/themes/saga-blue/theme.css'; // Tema de PrimeVue
import 'primeicons/primeicons.css'; // Iconos de PrimeIcons

//theme
import "primevue/resources/themes/lara-light-indigo/theme.css"; 
//core
import "primevue/resources/primevue.min.css";

// cada componente se importa de forma separada +++++++++++++++++++++++++
import Button from "primevue/button"
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import Panel from 'primevue/panel';
import ColumnGroup from 'primevue/columngroup';   // optional
import Row from 'primevue/row';
import Textarea from 'primevue/textarea';
import FileUpload from 'primevue/fileupload';
import Menu from 'primevue/menu';
import Password  from 'primevue/password';
import Dialog from 'primevue/dialog';
//import { useToast } from "primevue/usetoast";

const app = createApp(App);
app.use(PrimeVue);

//app.component('useToast', useToast);
app.component('Dialog',Dialog)
app.component('Password', Password);
app.component('Button', Button);
app.component('DataTable', DataTable);
app.component('Column', Column);
app.component('Panel', Panel);
app.component('Textarea', Textarea);
app.component('FileUpload',FileUpload);
app.component('Menu',Menu);


// aqui agregamos el componente ******************************************




app.mount("#app")