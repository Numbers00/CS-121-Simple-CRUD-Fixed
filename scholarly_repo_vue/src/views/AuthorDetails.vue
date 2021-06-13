<template>
  <div class='d-flex'>
    <AuthorCard :author='author' />
    <table class='table is-fullwidth table-striped' style='margin: 10px 0 0 30px;'>
        <thead>
            <tr style='background-color: hsl(0, 0%, 21%);'>
                <th style='color: white;'>Title</th>
                <th style='color: white;'>Category</th>
                <th style='color: white;'>Price</th>
                <th style='color: white;'>Number of Pages</th>
                <th style='color: white;'>Language</th>
            </tr>
        </thead>
        
        <tbody>
            <tr
                v-for='book in books'
                :key='book.id'
            >
                <td id='title-overflow'>{{book.book_title}}</td>
                <td>{{book.category}}</td>
                <td>${{book.price}}</td>
                <td>{{book.number_of_pages}}</td>
                <td>{{book.language}}</td>
            </tr>
        </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios'

import AuthorCard from '@/components/AuthorCard.vue'

export default {
    name: 'AuthorDetails',
    data() {
        return {
            author: {},
            books: []
        }
    },
    components: {
      AuthorCard
    },
    mounted() {
        this.getAuthor() 
    },
    watch: {
        $route(to, from) {
            to.name === 'AuthorDetails' ? this.getAuthor() : ''
        }
    },
    methods: {
        async getAuthor() {
            this.$store.commit('setIsLoading', true)
            this.author = {}

            let author_slug = this.$route.params.author_slug
            let first_name = author_slug.split('-')[0].charAt(0).toUpperCase() + author_slug.split('-')[0].slice(1)
            let last_name = author_slug.split('-')[1].charAt(0).toUpperCase() + author_slug.split('-')[1].slice(1)

            await axios
                .get(`/api/v1/alphabetical-authors/`)
                .then(response => {
                    for (let author in response.data) {
                      if (response.data[author].first_name === first_name && response.data[author].last_name === last_name) {
                        this.author = response.data[author]
                      }
                    }
                    document.title = this.author.first_name.charAt(0).toUpperCase() + this.author.first_name.slice(1) + ' ' + this.author.last_name.charAt(0).toUpperCase() + this.author.last_name.slice(1) + ' | The Scholarly Repo'
                })
                .catch(error => {
                    console.log(error)
                })

            this.books = this.author.books

            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>

<style>
#title-overflow {
    max-width: 50%;
    min-width: 50%;
    width: 50%;
}
</style>