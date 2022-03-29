<template>
  <div class="box-container">
    <div class="chat-box">
        <div class="box-banner"></div>
        <div class="box-body">
            <ChatRow v-for="(data, index) in chatData" 
                :key="index" 
                :isRight="data.username === 'Me'" 
                :username="data.username" 
                :content="data.content"
            />
        </div>
        <div class="box-end">
            <UserInput />
        </div>
    </div>
  </div>
</template>

<script>
import ChatRow from './ChatRow.vue'
import UserInput from './UserInput.vue'

export default {
  name: 'ChatContainer',
  data() {
    return {
        chatData: [{username: "Me", content: "What is the weather today?"},
        {username: "Bot", content: "Today is windy. Today is windy.Today is windy Today is windy Today is windy."}]
    };
  },
  components: {
      ChatRow,
      UserInput
  },
  methods: {
    
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.box-container {
    position: absolute;
    width: 100%;
}
.chat-box {
    position: relative;
    display: flex;
    flex-direction: column;
    width: 50vh;
    height: 80vh;
    background: white;
    margin: 0 auto;
    border-radius: 8px;
    box-shadow: 6px 6px 5px 2px #9da0a66b;
}
.box-banner {
    width: 100%;
    background: #abdbdb;
    height: 60px;
    border-radius: 8px 8px 0 0;
}
.box-body {
    flex: 1;
}
.box-end {}
</style>
