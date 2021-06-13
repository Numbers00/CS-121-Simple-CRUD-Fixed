<template>
<div class='d-flex flex-row' style='justify-content: space-around;'>
    <div class='addpage-body d-flex flex-column' style='min-width: 45%; max-width: 45%;'>
      <div class='d-flex flex-row is-fullwidth' style='height: 50px; margin: 20px 0 20px 0;'>
        <h1 style='background-color: hsl(0, 0%, 21%); color: white; max-width: 100px; min-width: 100px; padding: 15px 10px 10px 10px; text-align: center;'>Add</h1>
        <h2 style='background-color: #eeeeee; width: 100%; padding: 15px 10px 10px 10px; text-align: center;'>Author</h2>
      </div>

      <section class='black-section hero is-medium mb-6 black-section' id='left-section'>
        <form v-on:submit.prevent='addAuthor'>
          <div class='field d-flex flex-row'>
            <label class='label'>First Name</label>
            <div class='control'>
              <input class='input' type='text' v-model='first_name' required>
            </div>
          </div>

          <div class='field d-flex flex-row'>
            <label class='label'>Last Name</label>
            <div class='control'>
              <input class='input' type='text' v-model='last_name'>
            </div>
          </div>

          <div class='field d-flex flex-row'>
            <label class='label'>Country of Origin</label>
            <div class='control'>
              <input class='input' type='text' v-model='country_of_origin' required>
            </div>
          </div>

          <div class='field d-flex flex-row'>
            <label class='label'>Slug</label>
            <div class='control'>
              <input class='input' type='text' v-model='author_slug' required>
            </div>
          </div>

          <div class='field d-flex flex-row'>
            <label class='label'>Image</label>
            <div class='control'>
              <input class='input' type='text' v-model='image'>
            </div>
          </div>

          <div class="notification is-danger mt-4" v-if="authorErrors.length">
            <p v-for="authorError in authorErrors" :key="authorError">{{ authorError }}</p>
          </div>

          <div class='field'>
            <div class='control'>
              <button class='button add-button' id='add-author-button'><span class='btn btn-success' style='min-width: 100%; position: absolute; border-radius: 0;'>Add Author</span></button>
            </div>
          </div>
        </form>

      </section>
    </div>

    <div class='addpage-body d-flex flex-column' style='min-width: 45%; max-width: 45%;'>
      <div class='d-flex flex-row is-fullwidth' style='height: 50px; margin: 20px 0 20px 0;'>
        <h2 style='background-color: #eeeeee; width: 100%; padding: 15px 10px 10px 10px; text-align: center;'>Book</h2>
        <h1 style='background-color: hsl(0, 0%, 21%); color: white; max-width: 100px; min-width: 100px; padding: 15px 10px 10px 10px; text-align: center;'>Add</h1>
      </div>

      <section class='black-section hero is-medium mb-6 black-section' id='right-section'>
        <form v-on:submit.prevent='addBook'>
          <div class='field d-flex flex-row'>
            <label class='label select-label'>Author's First Name</label>
            <div class='select'>
              <select v-model='author_first_name' required>
                  <option v-for='author in authors' :value='author.first_name' :key='author.id'>{{author.first_name}}</option>
              </select>
            </div>
          </div>

          <div class='field d-flex flex-row'>
            <label class='label select-label'>Category</label>
            <div class='select'>
              <select v-model='category' required>
                <option value='Anthropology'>Anthropology</option>
                <option value='Biology'>Biology</option>
                <option value="Computer Science">Computer Science</option>
                <option value="Economics">Economics</option>
                <option value="History">History</option>
                <option value="Mathematics">Mathematics</option>
                <option value="Psychology">Psychology</option>
                <option value="Political Science">Political Science</option>
              </select>
            </div>
          </div>

          <div class='field d-flex flex-row'>
            <label class='label'>Book Title</label>
            <div class='control'>
              <input class='input' type='text' v-model='book_title' required>
            </div>
          </div>

          <div class='field d-flex flex-row'>
            <label class='label'>Price (USD)</label>
            <div class='control'>
              <input class='input' type='number' v-model='price' min='0.01' step='0.01' max='999999.99' required>
            </div>
          </div>

          <div class='field d-flex flex-row'>
            <label class='label'>Number of Pages</label>
            <div class='control'>
              <input class='input' type='number' v-model='number_of_pages' min='1' step='1' required>
            </div>
          </div>

          <div class='field d-flex flex-row'>
            <label class='label'>Language</label>
            <div class='control'>
              <input class='input' type='text' v-model='language' required>
            </div>
          </div>

          <div class='field d-flex flex-row'>
            <label class='label'>Slug</label>
            <div class='control'>
              <input class='input' type='text' v-model='book_slug' required>
            </div>
          </div>

          <div class="notification is-danger mt-4" v-if="bookErrors.length">
            <p v-for="bookError in bookErrors" v-bind:key="bookError">{{ bookError }}</p>
          </div>

          <div class='field'>
            <div class='control'>
              <button class='button add-button' id='add-book-button'><span class='btn btn-success' style='min-width: 100%; position: absolute; border-radius: 0;'>Add Book</span></button>
            </div>
          </div>
        </form>
      </section>
    </div>

