<template>
  <div class="home">
    <el-table
    :data="tableData"
  >
      <el-table-column
        prop="date"
        label="日期"
      ></el-table-column>
      <el-table-column
        prop="name"
        label="姓名">
      </el-table-column>
      <el-table-column
        prop="sex"
        label="性别">
      </el-table-column>
    </el-table>
  </div>

</template>

<script>
import PersonAPI from "../api/PersonAPI"

export default {
  name: 'Home',
  data () {
    return {
      tableData: []
    }
  },
  created () {
    this.getArticlesSpecific(1);
  },
  methods:{
    getArticlesSpecific: function({ commit, state }, id) { //得到指定文章详情
      PersonAPI.getArticlesSpecific({ commit, state }, id).then(result => {
        this.tableData = result.data;
      })
    }
  }
}
</script>

<style scoped>

</style>
