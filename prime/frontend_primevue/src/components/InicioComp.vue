<template>
    <div>
      <nav>
        <ul class="menu">
          <img class="imagen" src="https://siberia.ulasalle.edu.pe/logo_ulasalle.gif" alt="logo">
          <li v-for="item in menuItems" :key="item.id">
            <router-link :to="item.url" class="menu-item">
              <i :class="['pi', item.icon, 'menu-icon']"></i>
              {{ item.title }}
            </router-link>
          </li>
        </ul>
      </nav>
      <router-view></router-view>
    </div>
  </template>
  
  <style>
  .menu {
    list-style-type: none;
    margin: 0;
    padding: 0;
    background-color: #f1f1f1;
    display: flex;
  }
  
  .menu-item {
    display: flex;

    align-items: center;
    padding: 10px 20px;
    text-decoration: none;
    color: #003f52;
  }
  
  .menu-icon {
    margin-right: 5px;
  }
  
  .menu-item:hover {
    background-color: #0a6189;
    color: #c2c2c2;
  }
  .imagen {
  height: 2rem;
  margin: 0px;
  user-select: none;
  border-radius: 200rem;
  }
  </style>
  
  <script>
  export default {
    data() {
      return {
        menuItems: [
          { id: 1, title: 'Inicio', url: '/', icon: 'pi-home' },
          { id: 2, title: 'Alumno', url: '/Alumnos', icon: 'pi-user' },
          { id: 3, title: 'Docente', url: '/Docentes', icon: 'pi-users' },
          { id: 4, title: 'Usuario', url: '/Admin', icon: 'pi-file' }
        ]
      };
    }
  };
  </script>
  