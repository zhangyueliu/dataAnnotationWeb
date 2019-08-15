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
    <el-button type="primary" @click="select_local_files">Add Files</el-button>
    <input id="invisible_file_input" type="file" style="display: none;" multiple="multiple" accept=".jpg,.jpeg,.png,.bmp" @change="add_local_files"/>

    <div v-for="(item,index) in via_img_metadata" @click="jump_to_image(index)">{{item.filename}}</div>
    <div id="img_box"></div>

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
      },
      via_img_metadata: {},  // data structure to store loaded images metadata
      via_img_fileref: {},  // reference to local images selected by using browser file selector
      via_image_id_list: [],
      via_image_filename_list: [],
      via_img_count: 0,
      fileList: {}
    }
  },
  created () {
    this.getData(1)
  },
  methods: {
    select_local_files: function(){
      document.getElementById('invisible_file_input').click()
    },
    add_local_files: function(event){
      let select_local_files = event.target.files
      let new_img_index_list = []
      this.fileList = select_local_files
      for (let i = 0; i < select_local_files.length; i++) {
        let filetype =select_local_files[i].type.substr(0, 5)
        if (filetype === 'image') {
          let filename = select_local_files[i].name
          let size = select_local_files[i].size
          let img_id1 = this._via_get_image_id(filename, size)
          let img_id2  = this._via_get_image_id(filename, -1);
          let img_id = img_id1
          if (this.via_img_metadata.hasOwnProperty(img_id1) || this.via_img_metadata.hasOwnProperty(img_id2)) {
            if(this.via_img_metadata.hasOwnProperty(img_id2)) {
              img_id = img_id2
            }
            this.via_img_fileref[img_id] =select_local_files[i]
            if (this.via_img_metadata[img_id].size === -1 ) {
             this. via_img_metadata[img_id].size = size;
            }

          } else {
            img_id = this.project_add_new_file(filename, size)
            this.via_img_fileref[img_id] =select_local_files[i]
            new_img_index_list.push(this.via_image_id_list.indexOf(img_id))
          }
        } else {
          console.log('其它类型文件！')
        }
      }
      if(this.via_img_metadata) {
        if(new_img_index_list.length) {
          //显示new_img_index_list[0]
          this._via_show_img(new_img_index_list[0])
        } else {
          // show original image
        }
      } else {
        // 没有增加新文件
      }

    },
    project_add_new_file: function (filename, size, file_id){
      var img_id = file_id;
      if ( typeof(img_id) === 'undefined' ) {
        if ( typeof(size) === 'undefined' ) {
          size = -1;
        }
        img_id = this._via_get_image_id(filename, size);
      }

      if (!this.via_img_metadata.hasOwnProperty(img_id) ) {
        this.$set(this.via_img_metadata,img_id,new file_metadata(filename, size))
        this.via_image_id_list.push(img_id);
        this.via_image_filename_list.push(filename);
        this.via_img_count += 1;
      }
      return img_id;
    },
    _via_get_image_id: function (filename, size) {
      if ( typeof(size) === 'undefined' ) {
        return filename;
      } else {
        return filename + size;
      }
    },
    getObjectURL: function (file) {
      console.log(file)
      let url = null ;
      if (window.createObjectURL!=undefined) { // basic
        url = window.createObjectURL(file) ;
      }else if (window.webkitURL!=undefined) { // webkit or chrome
        url = window.webkitURL.createObjectURL(file) ;
      }else if (window.URL!=undefined) { // mozilla(firefox)
        url = window.URL.createObjectURL(file) ;
      }
      return url ;
    },
    _via_show_img: function (img_index) {
      let img_id = this.via_image_id_list[img_index]
      let url = this.getObjectURL(this.via_img_fileref[img_id])
      let bimg = document.createElement('img')
      bimg.setAttribute('src',url)
      document.getElementById('img_box').append(bimg)
    },
    jump_to_image: function (img_id) {
      console.log(this.via_image_id_list.indexOf(img_id))
      this._via_show_img(this.via_image_id_list.indexOf(img_id))
    },
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

function file_metadata(filename, size) {
  this.filename = filename;
  this.size     = size;         // file size in bytes
  this.regions  = [];           // array of file_region()
  this.file_attributes = {};    // image attributes
}
</script>

<style scoped>
  #img_box >>> img{
    visibility: hidden;
  }
</style>
