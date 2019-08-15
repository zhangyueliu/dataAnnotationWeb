<template>
    <div class="menu-box">
      <el-button-group>
        <el-button type="primary" icon="el-icon-arrow-left" size="small">上一张</el-button>
        <el-button type="primary" size="small">下一张<i class="el-icon-arrow-right el-icon--right"></i></el-button>
      </el-button-group>
      <el-button-group>
        <el-button type="success" icon="el-icon-zoom-in" size="small">放大</el-button>
        <el-button type="success" icon="el-icon-zoom-out" size="small">缩小</el-button>
      </el-button-group>
      <el-button type="success" icon="el-icon-download" size="small">导出</el-button>
    </div>
</template>

<script>
    export default {
        name: "MenuBar"
    }
</script>

<style scoped>
  .menu-box{
    padding: 2px 10px;
  }
</style>
