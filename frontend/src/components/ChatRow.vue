<template>
  <div :class="['row-container', { 'style-right': isRight }]"> 
      <div class="flex-left">
          <div class="avator"></div>
          <div class="username">{{ username }}</div>
      </div>
      <div class="flex-right">
        <div class="content-bg">
            <div class="content" v-if="content">
              {{ content }}
              <el-button type="text" @click="translation">
                <el-icon><DocumentCopy /></el-icon>
              </el-button>
            </div>
            <div class="translation" v-if="translatedText">
              {{ translatedText }}
            </div>
            <div class="audio" v-if="!content">
              <span>[audio]</span>.....
            </div>
        </div>
      </div>
  </div>
</template>

<script>
import { translate } from '../api/api'

export default {
  name: 'ChatRow',
  props: {
    isRight: {
      type: Boolean,
      default: false
    },
    username: String,
    content: String,
  },
  data() {
    return {
      translatedText: ''
    };
  },
  components: {
    
  },
  methods: {
    translation () {
      const content = this.content
      const lang = 'zh'
      
      if (!content) {
        return
      }

      if (this.translatedText) {
        this.translatedText = ''
        return
      }
      // https://cloud.google.com/translate/docs/basic/translating-text?hl=zh-cn#translate_translate_text-python
      translate({ content, lang }).then(data => {
        console.log('result of translation', data)
        this.translatedText = data.message
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.row-container {
    display: flex;
    justify-content: space-between;
}
.style-right {
    flex-direction: row-reverse;
}
.avator {
    width: 30px;
    height: 30px;
    background: bisque;
    border-radius: 50%;
    margin-top: 10px;
}
.style-right .avator, .style-right .content-bg {
    background: #abdbda;
}
.username {
    font-size: 12px;
}
.flex-left {
    width: 15%;
    display: flex;
    flex-direction: column;
    align-items: center;
}
.flex-right {
    flex: 1;
    position: relative;
}
.content-bg {
    margin: 10px 20px;
    line-height: 30px;
    background: bisque;
    padding: 5px 20px;
    left: 0;
    border-radius: 5px;
}
.content {
    text-align: left;
}
.translation {
  text-align: left;
  font-size: 12px;
  color: #666666;
}
</style>
