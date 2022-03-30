<template>
  <div class="input-container">
      <div class="send-options">
          <el-button type="text" @click="changeOpt(0)"><span class="option-label">Q & A</span></el-button>
          <el-button type="text" @click="changeOpt(1)"><span class="option-label">Fake detector</span></el-button>
          <el-button type="text" @click="changeOpt(2)"><span class="option-label">Cough</span></el-button>
      </div>
      <div class="send-box">
            <el-button v-if="option===2" class="record-btn" @click="recordClickHandler">
                <span v-if="recording">Stop</span>
                <span v-else>Record</span>
            </el-button>
            <el-input v-else v-model="input" placeholder="Please input" />

            <el-button @click="sendMessage">send</el-button>
      </div>
  </div>
</template>

<script>
import { postMsg, uploadAudio } from '../api/api'
import useRecorder from '@/composables/useRecorder'

export default {
  name: 'UserInput',
  props: {},
  setup () {
    const { recording, duration, audioBlob, recordClickHandler } = useRecorder()

    return {
      recording,
      duration,
      audioBlob,
      recordClickHandler
    }
  },
  data() {
    return {
        input: '',
        option: 0
    };
  },
  components: {

  },
  methods: {
      sendMessage () {
          const content = this.input
          const option = this.option
          const audio = this.audioBlob
          
          if (content) {
            console.log('content', content)
            this.$emit('submit', {content, user: 1})
            this.input = ''

            postMsg({ content, option }).then(data => {
                this.$emit('submit', {content: data.message, user: 0})
            })
          } else if (audio) {
            this.$emit('submit', {audio, user: 1, content: ''})
            uploadAudio({ audio }).then(data => {
                console.log('uploadAudio success', data)
                this.audioBlob = null
                this.$emit('submit', {content: data.message, user: 0})
            })
          } else {
              console.log('No any input content or audio data')
          }
          
      },
      changeOpt (option) {
          this.option = option
          let welcomemesg = ''
          if (option === 0) {
               welcomemesg = 'Now you can ask me some questions!'
               this.$emit('submit', {content: welcomemesg, user: 0})
          } else if (option === 1) {
              welcomemesg = 'Please paste the news and I will tell you weather it is real.'
              this.$emit('submit', {content: welcomemesg, user: 0})
          } else {
              welcomemesg = 'Now try to long click the record button and have a covid test!'
              this.$emit('submit', {content: welcomemesg, user: 0})
              // TODO the audio initialization

          }

          
          
      }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.input-container {
    position: relative;
    background: #abdbda;
    padding: 20px;
}
.option-label {
    background: white;
    text-align: left;
    font-size: 12px;
    padding: 5px;
    border-radius: 3px;
}
.send-box {
    display: flex;
}
.send-options {
    text-align: left;
}
.record-btn {
    flex: 1;
}
</style>
