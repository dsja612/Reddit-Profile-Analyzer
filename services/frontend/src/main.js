import { createApp } from 'vue'
import App from './App.vue'

import VueSweetalert2 from 'vue-sweetalert2';
import 'sweetalert2/dist/sweetalert2.min.css';

import  { reactive } from 'vue'

import PrimeVue from 'primevue/config';
import Badge from 'primevue/badge';
import ProgressBar from 'primevue/progressbar';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import ColumnGroup from 'primevue/columngroup';             //optional for column grouping
import Row from 'primevue/row';                             //optional for row
import 'primevue/resources/themes/vela-orange/theme.css';   //theme
import 'primevue/resources/primevue.css';                   //core css
import 'primeicons/primeicons.css';                         //icons

export const store = reactive({

    showOverview: false,
    showLoading: false,
    
    username: String,
    userDateJoined: Date,
    numComments: Number,
    numSubmissions: Number,
    commentKarma: Number,
    submissionKarma: Number,
    topSubreddits: Object,
    topWords: Object,
    numSubsToShow: Number,
    numWordsToShow: Number,
    commentPolarity: Object,
    commentSentiment: Object,
    commentFreqHrs: Object,
    commentFreqDays: Object
})

const app = createApp(App)

app.use(VueSweetalert2);
app.use(PrimeVue);

app.component(DataTable, 'DataTable')
app.component(Column, 'Column')
app.component(ColumnGroup, 'ColumnGroup')
app.component(Row, 'Row')
app.component(Badge, 'Badge')
app.component(ProgressBar, 'ProgressBar')

app.mount('#app');