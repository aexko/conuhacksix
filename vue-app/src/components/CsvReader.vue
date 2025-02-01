<template>
    <div>
        <input type="file" @change="handleFileUpload" />
        <table v-if="csvData.length">
            <thead>
                <tr>
                    <th v-for="(header, index) in csvData[0]" :key="index">{{ header }}</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(row, rowIndex) in csvData.slice(1)" :key="rowIndex">
                    <td v-for="(cell, cellIndex) in row" :key="cellIndex">{{ cell }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
export default {
    data() {
        return {
            csvData: []
        };
    },
    methods: {
        handleFileUpload(event) {
            const file = event.target.files[0];
            if (file && file.type === 'text/csv') {
                const reader = new FileReader();
                reader.onload = (e) => {
                    const text = e.target.result;
                    this.csvData = this.parseCSV(text);
                };
                reader.readAsText(file);
            } else {
                alert('Please upload a valid CSV file.');
            }
        },
        parseCSV(text) {
            const rows = text.split('\n');
            return rows.map(row => row.split(','));
        }
    }
};
</script>

<style scoped>
table {
    width: 100%;
    border-collapse: collapse;
}

th,
td {
    border: 1px solid #ddd;
    padding: 8px;
}

th {
    background-color: #f2f2f2;
}
</style>