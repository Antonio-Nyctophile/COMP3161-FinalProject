<template>
  <div>
    <div class="page-header">
      <h1> Register Students</h1>
    </div>

    <form id="RegisterForm" @submit.prevent="Register">
      <div v-if="success" class="alert alert-success">
        Student successfully added
      </div>
      <div v-if="errors.length" class="alert alert-danger">
        <ul>
          <li v-for="error in errors">{{ error }}</li>
        </ul>
      </div>
      <div class="form-group mb-3">
        <label for="firstname" class="form-label">First Name</label>
        <input type="text" name="firstname" class="form-control" />
      </div>
      <div class="form-group mb-3">
        <label for="lastname" class="form-label">Last Name</label>
        <textarea name="lastname" class="form-control"></textarea>
      </div>
      <div class="form-group mb-3">
        <label for="studentID" class="form-label">Username</label>
        <textarea name="studentID" class="form-control"></textarea>
      </div>
      <div class="form-group mb-3">
        <label for="studentemail" class="form-label">Student Email</label>
        <textarea name="studentemail" class="form-control"></textarea>
      </div>

      <div class="form-group mb-3">
        <label for="password" class="form-label">Password</label>
        <textarea name="password" class="form-control"></textarea>
      </div>

      <button type="submit" class="btn btn-primary">Submit</button>
    </form>


  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
let success = ref(false);
let errors = ref([]);
let csrf_token = ref("");
let errorDisplayStatus = ref({});
function getCsrfToken() {
  fetch('/api/v1/csrf-token')
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      csrf_token.value = data.csrf_token;
    })
}
onMounted(() => {
  getCsrfToken();
});

function validateForm() {
  errors.value = [];
  errorDisplayStatus.value = {};
  let firstnameInput = document.getElementsByName("firstname")[0];
  let lastnameInput = document.getElementsByName("lastname")[0];
  let studentID = document.getElementsByName("studentID")[0];
  let studentemail = document.getElementsByName("studentemail")[0];
  let password = document.getElementsByName("password")[0];

  if (!firstnameInput.value) {
    errors.value.push("First name is required");
  }
  if (!lastnameInput.value) {
    errors.value.push("Last name is required");
  }
  if (!studentID.value) {
    errors.value.push("Username is required");
  }
  if (!studentemail.value) {
    errors.value.push("Email is required");
  }
  if (!password.value) {
    errors.value.push("Password is required");
  }
  // Set errorDisplayStatus to false for each error that has not been displayed yet
  errors.value.forEach(error => {
    if (!errorDisplayStatus.value[error]) {
      errorDisplayStatus.value[error] = false;
    }
  });
  return errors.value.length === 0;
}
function Register() {
  let RegisterForm = document.getElementById('RegisterForm');
  let form_data = new FormData(RegisterForm);
  if (validateForm()) {
    fetch("/api/v1/register", {
      method: 'POST',
      body: form_data,
      headers: {
        'X-CSRFToken': csrf_token.value
      }
    })
      .then(function (response) {
        if (response.ok) {
          success.value = true;
        } else {
          throw new Error('Failed to register student');
        }
      })
      .catch(function (error) {
        console.log('Unable To Register Student');
        errors.value.push("Accepted file format: jpg, jpeg, jfif, png, gif");
      });
  }
}
</script>

<style>
@import url("https://fonts.googleapis.com/css?family=Lato:400,700");

.page-header1 {
  text-align: center;
  padding-right: 56%;
  margin-bottom: 20px;
}

* {
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;

}

form {
  margin: 55px;
}

label {
  display: block;
  font-size: 20px;
  font-weight: 600;
  margin-bottom: 10px;
}

input,
textarea {
  max-width: 700px;
  width: 100%;
}</style>