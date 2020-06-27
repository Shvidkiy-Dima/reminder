<template>
    <div id="app">
        <router-view></router-view>

        <div class="container">
          <div class="row">
            <div class="col-sm-10">
              <h1>My Events</h1>
              <hr><br><br>

              <button type="button" class="btn btn-success btn-sm" v-b-modal.event-modal>Add Event</button>
              <br><br>






<form class="form-inline">
  <div class="form-group mb-2">
    <input class="form-control form-control-sm ml-3 w-75" type="text" placeholder="Search"
      aria-label="Search">
  </div>
  <div class="form-group mx-sm-3 mb-2">
    <select class="form-control form-control-sm">
      <option>Large select</option>
    </select>
  </div>
  <button type="submit" class="btn btn-primary mb-2">Confirm identity</button>
</form>


              <table class="table table-hover">
                <thead>
                  <tr>
                    <th scope="col">Title</th>
                    <th scope="col">Description</th>
                    <th scope="col">Is Gone?</th>
                    <th></th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(event, index) in events" :key="index" v-b-modal.event-update-modal @click="editEvent(event)">
                    <td>{{ event.title }}</td>
                    <td>{{ event.body }}</td>
                    <td>
                      <span v-if="event.is_gone">Yes</span>
                      <span v-else>No</span>
                    </td>
                    <td>
                      <div class="btn-group" role="group">
                        <button
                                type="button"
                                class="btn btn-warning btn-sm"
                                v-b-modal.event-update-modal
                                @click="editEvent(event)">
                            Update
                        </button>
                        <button
                                type="button"
                                class="btn btn-danger btn-sm"
                                @click="onDeleteEvent(event)">
                            Delete
                        </button>
                      </div>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
          <b-modal ref="addEventModal"
            id="event-modal"
            title="Add a new event"
            hide-footer>
      <b-form  class="w-100">
      <b-form-group id="form-title-group"
                    label="Title:"
                    label-for="form-title-input">
          <b-form-input id="form-title-input"
                        type="text"
                        v-model="AddForm.title"
                        required
                        placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-description-group"
                      label="Description:"
                      label-for="form-description-input">
            <b-form-input id="form-description-input"
                          type="text"
                          v-model="AddForm.body"
                          required
                          placeholder="Enter description">
            </b-form-input>
          </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>

  <b-modal ref="editEventModal"
          id="event-update-modal"
          title="Update"
          hide-footer>
    <b-form  class="w-100">
    <b-form-group id="form-title-edit-group"
                  label="Title:"
                  label-for="form-title-edit-input">
        <b-form-input id="form-title-edit-input"
                      type="text"
                      v-model="editForm.title"
                      required
                      placeholder="Enter title">
        </b-form-input>
      </b-form-group>
      <b-form-group id="form-author-edit-group"
                    label="Description:"
                    required
                    label-for="form-author-edit-input">
          <b-form-textarea id="form-author-edit-input"
                        v-model="editForm.body"
                        required
                        placeholder="Enter Description">
          </b-form-textarea>
        </b-form-group>
        <b-form-group id="form-date-edit-group"
                      label="Date:"
                      required
                      label-for="form-date-edit-input">
        <div class="col-10">
          <b-form-input v-model="editForm.date" class="form-control" type="date"  id="form-date-edit-input">
          </b-form-input>
        </div>
        </b-form-group>
        <b-form-group id="form-time-edit-group"
                      label="Time:"
                      required
                      label-for="form-time-edit-input">
        <div class="col-10">
          <b-form-input v-model="editForm.time" class="form-control" type="time" id="form-time-edit-input">
          </b-form-input>
        </div>
        </b-form-group>
      <b-button-group>
        <b-button @click="onUpdateEvent()" variant="primary">Update</b-button>
        <b-button @click="onResetUpdateEvent()" variant="danger">Cancel</b-button>
      </b-button-group>
    </b-form>
  </b-modal>
    </div>
  </div>
</template>



<script>
import Request from '../utils/request'

    export default {
        name: 'Events',
        data() {
            return {
                events: [],
                AddForm: {
                  id: '',
                  title: '',
                  body: '',
                },
                editForm: {
                  id: '',
                  title: '',
                  body: '',
                  date: '',
                  time: ''
                },
            }
        },
        watch: {
              '$route'() {
                  this.getEvents()
              }
            },
            created(){
                this.getEvents()
            },
      methods: {
                formatDate(d){
                    return d.getFullYear() + '-' + ((d.getMonth()+1).toString().length === 1 ? '0' : '') +
                    (d.getMonth() + 1) + '-' + (d.getDate().toString().length === 1 ? '0' : '') + d.getDate()
                },
                formatTime(d){
                    return (d.getHours().toString().length === 1 ? '0' : '') + d.getHours() + ':' + (d.getMinutes().toString().length === 1 ? '0' : '') +
                    d.getMinutes() + ':' + (d.getSeconds().toString().length === 1 ? '0' : '') + d.getSeconds()
                },
                editEvent(event) {
                  let d = new Date(event.date)
                  this.editForm.date = this.formatDate(d)
                  this.editForm.time =  this.formatTime(d)
                  this.editForm.title = event.title
                  this.editForm.body = event.body
                  this.editForm.id = event.id
                },
                onUpdateEvent(){
                    let date = new Date(this.editForm.date + 'T' + this.editForm.time)
                    console.log(date)
                    Request({
                      method: 'patch',
                      url: 'http://localhost:8000/event/' + this.editForm.id + '/',
                      data: {
                          title: this.editForm.title,
                          body: this.editForm.body,
                          date: date,
                      }
                    },
                     (res)=>{
                       console.log(res)
                     })
                    this.$refs.editEventModal.hide();
                },
                onResetUpdateEvent(){
                    this.$refs.editEventModal.hide();
                },
                onDeleteEvent (event) {
                  console.log(event.id)
                },
                addEvent () {},
                onReset () {

                },
                getEvents(){
                  Request({
                    method: 'get',
                    url: 'http://localhost:8000/event'
                  },
                (res)=>{
                  this.events = res.data
                })
              }
        }
}
</script>
