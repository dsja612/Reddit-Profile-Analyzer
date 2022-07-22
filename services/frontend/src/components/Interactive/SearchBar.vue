<template>
    <div class="searchBarContainer" >
        <label id="searchBarPrefix" for="username"><h3>{{prefix}}</h3></label>
        <InputText type="text" name="username" v-model="username" placeholder="Username goes here!" size="50" />
        <Button :disabled="isDisabled" :label="searchBarButton" icon="pi pi-search" @click="search"></Button>
    </div>
</template>
<script>
import Button from 'primevue/button';
import InputText from 'primevue/inputtext';

export default {
    name: "SearchBar",
    data() {
        return {
          username: '',
          isDisabled: false,
        }
    },
    props: {
        prefix: String
    },
    components: {
        Button,
        InputText,
        Button
    },
    methods: {
        search(e) {
            e.preventDefault()
            if (!this.username) {
                this.$swal.fire({ 
                    icon: 'error',
                    title: 'Error!',
                    text: 'Please enter a username!'
                })
                return
            }
            this.timeoutButton()
            this.$parent.$emit('search', this.username)
        },

        timeoutButton() {
            this.isDisabled = !this.isDisabled

            setTimeout(() => {
                this.isDisabled = !this.isDisabled
            }, 5000)
            return
        },
    }
}
</script>

<style scoped>

.searchBarContainer {
    display: flex;
    justify-content: center;
    vertical-align: baseline;
    gap: 2px;
}

.searchBarContainer > * {
    display: flex;
    border-radius: 5px;
    align-items: center;
    justify-content: center;
}

#searchBarPrefix {
    background-color: #FCA311;
    width: 50px;
    height: 40px;
}

#searchBarButton {
    width: 60px;
    height: 40px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
}

input {
    text-indent: 6px;
}

    
</style>