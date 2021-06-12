<template>
  <div>
    <TopSection viewType='Author' />
    <router-link to='/addpage' class='button' id='add-button'><span class='btn btn-success' style='min-width: 100%; position: absolute; border-radius: 0;'>Add a New Author/Book</span></router-link>

    <div class='columns is-multiline' style='margin-top: 30px;'>
      <AuthorBox
      v-for='author in authors'
      :key='author'
      :author='author'
      />
    </div>
  </div>
</template>

<script>
import axios from 'axios'

import TopSection from '@/components/TopSection.vue'
import AuthorBox from '@/components/AuthorBox.vue'

export default {
  name: 'Home',
  components: {
      TopSection,
      AuthorBox
  },
  data () {
    return {
      authors: []
    }
  },
  mounted () {
    this.getAlphabeticalAuthors()
    console.log(this.authors)

    document.title = 'Authors | The Scholarly Repo'
  },
  methods: {
    async getAlphabeticalAuthors () {
      this.$store.commit('setIsLoading', true)

      await axios
        .get('/api/v1/alphabetical-authors/')
        .then(response => {
          this.authors = response.data
        })
        .catch(error => {
          console.log(error)
        })

      this.$store.commit('setIsLoading', false)
    }
  }
};
</script>

<style>
#add-button {
    text-align: center;
    width: 100%;
    margin-top: 20px;
    border-radius: 0;
}
</style>
