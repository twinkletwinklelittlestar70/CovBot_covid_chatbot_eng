<template>
  <div :class="['row-container', { 'style-right': isRight }]"> 
      <div class="flex-left">
          <div class="avator"></div>
          <div class="username">{{ username }}</div>
      </div>
      <div class="flex-right">
        <div class="content-bg">
            <div class="content">{{ content }}</div>
        </div>
      </div>
  </div>
</template>

<script>

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
</style>
