<template>
  <div id='wrapper'>
    <section class='section'>
    <nav class="navbar is-dark" id='top-nav'>
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><strong>The Scholarly Repo</strong></router-link>

        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu }">
        <div class="navbar-start">
          <div class="navbar-item">
            <form method="get" action="/search">
              <div class="field has-addons">
                <div class="control">
                  <input type="text" class="input" placeholder="What are you looking for?" name="query">
                </div>

                <div class="control">
                  <button class="button is-success">
                      <span class="icon">
                      <i class="fas fa-search"></i>
                      </span>
                  </button>
                </div>
              </div>
            </form>
          </div>
        </div>

        <div class="navbar-end">
          <router-link to="/authors" class="navbar-item" tag='nav-li'>Authors</router-link>
          <router-link
            :to='bookView.to'
            v-for='(bookView, index) in bookViews'
            :key='index' 
            class='navbar-item'
            :class="{'gray-bg': navHover}"
            @mouseover.native="navHover = true"
            @mouseleave.native="navHover = false"
          >
            {{bookView.name}}
          </router-link>
        </div>
      </div>
    </nav>

    <div class="is-loading-bar has-text-centered" v-bind:class="{'is-loading': $store.state.isLoading }">
      <div class="lds-dual-ring"></div>
    </div>

    <router-view/>

    </section>

    <footer class="footer">
      <p class="has-text-centered">Copyright (c) 2021</p>
    </footer>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      showMobileMenu: false,
      navHover: false,
      bookViews: [
        { name: 'Anthropology', to: '/categories/anthropology' },
        { name: 'Biology', to: '/categories/biology' },
        { name: 'Computer Science', to: '/categories/computer-science' },
        { name: 'Economics', to: '/categories/economics' },
        { name: 'History', to: '/categories/history' },
        { name: 'Mathematics', to: '/categories/mathematics' },
        { name: 'Psychology', to: '/categories/psychology' },
        { name: 'Political Science', to: '/categories/political-science' },
      ]
    }
  },
  beforeCreate () {
    this.$store.commit('initializeStore')
  }
}
</script>

<style lang="scss">
@import '../node_modules/bulma';
.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}
.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}
@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
.is-loading-bar {
  height: 0;
  overflow: hidden;
  -webkit-transition: all 0.3s;
  transition: all 0.3s;
  &.is-loading {
    height: 80px;
  }
}
</style>
