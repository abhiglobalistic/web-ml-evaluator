<template>
    <div class="login">
    <v-row align="center">
    <v-form
      ref="form"
      class="login-form"
      v-model="valid"
      :lazy-validation="lazy"
    >
      <v-text-field
        v-model="name"
        :counter="10"
        :rules="nameRules"
        label="Name"
      ></v-text-field>

      <v-text-field
        v-model="email"
        :rules="emailRules"
        label="E-mail"
        required
      ></v-text-field>

      <v-checkbox
        v-model="checkbox"
        :rules="[v => !!v || 'You must agree to continue!']"
        label="Do you agree?"
        required
      ></v-checkbox>

      <v-btn
        :disabled="!valid"
        color="success"
        class="mr-4"
        @click="validate"
      >
        Log In
      </v-btn>

    </v-form>
  </v-row>

</div>
</template>

<style scoped>
  * {
    margin:0 auto;
  }

  .login-form {
    border: 1px solid #8080809e;
    border-radius: 4px;
    padding: 30px;
  }

</style>


<script>
  export default {
    name:'Login',
    data: () => ({
      valid: true,
      name: '',
      nameRules: [
        v => !!v || 'Name is required',
        v => (v && v.length <= 10) || 'Name must be less than 10 characters',
      ],
      email: '',
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
      ],
      checkbox: false,
      lazy: false,
    }),

    methods: {
      validate () {
        this.$refs.form.validate()
      }
    },
  }
</script>
