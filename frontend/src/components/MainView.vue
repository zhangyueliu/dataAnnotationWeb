<template>
    <div class="img-view">
      <div id="img-box">
        <img v-for="item in image_list" :src="item.url" :id="item.id" class="img-item" />
      </div>
    </div>
</template>

<script>
    export default {
      name: "MainView",
      data(){
        return{
          via_img_fileref: {},
          image_list: []
        }
      },
      mounted(){
        let _this = this
        this.bus.$on('change-image-list', function (result) {
          _this.via_img_fileref = result
        })
        this.bus.$on('add-image-list', function (result) {
          let image_obj
          let i
          for (i = 0; i < result.length; i++) {
            image_obj = new img_obj()
            image_obj.url =_this.getObjectURL(_this.via_img_fileref[result[i]])
            image_obj.id = result[i]
            _this.image_list.push(image_obj)
          }
        })
        this.bus.$on('show-img', function (img_id) {
          _this.$nextTick(() => {
            _this.img_list_remove_all_active_class()
            _this.img_add_visible_class(img_id)
          })

        })
      },
      methods:{
        img_list_remove_all_active_class: function () {
            let imgs = document.getElementById('img-box').childNodes
            let j
            for (j = 0; j < imgs.length; j++) {
              console.log(imgs[j])
              imgs[j].classList.remove('visible')
            }
        },
        img_add_visible_class: function (img_id) {
          console.log(img_id)
          // image显示
          document.getElementById(img_id).classList.add('visible')
        },
        getObjectURL: function (file) {
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
      }
    }
    function img_obj(url, id) {
      this.url = url
      this.id = id
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
  #img-box >>> img{
    visibility: hidden;
    position: absolute;
    top: 0px;
    left: 0px;
  }
  #img-box >>> .img-item.visible{
    visibility: visible;
  }
</style>
