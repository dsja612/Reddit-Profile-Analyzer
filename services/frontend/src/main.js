import { createApp } from 'vue'
import App from './App.vue'

import VueSweetalert2 from 'vue-sweetalert2';
import 'sweetalert2/dist/sweetalert2.min.css';

import  { reactive } from 'vue'

import 'primevue/resources/themes/bootstrap4-light-blue/theme.css';   //theme
import 'primevue/resources/primevue.min.css';                   //core css
import 'primeicons/primeicons.css';                         //icons
import PrimeVue from 'primevue/config';
import Badge from 'primevue/badge';
import Button from 'primevue/button';
import Divider from 'primevue/divider';
import InputText from 'primevue/inputtext';
import ProgressBar from 'primevue/progressbar';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import ColumnGroup from 'primevue/columngroup';             //optional for column grouping
import Row from 'primevue/row';                             //optional for row


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
app.use(PrimeVue, {
    zIndex: {
        modal: 1100,        //dialog, sidebar
        overlay: 1000,      //dropdown, overlaypanel
        menu: 1000,         //overlay menus
        tooltip: 1100       //tooltip
    },
    ripple: true
});

app.component(DataTable, 'DataTable')
app.component(Column, 'Column')
app.component(ColumnGroup, 'ColumnGroup')
app.component(Row, 'Row')
app.component(Badge, 'Badge')
app.component(ProgressBar, 'ProgressBar')
app.component(InputText, 'InputText')
app.component(Button, 'Button')
app.component(Divider, 'Divider')

app.mount('#app');