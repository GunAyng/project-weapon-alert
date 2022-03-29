<template>
  <div class="col-md-6 form-control">
    <h3>กล้อง</h3>
    <hr />
    <h4>เพิ่มกล้อง</h4>
    <div>
      <label>URL:  </label>
      <input type="text" v-model="form.first_name" /><br><br>

      <label>INFO: </label>
      <input type="text" v-model="form.last_name" /><br><br>

      <label>NAME: </label>
      <input type="text" v-model="form.email" /><br><br>

      <button v-on:click="submit(form)">Submit</button>
    </div>
    <hr />
    <h4>ลบกล้อง</h4>
    <table class="table table-striped">
      <thead>
        <tr>
          <th scope="col">Cam</th>
          <th scope="col">Location</th>
          <th scope="col">Delete</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in products" :key="index">
          <td>{{ item.name }}</td>

          <td>{{ item.info }}</td>
          <td>
            <button v-on:click="deleteCam(item)">ลบ</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      products: [],
      form: {
        first_name: "",
        last_name: "",
        email: "",
      },
    };
  },
  mounted() {
    axios
      .get("http://127.0.0.1:8000/getdb")
      .then(
        (response) => (
          (this.products = response.data), console.log(this.products)
        )
      );
  },
  methods: {
    deleteCam: function (item) {
      const formData = new FormData();
      formData.append("cam_id", item.cam_id);
      axios
        .post("http://127.0.0.1:8000/deleteDB", formData)

        .then((response) => {
          console.log(response);
        });
      this.reloadPage();
    },
    reloadPage() {
      window.location.reload();
    },
    submit: function (form) {
      const formData = new FormData();
      formData.append("url", form.first_name);
      formData.append("info", form.last_name);
      formData.append("name", form.email);
      axios.post("http://127.0.0.1:8000/addDB", formData).then((response) => {
        console.log(response);
      });
      this.reloadPage();
    },
  },
};
</script>
