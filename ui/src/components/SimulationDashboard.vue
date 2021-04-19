<template>
  <div class="mx-5">
    <b-card footer-border-variant="light" title="Simulation form" sub-title="Please fill the query params for the simulation process (all time must be in minutes), if not just use the default values!">
      <b-form class="mt-5" @submit="onSubmit" v-if="showForm">
        <b-container>
          <b-row>
            <b-col>
              <b-form-group label="Random Seed:" label-for="random-seed" description="Generic random value, helps to obtain replicable results in the simulation.">
                <b-form-input
                    id="random-seed"
                    v-model.number="form.randomSeed"
                    type="number"
                    size="sm"
                    required
                ></b-form-input>
              </b-form-group>
            </b-col>

            <b-col>
              <b-form-group label="Working days:" label-for="working-days">
                <b-form-input
                    id="working-days"
                    v-model.number="form.workingDays"
                    type="number"
                    size="sm"
                    required
                ></b-form-input>
              </b-form-group>
            </b-col>

            <b-col>
              <b-form-group label="Working hours:" label-for="working-hours">
                <b-form-input
                    id="working-hours"
                    v-model.number="form.workingHours"
                    type="number"
                    size="sm"
                    required
                ></b-form-input>
              </b-form-group>
            </b-col>
          </b-row>

          <b-row>
            <b-col>
              <b-form-group label="Fruit packs:" label-for="fruit-pack" description="Initial packs of fruit to start fabric process.">
                <b-form-input
                    id="fruit-pack"
                    v-model.number="form.fruitPacks"
                    type="number"
                    size="sm"
                    required
                ></b-form-input>
              </b-form-group>
            </b-col>

            <b-col>
              <b-form-group label="Arrival interval:" label-for="arrival-interval" description="Time interval for incoming new fruit packs.">
                <b-form-input
                    id="arrival-interval"
                    v-model.number="form.arrivalInterval"
                    type="number"
                    size="sm"
                    required
                ></b-form-input>
              </b-form-group>
            </b-col>

            <b-col>
              <b-form-group label="Work count:" label-for="work-count" description="Determines the number of simultaneous work per stage.">
                <b-form-input
                    id="work-count"
                    v-model.number="form.workCount"
                    type="number"
                    size="sm"
                    required
                ></b-form-input>
              </b-form-group>
            </b-col>
          </b-row>

          <hr>
          <h5>Times for production steps</h5>
          <p class="text-muted">Every row in form represents a process stage.</p>
          <br>

          <b-row>
            <b-col>
              <b-form-group label="Washing time:" label-for="washing">
                <b-form-input
                    id="washing"
                    v-model.number="form.times.washing"
                    type="number"
                    size="sm"
                    required
                ></b-form-input>
              </b-form-group>
            </b-col>

            <b-col>
              <b-form-group label="Desinfection time:" label-for="desinfection">
                <b-form-input
                    id="desinfection"
                    v-model.number="form.times.desinfection"
                    type="number"
                    size="sm"
                    required
                ></b-form-input>
              </b-form-group>
            </b-col>
          </b-row>

          <b-row>
            <b-col>
              <b-form-group label="Pulping time:" label-for="pulping">
                <b-form-input
                    id="pulping"
                    v-model.number="form.times.pulping"
                    type="number"
                    size="sm"
                    required
                ></b-form-input>
              </b-form-group>
            </b-col>

            <b-col>
              <b-form-group label="Cooking time:" label-for="cooking">
                <b-form-input
                    id="cooking"
                    v-model.number="form.times.cooking"
                    type="number"
                    size="sm"
                    required
                ></b-form-input>
              </b-form-group>
            </b-col>
          </b-row>

          <b-row>
            <b-col>
              <b-form-group label="Plucking time:" label-for="plucking">
                <b-form-input
                    id="plucking"
                    v-model.number="form.times.plucking"
                    type="number"
                    size="sm"
                    required
                ></b-form-input>
              </b-form-group>
            </b-col>

            <b-col>
              <b-form-group label="Molding time:" label-for="molding">
                <b-form-input
                    id="molding"
                    v-model.number="form.times.molding"
                    type="number"
                    size="sm"
                    required
                ></b-form-input>
              </b-form-group>
            </b-col>
          </b-row>

          <b-row>
            <b-col>
              <b-form-group label="Cutting time:" label-for="cutting">
                <b-form-input
                    id="cutting"
                    v-model.number="form.times.cutting"
                    type="number"
                    size="sm"
                    required
                ></b-form-input>
              </b-form-group>
            </b-col>

            <b-col>
              <b-form-group label="Packing time:" label-for="packing">
                <b-form-input
                    id="packing"
                    v-model.number="form.times.packing"
                    type="number"
                    size="sm"
                    required
                ></b-form-input>
              </b-form-group>
            </b-col>
          </b-row>

          <b-row>
            <b-col>
              <b-form-group label="Box packing time:" label-for="box-packing">
                <b-form-input
                    id="box-packing"
                    v-model.number="form.times.boxPacking"
                    type="number"
                    size="sm"
                    required
                ></b-form-input>
              </b-form-group>
            </b-col>

            <b-col>
              <b-form-group label="Labeling time:" label-for="labeling">
                <b-form-input
                    id="labeling"
                    v-model.number="form.times.labeling"
                    type="number"
                    size="sm"
                    required
                ></b-form-input>
              </b-form-group>
            </b-col>
          </b-row>
        </b-container>

        <br>

        <div class="custom-container">
          <b-button type="submit" variant="primary">Submit</b-button>
        </div>
      </b-form>
    </b-card>

    <b-modal ref="results" hide-footer size="xl" title="Simulation results">
      <b-list-group>
        <b-list-group-item active>Produced lots</b-list-group-item>
        <b-list-group-item v-for="(lot, index) in results.lotTimes" v-bind:key="index">
          {{ lot }}
        </b-list-group-item>
      </b-list-group>

      <hr>

      <b-list-group class="mt-3">
        <b-list-group-item active>Fabric lines flow</b-list-group-item>
        <b-list-group-item v-for="(line, index) in results.flowLogs" v-bind:key="index">
          {{ line }}
        </b-list-group-item>
      </b-list-group>
    </b-modal>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: 'SimulationDashboard',
  data() {
    return {
      form: {
        workingDays: 25,
        workingHours: 8,
        randomSeed: 42,
        fruitPacks: 3,
        arrivalInterval: 120,
        workCount: 2,
        times: {
          washing: 4,
          desinfection: 10,
          pulping: 5,
          cooking: 45,
          plucking: 10,
          molding: 1440,
          cutting: 720,
          packing: 35,
          boxPacking: 10,
          labeling: 10
        }
      },
      showForm: true,
      results: {
        flowLogs: [],
        lotTimes: []
      }
    }
  },
  methods: {
    onSubmit(event) {
      event.preventDefault();

      axios
          .post('http://localhost:5000/simulate/', this.form)
          .then(response => {
            this.results = response.data;
            this.results.lotTimes = this.results.lotTimes.sort((a, b) => parseFloat(a) - parseFloat(b));
            this.results.lotTimes = this.results.lotTimes.map(number => this.convertToHours(number));
            this.$refs['results'].show();
          })
          .catch(error => console.log(error))
    },
    convertToHours(time) {
      let hours = Math.floor(time / 60);
      let minutes = time % 60;
      let day = Math.floor(hours / 8);
      return `${hours} hours with ${minutes} minutes (${day} production day - ${time} production minutes).`;
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.card-title, .card-subtitle, .custom-container {
  text-align: center;
}

.list-group{
  max-height: 300px;
  margin-bottom: 10px;
  overflow:scroll;
  -webkit-overflow-scrolling: touch;
}

button {
  width: 25%;
}
</style>
