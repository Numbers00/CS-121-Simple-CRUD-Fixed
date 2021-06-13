<template>
<div>
    <TopSection viewType='Authors' />
    <router-link to='/changepage' class='button' id='add-button'><span class='btn btn-success' style='min-width: 100%; position: absolute; border-radius: 0;'>Add a New Author/Book</span></router-link>
    <table class='table is-fullwidth table-striped' style='margin-top: 30px;'>
        <thead>
            <tr style='background-color: hsl(0, 0%, 21%);'>
                <th style='color: white;'>Name</th>
                <th style='color: white;'>Country of Origin</th>
                <th style='color: white;'>Number of Books (Here)</th>
            </tr>
        </thead>
        
        <tbody>
            <tr
                v-for='author in authors'
                :key='author.id'
            >
                <td id='title-overflow'>{{author.first_name + ' ' + author.last_name}}</td>
                <td>{{author.country_of_origin}}</td>
                <td>{{author.books.length}}</td>
            </tr>
        </tbody>
    </table>
</div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

import TopSection from '@/components/TopSection.vue'

export default {
    name: 'Authors',
    components: {
        TopSection
    },
    data () {
        return {
            authors: []
        }
    },
    mounted () {
        this.getAuthors()
    },
    watch: {
        $route(to, from) {
            to.name === 'Authors' ? this.getAuthors() : ''
        }
    },
    methods: {
        async getAuthors() {

            this.$store.commit('setIsLoading', true)

            await axios
                .get(`/api/v1/alphabetical-authors/`)
                .then(response => {
                    this.authors = response.data
                    document.title = 'Authors | The Scholarly Repo'
                })
                .catch(error => {
                    console.log(error)
                    toast({
                        message: 'Something went wrong. Please try again.',
                        type: 'is-danger',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-right',
                    })
                })

            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>

<style>
#add-button {
    text-align: center;
    width: 100%;
    margin-top: 20px;
    border-radius: 0;
}
</style>