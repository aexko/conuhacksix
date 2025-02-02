<template>
  <div class="field">
    <label class="label">Title Of Datasheet</label>
    <div class="control">
      <input class="input" type="text" v-model="fileName" placeholder="Enter title (Must be unique) (Ex : number of trees)" />
    </div>
  </div>

  <div class="field">
    <label class="label">Upload File</label>
    <div class="file is-normal is-boxed">
      <label class="file-label">
        <input class="file-input" type="file" name="resume" @change="handleFileUpload" />
        <span class="file-cta">
          <span class="file-icon">
            <i class="fas fa-upload"></i>
          </span>
          <span class="file-label"> Choose CSV File </span>
        </span>
        <span>
          <span class="file-name">{{ selectedFile ? selectedFile.name : 'No file uploaded' }}</span>
        </span>
      </label>
    </div>
    <button class="button" @click="uploadFile">Upload</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      selectedFile: null,
    }
  },
  methods: {
    handleFileUpload(event) {
      this.selectedFile = event.target.files[0]
    },
    async uploadFile() {
      if (!this.selectedFile) {
        alert('Please select a file first!')
        return
      }

      const formData = new FormData()
      formData.append('file', this.selectedFile)

      try {
        const response = await axios.post('http://localhost:8000/uploadfile/', formData)
        console.log(response.data)
      } catch (error) {
        console.error('Error uploading file:', error)
      }
    },
  },
}
</script>

<style>
.field {
  margin-bottom: auto;
  margin-top: auto;
  width: 50%;
  margin-left: auto;
  margin-right: auto;
}

.file-name {
  text-align: center;
}
</style>
