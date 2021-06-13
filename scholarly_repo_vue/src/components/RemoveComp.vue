<template>
<div class='d-flex flex-row' style='justify-content: space-around;'>
    <div class='addpage-body d-flex flex-column' style='min-width: 45%; max-width: 45%;'>
      <div class='d-flex flex-row is-fullwidth' style='height: 50px; margin: 20px 0 20px 0;'>
        <h1 style='background-color: hsl(0, 0%, 21%); color: white; max-width: 100px; min-width: 100px; padding: 15px 10px 10px 10px; text-align: center;'>Remove</h1>
        <h2 style='background-color: #eeeeee; width: 100%; padding: 15px 10px 10px 10px; text-align: center;'>Author</h2>
      </div>

      <section class='black-section hero is-medium mb-6 black-section' id='left-section'>
        <form v-on:submit.prevent='removeAuthor'>
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

          <div class="notification is-danger mt-4" v-if="authorErrors.length">
            <p v-for="authorError in authorErrors" :key="authorError">{{ authorError }}</p>
          </div>

          <div class='field'>
            <div class='control'>
              <button class='button remove-button' id='remove-author-button'><span class='btn btn-danger' style='min-width: 100%; position: absolute; border-radius: 0;'>Remove Author</span></button>
            </div>
          </div>
        </form>

      </section>
    </div>

    <div class='addpage-body d-flex flex-column' style='min-width: 45%; max-width: 45%;'>
      <div class='d-flex flex-row is-fullwidth' style='height: 50px; margin: 20px 0 20px 0;'>
        <h2 style='background-color: #eeeeee; width: 100%; padding: 15px 10px 10px 10px; text-align: center;'>Book</h2>
        <h1 style='background-color: hsl(0, 0%, 21%); color: white; max-width: 100px; min-width: 100px; padding: 15px 10px 10px 10px; text-align: center;'>Remove</h1>
      </div>

      <section class='black-section hero is-medium mb-6 black-section' id='right-section'>
        <form v-on:submit.prevent='removeBook'>

          <div class='field d-flex flex-row'>
            <label class='label'>Book Title</label>
            <div class='control'>
              <input class='input' type='text' v-model='book_title' required>
            </div>
          </div>

          <div class="notification is-danger mt-4" v-if="bookErrors.length">
            <p v-for="bookError in bookErrors" v-bind:key="bookError">{{ bookError }}</p>
          </div>

          <div class='field'>
            <div class='control'>
              <button class='button remove-button' id='remove-book-button'><span class='btn btn-danger' style='min-width: 100%; position: absolute; border-radius: 0;'>Remove Book</span></button>
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
  name: 'RemoveComp',
  data () {
    return {
      authors: [],
      books: [],
      first_name: '',
      last_name: '',
      country_of_origin: '',
      authorErrors: [],
      image: '',
      book_title: '',
      bookErrors: [],
      slug_checker: new RegExp(/^[a-z0-9]+(?:-[a-z0-9]+)*$/)
    }
  },
  mounted () {
    this.getAuthors()
    this.getBooks()
    document.title = 'Remove | The Scholarly Repo'
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
    async getBooks () {
      await axios
        .get(`/api/v1/alphabetical-books/`)
        .then(response => {
            this.books = response.data
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
    async removeAuthor () {
      this.$store.commit('setIsLoading', true)

      this.authorErrors = []

      let hasSavedAuthor = false

      for (let author in this.authors) {
        if (this.first_name === this.authors[author].first_name && this.last_name === this.authors[author].last_name && this.country_of_origin === this.authors[author].country_of_origin) {
          console.log('yes')
          hasSavedAuthor = true
        }
      }

      if (!hasSavedAuthor) {
        this.authorErrors.push('no matching authors found in database!')
      }

      if (!this.authorErrors.length) {
          await axios({
          method: 'delete',
          url: '/api/v1/alphabetical-authors/',
          data: {
            first_name: this.first_name,
            last_name: this.last_name,
            country_of_origin: this.country_of_origin
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
          message: 'The author was removed from the database',
          type: 'is-success',
          dismissible: true,
          pauseOnHover: true,
          duration: 2000,
          position: 'bottom-right',
        })
        this.first_name = ''
        this.last_name = ''
        this.country_of_origin = ''
        this.$store.commit('setIsLoading', false)
      }

      this.$store.commit('setIsLoading', false)
    },
    async removeBook () {
      this.$store.commit('setIsLoading', true)

      this.bookErrors = []

      let hasSavedBook = false

      for (let book in this.books) {
        if (this.book_title === this.books[book].book_title) {
          hasSavedBook = true
        }
      }

      if (!hasSavedBook) {
        this.bookErrors.push('no matching book in database!')
      }

      if (!this.slug_checker.test(this.book_slug)) {
        this.bookErrors.push('the slug is invalid!')
      }

      if (!this.bookErrors.length) {
        await axios({
          method: 'delete',
          url: '/api/v1/alphabetical-books/',
          data: {
            book_title: this.book_title
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
                message: 'The book was removed from the database',
                type: 'is-success',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'bottom-right',
          })
        this.book_title = ''
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
.remove-button {
    text-align: center;
    width: 100%;
    margin-top: 20px;
    border-radius: 0;
}
</style>