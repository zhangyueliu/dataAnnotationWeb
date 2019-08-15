<template>
    <div class="img-view">
      <div id="img-box"></div>
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
  #img-box {
    width: 100%;
    height: 100%;
    overflow: auto;
    position: relative;
  }
  #img_box >>> img{
    visibility: hidden;
    position: absolute;
    top: 0px;
    left: 0px;
  }
  #img-box >>> img.visible{
    visibility: visible;
  }
</style>
