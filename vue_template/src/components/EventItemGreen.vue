<template>
  <div v-if="indexX > 0" :id="getId" class="card" @click="setUserdata">
    {{ data }}
  </div>
  <div v-else :id="getId" class="card">{{ data }}</div>
</template>

<script>
import { mapState } from "vuex";
import axios from "axios";

export default {
  props: {
    indexX: Number,
    indexY: Number,
    data: String,
  },
  computed: {
    getId() {
      var x = this.indexX;
      var y = this.indexY;
      var divID = x + "_" + y;
      return divID;
    },
    ...mapState(["userdata", "userProfile", "access"]),
  },
  methods: {
    setUserdata(event) {
      var innertext = event.target.innerHTML;
      let user = this.userProfile.first_name + " " + this.userProfile.last_name;
      let url = "http://tennisvyshneve.pythonanywhere.com/api/kortgreenupdate/";
      const headers = {
        Authorization: "JWT " + this.$store.state.access,
        "Content-Type": "application/json",
      };
      let bookingdata = {
        userid: this.userProfile.id,
        bookingid: event.target.id,
      };
      let eventID = bookingdata.bookingid.split("_");

      if (innertext == "" && this.access != "") {
        axios
          .post(url, bookingdata, { headers })
          .then((response) => {
            let status = response.status;
            let data = response.data;
            if (status == 200 && data.msg == "That is good") {
              console.log(response);
              event.target.innerHTML = user;
            } else if (status == 200 && data.msg == "User have booking") {
              alert("Ви не можете бронювати більше однієї години в день.");
            }
          })
          .catch((error) => {
            this.errorMessage = error.message;
            console.error(error);
          });
      } else if (innertext == user && this.access != "") {
        if (eventID[0] == "1") {
          let periodEvent = document
            .getElementById("0_" + eventID[1])
            .innerHTML.split(" ");
          console.log(periodEvent);
          var currentTime = new Date();
          currentTime.setHours(currentTime.getHours() + 2);
          var date2 = new Date();
          date2 = date2.setHours.apply(date2, periodEvent[0].split(":"));
          if (currentTime > date2) {
            alert(
              "Ви не можете відмінити бронювання. Зв'яжіться з адміністратором"
            );
            return;
          }
        }
        console.log(bookingdata);
        axios
          .put(url, bookingdata, { headers })
          .then((response) => {
            let status = response.status;
            let data = response.data;
            console.log(response);
            if (status == 200 && data.msg == "Record was deleted") {
              event.target.innerHTML = "";
            }
          })
          .catch((error) => {
            this.errorMessage = error.message;
            console.error(error);
          });
      } else {
        alert("Цей час заброньованний. Або нема зв'язку з системою.");
      }
    },
  },
};
</script>

<style scoped>
.card {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  margin: auto;
  text-align: center;
  width: 150px;
  height: 35px;
  vertical-align: middle;
}
</style>
