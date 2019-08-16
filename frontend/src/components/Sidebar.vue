<template>
    <div class="sidebar-box">
      <div>
        <div class="img-list-title">图片列表</div>
        <div class="img-title-list-box">
          <div id="img-title-list">
            <div v-for="(item,index) in via_img_metadata" @click="jump_to_image(index)" class="img-title" :id="'title-' + index">{{item.filename}}</div>
          </div>
        </div>
        <div class="add-file-btn-group">
          <el-button icon="el-icon-circle-plus" size="small" @click="select_local_files">添加本地图片</el-button>
          <el-button icon="el-icon-circle-plus" size="small">添加URL</el-button>
          <input id="invisible_file_input" type="file" style="display: none;" multiple="multiple" accept=".jpg,.jpeg,.png,.bmp" @change="add_local_files"/>
        </div>
      </div>
    </div>
</template>

<script>
    export default {
      name: "Sidebar",
      data () {
        return {
          via_img_metadata: {},  // data structure to store loaded images metadata
          via_img_fileref: {},  // reference to local images selected by using browser file selector
          via_image_id_list: [],
          via_image_filename_list: [],
          via_img_count: 0,
          fileList: {}
        }
      },
      mounted () {
        let _this = this
        this.bus.$on('pre-img',function (is_selected_id) {
          let is_selected_index = _this.via_image_id_list.indexOf(is_selected_id)
          let pre_index = (is_selected_index - 1 + _this.via_image_id_list.length) % _this.via_image_id_list.length
          let pre_id = _this.via_image_id_list[pre_index]
          _this.jump_to_image(pre_id)
        })
        this.bus.$on('next-img',function (is_selected_id) {
          let is_selected_index = _this.via_image_id_list.indexOf(is_selected_id)
          let pre_index = (is_selected_index + 1 + _this.via_image_id_list.length) % _this.via_image_id_list.length
          let pre_id = _this.via_image_id_list[pre_index]
          _this.jump_to_image(pre_id)
        })
      },
      methods: {
        add_local_files: function (event) {
          let select_local_files = event.target.files
          let new_img_id_list = []
          this.fileList = select_local_files
          for (let i = 0; i < select_local_files.length; i++) {
            let filetype = select_local_files[i].type.substr(0, 5)
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
                new_img_id_list.push(img_id)
              }
            } else {
              console.log('其它类型文件！')
            }
          }
          this.bus.$emit('change-image-list', this.via_img_fileref)
          if(this.via_img_metadata) {
            if(new_img_id_list.length) {
              this.bus.$emit('add-image-list', new_img_id_list)
              //显示new_img_index_list[0]
              this._via_show_img(new_img_id_list[0])
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
        _via_show_img: function (img_id) {
          this.bus.$emit('show-img',img_id)
          this.$nextTick(() => {
            // 点击图片列表，样式切换
            this.img_title_list_remove_all_active_class()
            this.img_title_list_add_active_class(img_id)
          })
        },
        jump_to_image: function (img_id) {
          this._via_show_img(img_id)
        },
        select_local_files: function () {
          document.getElementById('invisible_file_input').click()
        },
        img_title_list_add_active_class: function (img_id) {
          // 列表高亮
          let element = document.getElementById('title-' + img_id)
          element.classList.add('img-title-active')
          // 当前选中列表滚动到可视区域
          this.img_title_list_scroll_to_view(element)
        },
        img_title_list_remove_all_active_class: function () {

            let els = document.getElementById('img-title-list').childNodes
            let i
            for (i = 0; i < els.length; i++) {
              els[i].classList.remove('img-title-active')
            }

        },
        // 图片列表根据选中元素滚动，以显示选中元素
        img_title_list_scroll_to_view: function (element) {
          let img_title_list_box = document.getElementsByClassName('img-title-list-box')[0]
          let img_list_title = document.getElementsByClassName('img-list-title')[0]
          // 该元素 距离 显示区域顶部 的距离
          let img_title_top = element.offsetTop - img_list_title.offsetHeight - img_title_list_box.scrollTop
          // 该元素的高度
          let img_title_height = element.offsetHeight
          // 显示区域的高度
          let box_height = img_title_list_box.clientHeight
          // 如果距离显示区域顶部的距离小于等于0，则是在显示区域上面，则向下滚动
          if (img_title_top <= 0) {
            // img_title_top为负值，直接加上即可
            img_title_list_box.scrollTop += img_title_top
          } else { //大于0，也就是在显示区域顶部的下面了
            // 元素底部 距离 显示区域底部 的距离
            let differ = box_height - (img_title_top + img_title_height)
            // 距离 显示区域底部 的距离小于0，则在显示区域的底部的下面了，则向上滚动；大于等于0，则在显示区域内，不需要滚动
            if (differ < 0) {
              // differ为负值，要减去它
              img_title_list_box.scrollTop -= differ
            }
          }
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
  .sidebar-box{
    border: 1px solid #c6e2ff;
  }
  .img-list-title{
    line-height: 40px;
    padding: 0 10px;
    background: #ecf5ff;
    border-bottom: 1px solid #c6e2ff;
  }
  .img-title-list-box{
    height: 300px;
    overflow: auto;
    border-bottom: 1px solid #c6e2ff;
    padding: 5px;
  }
  .img-title{
    padding: 0 5px;
    line-height: 24px;
    border-left: 3px solid #c6e2ff;
  }
  .img-title:hover{
    color: #409EFF;
    border-color: #409EFF;
    font-weight: bold;
    cursor: pointer;
  }
  .add-file-btn-group{
    padding: 0 10px;
    border-bottom: 1px solid #c6e2ff;
  }
  .add-file-btn-group >>> button{
    margin-top: 3px;
    margin-bottom: 3px;
  }
  .img-title-active {
    font-weight: bold;
    border-left: 3px solid;
  }
</style>
