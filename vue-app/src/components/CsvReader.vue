<template>
    <div>
        <input type="file" @change="handleFileUpload" />
        <button @click="uploadFile">Upload</button>
    </div>
  </div>

<div class="field">
    <label class="label">Upload File</label>
      <div class="file is-normal is-boxed">
    <label class="file-label">
      <input class="file-input" type="file" name="resume" />
      <span class="file-cta">
        <span class="file-icon">
          <i class="fas fa-upload"></i>
        </span>
        <span class="file-label"> Normal file… </span>
      </span>
      <span>
        <span class="file-name">No file uploaded</span>
      </span>
    </label>
</div>
</div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            selectedFile: null,
        };
    },
    methods: {
        handleFileUpload(event) {
            this.selectedFile = event.target.files[0];
        },
        async uploadFile() {
            if (!this.selectedFile) {
                alert("Please select a file first!");
                return;
            }

            const formData = new FormData();
            formData.append("file", this.selectedFile);

            try {
                const response = await axios.post("http://localhost:8000/uploadfile/", formData);
                console.log(response.data);
            } catch (error) {
                console.error("Error uploading file:", error);
            }
        },
    },
};
</script>
