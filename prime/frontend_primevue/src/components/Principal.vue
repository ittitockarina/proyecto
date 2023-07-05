<template>
    <div>
      <nav>
        <ul class="menu">
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
  </style>
  
  <script>
  export default {
    data() {
      return {
        menuItems: [
          { id: 1, title: 'Tomar Asistencia', url: '/tomar-asistencia', icon: 'pi-calendar' },
          { id: 2, title: 'Cursos', url: '/cursos', icon: 'pi-book' },
          { id: 3, title: 'Grupo', url: '/grupo', icon: 'pi-users' },
          { id: 4, title: 'Docente', url: '/docente', icon: 'pi-user' }
        ]
      };
    }
  };
  </script>
  