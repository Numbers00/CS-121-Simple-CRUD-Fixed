<template>
    <div class="column is-3">
        <div class="box">
            <figure class="image mb-4">
                <img :src="author.image" id='author-img'>
            </figure>

            <h3 class="is-size-4">{{ author.first_name }} {{ author.last_name }}</h3>
            <p class="is-size-6 has-text-grey">{{ author.country_of_origin }}</p>
        </div>
    </div>
</template>

<script>
export default {
    name: 'AuthorBox',
    props: {
        author: Object
    },
    methods: {
        getAuthorURL (str) {
            console.log(str.replace(/[^0-9\a-z\-]/g, '').trim())
            return str.replace(/[^0-9\a-z\-]/g, '').trim()
        }
    }
}
</script>

<style scoped>
  .box {
    max-width: 320px;
    width: 320px;
    background-color: hsl(0, 0%, 21%);
    text-align: center;
    color: white;
  }
  .image {
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
  }
  #author-img {
      max-width: 320px;
      width: 320px;
      max-height: 320px;
      height: 320px;
  }
</style>