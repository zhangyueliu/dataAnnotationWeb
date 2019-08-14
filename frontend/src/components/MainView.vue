<template>
    <div class="img-view">
      <div id="img_box"></div>
    </div>
</template>

<script>
    export default {
        name: "MainView"
    }
</script>

<style scoped>
  .img-view {
    padding: 10px;
  }
  #img_box {
    width: 100%;
    height: 100%;
    overflow: auto;
  }
  #img_box >>> img{
    visibility: hidden;
  }
</style>
