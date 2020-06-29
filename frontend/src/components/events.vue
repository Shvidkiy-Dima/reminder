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
    <input v-model="eventFilter.title" class="form-control form-control-sm ml-3 w-75" type="text" placeholder="Event title"
      aria-label="Search">
  </div>
  <div class="form-group mx-sm-3 mb-2">
    <select v-model="eventFilter.date" class="form-control form-control-sm">
      <option value="0"></option>
      <option value="24">Last day</option>
      <option value="148">Last week</option>
      <option value="592">Last month</option>
    </select>
  </div>
  <button @click="onEventFilter()" class="btn btn-primary mb-2">Filter Events</button>
</form>


              <table class="table table-hover">
                <thead>
                  <tr>
                    <th scope="col">Title</th>
                    <th scope="col">Description</th>
                    <th scope="col">Is Gone?</th>
                    <th scope="col">Date</th>
                    <th scope="col">{{count}}</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(event, index) in events" :key="index">

                    <td v-b-modal.event-update-modal @click="editEvent(event)">{{ event.title }}</td>
                    <td v-b-modal.event-update-modal @click="editEvent(event)">{{ event.body.slice(0, 30) }}</td>
                    <td v-b-modal.event-update-modal @click="editEvent(event)">
                      <span v-if="event.is_gone">Yes</span>
                      <span v-else>No</span>
                    </td>

                    <td v-b-modal.event-update-modal @click="editEvent(event)">{{ event.date | moment("calendar") }}</td>

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
                        v-model="addForm.title"
                        required
                        placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-description-group"
                      label="Description:"
                      label-for="form-description-input">
            <b-form-textarea id="form-description-input"
                          type="text"
                          v-model="addForm.body"
                          required
                          placeholder="Enter description">
            </b-form-textarea>
          </b-form-group>

        <b-form-group id="form-date-add-group"
                      label="Date:"
                      required
                      label-for="form-date-add-input">
        <div class="col-10">
          <b-form-input v-model="addForm.date" class="form-control" type="date"  id="form-date-add-input">
          </b-form-input>
        </div>
        </b-form-group>
        <b-form-group id="form-time-add-group"
                      label="Time:"
                      required
                      label-for="form-time-add-input">
        <div class="col-10">
          <b-form-input v-model="addForm.time" class="form-control" type="time" id="form-time-add-input">
          </b-form-input>
        </div>
        </b-form-group>


        <b-button-group>
          <b-button @click="onAddEvent()" variant="primary">Add</b-button>
          <b-button @click="onResetAddEvent()" variant="danger">Cancel</b-button>
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
                count: 0,
                events: [],
                eventFilter: {
                  title: '',
                  creation_date: ''
                },
                addForm: {
                  id: '',
                  title: '',
                  body: '',
                  date: '',
                  time: '00:00:00'
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
                    if (new Date() > date){
                      alert('Check date')
                      return
                    }
                    Request({
                      method: 'patch',
                      url: 'http://localhost:8000/event/' + this.editForm.id + '/',
                      data: {
                          title: this.editForm.title,
                          body: this.editForm.body,
                          date: date,
                      }
                    },
                     ()=>{
                       this.getEvents()
                       this.$refs.editEventModal.hide();
                     })


                },
                onResetUpdateEvent(){
                    this.$refs.editEventModal.hide();
                },
                onDeleteEvent (event) {
                  Request({
                    method: 'delete',
                    url: 'http://localhost:8000/event/' + event.id + '/'
                  },
                ()=>{
                  this.getEvents()
                })
                },
                onResetAddEvent(){
                    this.$refs.addEventModal.hide();
                },
                onAddEvent () {
                  let date = new Date(this.addForm.date + 'T' + this.addForm.time)
                  if (new Date() > date){
                    alert('Check date')
                    return
                  }

                  Request({
                    method: 'post',
                    url: 'http://localhost:8000/event/',
                    data: {
                        title: this.addForm.title,
                        body: this.addForm.body,
                        date: date,
                    }
                  },
                   ()=>{
                     this.getEvents()
                     this.$refs.addEventModal.hide();
                   })

                },
                getEvents(is_filter){
                  let data = {}
                  if (is_filter){
                    let timestamp = Date.now() - (this.eventFilter.date*60*60*1000)
                    data.creation_date = new Date(timestamp)
                    data.title = this.eventFilter.title
                  }
                  Request({
                    method: 'get',
                    url: 'http://localhost:8000/event',
                    params: data
                  },
                (res)=>{
                  this.count = res.data.length
                  this.events = res.data
                })
              },
              onEventFilter(){
                this.getEvents(true)
              }
        }
}
</script>
