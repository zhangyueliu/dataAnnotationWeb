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
    <el-form :inline="true" :model="formData" ref="formData">
      <el-form-item
        label="姓名"
        :rules="{required: true, message: '请输入姓名', trigger: 'blur'}"
      >
        <el-input v-model="formData.name"></el-input>
      </el-form-item>
      <el-form-item
        label="性别"
        :rules="{required: true, message: '请输入性别', trigger: 'blur'}"
      >
        <el-input v-model="formData.sex"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitData(formData)">提交</el-button>
      </el-form-item>
    </el-form>
  </div>

</template>

<script>
import PersonAPI from '../api/PersonAPI'
import axios from 'axios'
import Cookies from 'js-cookie'

export default {
  name: 'Home',
  data () {
    return {
      tableData: [],
      formData: {
        name: '',
        sex: ''
      }
    }
  },
  created () {
    this.getData(1)
  },
  methods: {
    getData: function ({ commit, state }, id) { // 得到指定文章详情
      PersonAPI.getAllData({ commit, state }, id).then(result => {
        this.tableData = result.data
      })
    },
    submitData: function (formData) {
      this.$refs.formData.validate((valid) => {
        if (valid) {
          this.addData()
        } else {
          return false
        }
      })
    },
    addData: function () {
      axios.get('http://127.0.0.1:8000/backend/add_data/').then(() => {
        PersonAPI.addData(this.formData).then(result => {
          if (result.data) {
            console.log('post成功')
          } else {
            console.log('post失败')
          }
        })
      })

    }
  }
}
</script>

<style scoped>

</style>
