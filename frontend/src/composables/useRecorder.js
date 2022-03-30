import { ref } from 'vue'
import Recorder from 'js-audio-recorder';

export default function useRecorder() {
  const recorder = new Recorder({
    sampleBits: 16,                 // 采样位数，支持 8 或 16，默认是16
    sampleRate: 16000,              // 采样率，支持 11025、16000、22050、24000、44100、48000，根据浏览器默认值，我的chrome是48000
    numChannels: 1,                 // 声道，支持 1 或 2， 默认是1
  })

  window.recorder = recorder
  
  const recording = ref(false)
  const duration = ref(0)
  const audioBlob = ref()
  
  const recordClickHandler = () => {
    const old = recording.value
    print('!!! recordClickHandler', old)
    if (!old) { // if not recording, click to start record
      recorder.onprocess = time => duration.value = time.toFixed(2)

      recorder.start().then(() => {
        // scuessfully start to record
        console.log('===>[Recorder start successfully]')
      }, (error) => {
        // start error
        console.log(`===>[Recorder start error] ${error.name} : ${error.message}`);
      });
    } else {
      // if is recording, click to get data.
      recorder.stop();
      audioBlob.value = recorder.getWAVBlob()
    }
    recording.value = !old
  }

//   onMounted(getUserRepositories)
//   watch(user, getUserRepositories)

  return {
    recording,
    duration,
    audioBlob,
    recordClickHandler
  }
}