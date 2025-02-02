<template>
  <p class="title has-text-centered">Upload CSV dataset</p>
  <div class="field">
    <label class="label">Dataset name</label>
    <input type="text" class="input" v-model="title" placeholder="Enter dataset name (Must be unique and precise) (Ex : number of trees)" />
  </div>
  
  <div class="field">
    <label class="label">Upload file</label>
    <div class="file is-normal is-boxed">
      <label class="file-label">
        <input class="file-input" type="file" @change="handleFileUpload" />
        <span class="file-cta">
          <span class="file-icon">
            <i class="fas fa-upload"></i>
          </span>
          <span class="file-label"> Choose CSV file </span>
        </span>
        <span>
          <span class="file-name">{{ selectedFile ? selectedFile.name : 'No file uploaded' }}</span>
        </span>
      </label>
    </div>
    <button class= "button" @click="uploadFile">Upload</button>

    <br><br><br>
    <p class="title has-text-centered">Current database</p>
    <p v-if="datasets.length === 0" class="has-text-centered is-size-3">Loading...</p>
    <br>
    <div class="columns is-multiline">
      <div class="box has-text-centered column"  style="width: 50%;" v-for="dataset in datasets" :key=dataset.id>
        <p>{{dataset.title}}</p> <p @click="deleteDataset(dataset.id)">🗑️</p>
      </div>
      

    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedFile: null,
      title: '',
      datasets: [],
    }
  },
  mounted() {
    console.log('Fetching datasets');
    this.fetchDatasets();
  },
  methods: {
    handleFileUpload(event) {
      this.selectedFile = event.target.files[0]
    },
    async fetchDatasets() {
      try {
        const response = await fetch('http://localhost:8000/getcorrelations')
        const data = await response.json();
        console.log(data);
        this.datasets = data;
      } catch (error) {
        console.error('There was a problem with the fetch operation:', error)
      }
    },

    async deleteDataset(id) {
      try {
        const response = await fetch('http://localhost:8000/deletefile/' + id, {
          method: 'DELETE'
        })
        if (!response.ok) {
          throw new Error('Network response was not ok')
        }
        alert('Dataset deleted successfully')
        window.location.reload();
      } catch (error) {
        console.error('There was a problem with the fetch operation:', error)
      }
    },
    async uploadFile() {
      if (!this.selectedFile) {
        alert('Please select a file first!')
        return
      }

      if (!this.title) {
        alert('Please enter a title!')
        return
      }

      const formData = new FormData()
      formData.append('file', this.selectedFile)
      formData.append('title', this.title)

      try {
        const response = await fetch('http://localhost:8000/uploadfile', {
          method: 'POST',
          body: formData
        })

        if (!response.ok) {
          throw new Error('Network response was not ok')
        }

        // const data = await response.json()
        alert('File uploaded successfully')
        window.location.reload();
      } catch (error) {
        alert('There was a problem with the fetch operation:', error)
        console.error('There was a problem with the fetch operation:', error)
      }
    }
  }
}
</script>

<style>

.field {
  margin-left: auto;
  margin-right: auto;
  width: 50%;
} 

.file-name {
  text-align: center;
}

</style>
