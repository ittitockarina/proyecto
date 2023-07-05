<template>
  <div>
    <!-- Formulario de toma de asistencia -->
    <Panel :value="asistencia" class="custom-panel">
      <template #header>
        <div class="header-wrapper">
          <span class="header-text">Tomar asistencia</span>
        </div>
      </template>

      <div id="container">
        <video autoplay="true" id="videoElement"></video>
      </div>

      
      <br>

      <canvas id="canvas" width="500px" height="375px"></canvas>

      <span class="p-float-label">
        <Textarea v-model="asistencia.dni" rows="1" cols="10" />
        <label>DNI</label>
      </span>
      <br>

      <span class="p-float-label">
        <!-- <Calendar id="calendar-timeonly" v-model="asistencia.hora" timeOnly /> -->
        <!-- <input v-model="asistencia.hora" type="text" /> -->
        
        <Calendar v-model="asistencia.fecha" />
        <label>fecha</label>
      </span>
      <span class="p-float-label">
        
        <Calendar id="calendar-timeonly" v-model="asistencia.hora" timeOnly/>

        <label>Hora</label>
      </span>
      <br>
      <Button icon="pi pi-unlock"  v-on:click="open"></Button>
      <Button icon="pi pi-lock" severity="warning"  v-on:click="stop"></Button>
      <Button icon="pi pi-camera"  severity="success" id="snap" v-on:click="snap"></Button>
      
    </Panel>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      asistencia: {
        dni: '',
        fecha:'',
        hora: '' // Nuevo campo 'hora' agregado
      },
      postURL: 'http://127.0.0.1:5000',
      my_video: {},
      loadingAsistencia: false
    };
  },
  methods: {
    stop(e) {
      var stream = document.querySelector("#videoElement").srcObject;
      var tracks = stream.getTracks();

      for (var i = 0; i < tracks.length; i++) {
        var track = tracks[i];
        track.stop();
      }

      document.querySelector("#videoElement").srcObject = null;
    },
    open() {
      this.my_video = document.querySelector("#videoElement");

      if (navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ video: true })
          .then(function (stream) {
            document.querySelector("#videoElement").srcObject = stream;
          })
          .catch(function (err) {
            console.log("Something went wrong!");
            console.log(err);
          });
      }
    },
    snap() {
      var video = document.querySelector('video');
      var canvas = document.querySelector('canvas');
      var context = canvas.getContext('2d');

      var ratio = video.videoWidth / video.videoHeight;
      var w = video.videoWidth - 100;
      var h = parseInt(w / ratio, 10);
      canvas.width = w;
      canvas.height = h;

      context.fillRect(0, 0, w, h);
      context.drawImage(document.querySelector('video'), 0, 0, w, h);

      var img = canvas.toDataURL();
      var file = this.dataURItoBlob(img);

      var data = new FormData();
      data.append('file', file, 'foto.png');
      data.append('dni', JSON.stringify(this.asistencia.dni));
      data.append('fecha', this.asistencia.fecha);
      data.append('hora', this.asistencia.hora); // Se agrega el campo 'hora' al FormData

      axios.post('http://127.0.0.1:5000/toma', data, { headers: { 'Content-Type': 'multipart/form-data' } })
        .then(function (response) {
          console.log(response.data);
          // Mostrar el resultado de la asistencia
        })
        .catch((error) => {
          console.log(error)
        });
    },
    dataURItoBlob(dataURI) {
      var byteString;
      if (dataURI.split(',')[0].indexOf('base64') >= 0)
        byteString = atob(dataURI.split(',')[1]);
      else
        byteString = unescape(dataURI.split(',')[1]);

      var mimeString = dataURI.split(',')[0].split(':')[1].split(';')[0];

      var ia = new Uint8Array(byteString.length);
      for (var i = 0; i < byteString.length; i++) {
        ia[i] = byteString.charCodeAt(i);
      }
      return new Blob([ia], { type: mimeString });
    },
    tomarAsistencia() {
      this.loadingAsistencia = true;

      // Realizar la llamada a la API para tomar la asistencia

      this.loadingAsistencia = false;
    }
  },
};
</script>

<style scoped>
.custom-panel {
  margin-bottom: 1rem;
}
.header-wrapper {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.header-text {
  font-size: 1.5rem;
  font-weight: bold;
}
.custom-password {
  margin-bottom: 1rem;
}

#videoElement {
  width: 350px;
  height: 280px;
  transform: rotateY(180deg);
  -webkit-transform: rotateY(180deg);
  -moz-transform: rotateY(180deg);
}

#canvas {
  width: 350px;
  height: 260px;
  transform: rotateY(180deg);
  -webkit-transform: rotateY(180deg);
  -moz-transform: rotateY(180deg);
}
</style>