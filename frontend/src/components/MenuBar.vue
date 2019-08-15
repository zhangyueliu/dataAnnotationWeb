<template>
    <div class="menu-box">
      <el-button-group>
        <el-button type="primary" icon="el-icon-arrow-left" size="small" @click="pre_img()">上一张</el-button>
        <el-button type="primary" size="small" @click="next_img()">下一张<i class="el-icon-arrow-right el-icon--right"></i></el-button>
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
      name: "MenuBar",
      methods:{
        pre_img: function () {
          let is_selected_id = document.getElementsByClassName('visible')[0].id
          this.bus.$emit('pre-img',is_selected_id)
        },
        next_img: function () {
          let is_selected_id = document.getElementsByClassName('visible')[0].id
          this.bus.$emit('next-img',is_selected_id)
        }
      }
    }
</script>

<style scoped>
  .menu-box{
    padding: 2px 10px;
  }
</style>
