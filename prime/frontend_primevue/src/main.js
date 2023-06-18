import { createApp } from 'vue';
import App from './App.vue';


// Importar PrimeVue y los estilos necesarios
import PrimeVue from 'primevue/config';
import 'primevue/resources/themes/saga-blue/theme.css';
import 'primevue/resources/primevue.min.css';
import 'primeicons/primeicons.css';

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

const app = createApp(App);

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

app.mount('#app');
