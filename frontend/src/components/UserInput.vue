<template>
  <div class="input-container">
      <div class="send-options">
          <span class="option-label">Q & A</span>
          <span class="option-label">Fake detector</span>
          <span class="option-label">Cough</span>
      </div>
      <div class="send-box">
            <el-input v-model="input" placeholder="Please input" v-on:change="sendMessage" />
            <el-button>send</el-button>
      </div>
    
  </div>
</template>

<script>

export default {
  name: 'UserInput',
  props: {

  },
  data() {
    return {
        input: ''
    };
  },
  components: {

  },
  methods: {

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
    margin: 2px;
    border-radius: 3px;
}
.send-box {
    display: flex;
}
.send-options {
    text-align: left;
}
</style>
