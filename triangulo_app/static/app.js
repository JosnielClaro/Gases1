axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';



const { createApp } = Vue

  createApp({
    delimiters: ['{$', '$}'],
    created(){
        axios.get('/api/buscar/')
        .then(response => this.transformadores = response.data);
    },
    data() {
      return {
        message: 'Hello ',
        mostrar: '',
        kword: '',
        transformadores: []
      }
    },
    watch:{
        
        mostrar: function(val) {
          this.Mostrar(val);
        },

        kword: function(val) {
            this.Buscar(val);
        }
    },
    methods:{
        Actualizar: function(){
          axios.get('/api/buscar/')
          .then(response => this.transformadores = response.data);
        },
        an_triangulo_1: function (ch4, c2h2, c2h4){
          var a_ch4 = Number(100*(ch4)/(ch4+c2h2+c2h4));
          var b_c2h2 = Number(100*(c2h2)/(ch4+c2h2+c2h4));
          var c_c2h4 = Number(100*(c2h4)/(ch4+c2h2+c2h4));
          if (20 <= b_c2h2 && b_c2h2 < 70){
            console.log('es')
          }
          console.log(a_ch4)
          console.log(b_c2h2)
          console.log(c_c2h4)
          if (0 <= a_ch4 && a_ch4 < 87 && 0 <= c_c2h4 && c_c2h4 <= 23 && 13 < b_c2h2 && b_c2h2 < 100){
            return ('D1')
          } else if (0 <= a_ch4 && a_ch4<50 && 30<c_c2h4 && c_c2h4 <77 && 23<=b_c2h2 && b_c2h2 <70){
            return ('D2')
          } else if (29<a_ch4 && a_ch4<64 && 23<c_c2h4 && c_c2h4<=40 && 13<b_c2h2 && b_c2h2<30){
            return ('D2')
          } else if (98<=a_ch4 && a_ch4<=100 && 0<=c_c2h4 && c_c2h4<2 && 0<=b_c2h2 && b_c2h2<2){
            return ('PD') 
          } else if (76<=a_ch4 && a_ch4<98 && 0<=c_c2h4 && c_c2h4<20 && 0<=b_c2h2 && b_c2h2<=4){
            return ('T1')
          } else if (46<=a_ch4 && a_ch4<80 && 20<c_c2h4 && c_c2h4<=50 && 0<=b_c2h2 && b_c2h2<=4){
            return ('T2')
          } else if (0<=a_ch4 && a_ch4<50 && 50<c_c2h4 && c_c2h4<100 && 0<=b_c2h2 && b_c2h2<15){
            return ('T3')
          } else if (0<=a_ch4 && a_ch4<=47 && 40<c_c2h4 && c_c2h4<100 && 15<=b_c2h2 && b_c2h2<30){
            return ('DT')
          } else if (35<a_ch4 && a_ch4<96 && 0<=c_c2h4 && c_c2h4<50 && 4<b_c2h2 && b_c2h2<15){
            return ('DT')
          } 
        },
        an_triangulo_4: function (h2, c2h6, ch4){
          var a_h2 = Number(100*(h2)/(h2+c2h6+ch4));
          var b_c2h6 = Number(100*(c2h6)/(h2+c2h6+ch4));
          var c_ch4 = Number(100*(ch4)/(h2+c2h6+ch4));
          if (0<a_h2 && a_h2<=9 && 0<c_ch4<70 && 30<=b_c2h6<100){
            return 'O'
          } else if (84<a_h2 && a_h2<98 && 2<c_ch4 && c_ch4<15 && 0<b_c2h6 && b_c2h6<=1){
            return 'PD'
          } else if (0<a_h2 && a_h2<64 && 36<c_ch4 && c_ch4<100 && 0<b_c2h6 && b_c2h6<24){
            return 'C'
          }else if (0<a_h2 && a_h2<=15 && 85<c_ch4 && c_ch4<100 && 0<b_c2h6 && b_c2h6<30){
            return 'C'
          } else if (9<a_h2 && a_h2<70 && 0<c_ch4 && c_ch4<61 && 30<b_c2h6 && b_c2h6<46){
            return 'S'
          } else if (15<a_h2 && a_h2<76 && 0<c_ch4 && c_ch4<61 && 24<=b_c2h6 && b_c2h6<30){
            return 'S'
          } else if (40<a_h2 && a_h2<100 && 0<c_ch4 && c_ch4<36 && 0<b_c2h6 && b_c2h6<24){
            return 'S'
          } else{
            return ''
          }
              
        },
        an_triangulo_5: function (ch4, c2h6, c2h4){
          var a_ch4 = Number(100*(ch4)/(ch4+c2h6+c2h4));
          var b_c2h6 = Number(100*(c2h6)/(ch4+c2h6+c2h4));
          var c_c2h4 = Number(100*(c2h4)/(ch4+c2h6+c2h4));

          if (0<a_ch4 && a_ch4<46 && 0<c_c2h4 && c_c2h4<10 && 54<b_c2h6 && b_c2h6<100){
            return 'O'
          } else if (75<a_ch4 && a_ch4<98 && 1<c_c2h4 && c_c2h4<10 && 0<b_c2h6 && b_c2h6<15){
            return 'O'
          } else if (88<a_ch4 && a_ch4<100 && 0<c_c2h4 && c_c2h4<10 && 0<b_c2h6 && b_c2h6<2){
            return 'O'
          } else if (36<a_ch4 && a_ch4<85 && 0<c_c2h4 && c_c2h4<10 && 15<b_c2h6 && b_c2h6<54){
            return 'S'
          } else if (84<a_ch4 && a_ch4<98 && 0<c_c2h4 && c_c2h4<=1 && 2<b_c2h6 && b_c2h6<15){
            return 'PD'
          } else if (53<a_ch4 && a_ch4<90 && 10<c_c2h4 && c_c2h4<35 && 0<b_c2h6 && b_c2h6<12){
            return 'T2'
          } else if (0<a_ch4 && a_ch4<35 && 35<c_c2h4 && c_c2h4<=70 && 30<b_c2h6 && b_c2h6<65){
            return 'T3'
          } else if (0<a_ch4 && a_ch4<30 && 70<c_c2h4 && c_c2h4<100 && 0<b_c2h6 && b_c2h6<30){
            return 'T3'
          } else if (0<a_ch4 && a_ch4<52 && 48<c_c2h4 && c_c2h4<100 && 0<b_c2h6 && b_c2h6<14){
            return 'T3'
          } else if (0<a_ch4 && a_ch4<65 && 35<c_c2h4 && c_c2h4<100 && 0<b_c2h6 && b_c2h6<12){
            return 'T3'
          } else if (0<a_ch4 && a_ch4<88 && 10<c_c2h4 && c_c2h4<70 && 14<b_c2h6 && b_c2h6<30){
            return 'C'
          } else if (22<a_ch4 && a_ch4<88 && 10<c_c2h4 && c_c2h4<48 && 12<b_c2h6 && b_c2h6<30){
            return 'C'
          } else{
            return ''
          }
              
        },
        Editar: function(transf){
            var id = transf.id;
            var Nombre = transf.nombre;
            var CH4ppm = transf.CH4ppm;
            var C2H4ppm = transf.C2H4ppm;
            var C2H2ppm = transf.C2H2ppm;
            var H2ppm = transf.H2ppm;
            var C2H6ppm = transf.C2H6ppm;
        
          Swal.fire({
            preConfirm: () => {
              const datos = document.querySelector("#Form");
              const act_datos = new FormData(datos);
              const formDataObj = {};
              act_datos.forEach((value, key) => (formDataObj[key] = value));
              let name = String(formDataObj.Nombre).trim();
                  if (name.length == 0) {
                    Swal.showValidationMessage(
                      `El nombre no puede estar vacio`)
                    return false
                    
                  }
                  if (Number(formDataObj.CH4ppm) + Number(formDataObj.C2H4ppm) + Number(formDataObj.C2H2ppm) == 0){
                    Swal.showValidationMessage('CH4ppm, C2H4ppm y C2H2ppm no pueden sumar 0')
                    return false
                  }
                
            },
            html:`
              <form id="Form">
              <div class="row" style="padding: 0.5in;">
                  <div class="col-md-6">
                      <input type="hidden" value="${id}" id="id" name="id">
                      <label class="form-label">Nombre</label>
                      <input class="form-control" type="text" name="Nombre" id="Nombre" value="${Nombre}"
                      placeholder="Nombre" maxlength="30" required autofocus minlength="3"/>
                      <label class="form-label">CH4pmm</label>
                      <input required class="form-control" type="number" name="CH4ppm" value="${CH4ppm}" id="CH4ppm"/>
                      <label class="form-label">C2H4ppm</label>
                      <input required class="form-control" type="number" name="C2H4ppm" value="${C2H4ppm}" id="C2H4ppm"/>
                  </div>
                  <div class="col-md-6">
                      <label class="form-label">C2H2ppm</label>
                      <input required class="form-control" type="number" name="C2H2ppm" value="${C2H2ppm}" id="C2H2ppm"/>
                      <label class="form-label">H2ppm</label>
                      <input required class="form-control" type="number" name="H2ppm" value="${H2ppm}" />
                      <label class="form-label">C2H6ppm</label>
                      <input required class="form-control" type="number" name="C2H6ppm" value="${C2H6ppm}" />                                
                  </div>
              </div>
              </form>
            `
          }).then((result) => {
            if (result.value) {
              const datos = document.querySelector("#Form");
              const act_datos = new FormData(datos);
              const formDataObj = {};
              var t4fallas = '-';
              var t5fallas = '-';
              act_datos.forEach((value, key) => (formDataObj[key] = value));
              const t1fallas = this.an_triangulo_1(Number(formDataObj.CH4ppm), Number(formDataObj.C2H2ppm), Number(formDataObj.C2H4ppm));
              if (t1fallas == 'PD' || t1fallas == 'T1' || t1fallas == 'T2'){
                t4fallas = this.an_triangulo_4(Number(formDataObj.H2ppm), Number(formDataObj.C2H6ppm), Number(formDataObj.CH4ppm));
              }
              if (t1fallas == 'T2' || t1fallas == 'T3'){
                t5fallas = this.an_triangulo_5(Number(formDataObj.CH4ppm), Number(formDataObj.C2H6ppm), Number(formDataObj.C2H4ppm));
              }
              console.log(t4fallas)
              axios.put(`/api/transformadores/${formDataObj.id}/`, {
                nombre : formDataObj.Nombre,
                CH4ppm : formDataObj.CH4ppm,
                C2H4ppm : formDataObj.C2H4ppm,
                C2H2ppm : formDataObj.C2H2ppm,
                H2ppm : formDataObj.H2ppm,
                C2H6ppm : formDataObj.C2H6ppm,
                t1fallas: t1fallas,
                t4fallas: String(t4fallas),
                t5fallas: String(t5fallas)

              }).then(response => {
                this.Actualizar()
              })
              Swal.fire('Saved!', '', 'success')
              
              
            } else if (result.isDenied) {
              Swal.fire('Changes are not saved', '', 'info')
            }
          })
        },
        Agregar: function(){
          Swal.fire({
            preConfirm: () => {
              const datos = document.querySelector("#Form");
              const act_datos = new FormData(datos);
              const formDataObj = {};
              act_datos.forEach((value, key) => (formDataObj[key] = value));
              let name = String(formDataObj.Nombre).trim();
                  if (name.length == 0) {
                    Swal.showValidationMessage(
                      `El nombre no puede estar vacio`)
                    return false
                    
                  }
                  if (Number(formDataObj.CH4ppm) + Number(formDataObj.C2H4ppm) + Number(formDataObj.C2H2ppm) == 0){
                    Swal.showValidationMessage('CH4ppm, C2H4ppm y C2H2ppm no pueden sumar 0')
                    return false
                  }
                
            },
            html:`
              <form id="Form">
              <div class="row" style="padding: 0.5in;">
                  <div class="col-md-6">
                      <label class="form-label">Nombre</label>
                      <input class="form-control" type="text" name="Nombre" id="Nombre" value=""
                      placeholder="Nombre" maxlength="30" required autofocus minlength="3"/>
                      <label class="form-label">CH4pmm</label>
                      <input required class="form-control" type="number" name="CH4ppm" value="0" id="CH4ppm"/>
                      <label class="form-label">C2H4ppm</label>
                      <input required class="form-control" type="number" name="C2H4ppm" value="0" id="C2H4ppm"/>
                  </div>
                  <div class="col-md-6">
                      <label class="form-label">C2H2ppm</label>
                      <input required class="form-control" type="number" name="C2H2ppm" value="0" id="C2H2ppm"/>
                      <label class="form-label">H2ppm</label>
                      <input required class="form-control" type="number" name="H2ppm" value="0" />
                      <label class="form-label">C2H6ppm</label>
                      <input required class="form-control" type="number" name="C2H6ppm" value="0" />                                
                  </div>
              </div>
              </form>
            `
          }).then((result) => {
            if (result.value) {
              
              const datos = document.querySelector("#Form");
              const act_datos = new FormData(datos);
              const formDataObj = {};
              var t4fallas = "-";
              var t5fallas = "-";
              act_datos.forEach((value, key) => (formDataObj[key] = value));
              const t1fallas = this.an_triangulo_1(Number(formDataObj.CH4ppm), Number(formDataObj.C2H2ppm), Number(formDataObj.C2H4ppm));
              if (t1fallas == 'PD' || t1fallas == 'T1' || t1fallas == 'T2'){
                t4fallas = this.an_triangulo_4(Number(formDataObj.H2ppm), Number(formDataObj.C2H6ppm), Number(formDataObj.CH4ppm));
              }
              if (t1fallas == 'T2' || t1fallas == 'T3'){
                t5fallas = this.an_triangulo_5(Number(formDataObj.CH4ppm), Number(formDataObj.C2H6ppm), Number(formDataObj.C2H4ppm));
              }
              
              console.log(formDataObj);
              console.log(formDataObj.C2H6ppm)
              axios.post('/api/transformadores/', {
                nombre : formDataObj.Nombre,
                CH4ppm : formDataObj.CH4ppm,
                C2H4ppm : formDataObj.C2H4ppm,
                C2H2ppm : formDataObj.C2H2ppm,
                H2ppm : formDataObj.H2ppm,
                C2H6ppm : formDataObj.C2H6ppm,
                t1fallas: t1fallas,
                t4fallas: t4fallas,
                t5fallas: t5fallas
              }).then(response => {
                this.Actualizar()
              })
              Swal.fire('Saved!', '', 'success')
              
              
            } else if (result.isDenied) {
              Swal.fire('Changes are not saved', '', 'info')
            }
          })
        },
        Borrar: function(e, key){
           Swal.fire({
              title: "Estás seguro?",
              text: "Este objeto no se podrá recuperar",
              icon: "warning",
              showCancelButton: true,
            })
            .then((result) => {
              if (result.isConfirmed) {
                
                axios.delete('/api/transformadores/' + e + '/').then(response => 
                  Swal.fire({
                    text: "Poof! El objeto ha sido eliminado",
                    icon: "success",
                  }),
                  this.transformadores.splice(key,1))
                
              } else {
                Swal.fire("Este objeto está a salvo")
                console.log(e, key)
              }
            })          
          },
        Mostrar: function(mostrar) {
          var self = this;
          axios.get('/api/mostrar/?kword=' + mostrar)
          .then(function(response){
              self.transformadores=response.data
              console.log(response.data)
          })
          .catch(function(error){
              console.log(error);
          })
      },
        Buscar: function(kword) {
            var self = this;
            axios.get('/api/buscar/?kword=' + kword)
            .then(function(response){
                self.transformadores=response.data
                console.log(response.data)
            })
            .catch(function(error){
                console.log(error);
            })
        }

    }
  }).mount('#app')

    