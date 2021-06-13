<template>
  <div class='d-flex flex-column'>
    <div class='is-fullwidth d-flex flex-row' style='height: 50px; margin: 20px 0 20px 0;'>
      <h1 style='background-color: hsl(0, 0%, 21%); color: white; max-width: 200px; min-width: 200px; padding: 15px 10px 10px 10px; text-align: center;'>Search Term</h1>
      <h2 style='background-color: #eeeeee; width: 100%; padding: 15px 10px 10px 10px;'>{{query}}</h2>
    </div>

    <div class='d-flex flex-row'>
      <div class='d-flex flex-col'>
        <AuthorBox 
            v-for="author in authors"
            :key="author.id"
            :author="author" />
      </div>
      <table v-if='books.length != 0' class='table is-fullwidth table-striped' style='margin: 10px 0 0 30px;'>
        <thead>
            <tr style='background-color: hsl(0, 0%, 21%);'>
                <th style='color: white;'>Title</th>
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
                <td>${{book.price}}</td>
                <td>{{book.number_of_pages}}</td>
                <td>{{book.language}}</td>
            </tr>
        </tbody>
      </table>
      <h2 v-else-if='authors.length == 0 && books.length == 0'>There are no matches with saved authors and books, please try another</h2>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import AuthorBox from '@/components/AuthorBox.vue'

export default {
    name: 'Search',
    components: {
        AuthorBox
    },
    data() {
        return {
            authors: [],
            books: [],
            query: ''
        }
    },
    mounted() {
        document.title = 'Search | The Scholarly Repo'
        let uri = window.location.search.substring(1)
        let params = new URLSearchParams(uri)
        if (params.get('query')) {
            this.query = params.get('query')
            this.performSearch()
        }
    },
    methods: {
        async performSearch() {
            this.$store.commit('setIsLoading', true)

            await axios
                .post('/api/v1/authors/search/', {'query': this.query})
                .then(response => {
                    this.authors = response.data
                })
                .catch(error => {
                    console.log(error)
                })
            
            await axios
                .post('/api/v1/books/search/', {'query': this.query})
                .then(response => {
                    this.books = response.data
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>