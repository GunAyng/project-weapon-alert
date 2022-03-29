<template>
  <div>
    <label>URL</label>
    <input type="text" v-model="form.first_name" />

    <label>INFO</label>
    <input type="text" v-model="form.last_name" />

    <label>NAME</label>
    <input type="text" v-model="form.email" />

    <button v-on:click="submit(form)">Submit</button>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      form: {
        first_name: "",
        last_name: "",
        email: "",
      },
    };
  },

  methods: {
    submit: function (form) {
      const formData = new FormData();
      formData.append("url", form.first_name);
      formData.append("info", form.last_name);
      formData.append("name", form.email);
      axios
        .post("http://127.0.0.1:8000/addDB", formData)
        .then((response) => {
          console.log(response);
        });
    },
  },
};
</script>