<template>
<div>
  <TopSection viewType='Add' v-if='addToggle' />
  <TopSection viewType='Remove' v-if='removeToggle' />
  <TopSection viewType='Update' v-if='updateToggle' />
  <div class='d-flex flex-row is-fullwidth'>
    <button @click='addToggle = !addToggle; removeToggle = false; updateToggle = false' class='button crud-toggle flex-grow-1 position-relative'><span class='btn btn-success' style='min-width: 100%; position: absolute; border-radius: 0;'>Add</span></button>
    <button @click='removeToggle = !removeToggle; addToggle = false; updateToggle = false' class='button crud-toggle flex-grow-1 position-relative'><span class='btn btn-danger' style='min-width: 100%; position: absolute; border-radius: 0;'>Remove</span></button>
    <button @click='updateToggle = !updateToggle; addToggle = false; removeToggle = false' class='button crud-toggle flex-grow-1 position-relative'><span class='btn btn-info' style='min-width: 100%; position: absolute; border-radius: 0;'>Update</span></button>
  </div>
  <AddComp v-if='addToggle' />
  <RemoveComp v-if='removeToggle' />
  <UpdateComp v-if='updateToggle' />
</div>
</template>

<script>
import axios from 'axios'
import {toast} from 'bulma-toast'

import TopSection from '@/components/TopSection.vue'
import AddComp from '@/components/AddComp.vue'
import RemoveComp from '@/components/RemoveComp.vue'
import UpdateComp from '@/components/UpdateComp.vue'

export default {
  name: 'ChangePage',
  components: {
    TopSection,
    AddComp,
    RemoveComp,
    UpdateComp
  },
  data () {
    return {
      addToggle: true,
      removeToggle: false,
      updateToggle: false
    }
  },
  mounted () {
    document.title = 'Changepage || The Scholarly Repo'
  }
}
</script>

<style scoped>
.crud-toggle {
    text-align: center;
    width: 100%;
    margin-top: 20px;
    border-radius: 0;
}
</style>