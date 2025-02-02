<template>
<div class="field">
  <label class="label">File Name</label>
  <div class="control">
    <input v-model="inputTitle" class="input" type="text" placeholder="Enter File Name">
  </div>
</div>

<div class="field">
  <label class="label">Description/Context</label>
  <div class="control">
    <textarea v-model="inputDescription" class="textarea" placeholder="Enter Description/Context" rows="10"></textarea>
    </div>
  </div>

<div class="field">
    <label class="label">Upload File</label>
    <div class="file is-boxed">
    <label class="file-label">
        <input class="file-input" type="file" name="resume" />
        <span class="file-cta">
        <span class="file-icon">
        <i class="fas fa-upload"></i>
        </span>
      <span class="file-label"> Choose a file… </span>
        </span>
    </label>
    </div>
</div>
</template>

<script>
export default {
  data() {
    return {
      inputTitle: '',
      inputDescription: '',
      inputFileName: ''
    };
  }
};
</script>

<style scoped>

.field {
    margin-bottom: 1.5rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

.label {
    font-weight: bold;
    margin-bottom: 0.5rem;
    text-align: center;
    color: black;
}

.input {
    width: 100%;
    padding: 0.5rem;
    border: 1px solid #ccc;
    border-radius: 4px;
    text-align: center;
}

.textarea {
  min-height: 200px;
  min-width: 1000px;
  max-width: 100%;
  max-width: 100%;
  resize: none;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  text-align: center;
}

.file {
    width: 50%;
    padding: 0.5rem;
    border: 1px solid #ccc;
    border-radius: 4px;
    text-align: center;
}
</style>