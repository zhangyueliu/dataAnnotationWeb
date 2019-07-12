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
  import axios from 'axios'

export default {
  name: 'Home',
  data () {
    return {
      tableData: []
    }
  },
  created () {
    axios.get('http://127.0.0.1:8000/backend/').then(response => {
      this.tableData = response.data;
    })
  }
}
</script>

<style scoped>

</style>
