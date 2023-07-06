import { createApp } from 'vue';
import App from './App.vue';

import { createRouter, createWebHistory } from 'vue-router'; 
import Vue from 'vue';


import PrimeVue from 'primevue/config';
import 'primevue/resources/themes/saga-blue/theme.css';
import 'primevue/resources/primevue.min.css';
import 'primeicons/primeicons.css';
import "primevue/resources/themes/lara-light-indigo/theme.css";

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
import ToastService from 'primevue/toastservice';
import PanelMenu from 'primevue/panelmenu';
import TieredMenu from 'primevue/tieredmenu';
import Dock from 'primevue/dock';
import TabMenu from 'primevue/tabmenu';
import Dialog from 'primevue/dialog';
import Calendar from 'primevue/calendar';
import InputSwitch from 'primevue/inputswitch';

//componentes inicio de sesion

import AlumnoLogin from './components/AlumnoLogin.vue';
import DocenteLogin from './components/DocenteLogin.vue';
//  componentes que se utilizarán en las rutas
import tomarAsistencia from './components/tomarAsistencia.vue';
import CursosComp from './components/CursosComp.vue';
import GrupoComp from './components/GrupoComp.vue';
import ParticipacionComp from './components/ParticipacionComp.vue';
import AlumnoComp from './components/AlumnoComp.vue';
import DocenteComp from './components/DocenteComp.vue';
import HorarioComp from './components/HorarioComp.vue';
import AsistenciaComp from './components/AsistenciaComp.vue';
import MatriculaComp from './components/MatriculaComp.vue';
import JustificacionComp from './components/JustificacionComp.vue';
import TipoUserComp from './components/TipoUserComp.vue';
import UsuarioComp from './components/UsuarioComp.vue';
import vistaParticipa from './components/vistaParticipa.vue';
import vistaComp from './components/vistaComp.vue';
import listado from './components/listado.vue';
import justiAlumno from './components/justiAlumno.vue';
import justiDocente from './components/justiDocente.vue';
import listadoDocente from './components/listadoDocente.vue';
const app = createApp(App);


// componentes correspondientes
const routes = [
  
  { path: '/Alumnos', component: AlumnoLogin },
  { path: '/Docentes', component: DocenteLogin },
  ///////////////////////////
  { path: '/tomar-asistencia', component: tomarAsistencia },
  { path: '/cursos', component: CursosComp },
  { path: '/grupo', component: GrupoComp },
  { path: '/participacion', component: ParticipacionComp },
  { path: '/alumno', component: AlumnoComp },
  { path: '/docente', component: DocenteComp },
  { path: '/horario', component: HorarioComp },
  { path: '/asistencia', component: AsistenciaComp },
  { path: '/matricula', component: MatriculaComp },
  { path: '/justificacion', component: JustificacionComp },
  { path: '/tipo-usuario', component: TipoUserComp },
  { path: '/usuario', component: UsuarioComp },
  { path: '/vistaParticipa', component: vistaParticipa },
  { path: '/vistaComp', component: vistaComp },
  { path: '/listado', component: listado },
  { path: '/justiAlumno', component: justiAlumno },
  { path: '/justiDocente', component: justiDocente },
  { path: '/listadoDocente', component: listadoDocente },
];
/* const router = createRouter({
  history: createWebHistory('/'),
  routes: [
    // tus rutas aquí
    { path: '/Admin', component: AdminLogin },
    { path: '/Alumnos', component: AlumnoLogin },
    { path: '/Docentes', component: DocenteLogin },
    ///////////////////////////
    { path: '/tomar-asistencia', component: tomarAsistencia },
    { path: '/cursos', component: CursosComp },
    { path: '/grupo', component: GrupoComp },
    { path: '/participacion', component: ParticipacionComp },
    { path: '/alumno', component: AlumnoComp },
    { path: '/docente', component: DocenteComp },
    { path: '/horario', component: HorarioComp },
    { path: '/asistencia', component: AsistenciaComp },
    { path: '/matricula', component: MatriculaComp },
    { path: '/justificacion', component: JustificacionComp },
    { path: '/tipo-usuario', component: TipoUserComp },
    { path: '/usuario', component: UsuarioComp },
    { path: '/vistaParticipa', component: vistaParticipa },
  ]
}); */
const router = createRouter({
  history: createWebHistory('/'),
  routes
});


/* const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/Admin', component: AdminLogin },
    { path: '/Alumnos', component: AlumnoLogin },
    { path: '/Docentes', component: DocenteLogin },
    { path: '/tomar-asistencia', component: tomarAsistencia },
    { path: '/cursos', component: CursosComp },
    { path: '/grupo', component: GrupoComp },
    { path: '/participacion', component: ParticipacionComp },
    { path: '/alumno', component: AlumnoComp },
    { path: '/docente', component: DocenteComp },
    { path: '/horario', component: HorarioComp },
    { path: '/asistencia', component: AsistenciaComp },
    { path: '/matricula', component: MatriculaComp },
    { path: '/justificacion', component: JustificacionComp },
    { path: '/tipo-usuario', component: TipoUserComp },
    { path: '/usuario', component: UsuarioComp },
    { path: '/vistaParticipa', component: vistaParticipa },
  ],
});

app.use(router); */

app.use(ToastService);
app.use(PrimeVue);
app.use(router);

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
app.component('Dialog', Dialog);
app.component('Calendar', Calendar);
app.component('InputSwitch', InputSwitch);




app.mount('#app');
