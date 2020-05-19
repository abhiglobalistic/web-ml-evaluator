<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <v-img
          :src="require('../assets/logo.png')"
          class="my-3"
          contain
          height="200"
        />
      </v-col>
    </v-row>
   
   <v-row class="text-center">
      <v-col cols="12">
        <h3 class="display-1 mb-3">
          Welcome to ML Web Evaluator
        </h3>
      </v-col>
    </v-row>
    
    <v-row class="text-center">
        <v-col cols="12">
          <Login/>
        </v-col>
    </v-row> 

  </v-container>
</template>

<script>
// @ is an alias to /src
import Login from '@/components/Login.vue'

  export default {
    name: 'Index',
    components: {
    Login
    },
    data: () => ({
     
    
    }),
  }
</script>
