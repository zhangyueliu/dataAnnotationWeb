<template>
  <div class="layout">
    <menu-bar class="menu-bar"></menu-bar>
    <div class="main">
      <sidebar class="sidebar"></sidebar>
      <main-view class="main-view"></main-view>
    </div>
  </div>
</template>

<script>
  import MenuBar from './MenuBar'
  import Sidebar from './Sidebar'
  import MainView from './MainView'
  export default {
    name: "Layout",
    components: {
      menuBar: MenuBar,
      sidebar: Sidebar,
      mainView: MainView
    },
  }
</script>

<style scoped>
  .layout{
    height: 100%;
    overflow: hidden;
  }
  .menu-bar{
    height: 40px;
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
  }
  .main{
    margin-top: 40px;
    height: calc(100% - 40px);
  }
  .sidebar{
    position: fixed;
    top: 40px;
    left: 0;
    bottom: 0;
    width: 260px;
  }
  .main-view{
    margin-left: 260px;
    height: 100%;
  }
</style>