</div>
</template>

<script>
import axios from 'axios'
import {toast} from 'bulma-toast'

export default {
  name: 'AddComp',
  data () {
    return {
      authors: [],
      first_name: '',
      last_name: '',
      country_of_origin: '',
      image: '',
      author_slug: '',
      author: '',
      authorErrors: [],
      author_first_name: '',
      book_title: '',
      category: '',
      price: '',
      number_of_pages: '',
      language: '',
      book_slug: '',
      bookErrors: [],
      slug_checker: new RegExp(/^[a-z0-9]+(?:-[a-z0-9]+)*$/)
    }
  },
  mounted () {
    this.getAuthors()
  },
  methods: {
    async getAuthors () {
      await axios
        .get(`/api/v1/alphabetical-authors/`)
        .then(response => {
            this.authors = response.data
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
    },
    async addAuthor () {
      this.$store.commit('setIsLoading', true)

      this.authorErrors = []
      this.bookErrors = []

      if (!this.slug_checker.test(this.author_slug)) {
        this.authorErrors.push('the slug is invalid!')
      }

      if (!this.authorErrors.length) {
          await axios({
          method: 'post',
          url: '/api/v1/alphabetical-authors/',
          data: {
            first_name: this.first_name,
            last_name: this.last_name,
            country_of_origin: this.country_of_origin,
            slug: this.author_slug,
            image: this.image
          },
          auth: {
            username: 'Pupumaru',
            password: 'Admin6464'
          }
        }).catch(error => {
          console.log(error)
        })

        this.authorErrors = []
        toast({
          message: 'The author was added to the database',
          type: 'is-success',
          dismissible: true,
          pauseOnHover: true,
          duration: 2000,
          position: 'bottom-right',
        })
        this.first_name = ''
        this.last_name = ''
        this.country_of_origin = ''
        this.author_slug = ''
        this.image = ''
        this.$store.commit('setIsLoading', false)
      }

      this.$store.commit('setIsLoading', false)
    },
    async addBook () {
      this.$store.commit('setIsLoading', true)

      this.bookErrors = []
      this.authorErrors = []

      if (this.book_title === '' || this.category === '' || this.price === '' || this.number_of_pages === '' || this.language === '' || this.book_slug === '') {
        this.bookErrors.push('all fields above are required!')
      }

      if (!this.slug_checker.test(this.book_slug)) {
        this.bookErrors.push('the slug is invalid!')
      }

      if (!this.bookErrors.length) {

        await axios({
          method: 'post',
          url: '/api/v1/alphabetical-books/',
          data: {
            author_first_name: this.author_first_name,
            book_title: this.book_title,
            category: this.category,
            price: this.price,
            number_of_pages: this.number_of_pages,
            language: this.language,
            slug: this.book_slug
          },
          auth: {
            username: 'Pupumaru',
            password: 'Admin6464'
          }
        }).catch(error => {
          console.log(error)
        })

        this.bookErrors = []
          toast({
                message: 'The book was added to the database',
                type: 'is-success',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'bottom-right',
          })
        this.author_first_name = ''
        this.book_title = ''
        this.category = ''
        this.price = ''
        this.number_of_pages = ''
        this.language = ''
        this.book_slug = ''
        this.$store.commit('setIsLoading', false)
      }

      this.$store.commit('setIsLoading', false)
    }
  }
}
</script>

<style scoped>
.addpage-body {
  position: relative;
  top: 20px;
}
.black-section {
  min-height: 500px;
  max-height: 500px;
  padding: 20px;
}
#left-section {
  min-height: 0;
}
.field {
  min-width: 100%;
  margin-bottom: 20px;
}
.image-field {
  margin-bottom: 20px;
}
.label {
  background-color: hsl(0, 0%, 21%);
  min-height: 30px;
  max-height: 30px;
  min-width: 25%;
  padding: 5px 5px 5px 5px;
  color: white;
  text-align: center;
}
.select-label {
  min-height: 40px;
  max-height: 40px;
}
.input,  .select, select, option {
  border-radius: 0;
  min-width: 480px;
  background-color: #eeeeee;
}
.input {
  max-height: 30px;
}
.add-button {
    text-align: center;
    width: 100%;
    margin-top: 20px;
    border-radius: 0;
}
</style>