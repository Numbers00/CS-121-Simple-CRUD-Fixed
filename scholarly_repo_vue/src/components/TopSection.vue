<template>
<section class='hero is-medium is-dark mb-6' id='top-section'>
    <div class='hero-body has-text-centered'>
      <p class='title mb-5' id='title'>
        Welcome to The Scholarly Repo
      </p>
      <p class='subtitle' v-for='content in subtitleContent' :key='content'>
        {{ viewType === content.type ? content.text : '' }}
      </p>
    </div>
</section>
</template>

<script>
export default {
    name: 'TopSection',
    props: {
        viewType: String
    },
    data () {
        return {
            subtitleContent: [
                {type: 'Author', text: 'Authors View'},
                {type: 'Category', text: 'Category View'},
                {type: 'Add', text: 'Add an Author/Book'},
                {type: 'Remove', text: 'Remove an Author/Book'},
                {type: 'Update', text: 'Update an Author/Book'}
            ]
        }
    }
}
</script>

<style>
#top-section {
  position: relative;
  top: 40px;
  height: 300px;
}
#title {
  position: relative;
  bottom: 50px;
}
</style>