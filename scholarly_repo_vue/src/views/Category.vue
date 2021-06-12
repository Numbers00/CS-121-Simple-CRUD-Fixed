<template>
<div>
    <TopSection viewType='Category' />
    <router-link to='/addpage' class='button' id='add-button'><span class='btn btn-success' style='min-width: 100%; position: absolute; border-radius: 0;'>Add a New Author/Book</span></router-link>
    <table class='table is-fullwidth table-striped' style='margin-top: 30px;'>
        <thead>
            <tr style='background-color: hsl(0, 0%, 21%);'>
                <th style='color: white;'>Title</th>
                <th style='color: white;'>Author</th>
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
                <td>{{getAuthor(book.get_absolute_url)}}</td>
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
import { toast } from 'bulma-toast'

import TopSection from '@/components/TopSection'

export default {
    name: 'Category',
    props: {
        bookView: String
    },
    components: {
        TopSection
    },
    data () {
        return {
            categoryName: '',
            books: []
        }
    },
    mounted () {
        this.getCategory()
    },
    watch: {
        $route(to, from) {
            to.name === 'Category' ? this.getCategory() : ''
        }
    },
    methods: {
        async getCategory() {
            this.categoryName = ''
            console.log(this.$route.params.category_slug)
            let categorySplit = this.$route.params.category_slug.split('-')
            for (let split of categorySplit) {
                this.categoryName += split.charAt(0).toUpperCase() + split.slice(1) + ' '
            }

            this.$store.commit('setIsLoading', true)

            await axios
                .get(`/api/v1/alphabetical-books/`)
                .then(response => {
                    this.books = response.data.filter(book => {
                        if (this.categoryName.trim() === book.category.trim()) return book
                        else return null
                    })
                    document.title = this.categoryName + ' | The Scholarly Repo'
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
        },
        getAuthor (url) {
            let authorUrlSplit = url.split('/')[1].split('-')
            let author = ''
            for (let split of authorUrlSplit) {
                author += split.charAt(0).toUpperCase() + split.slice(1) + ' '
            }
            return(author.trim())
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
#add-button {
    text-align: center;
    width: 100%;
    margin-top: 20px;
    border-radius: 0;
}
</style>