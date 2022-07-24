<template>
    
    <div class="CommentTableContainer" background-color="dim">
        <DataTable :value="comments" :scrollable="true" showGridlines responsiveLayout="scroll" scrollHeight="400px">
            <template #header>
                Sentiment of Comments
            </template>
            <Column field="comment" header="Comment" style="min-width:450px; max-width: 800px;" :sortable="true">
                <template #body="slotProps">
                    <p style="text-align:justify">{{slotProps.data.comment}}</p>
                </template>            
            </Column>
            <Column field="compound" header="Sentiment" style="min-width:50px; max-width: 100px;" :sortable="true">
                <template #body="slotProps">
                    <p> {{formatSentimentText(slotProps.data.compound)}} </p>
                </template>
            </Column>     
            <Column field="compound" header="Percentage" style="min-width:100px; max-width: 200px;" :sortable="true">
                <template #body="slotProps">
                    <ProgressBar :value=formatPercentage(slotProps.data.compound) :showValue="true" style="width: 200px"></ProgressBar>
                </template>
            </Column>  
            <template #footer>
                {{this.comments ? this.comments.length : 0}} comments loaded.
            </template>
            <template #empty>
                <p>No comments found.</p>
            </template>               
        </DataTable>
    </div>

</template>

<script>
import { store } from "../../main.js";
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import Badge from 'primevue/badge';
import ProgressBar from 'primevue/progressbar';
import Row from 'primevue/row';

export default {
    name: 'CommentTable',
    components: {
        DataTable,
        Column,
        ProgressBar,
        Badge,
        Row
    },
    data() {
        return {
            comments: null,
            store
        }
    },
    created() {
        this.comments = Object.values(store.commentSentiment)
    },
    methods: {
        formatPercentage(value) {
            return parseInt(Math.abs(parseFloat(value)*100).toFixed(2))
        },
        formatSentimentText(value) {
            return parseFloat(value) == 0
                ? 'Neutral' 
                : parseFloat(value) > 0
                ? 'Positive'
                : 'Negative'
        },
    }
}
</script>

<style scoped>

.CommentTableContainer {
    margin-bottom: 10px;
}
.table-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
}
h2 {
    margin-top: -10px;
    margin-bottom: 20px;
}
p {
    text-align: center;
    justify-content: center;
}
ProgressBar {
    height: 4px;
}
</style>